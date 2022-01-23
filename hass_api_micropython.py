import urequests as requests
import ujson as json

class homeassistant_api_client:
    def __init__(self, homeassistant_base_url, homeassistant_token, homeassistant_api_method="REST", homeassistant_api_endpoint="/api"):
        self.token = homeassistant_token
        self.base_url = homeassistant_base_url
        self.api_method = homeassistant_api_method

        self.api_url = str(self.base_url) + str(homeassistant_api_endpoint)

        ''' 
        Check if there's a forward slash at the end of the API URL
        Add one if not
        ''' 
        if self.api_url[-1] != "/":
            self.api_url = str(self.api_url) + "/"

        
        self.headers = {
            "Authorization": "Bearer " + str(self.token),
            "content-type": "application/json",
        }

        if self.__healthcheck__() == True:
            print("API initialized")
        
    def __healthcheck__(self):
        healthcheck_response = self.__get__()
        api_status = healthcheck_response
        if "API running." in str(api_status['message']):
            return True
        else:
            print("API Error: " + str(api_status['message']))
            return False

    def __get__(self, endpoint=""):
        scrape_url = str(self.api_url) + str(endpoint)
        response = requests.get(scrape_url, headers=self.headers)
        return json.loads(response.text)

    def __post__(self, endpoint="", data=""):
        scrape_url = str(self.api_url) + str(endpoint)
        data = json.dumps(data)
        response = requests.post(scrape_url, headers=self.headers, data=data)
        
        try: 
            return json.loads(response.text)
        except ValueError:
            return response.text