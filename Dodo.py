#Тут названия выгружаються.
import asyncio
from playwright.async_api import async_playwright
import time

async def check_access(url):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        )
        page = await context.new_page()

        await page.set_extra_http_headers({
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive"
        })

        try:
            response = await page.goto(url)
            if response.status == 200:
                print(f"Сайт {url} доступен.")
                time.sleep(10)

                # Извлекаем названия продуктов
                product_elements = await page.locator('span.sc-77undf-1.jHwIyu').element_handles()
                product_names = [await element.inner_text() for element in product_elements]

                if product_names:
                    print("Названия продуктов:")
                    for name in product_names:
                        print(name)
                else:
                    print("Продукты не найдены.")
            else:
                print(f"Сайт {url} недоступен. Статус код: {response.status}")
        except Exception as e:
            print(f"Произошла ошибка при проверке доступа к сайту: {e}")
        finally:
            await browser.close()

# URL сайта Додо Пицца
url = 'https://dodopizza.ru/belgorod'

# Запускаем асинхронную функцию
asyncio.run(check_access(url))
