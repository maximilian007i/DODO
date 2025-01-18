import undetected_chromedriver as uc # это даже отдельно скрытый браузер использовал
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_pizza_names(url):
    # Запускаем браузер
    driver = uc.Chrome()
    try:
        # Открываем страницу
        driver.get(url)

        # Ожидаем, пока элементы с классом 'menu-item-title' станут доступными
        wait = WebDriverWait(driver, 20)
        pizza_elements = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "menu-item-title")))

        # Извлекаем текст наименований пиццы
        pizza_names = [pizza.text for pizza in pizza_elements]

        return pizza_names

    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return []

    finally:
        driver.quit()

if __name__ == "__main__":
    url = "https://dodopizza.ru/belgorod"
    pizza_names = scrape_pizza_names(url)

    print("Названия пиццы:")
    for name in pizza_names:
        print(name)