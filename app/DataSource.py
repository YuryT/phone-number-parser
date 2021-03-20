from typing import List
from .models import Company


class DataSource:
    def __init__(self):
        pass

    # get data from db or api
    def get_companies_to_refresh(self) -> List[Company]:
        return [Company(
            name='masterdel',
            contact_pages=[
                'https://masterdel.ru',
                'https://masterdel.ru/reg.php',
            ],
        ),
            Company(
                name='repetitors.info',
                contact_pages=[
                    'https://repetitors.info/',
                    'https://repetitors.info/repetitor/',
                ],
            )]

    #  write data to db or post to api
    def save_updated_companies(self, companies: List[Company]):
        print('Output:')
        for company in companies:
            print(company.name)
            print(company.phone_numbers)