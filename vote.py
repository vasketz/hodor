#!/usr/bin/python3
"""
This is the module documentation
vote 1024 times for mi id
"""
import requests


url = "http://158.69.76.135/level0.php"

for i in range(0, 1024):
    requests.post(url, data={"id": "2842", "holdthedoor": "Submit"})
