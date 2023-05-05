from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def instantiate_driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=400,868")

    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    options.add_argument('user-agent={0}'.format(user_agent))

    return webdriver.Chrome(options=options)
