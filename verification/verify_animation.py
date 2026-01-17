
from playwright.sync_api import sync_playwright, expect

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Navigate to the page
        page.goto("http://localhost:8000/index.html")

        # Click to open the invite
        # The main container is clickable or the specific element with text "TOP SECRET"
        # The "State 1" div has onClick={handleOpen}
        # It contains "TOP SECRET"
        page.get_by_text("TOP SECRET").click()

        # Wait for the animation and reveal (handleOpen has 1200ms timeout)
        # Then the new view appears.
        # "Mission Objective" text should appear.

        # Wait for the text to appear in the DOM
        # Note: it scrambles, but the container should be visible
        # We can wait for "Case File #210226" which is static in the header
        page.get_by_text("Case File #210226").wait_for(timeout=5000)

        # Now wait for the scrambling to finish.
        # The title "ARIASY'S BIRTHDAY" takes about 1.5s (17 chars * 30ms * 3)
        # "MISSION OBJECTIVE" takes similar time.
        # Let's wait 3 seconds to be safe.
        page.wait_for_timeout(3000)

        # Take a screenshot
        page.screenshot(path="verification/screenshot.png")

        browser.close()

if __name__ == "__main__":
    run()
