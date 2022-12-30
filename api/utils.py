from datetime import datetime

import requests
from bs4 import BeautifulSoup


def parse_short_data(link, parse_pages=1):
    result = []
    domain = '/'.join(link.split('/')[:3])
    for page in range(1, parse_pages + 1):
        if page > 1:
            link += f'&page={page}'
        response = requests.get(link)
        html = BeautifulSoup(response.text, "lxml")
        vacancies = html.find_all('li', class_='list-jobs__item list__item')
        for vacancy in vacancies:
            short_info_vacancy = ShortInfoVacancy(vacancy, domain)
            result.append(short_info_vacancy())
        print(result)
    return result


def parse_full(links):
    result = []
    for vacancy in links['url']:
        response = requests.get(vacancy)
        html = BeautifulSoup(response.json())
        print(html)
    print(result)
    return result


class ShortInfoVacancy:
    def __init__(self, vacancy, domain):
        self.vacancy = vacancy
        self.domain = domain

    def __call__(self, *args, **kwargs):
        return {
            'url': self.get_url(self.domain),
            'title': self.get_title(),
            'publication_date': self.get_publication_date(),
            'views': self.get_views(),
            'reviews': self.get_reviews(),
            'salary': self.get_salary(),
            'description': self.get_description(),
            'company': self.get_company(),
            'recruiter': self.get_recruiter(),
            'geo': self.get_geo(),
            'other': self.get_other_info()
        }

    def get_url(self, domain):
        return domain + self.vacancy.find('a', class_='profile').get('href')

    def get_title(self):
        return self.vacancy.find('a', class_='profile').text.strip('\n')

    def get_publication_date(self):
        pub_date = self.vacancy.find(
            'div',
            class_='text-date order-2 ml-md-auto pr-2 mb-2 mb-md-0 nowrap'
        ).text.split()
        if pub_date[0] == 'сьогодні':
            return str(datetime.now())[8:10]
        elif pub_date[0] == 'вчора':
            date = str(datetime.now())[8:10]
            return f'{int(date) - 1}'
        else:
            return ' '.join(pub_date[:2])

    def get_views(self):
        return self.vacancy.find('span', class_="ml-2").get('title')

    def get_reviews(self):
        return self.vacancy.find('span', class_="ml-2"
                                 ).next_sibling.next_sibling.get('title')

    def get_salary(self):
        salary = self.vacancy.find('span', class_='public-salary-item')
        return salary.text if salary else None

    def get_description(self):
        return self.vacancy.find('div', class_='list-jobs__description'
                                 ).text.replace('\n', ' ').strip()

    def get_company(self):
        return self.vacancy.find('div', class_="list-jobs__details__info"
                                 ).a.text.strip()

    def get_recruiter(self):
        recruiter = self.vacancy.find('a', class_="link-muted"
                                      ).text.replace('\n', '').split(' ')
        return ''.join(recruiter)

    def get_geo(self):
        return self.vacancy.find('span', class_="location-text"
                                 ).text.strip().replace('\n', ' ')

    def get_other_info(self):
        other_info = self.vacancy.find_all('nobr')
        return [item.text.strip('·').strip() for item in other_info]


parse_short_data(
    'https://djinni.co/jobs/?primary_keyword=Python&exp_level=no_exp&exp_level=1y&exp_level=2y')
