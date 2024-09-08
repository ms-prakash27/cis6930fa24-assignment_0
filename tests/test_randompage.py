# test_randompage.py
from main import parse_data  # Import the function to test


def test_parse_data():
    sample_data = {
        "items": [
            {
                "title": "Extreme loss",
                "subjects": ["sebastian", "Pit Bull"],
                "field_offices": ["Miami"]
            },
            {
                "title": "Dissapointing team",
                "subjects": ["DJ"],
                "field_offices": ["Tallahassee", "Dublin"]
            },
            {
                "title": "Florida Man",
                "subjects": ["Seeking Information"],
                "field_offices": ["Gainesville"]
            },
            {
                "title": "Data Engineer",
                "subjects": [],
                "field_offices": ["all over"]
            }
        ]
    }
    formatted_data = parse_data(sample_data)
    expected_output = [
        "Extreme lossþsebastian,Pit BullþMiami",
        "Dissapointing teamþDJþTallahassee,Dublin",
        "Florida ManþSeeking InformationþGainesville",
        "Data Engineerþþall over"
    ]
    assert formatted_data == expected_output
