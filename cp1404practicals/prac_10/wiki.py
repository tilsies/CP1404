import wikipedia
def article_page(search):
    try:
        page = wikipedia.page(search)
    except wikipedia.exceptions.DisambiguationError:
        page_titles = wikipedia.search(search_term)
        if page_titles[1].lower() == page_titles[0].lower():
            title = page_titles[2]
        else:
            title = page_titles[1]
        page = get_page(wikipedia.page(title))
    return page

def main():

    user_search = input("What would you like to search for? \n >>> ")
    while user_search != "":
        page = article_page(user_search)
        print(page.title)
        print(page.summary)
        print(page.url)

        user_search = input("What would you like to search for? \n >>> ")

if __name__ == '__main__':
    main()

