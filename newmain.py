
import requests
from bs4 import BeautifulSoup
from save_json import store_data_to_json


a = {'Business Operations': ['https://www.smartrecruiters.com/Cermaticom/743999905121103-Desk%20Collection', 'https://www.smartrecruiters.com/Cermaticom/743999900329683-Credit%20Analyst', 'https://www.smartrecruiters.com/Cermaticom/743999900317598-Car%20Insurance%20Telesales%20(Supervisor)', 'https://www.smartrecruiters.com/Cermaticom/743999897145693-Health%20Insurance%20Telemarketing', 'https://www.smartrecruiters.com/Cermaticom/743999896625403-Offline%20Promoter%20(Jabodetabek)', 'https://www.smartrecruiters.com/Cermaticom/743999896199337-Field%20Collection-Bandung', 'https://www.smartrecruiters.com/Cermaticom/743999896166683-Field%20Collection', 'https://www.smartrecruiters.com/Cermaticom/743999893825006-Offline%20Promoter%20(Bali)', 'https://www.smartrecruiters.com/Cermaticom/743999893814553-Offline%20Promoter%20(Jawa%20Tengah)', 'https://www.smartrecruiters.com/Cermaticom/743999893813003-Offline%20Promoter%20(Jawa%20Timur)', 'https://www.smartrecruiters.com/Cermaticom/743999893812183-Offline%20Promoter%20(Jawa%20Barat)', 'https://www.smartrecruiters.com/Cermaticom/743999891515563-Anti%20Fraud%20Analyst', 'https://www.smartrecruiters.com/Cermaticom/743999891514283-Insurance%20Claim%20Analyst', 'https://www.smartrecruiters.com/Cermaticom/743999890422448-Field%20Collection-Surabaya', 'https://www.smartrecruiters.com/Cermaticom/743999880518513-Car%20Insurance%20Telemarketing', 'https://www.smartrecruiters.com/Cermaticom/743999879343854-Team%20Leader%20Desk%20Collection', 'https://www.smartrecruiters.com/Cermaticom/743999875845201-Telemarketing', 'https://www.smartrecruiters.com/Cermaticom/743999862763991-Retail%20Credit%20Risk%20Analytics%20&%20Modelling%20Manager', 'https://www.smartrecruiters.com/Cermaticom/743999862762431-Head%20of%20Compliance', 'https://www.smartrecruiters.com/Cermaticom/743999862760821-Supervisor%20Field%20Collection', 'https://www.smartrecruiters.com/Cermaticom/743999862461145-Team%20Leader%20Field%20Collection', 'https://www.smartrecruiters.com/Cermaticom/743999832564229-Field%20Investigator'], 'People Operations': ['https://www.smartrecruiters.com/Cermaticom/743999904936753-Finance%20Staff', 'https://www.smartrecruiters.com/Cermaticom/743999904865246-Procurement%20Staff', 'https://www.smartrecruiters.com/Cermaticom/743999900534203-Internal%20Audit%20Staff', 'https://www.smartrecruiters.com/Cermaticom/743999894359514-Asset%20Management%20Staff', 'https://www.smartrecruiters.com/Cermaticom/743999891514663-Senior%20Litigation%20Officer', 'https://www.smartrecruiters.com/Cermaticom/743999891514473-Legal%20Senior%20Associate', 'https://www.smartrecruiters.com/Cermaticom/743999888640973-Compliance%20(Senior%20Associate%20/%20Manager)', 'https://www.smartrecruiters.com/Cermaticom/743999866765062-Internal%20Audit%20(Lead/Manager)'], 'Business Development': ['https://www.smartrecruiters.com/Cermaticom/743999904867613-Business%20Development%20Manager', 'https://www.smartrecruiters.com/Cermaticom/743999902710524-Insurance%20Partnership%20Manager', 'https://www.smartrecruiters.com/Cermaticom/743999899506872-Business%20Development%20Support', 'https://www.smartrecruiters.com/Cermaticom/743999897538273-Insurance%20Technical%20Manager', 'https://www.smartrecruiters.com/Cermaticom/743999896639234-Business%20Development%20Manager%20-%20Employee%20Loan', 'https://www.smartrecruiters.com/Cermaticom/743999896162573-Health%20Insurance%20Claim%20Head', 'https://www.smartrecruiters.com/Cermaticom/743999895530194-District%20Sales%20Manager%20(Jawa%20timur)', 'https://www.smartrecruiters.com/Cermaticom/743999895528998-Distric%20Sales%20Manager%20(Bali)', 'https://www.smartrecruiters.com/Cermaticom/743999894109326-Insurance%20Business%20Development%20-%20Employee%20Benefit', 'https://www.smartrecruiters.com/Cermaticom/743999894104893-District%20Sales%20Manager', 'https://www.smartrecruiters.com/Cermaticom/743999893814213-Business%20Development%20Associate', 'https://www.smartrecruiters.com/Cermaticom/743999893814123-Business%20Development%20Manager%20-%20Merchant%20Acquisition', 'https://www.smartrecruiters.com/Cermaticom/743999891773878-General%20Insurance%20Marketing', 'https://www.smartrecruiters.com/Cermaticom/743999891772934-Head%20of%20Claim%20and%20Placement', 'https://www.smartrecruiters.com/Cermaticom/743999891515783-Health%20Insurance%20Account%20Manager', 'https://www.smartrecruiters.com/Cermaticom/743999891514393-Business%20Development%20Manager%20Insurance%20(All%20Levels)', 'https://www.smartrecruiters.com/Cermaticom/743999891506733-Business%20Development%20Associate%20(Jakarta)', 'https://www.smartrecruiters.com/Cermaticom/743999891506563-Merchant%20Relation%20Officer%20(Surabaya)', 'https://www.smartrecruiters.com/Cermaticom/743999890936729-Head%20of%20Marketing%20-%20General%20Insurance', 'https://www.smartrecruiters.com/Cermaticom/743999883625093-District%20Sales%20Manager', 'https://www.smartrecruiters.com/Cermaticom/743999871360770-Head%20of%20Marketing%20-%20Employee%20Benefit', 'https://www.smartrecruiters.com/Cermaticom/743999865105541-Head%20Of%20Placement%20Insurance%20-%20Employee%20Benefit', 'https://www.smartrecruiters.com/Cermaticom/743999860344921-Mutual%20Fund%20Business%20Development%20Manager%20-%20Bandung', 'https://www.smartrecruiters.com/Cermaticom/743999855462234-Mutual%20Fund%20Business%20Development%20Manager', 'https://www.smartrecruiters.com/Cermaticom/743999850971431-General%20Insurance%20Marketing', 'https://www.smartrecruiters.com/Cermaticom/743999842499771-Mutual%20Fund%20Business%20Development%20Manager', 'https://www.smartrecruiters.com/Cermaticom/743999832533238-General%20Insurance%20Marketing%20Staff'], 'Risk': ['https://www.smartrecruiters.com/Cermaticom/743999903964083-Data%20Scientist%20-%20Risk%20Platform', 'https://www.smartrecruiters.com/Cermaticom/743999903962133-Data%20Scientist'], 'Engineering': ['https://www.smartrecruiters.com/Cermaticom/743999902785605-Software%20Engineer%20In%20Test%20Automation%20Testing', 'https://www.smartrecruiters.com/Cermaticom/743999901966353-Lead%20Software%20Quality%20Assurance%20.', 'https://www.smartrecruiters.com/Cermaticom/743999901966323-Senior%20Software%20Quality%20Assurance%20.', 'https://www.smartrecruiters.com/Cermaticom/743999901966303-Lead%20Software%20Quality%20Assurance', 'https://www.smartrecruiters.com/Cermaticom/743999901966233-Senior%20Software%20Quality%20Assurance', 'https://www.smartrecruiters.com/Cermaticom/743999901761756-Lead%20Data%20Engineer-%20Bangalore', 'https://www.smartrecruiters.com/Cermaticom/743999897207847-Software%20Quality%20Assurance%20%20-%20%20Manual%20Testing%20.', 'https://www.smartrecruiters.com/Cermaticom/743999896690090-SEIT%20(%20Software%20Engineer%20in%20Test)', 'https://www.smartrecruiters.com/Cermaticom/743999896672229-Lead%20SEIT%20(Lead%20Software%20Engineer%20in%20Test)', 'https://www.smartrecruiters.com/Cermaticom/743999891746578-Senior%20Data%20Scientist%20-%20Fraud%20Modelling', 'https://www.smartrecruiters.com/Cermaticom/743999891746803-Software%20Engineer%20(Senior/Principal%20Position)', 'https://www.smartrecruiters.com/Cermaticom/743999891746643-Software%20Engineer%20(Associate/Senior/Principal%20Position)', 'https://www.smartrecruiters.com/Cermaticom/743999890040313-Lead%20Data%20Engineer', 'https://www.smartrecruiters.com/Cermaticom/743999874413809-Data%20Engineer%20-%20India'], 'Digital Marketing and Content': ['https://www.smartrecruiters.com/Cermaticom/743999899762383-Telemarketing%20Borrower', 'https://www.smartrecruiters.com/Cermaticom/743999891514413-Public%20Relations%20Lead'], 'Product': ['https://www.smartrecruiters.com/Cermaticom/743999894578783-Product%20Owner%20(Entry,%20Mid%20and%20Senior%20%20Levels)', 'https://www.smartrecruiters.com/Cermaticom/743999894578377-Product%20Owner%20(Entry,%20Mid%20and%20Senior%20Levels%20Available)%20.', 'https://www.smartrecruiters.com/Cermaticom/743999848691301-Product%20Management%20-%20People%20Lead%20(Senior/Head/VP%20Level)'], 'Strategic Operations': ['https://www.smartrecruiters.com/Cermaticom/743999880478048-CEO%20Office%20-%20Special%20Projects', 'https://www.smartrecruiters.com/Cermaticom/743999879326823-Operations%20Strategist']}
dept_wise_jobs = dict()
for k, v in a.items():
    for url in v:
        response = requests.get(url)
        parsed_html = BeautifulSoup(response.content, 'html.parser')
        job = parsed_html.find_all('div', class_='jobad site')
        for j in job:
            job_posted_by, job_descr, job_qualification, location = None, None, None, None
            job_header = j.find('header', class_='jobad-header').find_all('a')
            for t in job_header:
                job_posted_by = t.get('title').strip()
            if job_posted_by.lower() == 'indodana':
                if j.find('div', itemprop='qualifications') is not None:
                    job_qualification = j.find('div', itemprop='qualifications').text.strip()
                job_descr = j.find('div', itemprop='responsibilities').text.strip()
            elif job_posted_by.lower() == 'cermati.com':
                job_qualification = j.find('div', itemprop='responsibilities').text.strip()
                job_descr = j.find('div', class_='wysiwyg').text.strip()
            job_location = j.find_all('spl-job-location')
            for l in job_location:
                location = l.get('formattedaddress').strip()
            job_map = {
                "title": j.find('h1', class_='job-title').text.strip(),
                "description": job_descr,
                "posted by": job_posted_by,
                "qualification": job_qualification,
                "location": location
            }
            if k not in dept_wise_jobs.keys():
                dept_wise_jobs[k] = list()
            dept_wise_jobs[k].append(job_map)
        store_data_to_json(dept_wise_jobs)



