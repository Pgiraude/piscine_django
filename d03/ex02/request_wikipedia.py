import requests
import json
import dewiki
import sys

def request_wikipedia(page):
    PARAMS = {
        "action": "parse",
        "page": page,
        "prop": "wikitext",
        "format": "json",
        "redirects": "true"
    }

    try:
        wiki_request = requests.get(url="https://en.wikipedia.org/w/api.php", params=PARAMS)
        wiki_request.status_code
        print('json: ', wiki_request.json)
        data = json.loads(wiki_request.text)
        print("data json: ", data)
    except requests.HTTPError as e:
        print(requests.HTTPError)
    return dewiki.from_string(data["parse"]["wikitext"]["*"])

def main():
    if len(sys.argv) != 2:
        return
    title = sys.argv[1]
    wiki_data = request_wikipedia(title)
    f = open("{}.wiki".format(title), "w")
    f.write(wiki_data)
    f.close

if __name__ == '__main__':
    main()