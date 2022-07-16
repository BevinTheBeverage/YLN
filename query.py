import requests
import pickle

class QuotaExceeded(Exception):
    pass

def search(query, page=1, days=2):
    API_KEY = "AIzaSyDrW-yFozgpkEgAs48kwq7h37X_m6vFOAg"

    SEARCH_ENGINE_ID = "4573bc7148314e3ec"

    start = (page-1)*10+1

    # constructing the URL
    # doc: https://developers.google.com/custom-search/v1/using_rest
    # optional parameters: https://developers.google.com/custom-search/v1/reference/rest/v1/cse/list
    url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&lr=lang_en&dateRestrict=d2&sort=date"
    #url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&lr=lang_en&dateRestrict=d{days}"

    data = requests.get(url).json()

    if data.get('error') != None and data.get('error').get('code')==429:
        raise QuotaExceeded()

    # get the result items
    return data.get("items")

def download_list(list, fname):
    with open(fname, "wb") as fp:
        pickle.dump(list, fp)

if __name__ == "__main__":
    # queries = ["Yuh-Line Niou",
    #         "Bill de Blasio",
    #         "Mondaire Jones",
    #         "Carlina Rivera",
    #         "Dan Goldman",
    #         "Jo Anne Simon"]
    queries = ["New York Primary Election Results"]
    page = 1
    results = [search(i, page) for i in queries]

    # download_list(results[0], "data")

    for result in results:
        # iterate over 10 results found
        for i, search_item in enumerate(result, start=1):
            try:
                long_description = search_item["pagemap"]["metatags"][0]["og:description"]
            except KeyError:
                long_description = "N/A"
            # get the page title
            title = search_item.get("title")
            # page snippet
            snippet = search_item.get("snippet")
            # alternatively, you can get the HTML snippet (bolded keywords)
            html_snippet = search_item.get("htmlSnippet")
            # extract the page url
            link = search_item.get("link")
            # print the results
            print("="*10, f"Result #{i+(page-1)*10}", "="*10)
            print("Title:", title)
            print("Snippet:", snippet)
            print("Long description:", long_description)
            print("URL:", link, "\n")
