# -*- coding: utf-8 -*-
import pytest
import io
import sys
from unittest.mock import patch
import main


@patch('sys.stdout', new_callable=io.StringIO)
@patch('main.fetch_data')
@patch('main.parse_data')
def test_print_thorn_separated_file(mock_parse_data, mock_fetch_data, mock_stdout):
    # Mock data for testing
    mock_fetch_data.return_value = {
        'items': [
            {'title': 'Title A', 'subjects': ['Subject A1'], 'field_offices': ['Office A1']},
            {'title': 'Title B', 'subjects': ['Subject B1'], 'field_offices': ['Office B1']}
        ]
    }

    mock_parse_data.return_value = [
        'Title AþSubject A1þOffice A1',
        'Title BþSubject B1þOffice B1'
    ]

    # Run the main function
    main.main(page=1)

    # Get the printed output
    output = mock_stdout.getvalue().strip().split('\n')

    # Filter out any lines that don't match the expected thorn-separated format
    filtered_output = [line for line in output if 'þ' in line]

    expected_output = [
        'Title AþSubject A1þOffice A1',
        'Title BþSubject B1þOffice B1'
    ]

    assert filtered_output == expected_output
