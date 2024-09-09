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
   The function fetch_data(page=None) is designed to retrieve data from the FBI's Most Wanted API. It accepts an optional page parameter, which allows users to specify a particular page of results they want to fetch. The function constructs the API URL using this page number and uses requests.get() to make the HTTP request. If the request is successful, it returns the 
   fetched JSON data. To ensure robustness, it implements error handling using a try/except block to catch any RequestException that may occur during the request. In case of an error, such as network issues or invalid responses, the function raises an HTTPError for bad responses and returns an empty dictionary to allow the system to continue operating smoothly.

2. `parse_data(data)`
   The function processes JSON data retrieved from an API into a specific output format. 
   It takes a single parameter, data, which is the JSON data. The function returns a list
   of formatted strings, each representing the information of a wanted person. 
   To achieve this, the function iterates through each item in the 'items' 
   list of the JSON data, extracting values for 'title', 'subjects', and 'field_offices'. 
   It handles cases where 'subjects' or 'field_offices' might not be lists by using the .get() 
   method with default values to manage missing keys and ensuring that any non-list values are 
   converted to lists. Multiple subjects or field offices are joined with commas. For each item,
   the function creates a thorn-separated string combining the title, formatted subjects, and 
   field offices. This approach ensures that the function robustly handles various data scenarios
   and formats the output correctly.

3. `main(page=None, thefile=None)`
   The function orchestrates the entire process of fetching, parsing, and outputting data. It accepts two optional parameters: page, which specifies the page number for fetching data from the API, and thefile, which provides the file path for reading local JSON data. Depending on which parameter is provided, the function either fetches data from the API using fetch_data() if a page is given or reads and parses JSON from a local file if thefile is specified. Once the data is obtained, it is processed using parse_data(). The function then prints the formatted output to standard output. It includes error handling to manage scenarios such as file not found and JSON decoding errors when reading from the file, ensuring that informative error messages are displayed for various issues that may arise. This approach provides flexibility in sourcing data and robustness in managing potential errors.


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

### 'test_download.py'

#### functions

1. `Utility Function`
   load_test_data(file_path): This function loads test data from a JSON file. It reads the contents of the file specified by file_path and returns the data as a Python dictionary.

2. `test_download_non_empty_data`
This test ensures that the downloaded data is not empty and contains the necessary structure. It loads the JSON data from wanted.json and simulates the fetching process using main.fetch_data(). The test checks that the fetched data is not None, contains an 'items' key, and has at least one item in the 'items' list.

3.  `test_download_data_fields`
This test validates that each item in the downloaded data contains all required fields. It loads the JSON data from wanted.json and uses main.fetch_data() to simulate the fetching process. The test checks that each item in the 'items' list contains the fields 'title', 'subjects', and 'field_offices', ensuring that the data structure is correct and complete.

### 'test_randompage.py'

#### Functions

1. `test_extract_title`
The test_extract_title function checks if the title "BORIS YAKOVLEVICH LIVSHITS" is correctly extracted from the JSON data loaded from wanted.json. It ensures that the title is present in the formatted output.

2.  `test_extract_subjects`
The test_extract_subjects function verifies that the subject "Counterintelligence" is included in the comma-separated string of subjects after parsing the data from wanted.json. It confirms proper extraction and formatting.

3.  `test_extract_field_offices`
The test_extract_field_offices function ensures that "newyork" appears in the comma-separated list of field offices after parsing the JSON data from wanted.json. It checks the correct extraction and formatting of field offices.

4.  `test_print_thorn_separated`
The test_print_thorn_separated function verifies that the final output string is formatted as "BORIS YAKOVLEVICH LIVSHITSþCounterintelligenceþnewyork". It ensures that data is combined and separated by the thorn character as required.

## Assumption

In test cases, I have created a wanted.json file from the API(from the first page) and used that, alternatively, we can use API calls using the request mock module, as the page refreshes frequently, I didn't prefer.



