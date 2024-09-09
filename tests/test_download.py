# tests/test_download.py
import pytest
import requests
import requests_mock
import main


def test_download_non_empty_data():
    with requests_mock.Mocker() as m:
        m.get('https://api.fbi.gov/wanted/v1/list?page=1', json={
            "items": [
                {"title": "John Doe", "subjects": ["Theft"], "field_offices": ["Miami"]}
            ]
        })
        data = main.fetch_data(1)
        assert data is not None, "Data should not be None"
        assert 'items' in data, "Data should contain 'items' key"
        assert len(data['items']) > 0, "Data should contain at least one item"


def test_download_data_fields():
    with requests_mock.Mocker() as m:
        m.get('https://api.fbi.gov/wanted/v1/list?page=1', json={
            "items": [
                {"title": "John Doe", "subjects": ["Theft"], "field_offices": ["Miami"]}
            ]
        })
        data = main.fetch_data(1)
        items = data.get('items', [])
        assert len(items) > 0, "Data should contain items"
        for item in items:
            assert 'title' in item, "Each item should have a 'title' field"
            assert 'subjects' in item, "Each item should have 'subjects' field"
            assert 'field_offices' in item, "Each item should have 'field_offices' field"
