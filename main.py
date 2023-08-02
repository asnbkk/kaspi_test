import requests
from get_headesrs import get_headers
import sys
import json


def get_by_category(pages, category):
    for page in range(pages):
        try:
            url = f"https://kaspi.kz/yml/product-view/pl/results?page={page}&q=%3Acategory%3A{category}"

            response = requests.get(
                url,
                headers=get_headers(page=page),
            )

            # Process the response as needed
            json_data = response.json()

            filename = f"data/{category}_output_{page}.json"

            # Save the JSON data to a file
            with open(filename, "w") as file:
                json.dump(json_data, file)

            print(f"JSON data saved to {filename} successfully.")
        except Exception as e:
            print(e)
            print(f"{page} ERROR PAGE")
            pass
        print(f"THE PAGE IS {page}")


if __name__ == "__main__":
    # category = "Smartphones%20and%20gadgets"
    category = "child%20goods"
    pages = int(sys.argv[1])
    get_by_category(pages, category)
