# Assignment -0 -- FBI Wanted API Project

## Project Overview

The main objective of this project is to create a Python package that interacts with the FBI's Most Wanted API, 
retrieves data about wanted individuals, and formats this data into a specific output format,here we used thorn character.

Key features:
- Fetches data from the FBI's Most Wanted API
- Parses JSON data and extracts relevant information
- Formats data into a thorn-separated output
- Supports both API data retrieval and local file reading
- Includes comprehensive error handling and testing

## Installation
for  This project runs on Python( here I used 3.12) and pipenv installed in your pc/system
To install the project, use pipenv:

```
pip install pipenv
```

Once pipenv is installed, navigate to your project directory

Create and activate a virtual environment using pipenv:
```
pipenv shell
```

Install the required dependencies for the project:
```
pipenv install -e .
```

we also use  request library in main.py

```
pipenv install request
```
( we can do this manually anyway it will be installed in dependencies in the above step)

## How to run

The project can be run in two primary modes:

1. Fetch data from the FBI API:

```
pipenv run python main.py --page <interger>
```
    
ex : 
```
pipenv run python main.py --page 1
```

Replace `<integer>` with the desired page number of the API results.

2. Read data from a local JSON file:

```
pipenv run python main.py --file <file-location>
```
    
or we can use
    
ex : 
```
pipenv run python main.py --file wanted.json
```

Replace <file-location>with the path to your local JSON file.

Output Format:
```
{title}þ{subjects}þ{field_offices}
```
Where `þ` is the lowercase thorn character used as a separator. Multiple subjects or field offices are comma-separated.

## Project Structure

```
cis6930fa24-assignment0/
├── COLLABORATORS.md
├── LICENSE
├── Pipfile
├── README.md
├── main.py
├── docs/
├── setup.cfg
├── setup.py
└── tests/
    ├── test_download.py
    └── test_randompage.py
```

- `main.py`: Core script containing main functionality
- `tests/`: Directory containing test files
- `setup.py` & `setup.cfg`: Configuration files for the Python package
- `Pipfile`: Specifies project dependencies
- `COLLABORATORS.md`: Lists project collaborators and resources used
- `LICENSE`: Contains the project's license information

## Functions/Code Explanation

### main.py

#### Import Statements

```python

import argparse
import requests
import json
```
- `argparse`: Used for parsing command-line arguments
- `requests`: Handles HTTP requests to the FBI API
- `json`: Processes JSON data

#### Constants

```python
THORN = 'þ'
```

Defines the thorn character used as a separator in the output.

#### Functions

1. `fetch_data(page=None)`
   - Purpose: Retrieves data from the FBI's Most Wanted API
   - Parameters: 
     - `page` (optional): Specifies which page of results to fetch
   - Returns: JSON data from the API or an empty dictionary if there's an error
   - Implementation details:
     - Constructs the API URL with the page parameter
     - Uses `requests.get()` to fetch data
     - Implements error handling with try/except block
     - Raises an HTTPError for bad responses
   - Error Handling:
     - Catches and reports any `RequestException`
     - Returns an empty dictionary on error to allow graceful degradation

2. `parse_data(data)`
   - Purpose: Processes the JSON data into the required output format
   - Parameters:
     - `data`: The JSON data retrieved from the API
   - Returns: A list of formatted strings, each representing one wanted person's data
   - Implementation details:
     - Iterates through each item in the 'items' list of the JSON data
     - Extracts 'title', 'subjects', and 'field_offices' for each item
     - Handles cases where 'subjects' or 'field_offices' might not be lists
     - Joins multiple subjects or field offices with commas
     - Creates a thorn-separated string for each item
   - Error Handling:
     - Uses `.get()` method with default values to handle missing keys
     - Checks and converts non-list 'subjects' and 'field_offices' to lists

