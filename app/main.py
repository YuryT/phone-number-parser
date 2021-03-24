from .DataSource import DataSource


def reload_contacts(ds):
    companies = ds.get_companies_to_reload()
    refreshed_data = []
    for company in companies:
        company.load_contact_pages()
        refreshed_data.append(company)


def parse_contacts(mode, ds):
    companies = ds.get_companies_to_parse()
    for c in companies:
        numbers_set = set()
        for page in c.contact_pages:
            numbers_set.update(page.parse(mode))
        c.phone_numbers = list(numbers_set)