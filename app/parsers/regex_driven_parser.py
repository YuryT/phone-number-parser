import re

# +7/8KKKNNNNNNN
DIGITS_ONLY_REGEX = r'[87]\d{10}'
# NNN-NN-NN
MOSCOW_REGEX = r'\d{3}-\d{2}-\d{2}'
# +7/8 (KKK) NNN-NN-NN
FULL_FORMAT_REGEX = r'[87]?\(\d{3}\)\s*\d{3}-\d{2}-\d{2}'

REGEX_LIST = [DIGITS_ONLY_REGEX, MOSCOW_REGEX, FULL_FORMAT_REGEX]
NON_WORD = r'\W'
regex_separator = f'{NON_WORD}|{NON_WORD}'

regex_string_for_html = \
    f'({NON_WORD}{regex_separator.join(REGEX_LIST)}{NON_WORD})'
regex_string_for_results = '|'.join(REGEX_LIST)

MOSCOW_CODE = 495


def parse_by_regex(text):
    not_validated_numbers = set()
    for match in re.findall(regex_string_for_html, text):
        not_validated_numbers.add(
            re.search(regex_string_for_results, match).group(),
        )
    formatted_numbers = set()
    for number in not_validated_numbers:
        if re.search(DIGITS_ONLY_REGEX, number):
            formatted_numbers.add(f'8{number[1:]}')
        elif re.search(FULL_FORMAT_REGEX, number):
            cleaned_number = number.replace('(', '').replace(')', ''). \
                replace('-', '').replace(' ', '')
            if number[0] == '8':
                formatted_numbers.add(cleaned_number)
            elif number[0] == '7':
                formatted_numbers.add(f'8{cleaned_number[1:]}')
            else:
                # no country code
                formatted_numbers.add(f'8{cleaned_number}')
        else:
            number = number.replace('-', '')
            formatted_numbers.add(f'8{MOSCOW_CODE}{number}')
    return formatted_numbers
