"""
This script takes screenshots of urls you put in the 

async def main():

function. 

Dependenices: 
pip install playwright
playwright install
sudo playwright install-deps                     


"""
import asyncio
import os
from playwright.async_api import async_playwright

async def take_screenshots(urls, output_dir="screenshots"):
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        
        for idx, url in enumerate(urls, 1):
            try:
                print(f"Processing URL {idx}: {url}")
                page = await browser.new_page()
                
                # Navigate to the URL and wait until the page is fully loaded
                await page.goto(url, wait_until="networkidle", timeout=30000)
                
                # Get the page title for filename (sanitize it)
                title = (await page.title()).replace(" ", "_").replace("/", "_").replace(":", "_")
                if not title:
                    title = f"page_{idx}"
                
                # Take JPEG screenshot
                jpeg_path = os.path.join(output_dir, f"{title}.jpg")
                await page.screenshot(path=jpeg_path, full_page=True, quality=100)
                print(f"Saved JPEG screenshot: {jpeg_path}")
                
                # Take PDF screenshot
                pdf_path = os.path.join(output_dir, f"{title}.pdf")
                await page.pdf(path=pdf_path, format="A4", print_background=True)
                print(f"Saved PDF screenshot: {pdf_path}")
                
                await page.close()
                
            except Exception as e:
                print(f"Error processing {url}: {str(e)}")
        
        await browser.close()

async def main():
    # List of URLs to process (replace with your own URLs)
    # You are experimenting with the following: https://www.coursehero.com/file/168305435/DTR-anxiety-and-depressionpdf/
    # the proper format for multiple is: 
    #  urls = [
    # "https://example.com",
    # "https://python.org",
    # "https://github.com"
    # ]
    urls = [
        "https://www.coursehero.com/file/168305435/DTR-anxiety-and-depressionpdf/",
        "https://python.org",
        "https://github.com"
    ]git status
    
    
    # Run the screenshot function
    await take_screenshots(urls)

if __name__ == "__main__":
    asyncio.run(main())