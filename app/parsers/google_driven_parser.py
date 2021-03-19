import phonenumbers

NO_CITY_CODE_LEN_NUMBER = 9
MOSCOW_CODE = 495


def parse_by_phonenumbers(text):
    not_validated_numbers = set()
    validated_numbers = set()

    def format_number(number_object):
        return phonenumbers.format_number(
            number_object,
            phonenumbers.PhoneNumberFormat.E164,
        )

    for match in phonenumbers.PhoneNumberMatcher(
            text,
            'RU',
            # I used POSSIBLE to get numbers without city code
            phonenumbers.Leniency.POSSIBLE,
    ):
        # let's suppose: number without city code always have "-" symbol
        if phonenumbers.is_valid_number(match.number):
            validated_numbers.add(format_number(match.number))
        elif '-' in match.raw_string:
            not_validated_numbers.add(format_number(match.number))

    for number in not_validated_numbers:
        if len(number) == NO_CITY_CODE_LEN_NUMBER:
            number = f'+7{MOSCOW_CODE}{number[2:]}'
            validated_numbers.add(number)
    # convert international format to russian internal format
    return {f'8{n[2:]}' for n in validated_numbers}
