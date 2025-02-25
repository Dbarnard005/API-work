API work

This project fetches data from The Dog API, stores it in an SQLite database, and allows users to interact with the data through a simple command-line interface (CLI). The system supports basic CRUD (Create, Read, Update, Delete) operations.

What data does the API provide?
I chose The Dog API, which provides detailed information about different dog breeds. Each breed’s data includes:

Breed Name: The name of the dog breed (e.g., "Affenpinscher").
Breed Group: The group the breed belongs to (e.g., "Toy", "Herding").
Life Expectancy: The average lifespan of the breed (e.g., "12 - 14 years").
Weight: The weight range of the breed (e.g., "7 - 10 lbs").
Height: The height range of the breed (e.g., "9 - 12 inches").
Image URL: A URL for an image of the breed.

{
    "id": 1,
    "name": "Affenpinscher",
    "breed_group": "Toy",
    "life_expectancy": "12 - 14 years",
    "weight": "7 - 10 lbs",
    "height": "9 - 12 inches",
    "image_url": "https://cdn2.thedogapi.com/images/B1svZg9E7.jpg"
}

Adding new breed data:

def create_breed(conn, breed):
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO dog_breeds (name, breed_group, life_expectancy, weight, height, image_url)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (breed['name'], breed['breed_group'], breed['life_expectancy'], breed['weight'], breed['height'], breed['image_url']))
    conn.commit()


Retrieving data by ID: 

def get_breed_by_id(conn, breed_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dog_breeds WHERE id=?", (breed_id,))
    return cursor.fetchone()

Changing exisating data: def update_breed(conn, breed_id, updated_breed):
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE dog_breeds 
    SET name = ?, breed_group = ?, life_expectancy = ?, weight = ?, height = ?, image_url = ?
    WHERE id = ?
    ''', (updated_breed['name'], updated_breed['breed_group'], updated_breed['life_expectancy'], 
          updated_breed['weight'], updated_breed['height'], updated_breed['image_url'], breed_id))
    conn.commit()


Removing a breed:

def delete_breed(conn, breed_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM dog_breeds WHERE id=?", (breed_id,))
    conn.commit()


The system uses the requests library to fetch dog breed data from The Dog API. The fetch_dog_breeds() function makes a GET request to the API and processes the response. After it has got the data it stores it using the create function.

import requests

def fetch_dog_breeds():
    url = "https://api.thedogapi.com/v1/breeds"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data: {response.status_code}")
        return None


This project demonstrates how to fetch data from an API, store it in a database, and provide a simple CLI for interacting with the data. The system supports full CRUD operations and is designed to be modular, so it's easy to add new features or modify the existing functionality.


