import requests

URL = "http://pinoc.serveo.net/name"


def ask_name_action(name):
    requests.get(url="{}/{}".format(URL, name))
    response = "Bonjour {}".format(name)
    return response
