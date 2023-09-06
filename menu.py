from facebook_sc import facebook_scraper
from playwright.sync_api import sync_playwright
import json

def menu():
    print(':D')
    print('/█')
    print('.Π.')
    print('█╬╬╬█ █╬█ ███ ███ ╬╬ ██▄ █ ███ ╬╬ ██▄ █ ███ ╬╬ █╬╬╬█ ███ ███ █╬ ██▄')
    print('█╬█╬█ █▄█ █▄█ ╬█╬ ╬╬ █▄█ █ █╬▄ ╬╬ █▄█ █ █╬▄ ╬╬ █╬█╬█ █╬█ █▄╬ █╬ █╬█')
    print('█▄█▄█ █╬█ █╬█ ╬█╬ ╬╬ █▄█ █ █▄█ ╬╬ █▄█ █ █▄█ ╬╬ █▄█▄█ █▄█ █╬█ ██ ███ what a beautiful day to do suspicious things :)\n')

    print('########################### ~ Menu ~ ##############################')
    print('#    1. Facebook                                                  #')
    print('#    2. Instagram (nothing done)                                  #')
    print('#    3. create html file to display all data scraped              #')
    print('#    0. Exit                                                      #')
    print('###################################################################')

    option = input(str('Enter a scraper: '))

    try:
        if option == '1':
            with sync_playwright() as p:
                facebook_scraper(p)
        elif option == '2':
            print('2')
        elif option == '3':
            # Read the JSON data
            with open("names_and_links.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                accounts = data["accounts"]

            # Convert the JSON data to HTML content
            html_content = "<ul>\n"
            for account in accounts:
                name = account['name']
                link = account['link']
                image = account['image']
                html_content += f'  <li><img src="{image}"><a href="{link}">{name}</a></li>\n'
            html_content += "</ul>"

            # Inject the HTML content into search.html
            # we'll overwrite the entire content of search.html.
            with open("search.html", "w", encoding="utf-8") as f:
                f.write(html_content)
            print('\n')
            print('#######################################')
            print('#  generated html file successfully!  #')
            print('#######################################')

        elif option == '0':
            exit()

    except:
        print("An exception occurred")
    
menu()
