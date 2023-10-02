#!/usr/bin/python3
"""Python script that takes in a letter and sends
a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter."""
import sys
import requests
if __name__ == "__main__":
    if len(sys.argv) == 1:
        flop = ""
    else:
        flop = sys.argv[1]
    value = {"q": flop}
    req = requests.post("http://0.0.0.0:5000/search_user", data=value)
    try:
        resp = req.json()
        if resp == {}:
            print("No result")
        else:
            print(f"[{resp['id']}] {resp['name']}")
    except ValueError:
        print("Not a valid JSON")