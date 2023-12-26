import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FireOptions
from selenium.webdriver.chrome.service import Service

def pytest_addoption(parser):
    parser.addoption(
        '--language',
        action='store',
        default='', 
        type=str,
        required=False,
        help="Choose: language"
    )    
    parser.addoption(
        '--browser_name',
        action='store',
        default='chrome', 
        type=str,
        required=False,
        help="Choose: browser"
    )

@pytest.fixture(scope='function')
def browser(request):

    user_language = request.config.getoption('language')    
    browser_name = request.config.getoption('browser_name')

    if browser_name == 'firefox':
        print('\nfirefox for test..')
        options = FireOptions()
        options.set_preference("intl.accept_languages", user_language) 
        browser = webdriver.Firefox(options=options)                  

    elif browser_name == 'chrome':
        # Path to chromedriver.exe
        driver_path = "C:\\drivers\\chromedriver-win64\\chromedriver.exe"
        service = Service(driver_path)
        print('\nchrome for test..')        
        options = ChromeOptions()       
        options.add_experimental_option('prefs', 
                                        {'intl.accept_languages': user_language}) 
        browser = webdriver.Chrome(service=service, options=options) 

    print(f'\nlanguage: {user_language}..')

    yield browser
    print('\nquit..')
    browser.quit()
