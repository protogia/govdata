import pretty_errors
from typing import Type, List
import requests

class DKANClient():
    def __init__(self, city: str, apiversion: int):
        self.city: str = city
        self.apiversion: int = apiversion
        self.base_url: str = f"https://opendata.{city}.de/api/{apiversion}/"


    def __current_package_list_with_resources(self) -> List:
        url = f"{self.base_url}action/current_package_list_with_resources"
        response = requests.get(url)
        return response.json()
    
    def get_available_datasets(self) -> Type[List]:
        response = self.__current_package_list_with_resources()

        if response["success"] == True:
            l = [element for element in response["result"][0]]
        return  l