import voluptuous as vol
from homeassistant import config_entries
from homeassistant.helpers.aiohttp_client import async_get_clientsession
import logging

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

class PollenflugBayernConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Pollenflug Bayern."""
    
    VERSION = 1

    def __init__(self):
        """Initialize the config flow."""
        self._locations = {}

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}

        if user_input is not None:
            location_id = user_input["location"]
            location_name = self._locations.get(location_id, location_id)
            
            # Verhindert, dass dieselbe Messstation mehrfach hinzugefügt wird
            await self.async_set_unique_id(location_id)
            self._abort_if_unique_id_configured()
            
            return self.async_create_entry(
                title=f"Pollenflug {location_name}", 
                data={"location": location_id, "name": location_name}
            )

        # Lade die Standorte live von der ePIN API
        try:
            session = async_get_clientsession(self.hass)
            response = await session.get("https://epin.lgl.bayern.de/api/locations")
            response.raise_for_status()
            locations_data = await response.json()
            
            # Formatieren für das Dropdown-Menü: "Altötting (DEALTO)"
            self._locations = {
                loc["id"]: f"{loc['name']} ({loc['id']})" 
                for loc in locations_data if "id" in loc and "name" in loc
            }

        except Exception as e:
            _LOGGER.error("Fehler beim Abrufen der Messstationen: %s", e)
            errors["base"] = "cannot_connect"
            # Fallback, falls die API beim Setup kurzzeitig nicht erreichbar ist
            self._locations = {"DEVIEC": "Viechtach (DEVIEC)"}

        # Zeigt das Auswahlmenü an
        data_schema = vol.Schema({
            vol.Required("location"): vol.In(self._locations)
        })

        return self.async_show_form(
            step_id="user",
            data_schema=data_schema,
            errors=errors
        )
###
