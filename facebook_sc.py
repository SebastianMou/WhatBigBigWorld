from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time
import subprocess
import json

def facebook_scraper(playwright):
    # Get the name for the public profile search
    name = input(str('name: '))
    url_path = f'https://www.facebook.com/public/{name}'

    # Launch a new browser instance
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # WHERE THE LOGIN WAS 
    ##############################################################################################
    # Navigate to Facebook login page
    # page.goto("https://www.facebook.com/login")

    # # Input your email and password (make sure to keep these secure and not hard-code them)
    # email = ''
    # password = ''

    # # Fill in the email and password fields
    # page.fill("input[name='email']", email)
    # page.fill("input[name='pass']", password)

    # # Click the login button
    # page.click("button[name='login']")

    # # Wait for navigation to complete (you can adjust the timeout as needed)
    # page.wait_for_load_state("networkidle")

    # Wait for the "Ver todo" button to appear and then click it
    # page.click('a[aria-label="Ver todo"]')
    ##############################################################################################

    # Now navigate to the desired public profile URL
    page.goto(url_path)

    # Get the title of the page and print it
    title = page.title()
    print(f"Title of the page is: {title}")
    print(f"Searching for: {name} on facebook")

    # Scroll down multiple times to load all content
    last_height = page.evaluate("document.body.scrollHeight")
    screenshot_count = 1  # Counter for screenshot naming
    while True:
        # Scroll to the bottom of the page
        page.evaluate("window.scrollTo(0, document.body.scrollHeight);")

        # Wait for new content to load
        time.sleep(2)  # Adjust this delay as needed

        # Take a screenshot
        screenshot_name = f"ss_facebook_acc{screenshot_count}_{name}.png"
        page.screenshot(path=screenshot_name)
        screenshot_count += 1
        print(f"taking screenshot of page - {screenshot_count}")

        # Check the new scroll height after content has loaded
        new_height = page.evaluate("document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # Save the entire page content to a file
    content = page.content()
    with open("page_content.html", "w", encoding="utf-8") as f:
        f.write(content)

    # Open a new terminal and display the content of the page_content.html file
    # subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', 'cat page_content.html; read -n1'])
    command = 'cat page_content.html; sleep 5; exit'
    subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', command])

    time.sleep(10)
    print('Done!')

    # Close the browser
    browser.close()

    ########################################################################
    # Load the saved HTML file
    with open("page_content.html", "r", encoding="utf-8") as f:
        content = f.read()

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(content, "lxml")

    # Find all account names using the provided class
    account_elements = soup.find_all("a", class_="_32mo")

    # Collect names and links
    accounts = []
    for account in account_elements:
        name = account.text
        link = account['href']
        accounts.append({"name": name, "link": link})
        print(f"Name: {account['name']}")
        print(f"Link: {account['link']}")
        print("-" * 50)  # print a separator for clarity


    # Collect names
    account_elements = [account.text for account in account_elements]

    # Structure data as a dictionary with a title or key
    data = {
        "accounts": accounts
    }

    # Save data to a JSON file
    with open("names_and_links.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    command = 'cat names_and_links.json; sleep 5; exit'
    subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', command])


if __name__ == "__main__":
    with sync_playwright() as p:
        facebook_scraper(p)


