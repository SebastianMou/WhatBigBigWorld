from facebook_sc import facebook_scraper
from playwright.sync_api import sync_playwright
import json

def menu():
    print('╔╦╦╦═╦╗╔═╦═╦══╦═╗╔═╦═╦═╦╦╗╔══╦═╦╗╔╦╦╦╦═╦╦═╗')
    print('║║║║╦╣╚╣╠╣║║║║║╦╣║╣╣╩║╠╣═╣║║║║╩║╚╝║╔╣║╠╣║║║')
    print('╚══╩═╩═╩═╩═╩╩╩╩═╝╚═╩╩╩═╩╩╝╚╩╩╩╩╩══╩╝╚╩═╩╩═╝ What a beautiful day for suspicious activity.\n')

    print('########################### ~ Menu ~ ##############################')
    print('#    1. Facebook                                                  #')
    print('#    2. Instagram (nothing done)                                  #')
    print('#    3. create html file to display all data scraped              #')
    print('#    0. Exit                                                      #')
    print('###################################################################')

    option = input(str('Enter a scraper: '))

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
            html_content += f'  <li><a href="{link}">{name}</a></li>\n'
        html_content += "</ul>"

        # Inject the HTML content into search.html
        # For this example, we'll overwrite the entire content of search.html.
        # You can modify this part to insert the content at a specific location if needed.
        with open("search.html", "w", encoding="utf-8") as f:
            f.write(html_content)

        print('#######################################')
        print('#  generated html file successfully!  #')
        print('#######################################')

    elif option == '0':
        exit()

menu()
