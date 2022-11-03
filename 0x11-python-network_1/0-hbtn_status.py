#!/usr/bin/python3
"""Fetches a URL."""
import urllib.request as request


if __name__ == "__main__":
    with request.urlopen("http://0.0.0.0:5050/status") as response:
        if response.readable():
            data = response.read()
            print("Body response:")
            print("\t- type: {}".format(type(data)))
            print("\t- content: {}".format(data))
            print("\t- utf8 content: {}".format(data.decode("utf-8")))
