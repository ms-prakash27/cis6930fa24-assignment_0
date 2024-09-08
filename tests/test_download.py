# test_download.py
import requests
from unittest.mock import patch

from main import fetch_data


def test_fetch_data_success():
    url = "https://api.fbi.gov/wanted/v1/list?page=1"
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'items': [{'title': 'Test Title'}]}
        data = fetch_data(page=1)
        assert data['items'] is not None
        assert len(data['items']) > 0
