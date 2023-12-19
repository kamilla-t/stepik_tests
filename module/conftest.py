from flask import request
from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="es", 
                     help="Choose language: es or ru")


@pytest.fixture(scope="function")
def browser(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    user_language = request.config.getoption("language")
    print(f"\nstart browser with lang {user_language} for test..")
    
    if user_language == "es":
        options.add_experimental_option('prefs', {'intl.accept_languages': 'es-ES'})
    elif user_language == "ru":
        options.add_experimental_option('prefs', {'intl.accept_languages': 'ru-RU'})
    elif user_language == "fr":
        options.add_experimental_option('prefs', {'intl.accept_languages': 'fr-FR'})
    elif user_language == "en":
        options.add_experimental_option('prefs', {'intl.accept_languages': 'en-EN'})
    else:
        raise pytest.UsageError("--language should be es or ru")
    
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()

# вызов 
# pytest -s -v --language=es test_items.py
