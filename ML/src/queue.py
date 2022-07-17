import requests


def get_berco(berco: str):
    r = requests.GET('http://localhost:8000/')