from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


def test_title_main(browser, get_url):
    browser.get(get_url)
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.title-content__left '
                                                                                        '.registration-button')))
    assert "Образовательный портал" in browser.title, "text not found"