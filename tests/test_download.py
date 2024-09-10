# tests/test_download.py
import pytest
import json
import main


def load_test_data(file_path):
    """Utility function to load test data from a JSON file."""
    with open(file_path, 'r') as file:
        return json.load(file)


def test_download_non_empty_data():
    # Load data from JSON file
    data = load_test_data('wanted.json')
    fetched_data = main.fetch_data(1)
    assert fetched_data is not None, "Data should not be None"
    assert 'items' in fetched_data, "Data should contain 'items' key"
    assert len(fetched_data['items']) > 0, "Data should contain at least one item"


def test_download_data_fields():
    # Loading data from JSON file
    data = load_test_data('wanted.json')
    fetched_data = main.fetch_data(1)
    items = fetched_data.get('items', [])
    assert len(items) > 0, "Data should contain items"
    for item in items:
        assert 'title' in item, "Each item should have a 'title' field"
        assert 'subjects' in item, "Each item should have 'subjects' field"
        assert 'field_offices' in item, "Each item should have 'field_offices' field"
