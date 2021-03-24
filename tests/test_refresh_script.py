
from unittest.mock import patch
from app import main
from app.models import Company, MODE_GOOGLE_DRIVEN, MODE_REGEX, MODE_REGEX_BS4
from app.DataSource import DataSource


def test_google_parser():
    print('\r\ngoogle driven parsing')
    ds = DataSource()
    main.reload_contacts(ds)
    main.parse_contacts(MODE_GOOGLE_DRIVEN, ds)
    ds.print_content()


def test_regex_parsing():
    print('\r\nregex driven parsing')
    ds = DataSource()
    main.reload_contacts(ds)
    main.parse_contacts(MODE_REGEX, ds)
    ds.print_content()

def test_regex_bs4_parsing():
    print('\r\nregex_bs4 driven parsing')
    ds = DataSource()
    main.reload_contacts(ds)
    main.parse_contacts(MODE_REGEX_BS4, ds)
    ds.print_content()

@patch.object(Company, 'get_contact_page_text')
def test_refresh_script_with_fake_data(get_contact_page_text_mock):
    ds = DataSource(
        companies=[
            Company(
                name='fake_company',
                contact_pages_urls=['https://yandex.ru/'],
            ),
        ]
    )
    get_contact_page_text_mock.return_value = \
        'sdasdas 666-66-66 +79525573453 sdfdfsdf'

    for mode in [MODE_REGEX, MODE_GOOGLE_DRIVEN]:
        main.reload_contacts(ds)
        main.parse_contacts(mode, ds)
        ds.print_content()