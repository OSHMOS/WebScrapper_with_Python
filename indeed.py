import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

def extract_indeed_pages():
    result = requests.get(URL)

    soup = BeautifulSoup(result.text, 'html.parser')

    pagination = soup.find('div', {'class': 'pagination'})

    links = pagination.find_all('a')
    pages=[]
    for link in links[:-1]:
        pages.append(int(link.string))

    max_page = pages[-1]
    return max_page

def extract_indeed_jobs(last_page):
    jobs = []
    # for page in range(last_page):
    result = requests.get(f'{URL}&start={0*LIMIT}')
    soup = BeautifulSoup(result.text, 'html.parser')
    results = soup.find_all('div', {'class': 'fs-unmask'})
    print('')
    for result in results:
        job_title = result.find('h2', {'class':'jobTitle'})
        title = job_title.find('span').string
        company = result.find('span', {'class':'companyName'})
        
        if title == 'new':
            title = job_title.find_all('span')[1].string

        if company is not None:
            company = company.string
        else:
            company = None
            print(title, company)

        print(title, company)
    return jobs
