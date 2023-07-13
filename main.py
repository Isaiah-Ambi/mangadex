import requests
import json
import os

base_url = "https://api.mangadex.org"

# request manga titles
def search_manga_title(title):
    r = requests.get(
        f"{base_url}/manga",
        params={"title": title}
    )

    print([manga["attributes"]["title"]["en"] for manga in r.json()["data"]])

    #searching manga title
    result = []
    for manga in r.json()["data"]:
        result.append(manga["attributes"]["title"]["en"])
    #return result
    sn = 0
    #display results
    for manga in result:
        sn += 1
        print(f"{sn} {manga}")

    #accept user choice
    l = len(result)
    print(l)
    choice = int(input('choose'))
    if choice >= 1 and choice <= l:
        choice -= 1
        title = result[choice]
        print(title)
        return title
    else:
        print("invalid input")

#get manga id
def get_manga_id(title):
    r = requests.get(
        f"{base_url}/manga",
        params={"title": title}
    )

    id = [manga["id"] for manga in r.json()["data"]]
    
    m_id = id[0]
    print(m_id)
    return m_id

# get manga id
def get_chapter_id(manga_id):
    print(manga_id)
    languages = ["en"]
    r = requests.get(
    f"{base_url}/manga/{manga_id}/feed",
    params={"translatedLanguage[]": languages},
)

    chapters = [chapter["id"] for chapter in r.json()["data"]]
    return chapters

#list meta
def display_meta():
    pass

#download chapters
def download_chapter(chapter_id):

    r = requests.get(f"{base_url}/at-home/server/{chapter_id}")
    r_json = r.json()

    host = r_json["baseUrl"]
    chapter_hash = r_json["chapter"]["hash"]
    data = r_json["chapter"]["data"]
    data_saver = r_json["chapter"]["dataSaver"]
        

def main():
    title = input('input title ')
    manga_title = search_manga_title(title)
    manga_id = get_manga_id(manga_title)
    chapter_id = get_chapter_id(manga_id)
    chapter_len = len(chapter_id)
    print(chapter_len)
    chapter_select = input('select chapters 1 to {chapter_len}')
    if chapter_select > 0 and chapter_select <= chapter_len:
        chapter_id = chapter_id[chapter_select - 1]
    else:
        print("invalid chapter")

    download_chapter(chapter_id)
        
if __name__ == "__main__":
    main()