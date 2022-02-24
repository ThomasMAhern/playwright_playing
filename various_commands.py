# from playwright.async_api import async_playwright

# start browser and instance
playwright = await async_playwright().start()
browser = await playwright.chromium.launch(headless=False)
context = await browser.new_context(accept_downloads= True)
page = await context.new_page()


# bring up pause window to allow recording of commands
await page.pause() 



