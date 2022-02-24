# from playwright.async_api import async_playwright

# start browser and instance
playwright = await async_playwright().start()
browser = await playwright.chromium.launch(headless=False)
context = await browser.new_context(accept_downloads= True)
page = await context.new_page()


# bring up pause window to allow recording of commands
await page.pause() 





#Automating clicking the no buttons for e-qip paperwork 
#
await page.click("p:has-text(\"No\")")
await page.click("fieldset:nth-child(10) .eqip-block-error .usa-grid div:nth-child(2) .eqip-height-2 p")
await page.click("fieldset:nth-child(12) .eqip-block-error .usa-grid div:nth-child(2) .eqip-height-2 p")
await page.click("fieldset:nth-child(14) .eqip-block-error .usa-grid div:nth-child(2) .eqip-height-2 p")
await page.click("fieldset:nth-child(16) .eqip-block-error .usa-grid div:nth-child(2) .eqip-height-2 p")
await page.click("fieldset:nth-child(18) .eqip-block-error .usa-grid div:nth-child(2) .eqip-height-2 p")
await page.click("fieldset:nth-child(20) .eqip-block-error .usa-grid div:nth-child(2) .eqip-height-2 p")
await page.click("text=Save/Continue")
#
#



#Automating clicking through saying relatives aren't deceased for e-qip paperwork 
#
await page.click("text=Relative Deceased Question")
await page.click("text=Save")
await page.click("text=Summary")
#
#





await page.close()
await playwright.stop()