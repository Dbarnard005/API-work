import requests

def fetch_dog_breeds():
    url = "https://api.thedogapi.com/v1/breeds"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data: {response.status_code}")
        return None
import sqlite3

def create_breed(conn, breed):
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO dog_breeds (name, breed_group, life_expectancy, weight, height, image_url)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (breed['name'], breed['breed_group'], breed['life_expectancy'], breed['weight'], breed['height'], breed['image_url']))
    conn.commit()
def get_breed_by_id(conn, breed_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dog_breeds WHERE id=?", (breed_id,))
    return cursor.fetchone()
def update_breed(conn, breed_id, updated_breed):
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE dog_breeds 
    SET name = ?, breed_group = ?, life_expectancy = ?, weight = ?, height = ?, image_url = ?
    WHERE id = ?
    ''', (updated_breed['name'], updated_breed['breed_group'], updated_breed['life_expectancy'], 
          updated_breed['weight'], updated_breed['height'], updated_breed['image_url'], breed_id))
    conn.commit()
def delete_breed(conn, breed_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM dog_breeds WHERE id=?", (breed_id,))
    conn.commit()
def search_breed_by_name(conn, name):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dog_breeds WHERE name LIKE ?", ('%' + name + '%',))
    return cursor.fetchall()
def show_menu():
    print("1. View All Breeds")
    print("2. Search Breed by ID")
    print("3. Search Breed by Name")
    print("4. Update Breed")
    print("5. Delete Breed")
    print("6. Exit")

def main():
    conn = sqlite3.connect("dog_breeds.db")
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM dog_breeds")
            breeds = cursor.fetchall()
            for breed in breeds:
                print(breed)
        
        elif choice == "2":
            breed_id = int(input("Enter Breed ID: "))
            breed = get_breed_by_id(conn, breed_id)
            if breed:
                print(breed)
            else:
                print("Breed not found.")
        
        elif choice == "3":
            name = input("Enter breed name: ")
            breeds = search_breed_by_name(conn, name)
            if breeds:
                for breed in breeds:
                    print(breed)
            else:
                print("Breed not found.")
        
        elif choice == "4":
            breed_id = int(input("Enter Breed ID to update: "))
            name = input("Enter new name: ")
            breed_group = input("Enter new breed group: ")
            life_expectancy = input("Enter new life expectancy: ")
            weight = input("Enter new weight: ")
            height = input("Enter new height: ")
            image_url = input("Enter new image URL: ")
            updated_breed = {
                'name': name,
                'breed_group': breed_group,
                'life_expectancy': life_expectancy,
                'weight': weight,
                'height': height,
                'image_url': image_url
            }
            update_breed(conn, breed_id, updated_breed)
            print("Breed updated.")
        
        elif choice == "5":
            breed_id = int(input("Enter Breed ID to delete: "))
            delete_breed(conn, breed_id)
            print("Breed deleted.")
        
        elif choice == "6":
            print("Goodbye!")
            conn.close()
            break
breeds = fetch_dog_breeds()
if breeds:
    for breed in breeds:
        create_breed(conn, breed)
import json

def save_data_to_file(data):
    with open('dog_breeds.json', 'w') as f:
        json.dump(data, f)

def load_data_from_file():
    with open('dog_breeds.json', 'r') as f:
        return json.load(f)
