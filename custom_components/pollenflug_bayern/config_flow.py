import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import HomeAssistant

from .const import DOMAIN

class PollenflugBayernConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Pollenflug Bayern."""
    
    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if user_input is not None:
            # Verhindern, dass die Integration mehrfach eingerichtet wird
            await self.async_set_unique_id(DOMAIN)
            self._abort_if_unique_id_configured()
            
            return self.async_create_entry(title="Pollenflug Bayern", data=user_input)

        # Zeigt das simple Bestätigungsfenster an
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({})
        )
