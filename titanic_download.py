#!/usr/bin/env python3
import requests

if __name__=="__main__":
    URL="https://sololearn.com/uploads/files/titanic.csv"
    data = requests.get(URL)

    with open("titanic.csv", "w") as f:
        f.write(data.content.decode('utf-8'))
