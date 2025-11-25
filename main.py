import asyncio
import pandas as pd
from playwright.async_api import async_playwright

CHROME_PROFILE_PATH = r"C:/Users/hp/AppData/Local/Google/Chrome/User Data/Default"

async def scrape_indeed(job, location, days=3, max_pages=5):
    async with async_playwright() as p:
        context = await p.chromium.launch_persistent_context(
            user_data_dir=CHROME_PROFILE_PATH,
            channel="chrome",
            headless=False,
            args=[
                "--start-maximized",
                "--disable-blink-features=AutomationControlled",
                "--no-sandbox"
            ]
        )
        page = context.pages[0]
        seen = set() # store unique job IDs
        all_results = []

        for page_num in range(max_pages):
            start = page_num * 10

            url = (
                f"https://www.indeed.com/jobs?"
                f"q={job.replace(' ', '+')}&"
                f"l={location.replace(' ', '+')}&"
                f"radius=100&" 
                f"fromage={days}&start={start}"
            )

            print(f"\n🌐 Page {page_num + 1} → {url}")
            await page.goto(url, timeout=0)
            #await asyncio.sleep(9999999)

            if "verify" in page.url or "__cf" in page.url:
                print("Cloudflare challenge detected — stopping.")
                break

            try:
                await page.wait_for_selector("td.resultContent", timeout=15000)
            except:
                print("No job cards found - stopping")
                break

            job_cards = await page.query_selector_all("td.resultContent")
            print(f"✔ Found {len(job_cards)} jobs")

            if not job_cards:
                break

            for job_card in job_cards:

                link_el = await job_card.query_selector("a")
                href = await link_el.get_attribute("href") if link_el else None
                if not href:
                    continue

                # Extract job key from any type of URL
                job_id = None
                if "jk=" in href:
                    job_id = href.split("jk=")[-1].split("&")[0]
                else:
                    continue  # skip weird items

                # Skip duplicates
                if job_id in seen:
                    continue

                seen.add(job_id)

                # Extract fields
                title_el = await job_card.query_selector("h2.jobTitle span")
                company_el = await job_card.query_selector('[data-testid="company-name"]')
                location_el = await job_card.query_selector('[data-testid="text-location"]')

                title = await title_el.inner_text() if title_el else "N/A"
                company = await company_el.inner_text() if company_el else "N/A"
                loc = await location_el.inner_text() if location_el else "N/A"

                # Always construct a normalized URL
                link = f"https://www.indeed.com/viewjob?jk={job_id}"

                all_results.append({
                    "Title": title,
                    "Company": company,
                    "Location": loc,
                    "URL": link
                })
        df = pd.DataFrame(all_results)
        #print(df)
        output_file = "indeed_results.csv"
        df.to_csv(output_file, index=False, encoding="utf-8-sig")
        print(f"\n💾 Saved {len(all_results)} jobs to {output_file}")

        await context.close()

if __name__ == "__main__":
    job = input("Enter job title: ").strip()
    location = input("Enter location: ").strip()
    days = input("Enter days (default=3): ").strip()
    days = int(days) if days else 3
    max_pages = input("Enter the number of pages to scrape (default=5): ").strip()
    max_pages = int(max_pages) if max_pages else 5

    asyncio.run(scrape_indeed(job, location, days, max_pages))