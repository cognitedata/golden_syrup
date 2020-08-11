from requests import get
import json


class OxfordSearcher:
    def __init__(self, s, lang):
        self.s = s
        self.lang = lang

    def os(self):
        searchString = "https://od-api.oxforddictionaries.com/api/v2/entries/" + self.lang + "/" + self.s
        result = get(searchString, headers={"Accept": "application/json", "app_id": "580153d7",
                                            "app_key": "100b40f07ad22375f69741ae4531735a"})
        return json.loads(result.content)["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"][0]


def search_for_user_input():
    user_input = input("Enter list of search terms (comma-separated): ")
    user_input_list = user_input.split(",")
    american = bool(input("Do you want to search using the American dictionary? (Brittish is default)"))
    results = []

    if len(user_input) != 0:
        for s in user_input_list:
            if american == True:
                oxs = OxfordSearcher(s, "en-us")
                result = oxs.os()
                results.append(result)
            else:
                oxs = OxfordSearcher(s, "en-gb")
                result = oxs.os()
                results.append(result)

    for result in results:
        print(result)


search_for_user_input()


