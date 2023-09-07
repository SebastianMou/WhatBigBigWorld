from playwright.sync_api import sync_playwright
import time
def search_google(query):
    with sync_playwright() as p:
        browser = p.chromium.launch()  # Launches a new browser window
        page = browser.new_page()  # Opens a new tab in the browser
        page.goto(f"https://www.google.com/search?tbm=isch&q={query}")  

        # Set the zoom level to 50%
        page.evaluate("document.body.style.zoom = '0.5'")

        last_height = page.evaluate("document.body.scrollHeight")
        screenshot_count = 1  # Counter for screenshot naming
        while True:
            # Scroll to the bottom of the page
            page.evaluate("window.scrollTo(0, document.body.scrollHeight);")

            time.sleep(4)  # Adjust this delay as needed

            # Take a screenshot
            screenshot_name = f"ss_google{screenshot_count}_{query}.png"
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
        with open("page_content_google.html", "w", encoding="utf-8") as f:
            f.write(content)
        print("Save the entire page content to a file ...")

        browser.close()  # Closes the browser

if __name__ == "__main__":
    query = input("Enter your search query: ")
    search_google(query)
