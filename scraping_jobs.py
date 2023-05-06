import requests
import time

from bs4 import BeautifulSoup
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from save_json import store_data_to_json
from utils import check_exists_by_xpath


def job_posts(web_driver):
    dept_element_map = dict()
    try:
        elements = web_driver.find_elements(By.XPATH, '//*[@id="career-jobs"]/div/div[6]/div')
        for e in elements:
            jd = job_details(web_driver, e)
            for k, v in jd.items():
                if k not in dept_element_map:
                    dept_element_map[k] = list()
                dept_element_map[k].extend(v)
            get_jd_and_qualifications(dept_element_map)
    except NoSuchElementException:
        print('No such element present!')


def job_details(web_driver, e):
    dept_element_map = dict()  # Dept: Href
    btn_num = 1
    while check_exists_by_xpath(web_driver, f'//button[text()="{btn_num}"]'):
        try:
            btn_num += 1
            for k, v in create_dept_url_map(e).items():
                if k not in dept_element_map:
                    dept_element_map[k] = list()
                dept_element_map[k].extend(v)
            web_driver.find_element(By.XPATH, f'//button[text()="{btn_num}"]').click()
            time.sleep(5)
        except NoSuchElementException:
            print('No next page!')
    return dept_element_map


def create_dept_url_map(e):
    dept_element_map = dict()  # Dept: Href
    job_list_wrapper_element = e.find_elements(By.CLASS_NAME, 'page-job-list-wrapper')
    index = 1
    total = len(job_list_wrapper_element)
    print(f'total: {total}')
    for el in job_list_wrapper_element:
        if index <= total:
            key = el.find_element(By.XPATH, f'//*[@id="career-jobs"]/div/div[6]/div/div[{index}]/p[1]'). \
                text.strip()
            value = el.find_element(By.XPATH, f'//*[@id="career-jobs"]/div/div[6]/div/div[{index}]/a'). \
                get_attribute('href')
            if key not in dept_element_map.keys():
                dept_element_map[key] = list()
            index += 1
            if key.lower().strip() == 'product':
                print(value)
            dept_element_map[key].append(value)
    return dept_element_map


def get_jd_and_qualifications(dept_element_map):
    dept_wise_jobs = dict()
    for k, v in dept_element_map.items():
        for url in v:
            response = requests.get(url)
            parsed_html = BeautifulSoup(response.content, 'html.parser')
            job = parsed_html.find_all('div', class_='jobad site')
            dept_map = create_dept_wise_map(k, job)
            for key, val in dept_map.items():
                if key not in dept_wise_jobs:
                    dept_wise_jobs[key] = list()
                dept_wise_jobs[key].extend(val)
    store_data_to_json(dept_wise_jobs)


def create_dept_wise_map(dept, job):
    dept_wise_jobs_details = dict()
    job_map_list = list()
    for j in job:
        job_posted_by, job_desc, job_qualification, location = None, None, None, None
        job_header = j.find('header', class_='jobad-header').find_all('a')
        for t in job_header:
            job_posted_by = t.get('title').strip()
        if job_posted_by.lower() == 'indodana':
            if j.find('div', itemprop='qualifications') is not None:
                job_qualification = j.find('div', itemprop='qualifications').text.strip()
            job_desc = j.find('div', itemprop='responsibilities').text.strip()
        elif job_posted_by.lower() == 'cermati.com':
            job_qualification = j.find('div', itemprop='responsibilities').text.strip()
            job_desc = j.find('div', class_='wysiwyg').text.strip()
        job_location = j.find_all('spl-job-location')
        for loc in job_location:
            location = loc.get('formattedaddress').strip()
        job_map = {
            "title": j.find('h1', class_='job-title').text.strip(),
            "description": job_desc,
            "posted by": job_posted_by,
            "qualification": job_qualification,
            "location": location
        }
        if dept not in dept_wise_jobs_details.keys():
            dept_wise_jobs_details[dept] = list()
        job_map_list.append(job_map)
    dept_wise_jobs_details[dept].extend(job_map_list)
    return dept_wise_jobs_details