3. `main(page=None, thefile=None)`
   - Purpose: Orchestrates the entire process of fetching, parsing, and outputting data
   - Parameters:
     - `page` (optional): Page number for API fetching
     - `thefile` (optional): File path for reading local JSON data
   - Implementation details:
     - Determines whether to fetch from API or read from file based on input parameters
     - Calls `fetch_data()` if `page` is provided
     - Reads and parses JSON from file if `thefile` is provided
     - Uses `parse_data()` to process the data
     - Prints the formatted output to stdout
   - Error Handling:
     - Handles file not found and JSON decoding errors when reading from file
     - Prints informative error messages for various scenarios

#### Command-line Interface
The script uses `argparse` to create a command-line interface:

- Defines two optional arguments: `--file` and `--page`
- Calls `main()` with appropriate arguments based on user input
- Prints help message if no arguments are provided

#### Execution Flow
1. Script parses command-line arguments
2. Based on arguments, it either:
   a. Fetches data from the API using `fetch_data()`
   b. Reads data from a local file
3. Data is parsed using `parse_data()`
4. Formatted data is printed to stdout

## Testing

To run the tests:

```
pipenv run python -m pytest -v
```

we have two test files as shown below

### test_download.py

Tests the data downloading functionality:
- Ensures non-empty data is downloaded from the API
- Checks if the downloaded data contains the expected fields

#### test_download.py test functions

1. `test_download_non_empty_data`
   This test checks that the fetch_data function correctly handles
   non-empty responses from the FBI API. It performs the following checks:
        The data returned by fetch_data is not None.
   The data contains the key 'items'.
   The 'items' list contains at least one item.
    
    requests_mock.Mocker() is used to mock the HTTP GET request to the FBI API.
   The mock response is configured to return a JSON object with a single item.
   Assertions verify that the data structure is as expected.

2. `test_download_data_fields`
   This test verifies that each item in the response from fetch_data
   contains the required fields:
       Each item should have a 'title' field.
   Each item should have a 'subjects' field.
   Each item should have a 'field_offices' field.

### test_randompage.py
Tests the data parsing and formatting functionality:
- Verifies correct extraction of title, subjects, and field offices
- Ensures proper formatting of the thorn-separated output

1. `test_extract_title`
This test checks if the title field is extracted correctly from the data returned by the FBI API:
    The mocked API response contains a single item with the title field set to "John Doe".
    The fetch_data function fetches the data, and parse_data processes it.
    The test asserts that the formatted data contains "John Doe" in the first record.

2. `test_extract_subjects`
This test ensures that the subjects field is extracted and formatted correctly:
    The mocked API response contains an item with the subjects field set to ["Theft", "Fraud"].
    The parse_data function should format the subjects as a comma-separated string ("Theft,Fraud").
    The test checks if "Theft,Fraud" is present in the formatted data.

3. `test_extract_field_offices`
This test verifies that the field_offices field is correctly extracted and formatted:
    The mocked API response includes an item with field_offices set to ["Miami", "Dallas"].
    The parse_data function should format the field offices as a comma-separated string ("Miami,Dallas").
    The test asserts that "Miami,Dallas" appears in the formatted data.

4. `test_print_thorn_separated`
This test checks the final output formatting, which uses a thorn (þ) character to separate fields:
    The mocked API response includes title, subjects, and field_offices.
    The parse_data function should return a string where the fields are separated by the thorn character (þ), e.g., "John DoeþTheft,FraudþMiami,Dallas".
    The test asserts that the formatted data matches this thorn-separated format.

#### test_randompage.py  functions

## Assumptions

This script assumes that the FBI Wanted API (https://api.fbi.gov/wanted/v1/list) is available and working properly.
The API is expected to return data in a JSON format with an "items" key, which should be a list of entries.
Each entry should have the fields "title", "subjects", and "field_offices".

The code assumes that the values for "title", "subjects", and "field_offices" in each item of the API response
will be properly formatted.

The code assumes that "subjects" and "field_offices" are either lists or can be converted to lists if they are not. 
It also assumes that the THORN character (þ) is appropriate for separating fields in the output.

The script assumes you have Python(preferbly 3.12) and the necessary libraries (requests, argparse, json, and pytest) installed.
It should run without compatibility problems in this setup.

### Assumption for Tests

The tests use the requests_mock library to mock API responses, 
assuming that mocking is sufficient to test the behavior of the fetch_data and parse_data functions.
