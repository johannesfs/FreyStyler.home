import requests
import json
import logging


class HomeCenter:
    responseCodes = {
        200: "OK",
        400: "Bad request – missing parameter",
        401: "Unauthorized request",
        404: "Not found – no content",
        405: "Method not allowed – no content",
        500: "Internal server error – unexpected condition",
        501: "Not implemented – no content"
    }

    server = 'http://192.168.86.124/api'
    general_requests = ["devices", "sections", "rooms", "scenes", "users", "globalVariables", "linkedDevices", "virtualDevices", "iosDevices", "icons"]
    settings_requests = ["info", "location", "network"]
    info = None
    devices = None

    def parse_response_code(self, status_code):
        if status_code in self.responseCodes:
            print(f"Status: {status_code} - {self.responseCodes[status_code]}")
            if status_code == 200:
                return True
        else:
            print(f"Status: {status_code} - Unknown response")

        return False

    def __init__(self):
        """Constructor establishing the connection to HomeCenter"""

        # Connect to Home Center
        r = requests.get(f'{self.server}/devices', auth=("johannesfs@gmail.com", "Jagheterjohannes75!"))
        
        if self.parse_response_code(r.status_code):

            self.devices = json.loads(r.content.decode('UTF-8'))
            for element in self.devices:
                for key in element.keys():
                    print(f"{key} - {element[key]}, ", end="")
                print()

        r = requests.get(f'{self.server}/settings/info', auth=("johannesfs@gmail.com", "Jagheterjohannes75!"))

        if self.parse_response_code(r.status_code):
            self.info = json.loads(r.content.decode('UTF-8'))

            for element in self.info:
                print(f"{element} - {self.info[element]}, ", end="")
            print()


    def __repr__(self):
        return f"HomeCenter@{self.server}"


if __name__ == "__main__":
    hc_host = HomeCenter()
    print(f"{hc_host}")
