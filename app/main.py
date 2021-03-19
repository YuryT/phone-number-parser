from .DataSource import DataSource


def refresh_contacts(mode):
    ds = DataSource()
    companies = ds.get_companies_to_refresh()
    refreshed_data = []
    for company in companies:
        company.refresh_contacts(mode)
        refreshed_data.append(company)
    ds.save_updated_companies(refreshed_data)


def validate_phone_numbers(phone_numbers_list):
    for n in phone_numbers_list:
        validate_phone_number(n)


def validate_phone_number(number):
    raise NotImplementedError()