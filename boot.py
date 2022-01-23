# This file is executed on every boot (including wake-boot from deepsleep)
import network
import ujson as json

def load_json_configuration(config_file_path):
    """
    Loads the JSON configuration file from the variable config_file_path and returns a dictionary
    `config_file_path` - The relative or fully qualifed path of the JSON configuration file
    """
    config = json.load(open(config_file_path, "r"))
    return config

def configure_network(config):
    """
    Configures the network using parameters loaded from the configuration. \n
    `config` - The dictionary that is holding the loaded JSON configuration
    """
    sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
    sta_if.connect(config["board"]["wifi"]["ssid"], config["board"]["wifi"]["passphrase"]) # Connect to an AP
    while sta_if.isconnected() == False:
        pass
    print("Network is now configured!")

config = load_json_configuration("config.json")
configure_network(config)
