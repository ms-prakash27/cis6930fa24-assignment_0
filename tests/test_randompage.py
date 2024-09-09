# # -*- coding: utf-8 -*-
# import pytest
# import io
# import sys
# from unittest.mock import patch
# import main
#
#
# @patch('sys.stdout', new_callable=io.StringIO)
# @patch('main.fetch_data')
# @patch('main.parse_data')
# def test_print_thorn_separated_file(mock_parse_data, mock_fetch_data, mock_stdout):
#     # Mock data for testing
#     mock_fetch_data.return_value = {
#         'items': [
#             {'title': 'Title A', 'subjects': ['Subject A1'], 'field_offices': ['Office A1']},
#             {'title': 'Title B', 'subjects': ['Subject B1'], 'field_offices': ['Office B1']}
#         ]
#     }
#
#     mock_parse_data.return_value = [
#         'Title AþSubject A1þOffice A1',
#         'Title BþSubject B1þOffice B1'
#     ]
#
#     # Run the main function
#     main.main(page=1)
#
#     # Get the printed output
#     output = mock_stdout.getvalue().strip().split('\n')
#
#     # Filter out any lines that don't match the expected thorn-separated format
#     filtered_output = [line for line in output if 'þ' in line]
#
#     expected_output = [
#         'Title AþSubject A1þOffice A1',
#         'Title BþSubject B1þOffice B1'
#     ]
#
#     assert filtered_output == expected_output

# -*- coding: utf-8 -*-
import pytest
import io
import sys
from unittest.mock import patch
from main import fetch_data, parse_data, main

@patch('sys.stdout', new_callable=io.StringIO)
# -*- coding: utf-8 -*-


import pytest
import io
import sys
from unittest.mock import patch
from main import fetch_data, parse_data, main


@patch('sys.stdout', new_callable=io.StringIO)
def test_print_thorn_separated_file_with_real_data(mock_stdout):
    # Fetch real data from the FBI API (page 1)
    data = fetch_data(page=1)

    # Parse the fetched data
    parsed_data = parse_data(data)

    # Print the parsed data using thorn-separated format
    for item in parsed_data:
        print(item)

    # Capture the printed output
    output = mock_stdout.getvalue().strip().split('\n')

    # Filter out any lines that don't match the expected thorn-separated format
    filtered_output = [line for line in output if 'þ' in line]

    # Make sure we got real data and it's correctly formatted
    assert len(filtered_output) > 0  # Ensure some thorn-separated data is present
    assert 'þ' in filtered_output[0]  # Check that thorn-separated formatting is applied

    # Example assertions (You can adjust these based on real fetched data)
    for line in filtered_output:
        # Each line should follow the format "TitleþSubjectþField Office"
        assert len(line.split('þ')) == 3

        # Debugging: Print the line to understand what fields are causing issues
        print(f"Debug: Thorn-separated line: {line}")

        # Ensure none of the fields are empty
        fields = line.split('þ')
        for field in fields:
            print(f"Debug: Field value: {field}")  # Print field values for debugging
        assert all(field.strip() for field in fields)  # Ensure fields are non-empty
