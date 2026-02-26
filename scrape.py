import asyncio
from playwright.async_api import async_playwright

SEEDS = list(range(19, 29))
BASE = "https://sanand0.github.io/tdsdata/js_table/?seed="

async def main():
    total_sum = 0

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        for seed in SEEDS:
            url = BASE + str(seed)
            await page.goto(url)
            await page.wait_for_selector("table")

            numbers = await page.locator("table td").all_inner_texts()

            for n in numbers:
                n = n.strip()
                if n.isdigit():
                    total_sum += int(n)

        await browser.close()

    print(f"FINAL_TOTAL={total_sum}")

asyncio.run(main())
