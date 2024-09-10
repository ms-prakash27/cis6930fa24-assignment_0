# tests/test_randompage.py
import pytest
import json
import main


def load_test_data(file_path):
    """Utility function to load test data from a JSON file."""
    with open(file_path, 'r') as file:
        return json.load(file)


def test_extract_title():
    data = load_test_data('wanted.json')
    formatted_data = main.parse_data(data)
    assert "BORIS YAKOVLEVICH LIVSHITS" in formatted_data[0], "Title should be extracted correctly"


def test_extract_subjects():
    data = load_test_data('wanted.json')
    formatted_data = main.parse_data(data)
    assert "Counterintelligence" in formatted_data[
        0], "Subjects should be extracted and formatted as a comma-separated string"


def test_extract_field_offices():
    data = load_test_data('wanted.json')
    formatted_data = main.parse_data(data)
    assert "newyork" in formatted_data[0], "Field offices should be extracted and formatted as a comma-separated string"


def test_print_thorn_separated():
    data = load_test_data('wanted.json')
    formatted_data = main.parse_data(data)
    assert formatted_data[
               0] == "BORIS YAKOVLEVICH LIVSHITSþCounterintelligenceþnewyork", "Output should be thorn-separated"
