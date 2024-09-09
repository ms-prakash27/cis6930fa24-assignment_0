# tests/test_randompage.py
import pytest
import json
import main


def load_test_data(file_path):
    """Utility function to load test data from a JSON file."""
    with open(file_path, 'r') as file:
        return json.load(file)


def test_extract_title():
    # Load data from JSON file
    data = load_test_data('wanted.json')

    # Simulate fetching and parsing data
    formatted_data = main.parse_data(data)
    assert "BORIS YAKOVLEVICH LIVSHITS" in formatted_data[0], "Title should be extracted correctly"


def test_extract_subjects():
    # Load data from JSON file
    data = load_test_data('wanted.json')

    # Simulate fetching and parsing data
    formatted_data = main.parse_data(data)
    assert "Counterintelligence" in formatted_data[
        0], "Subjects should be extracted and formatted as a comma-separated string"


def test_extract_field_offices():
    # Load data from JSON file
    data = load_test_data('wanted.json')

    # Simulate fetching and parsing data
    formatted_data = main.parse_data(data)
    assert "newyork" in formatted_data[0], "Field offices should be extracted and formatted as a comma-separated string"


def test_print_thorn_separated():
    # Loading data from JSON file
    data = load_test_data('wanted.json')

    # Simulating fetching and parsing data
    formatted_data = main.parse_data(data)
    assert formatted_data[
               0] == "BORIS YAKOVLEVICH LIVSHITSþCounterintelligenceþnewyork", "Output should be thorn-separated"

# # tests/test_randompage.py
# import pytest
# import requests_mock
# import main
#
#
# def test_extract_title():
#     with requests_mock.Mocker() as m:
#         m.get('https://api.fbi.gov/wanted/v1/list?page=1', json={
#             "items": [
#                 {"title": "John Doe"}
#             ]
#         })
#         data = main.fetch_data(1)
#         formatted_data = main.parse_data(data)
#         assert "John Doe" in formatted_data[0], "Title should be extracted correctly"
#
#
# def test_extract_subjects():
#     with requests_mock.Mocker() as m:
#         m.get('https://api.fbi.gov/wanted/v1/list?page=1', json={
#             "items": [
#                 {"title": "John Doe", "subjects": ["Theft", "Fraud"]}
#             ]
#         })
#         data = main.fetch_data(1)
#         formatted_data = main.parse_data(data)
#         assert "Theft,Fraud" in formatted_data[
#             0], "Subjects should be extracted and formatted as a comma-separated string"
#
#
# def test_extract_field_offices():
#     with requests_mock.Mocker() as m:
#         m.get('https://api.fbi.gov/wanted/v1/list?page=1', json={
#             "items": [
#                 {"title": "John Doe", "field_offices": ["Miami", "Dallas"]}
#             ]
#         })
#         data = main.fetch_data(1)
#         formatted_data = main.parse_data(data)
#         assert "Miami,Dallas" in formatted_data[
#             0], "Field offices should be extracted and formatted as a comma-separated string"
#
#
# def test_print_thorn_separated():
#     with requests_mock.Mocker() as m:
#         m.get('https://api.fbi.gov/wanted/v1/list?page=1', json={
#             "items": [
#                 {"title": "John Doe", "subjects": ["Theft", "Fraud"], "field_offices": ["Miami", "Dallas"]}
#             ]
#         })
#         data = main.fetch_data(1)
#         formatted_data = main.parse_data(data)
#         assert formatted_data[0] == "John DoeþTheft,FraudþMiami,Dallas", "Output should be thorn-separated"
