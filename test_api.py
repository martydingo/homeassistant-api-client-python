from homeassistant_api_client import homeassistant_api_client
import json

config_file_path = "config.json"

def load_yaml_configuration(config_file_path):
  config = json.load(open(config_file_path, "r"))
  return config

def init_api_class(config):
    hass_api = homeassistant_api_client(config["homeassistant"]["homeassistant_base_url"], config["homeassistant"]["homeassistant_token"])
    return hass_api

config = load_yaml_configuration(config_file_path)
hass_api = init_api_class(config)
# print(hass_api.__get__('states'))
data = {"template": "The sun changed {{ relative_time(states.sun.sun.last_changed) }} ago "}
    
print(hass_api.__post__(endpoint="template", data=data))