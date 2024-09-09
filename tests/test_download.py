# -*- coding: utf-8 -*-
import pytest
import requests
from unittest.mock import patch
import main


@patch('main.requests.get')
def test_fetch_data_non_empty(mock_get):
    # Mock successful API response with non-empty data
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'items': [
            {
                'title': 'Title 1',
                'subjects': ['Subject 1'],
                'field_offices': ['Office 1']
            }
        ]
    }

    data = main.fetch_data(page=1)
    assert 'items' in data
    assert len(data['items']) > 0


def test_extract_title_field():
    input_data = {
        'items': [
            {'title': 'Test Title 1', 'subjects': [], 'field_offices': []},
            {'title': 'Test Title 2', 'subjects': [], 'field_offices': []}
        ]
    }

    titles = [item['title'] for item in input_data['items']]
    assert titles == ['Test Title 1', 'Test Title 2']


def test_extract_subjects_field():
    input_data = {
        'items': [
            {'title': 'Title 1', 'subjects': ['Subject 1'], 'field_offices': []},
            {'title': 'Title 2', 'subjects': ['Subject 2'], 'field_offices': []}
        ]
    }

    subjects = [item['subjects'] for item in input_data['items']]
    assert subjects == [['Subject 1'], ['Subject 2']]


def test_extract_field_offices_field():
    input_data = {
        'items': [
            {'title': 'Title 1', 'subjects': [], 'field_offices': ['Office 1']},
            {'title': 'Title 2', 'subjects': [], 'field_offices': ['Office 2', 'Office 3']}
        ]
    }

    field_offices = [item['field_offices'] for item in input_data['items']]
    assert field_offices == [['Office 1'], ['Office 2', 'Office 3']]
