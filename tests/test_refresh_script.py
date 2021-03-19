
from unittest.mock import patch
from app import main
from app.models import Company, MODE_GOOGLE_DRIVEN, MODE_REGEX
from app.DataSource import DataSource


def test_google_parser():
    print('\r\ngoogle driven parsing')
    main.refresh_contacts(MODE_GOOGLE_DRIVEN)


def test_regex_parsing():
    print('\r\nregex driven parsing')
    main.refresh_contacts(MODE_REGEX)


@patch.object(DataSource, 'get_companies_to_refresh')
@patch.object(Company, 'get_contact_page_text')
def test_refresh_script_with_fake_data(
        get_contact_page_text_mock,
        get_companies_to_refresh_mock,
):
    get_companies_to_refresh_mock.return_value = [
        Company(name='fake_company', contact_pages=['https://yandex.ru/']),
    ]
    get_contact_page_text_mock.return_value = \
        'sdasdas 666-66-66 +79525503453 sdfdfsdf'

    test_google_parser()
    test_regex_parsing()