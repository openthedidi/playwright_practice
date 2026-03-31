# need install pytest-asyncio first
from playwright.async_api import Page, expect, async_playwright
import pytest


@pytest.mark.asyncio
async def test_verifyPageUrl():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://www.saucedemo.com/")
        myurl = page.url
        await expect(page).to_have_url("https://www.saucedemo.com/")
        print(myurl)
        await browser.close()
