"""Checks the enviroment and sends an email to affected user"""
import os
import requests

def send_alert(alert):
    """Send notification"""
    print(alert)

def https_check(website):
    """Checks http resources"""
    try:
        result = requests.get(website, verify=False)
    except:
        print(website)
        return "na"
    return result.status_code

def get_text_path():
    """Gets file path"""
    script_dir = os.path.dirname(__file__)
    rel_path = "websites.txt"
    return os.path.join(script_dir, rel_path)

def load_websites():
    """Loads all websites from text file"""
    with open(str(get_text_path())) as file_contents:
        content = file_contents.read().splitlines()
    return content

WEBSITES = load_websites()
for site in WEBSITES:
    status_code = https_check(site)
    if str(status_code) == "na":
        send_alert("fail")

print("Done")
