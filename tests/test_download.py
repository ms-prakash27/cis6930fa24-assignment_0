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

    # Simulate fetching data from the function
    fetched_data = main.fetch_data(1)  # You might want to adjust this to work with the JSON

    assert fetched_data is not None, "Data should not be None"
    assert 'items' in fetched_data, "Data should contain 'items' key"
    assert len(fetched_data['items']) > 0, "Data should contain at least one item"


def test_download_data_fields():
    # Load data from JSON file
    data = load_test_data('wanted.json')

    # Simulate fetching data from the function
    fetched_data = main.fetch_data(1)  # Adjust accordingly to fit your function logic

    items = fetched_data.get('items', [])
    assert len(items) > 0, "Data should contain items"
    for item in items:
        assert 'title' in item, "Each item should have a 'title' field"
        assert 'subjects' in item, "Each item should have 'subjects' field"
        assert 'field_offices' in item, "Each item should have 'field_offices' field"
#
#
# # tests/test_download.py
# import pytest
# import requests
# import requests_mock
# import main
#
#
# def test_download_non_empty_data():
#     with requests_mock.Mocker() as m:
#         m.get('https://api.fbi.gov/wanted/v1/list?page=1', json={
#             "items": [
#                 {"title": "BORIS YAKOVLEVICH LIVSHITS", "subjects": ["Counterintelligence"], "field_offices": ["newyork"]}
#             ]
#         })
#         data = main.fetch_data(1)
#         assert data is not None, "Data should not be None"
#         assert 'items' in data, "Data should contain 'items' key"
#         assert len(data['items']) > 0, "Data should contain at least one item"
#
#
# def test_download_data_fields():
#     with requests_mock.Mocker() as m:
#         m.get('https://api.fbi.gov/wanted/v1/list?page=1', json={
#             "items": [
#                 {"title": "BORIS YAKOVLEVICH LIVSHITS", "subjects": ["Counterintelligence"], "field_offices": ["newyork"]}
#             ]
#         })
#         data = main.fetch_data(1)
#         items = data.get('items', [])
#         assert len(items) > 0, "Data should contain items"
#         for item in items:
#             assert 'title' in item, "Each item should have a 'title' field"
#             assert 'subjects' in item, "Each item should have 'subjects' field"
#             assert 'field_offices' in item, "Each item should have 'field_offices' field"
#             assert item['title'] == "BORIS YAKOVLEVICH LIVSHITS", "Title should match the expected value"
#             assert item['subjects'] == ["Counterintelligence"], "Subjects should match the expected value"
#             assert item['field_offices'] == ["newyork"], "Field offices should match the expected value"
