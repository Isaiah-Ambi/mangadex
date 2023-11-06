import requests

base_url = "https://api.mangadex.org"
manga_id = "be7dda55-4eb6-4a73-92a7-21e5e8faf0a5"
r = requests.get(f"{base_url}/manga/{manga_id}/feed")

print([chapter["id"] for chapter in r.json()["data"]])