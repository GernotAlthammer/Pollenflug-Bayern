import logging
from datetime import timedelta
import async_timeout

from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, CoordinatorEntity, UpdateFailed
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .const import DOMAIN, SENSOR_TYPES

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass, entry, async_add_entities):
    """Set up the sensor platform via UI configuration."""
    session = async_get_clientsession(hass)
    
    # Ausgewählte Messstation laden (Standard: DEVIEC als Fallback)
    location_id = entry.data.get("location", "DEVIEC")
    location_name = entry.data.get("name", location_id)
    
    api_url = f"https://epin.lgl.bayern.de/api/measurements?locations={location_id}"

    async def async_update_data():
        try:
            async with async_timeout.timeout(10):
                response = await session.get(api_url)
                response.raise_for_status()
                data = await response.json()
                
                parsed_data = {}
                if "measurements" in data:
                    for item in data["measurements"]:
                        pollen = item.get("pollen")
                        if item.get("data") and len(item["data"]) > 0:
                            parsed_data[pollen] = float(item["data"][0].get("value", 0.0))
                return parsed_data
        except Exception as err:
            raise UpdateFailed(f"Fehler bei der API-Abfrage für {location_name}: {err}")

    coordinator = DataUpdateCoordinator(
        hass,
        _LOGGER,
        name=f"pollenflug_bayern_{location_id}",
        update_method=async_update_data,
        update_interval=timedelta(hours=3),
    )

    await coordinator.async_config_entry_first_refresh()

    # Den Stationsnamen übergeben, damit die Sensoren "Pollenflug München Birke" o.ä. heißen
    entities = [PollenSensor(coordinator, pollen_type, location_id, location_name) for pollen_type in SENSOR_TYPES]
    async_add_entities(entities)


class PollenSensor(CoordinatorEntity, SensorEntity):
    """Representation of a Pollen Sensor."""

    def __init__(self, coordinator, pollen_type, location_id, location_name):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._pollen_type = pollen_type
        
        # Name dynamisch anpassen: "Pollenflug Altötting Betula"
        self._attr_name = f"Pollenflug {location_name} {pollen_type}"
        self._attr_native_unit_of_measurement = "Pollen/m³"
        self._attr_icon = "mdi:flower-pollen"
        
        # Unique ID muss die Location ID enthalten, damit mehrere Stationen konfliktfrei koexistieren
        self._attr_unique_id = f"pollen_{location_id.lower()}_{pollen_type.lower().replace(' ', '_')}"

    @property
    def native_value(self):
        """Return the state of the sensor."""
        if self.coordinator.data:
            val = self.coordinator.data.get(self._pollen_type)
            return f"{val:.1f}" if val is not None else None
        return None
###
