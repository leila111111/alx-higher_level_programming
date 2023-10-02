#!/usr/bin/python3
"""Python script that takes 2 arguments
in order to list the 10 most recent commits on a
GitHub repository"""
from sys import argv
import requests

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    req = requests.get(url)
    commits = req.json()
    for i in range(10):
        print(commits[i].get("sha"), end=': ')
        print(commits[i].get("commit").get("author").get("name"))
