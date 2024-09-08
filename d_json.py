import requests
import json


def download_json(url, filename):
    try:
        # Fetch data from the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for HTTP errors

        # Parse the JSON data
        data = response.json()

        # Save the JSON data to a file
        with open(filename, 'w') as json_file:
            json.dump(data, json_file, indent=4)  # Use indent for pretty formatting

        print(f"JSON data has been saved to {filename}")

    except requests.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
    except ValueError:
        print("Error decoding the JSON response.")


# Example usage
url = "https://api.fbi.gov/wanted/v1/list"  # Replace this with the actual URL
filename = "fbi_data.json"
download_json(url, filename)
