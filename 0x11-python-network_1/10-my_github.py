#!/usr/bin/python3
"""Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""
import sys
import requests

if __name__ == "__main__":
    url = "https://api.github.com/user"
    res = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
    print(res.json().get("id"))
