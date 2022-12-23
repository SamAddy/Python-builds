import requests

"""
This program performs a get request on the provided route and counts the number of items with an age >= 50

"""
# Make the GET request to the API
request_data = requests.get("https://coderbyte.com/api/challenges/json/age-counting")

# Check the status code of the response 
if request_data.status_code != 200:
    print("Error: API request failed")

else: 
    # Parse the data returned by the API
    data = request_data.json()["data"].split(",")
    count = 0
    for item in data:
        # Split the item into a key-value pair and extract the age
        key, value = item.split("=")
        if key.strip() == "age":
            age = int(value)
            # Increment the count if the age is >= 50
            if age >= 50:
                count += 1 
    print(f"Number of items with age >= 50: {count}")
