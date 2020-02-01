import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import pyautogui


def get_profile():
    profile = webdriver.FirefoxProfile()
    profile.set_preference(
        "general.useragent.override",
        "Mozilla/5.0 (Android 8.1.0; Mobile; rv:61.0) Gecko/61.0 Firefox/61.0",
    )
    return profile


def post_to_instagram(username, password, photo, caption, share=False):
    browser = webdriver.Firefox(
        get_profile(), firefox_binary="/usr/bin/firefox-trunk"
    )
    browser.set_window_position(0, 0)
    browser.set_window_size(500, 1200)
    browser.get("https://www.instagram.com")
    wait = WebDriverWait(browser, 30)

    login_xpath = "//button[contains(text(),'Log In')]"
    wait.until(EC.element_to_be_clickable((By.XPATH, login_xpath)))
    browser.find_element_by_xpath(login_xpath).click()

    time.sleep(2)
    username_xpath = "//input[@name='username']"
    password_xpath = "//input[@name='password']"

    browser.find_element_by_xpath(username_xpath).send_keys(username)
    password_input = browser.find_element_by_xpath(password_xpath)
    password_input.send_keys(password)
    password_input.submit()

    cred_save_xpath = "//button[contains(text(),'Not Now')]"
    wait.until(EC.element_to_be_clickable((By.XPATH, cred_save_xpath)))
    browser.find_element_by_xpath(cred_save_xpath).click()

    new_post_xpath = "//div[@role='menuitem']"
    wait.until(EC.element_to_be_clickable((By.XPATH, new_post_xpath)))
    browser.find_element_by_xpath(new_post_xpath).click()

    time.sleep(1)
    pyautogui.hotkey("ctrl", "l")
    pyautogui.typewrite(photo)
    time.sleep(1)
    pyautogui.hotkey("enter")
    time.sleep(1)

    next_xpath = "//button[contains(text(),'Next')]"
    wait.until(EC.element_to_be_clickable((By.XPATH, next_xpath)))
    browser.find_element_by_xpath(next_xpath).click()

    share_xpath = "//button[contains(text(),'Share')]"
    wait.until(EC.element_to_be_clickable((By.XPATH, share_xpath)))

    textarea = "//textarea"
    browser.find_element_by_xpath(textarea).send_keys(caption)

    # Share!!!
    if share:
        browser.find_element_by_xpath(share_xpath).click()


if __name__ == "__main__":
    import sys

    username, password, photo, caption = (
        sys.argv[1],
        sys.argv[2],
        sys.argv[3],
        sys.argv[4],
    )
    post_to_instagram(username, password, photo, caption)
