import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

user_agent = UserAgent()


def parse_vacancies(link, parse_pages=1):
    result = []
    domain = '/'.join(link.split('/')[:3])
    for page in range(1, parse_pages + 1):
        if page > 1:
            link += f'&page={page}'
        html = get_html(link, useragent=True)
        vacancies = html.find_all('li', class_='list-jobs__item list__item')
        for vacancy in vacancies:
            url = domain + vacancy.find('a', class_='profile').get('href')
            vacancy = get_html(url)
            short_info_vacancy = ShortInfoVacancy(vacancy, domain, url)
            result.append(short_info_vacancy())
        print(result)
    return result


def get_html(link, useragent=False):
    if useragent:
        response = requests.get(link, headers={'User-Agent': user_agent.random})
    else:
        response = requests.get(link)
    return BeautifulSoup(response.text, "lxml")


class ShortInfoVacancy:
    def __init__(self, vacancy, domain, url):
        self.vacancy = vacancy
        self.domain = domain
        self.url = url
        self.title = None
        self.publication_date = None

    def __call__(self, *args, **kwargs):
        return {
            'url': self.url,
            'title': self.get_title(),
            'salary': self.get_salary(),
            'company': self.get_company(),
            'recruiter': self.get_recruiter(),
            'publication_date': self.get_publication_date(),
            'views': self.get_views(),
            'reviews': self.get_reviews(),
            'short_description': self.get_short_description(),
            'description': self.get_description(),
            'other': self.get_additional_info()
        }

    # def get_url(self, domain):
    #     return domain + self.vacancy.find('a', class_='profile').get('href')

    def get_title(self):
        title = self.vacancy.find('div',
                                  class_='detail--title-wrapper'
                                  ).get_text(strip=True, separator='|')
        self.title = title.split('|')
        return self.title[0]

    def get_publication_date(self):
        self.publication_date = self.vacancy.find(
            'p', class_='text-muted').get_text(separator='|', strip=True)
        self.publication_date = self.publication_date.split('|')
        return self.publication_date[0].replace(
            'Вакансія опублікована', '').strip()

    def get_views(self):
        return self.publication_date[1]

    def get_reviews(self):
        return self.publication_date[2]

    def get_salary(self):
        return self.title[1] if len(self.title) > 1 else None

    def get_short_description(self):
        return self.vacancy.find('p', class_='job-post--short-description'
                                 ).get_text(strip=True)

    def get_description(self):
        return self.vacancy.find('div', class_='profile-page-section'
                                 ).get_text(strip=True)

    def get_company(self):
        return self.vacancy.find('a', class_="job-details--title"
                                 ).get_text(strip=True)

    def get_recruiter(self):
        return self.vacancy.find('a', class_="job-details--recruiter-name"
                                 ).get_text(strip=True)

    def get_additional_info(self):
        additional_info = self.vacancy.find_all(
            'div', class_='job-additional-info--item-text')
        return [item.get_text(strip=True) for item in additional_info]


parse_vacancies(
    'https://djinni.co/jobs/?primary_keyword=Python&exp_level=no_exp&exp_level=1y&exp_level=2y')