# def check_exists_by_xpath(xpath):
#     try:
#         driver.find_element(By.XPATH, xpath)
#     except NoSuchElementException:
#         return False
#     return True
#
#
# def job_post():
#     btn_num = 2
#     try:
#         elements = driver.find_elements(By.XPATH, '//*[@id="career-jobs"]/div/div[6]/div')
#         for e in elements:
#             job_details(e)
#     except NoSuchElementException:
#         print('No element')
#
#
# def job_details(e):
#     btn_num = 2
#
#     while check_exists_by_xpath(f'//button[text()="{btn_num}"]'):
#         try:
#             elements1 = e.find_elements(By.CLASS_NAME, 'page-job-list-wrapper')
#             print(len(elements1))
#             index = 1
#             total = len(elements1)
#             for el in elements1:
#                 if index <= total:
#                     print(el.find_element(By.XPATH, f'//*[@id="career-jobs"]/div/div[6]/div/div[{index}]/p[1]').text)
#                     print(el.find_element(By.XPATH, f'//*[@id="career-jobs"]/div/div[6]/div/div[{index}]/a').get_attribute('href'))
#                     index += 1
#
#             time.sleep(10)
#             driver.find_element(By.XPATH, f'//button[text()="{btn_num}"]').click()
#             WebDriverWait(driver, 10).until(EC.url_changes(url))
#             btn_num += 1
#         except NoSuchElementException:
#             print('No next page')
#             return False
#
#
# url = "https://www.cermati.com/karir"
#
# driver = webdriver.Chrome()
# driver.get(url)
#
# # Find and click the "View All Jobs" button
# view_all_jobs_button = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.XPATH, '//*[@id="career-landing"]/div/div[4]/div/a')))
# view_all_jobs_button.click()
#
# # Wait for the new page to load
# WebDriverWait(driver, 10).until(EC.url_changes(url))
#
# # Scrape the page as desired
# # ...
# # select elements by class name
# job_post_list = []
#
# job_post()
#
#
# driver.quit()




