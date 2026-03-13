import pytest
import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Список ссылок для параметризации
urls = [
    "https://stepik.org/lesson/236905/step/1"
]


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('url', urls)
def test_stepik_feedback(browser, url):
    # Открываем страницу
    browser.get(url)

    # Авторизация
    # Ждем кнопку "Войти" и нажимаем её
    login_link = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.navbar__auth"))
    )
    login_link.click()

    # Вводим логин и пароль (ЗАМЕНИТЕ НА СВОИ)
    email_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='login']"))
    )
    email_input.send_keys("login")

    password_input = browser.find_element(By.CSS_SELECTOR, "input[name='password']")
    password_input.send_keys("password")

    # Нажимаем кнопку "Войти"
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

    # Ждем завершения авторизации (появление имени пользователя)
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".navbar__profile"))
    )

    # Небольшая пауза для полной загрузки страницы
    time.sleep(2)

    # Вычисляем ответ
    answer = math.log(int(time.time()))

    # Пробуем найти поле для ввода ответа
    try:
        # Поле для ввода ответа
        textarea = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "textarea"))
        )
        textarea.clear()
        textarea.send_keys(str(answer))

        # Кнопка отправки
        submit_answer = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))
        )
        submit_answer.click()

        # Ждем появления фидбека
        time.sleep(3)

        # Ищем фидбек (черное поле с результатом)
        feedback = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))
        )

        feedback_text = feedback.text
        print(f"\nФидбек для {url}: '{feedback_text}'")  # Выводим фидбек в консоль

        # Проверяем, что фидбек равен "Correct!"
        assert feedback_text == "Correct!", f"Текст фидбека: '{feedback_text}'"

    except Exception as e:
        print(f"\nОшибка на {url}: {str(e)}")
        # Если не нашли поле или кнопку, выводим что есть на странице
        page_source = browser.page_source
        if "Correct!" in page_source:
            print("На странице есть текст 'Correct!'")
        raise e