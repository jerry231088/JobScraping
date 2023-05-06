from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from scraping_jobs import job_posts


def main(web_driver, url):
    web_driver.get(url)

    # Find and click the "View All Jobs" button
    view_all_jobs_button = WebDriverWait(web_driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="career-landing"]/div/div[4]/div/a')))
    view_all_jobs_button.click()

    # Wait for the new page to load
    WebDriverWait(web_driver, 10).until(EC.url_changes(url))
    job_posts(web_driver)


if __name__ == '__main__':
    # Web URL
    job_post_url = f'https://www.cermati.com/karir'
    # check for different Browser, if Chrome doesn't exist
    driver = webdriver.Chrome()
    main(driver, job_post_url)
    driver.quit()
