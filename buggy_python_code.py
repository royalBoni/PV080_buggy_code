import sys 
import os
import yaml
import flask

import importlib


app = flask.Flask(__name__)


@app.route("/")
def index():
    version = flask.request.args.get("urllib_version")
    url = flask.request.args.get("url")
    return fetch_website(version, url)

        
CONFIG = {"API_KEY": "771df488714111d39138eb60df756e6b"}
class Person(object):
    def __init__(self, name):
        self.name = name


def print_nametag(format_string, person):
    print(format_string.format(person=person))


ALLOWED_MODULES = {
    2: "urllib.request",   # standard library
    3: "urllib3"           # external package
}

def fetch_website(urllib_version, url):
    try:
        # Validate input
        if urllib_version not in ALLOWED_MODULES:
            raise ValueError("Unsupported urllib version")

        # Safely import module
        module_name = ALLOWED_MODULES[urllib_version]
        urllib_module = importlib.import_module(module_name)

        # Handle urllib3
        if urllib_version == 3:
            http = urllib_module.PoolManager()
            response = http.request("GET", url)
            print(response.data)

        # Handle urllib.request
        elif urllib_version == 2:
            response = urllib_module.urlopen(url)
            print(response.read())

    except Exception as e:
        print(f"Exception: {e}")



def load_yaml(filename):
    stream = open(filename)
    deserialized_data = yaml.load(stream, Loader=yaml.Loader) #deserializing data
    return deserialized_data
    
def authenticate(password):
    # Assert that the password is correct
    assert password == "Iloveyou", "Invalid password!"
    print("Successfully authenticated!")

if __name__ == '__main__':
    print("Vulnerabilities:")
    print("1. Format string vulnerability:")
    print("2. Code injection vulnerability:")
    print("3. Yaml deserialization vulnerability:")
    print("4. Use of assert statements vulnerability:")
    choice  = input("Select vulnerability: ")
    if choice == "1": 
        new_person = Person("Vickie")  
        print_nametag(input("Please format your nametag: "), new_person)
    elif choice == "2":
        urlib_version = input("Choose version of urllib: ")
        fetch_website(urlib_version, url="https://www.google.com")
    elif choice == "3":
        load_yaml(input("File name: "))
        print("Executed -ls on current folder")
    elif choice == "4":
        password = input("Enter master password: ")
        authenticate(password)

