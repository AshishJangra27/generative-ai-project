import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

def get_links(topic):

    topic = topic.replace(" ", "+")
    api_key = os.getenv("SERPER_API_KEY")

    url = f"https://google.serper.dev/search?q={topic}&apiKey={api_key}"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    json_data = json.loads(response.text)

    links = []

    for item in json_data["organic"]:
        links.append(item['link'])
        if "sitelinks" in item:
            for sub in item["sitelinks"]:
                links.append(sub['link'])

    return links