import argparse
import requests
import json

THORN = 'þ'


def fetch_data(page=None):
    url = f"https://api.fbi.gov/wanted/v1/list?page={page}"
    try:
        response = requests.get(url)
        # Raising an HTTPError for bad responses
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return {}


def parse_data(data):
    formatted_rows = []

    for item in data.get('items', []):
        title = item.get('title', '')
        subjects = item.get('subjects', [])
        field_offices = item.get('field_offices', [])

        # Ensure subjects and field_offices are lists
        if not isinstance(subjects, list):
            subjects = [subjects] if subjects else []
        if not isinstance(field_offices, list):
            field_offices = [field_offices] if field_offices else []

        subjects_str = ','.join(subjects)
        field_offices_str = ','.join(field_offices)

        formatted_row = f"{title}{THORN}{subjects_str}{THORN}{field_offices_str}"
        formatted_rows.append(formatted_row)

    return formatted_rows


def main(page=None, thefile=None):
    if page is not None:
        print(f"Fetching data from API, page: {page}")
        data = fetch_data(page)
        if not data:
            return
    elif thefile is not None:
        print(f"Reading data from file: {thefile}")
        try:
            with open(thefile, 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            print(f"File not found: {thefile}")
            return
        except json.JSONDecodeError:
            print(f"Error decoding JSON from file: {thefile}")
            return
    else:
        print("Please provide either a page number or a file path.")
        return

    formatted_data = parse_data(data)
    for line in formatted_data:
        print(line)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=str, help="Path to a JSON file with FBI wanted data.")
    parser.add_argument("--page", type=int, help="Page number for the FBI wanted API.")

    args = parser.parse_args()
    if args.page is not None:
        main(page=args.page)
    elif args.file is not None:
        main(thefile=args.file)
    else:
        parser.print_help()
