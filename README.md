# API-work

Report on Modular API-Database Integration System 

1. The API Chosen and the Type of Data It Provides 

For this project, I chose The Dog API. This API provides detailed information about various dog breeds. The data returned includes the following information: 

Breed Name: The name of the dog breed (e.g., "Affenpinscher"). 
Breed Group: The group to which the breed belongs (e.g., "Toy", "Herding"). 
Life Expectancy: The average lifespan of the breed (e.g., "12 - 14 years"). 
Weight: The typical weight range for the breed (e.g., "7 - 10 lbs"). 
Height: The typical height range for the breed (e.g., "9 - 12 inches"). 
Image URL: A URL pointing to an image of the breed. 
I used the /breeds endpoint to get the list of all dog breeds and stored this data in an SQLite database. 

2. The Structure of the SQLite Database 

The database contains one table named dog_breeds, where I store information about each breed retrieved from the API. The table structure is as follows: 

Table: dog_breeds 

Column 
Data Type 
Description 
id 
INTEGER 
Unique identifier for each breed (auto-incremented) 
name 
TEXT 
Name of the dog breed 
breed_group 
TEXT 
The group the breed belongs to (e.g., Herding) 
life_expectancy 
TEXT 
Expected lifespan of the breed 
weight 
TEXT 
Weight range of the breed 
height 
TEXT 
Height range of the breed 
image_url 
TEXT 
URL of an image for the breed 
This simple structure allows the system to store relevant breed data and supports basic operations like adding, updating, deleting, and querying the data. 

3. How the CRUD Functions Work and How They Interact with the Database 

The system has four key CRUD functions, each of which interacts with the SQLite database: 

Create: This function adds a new breed's data into the dog_breeds table. 
python 
Copy 
def create_breed(conn, breed): 
    cursor = conn.cursor() 
    cursor.execute(''' 
    INSERT INTO dog_breeds (name, breed_group, life_expectancy, weight, height, image_url) 
    VALUES (?, ?, ?, ?, ?, ?) 
    ''', (breed['name'], breed['breed_group'], breed['life_expectancy'], breed['weight'], breed['height'], breed['image_url'])) 
    conn.commit() 
 
Read: This function allows users to retrieve a breed’s information by its ID. 
python 
Copy 
def get_breed_by_id(conn, breed_id): 
    cursor = conn.cursor() 
    cursor.execute("SELECT * FROM dog_breeds WHERE id=?", (breed_id,)) 
    return cursor.fetchone() 
 
Update: This function lets users modify an existing breed’s information (e.g., updating the breed’s name or weight). 
python 
Copy 
def update_breed(conn, breed_id, updated_breed): 
    cursor = conn.cursor() 
    cursor.execute(''' 
    UPDATE dog_breeds  
    SET name = ?, breed_group = ?, life_expectancy = ?, weight = ?, height = ?, image_url = ? 
    WHERE id = ? 
    ''', (updated_breed['name'], updated_breed['breed_group'], updated_breed['life_expectancy'],  
          updated_breed['weight'], updated_breed['height'], updated_breed['image_url'], breed_id)) 
    conn.commit() 
 
Delete: This function removes a breed from the database by its ID. 
python 
Copy 
def delete_breed(conn, breed_id): 
    cursor = conn.cursor() 
    cursor.execute("DELETE FROM dog_breeds WHERE id=?", (breed_id,)) 
    conn.commit() 
 
These functions ensure that users can perform full CRUD operations on the database with the dog breed data. 

4. How the User Interface Works and How the User Can Interact with the System 

The system provides a simple command-line interface (CLI) where users can interact with the database. The menu displays the following options: 

View All Breeds: Shows a list of all the dog breeds stored in the database. 
Search Breed by ID: Allows the user to search for a specific breed using its unique ID. 
Search Breed by Name: Lets the user search for breeds by their name (partial matches allowed). 
Update Breed: Lets the user update the details of a breed by providing its ID and new information. 
Delete Breed: Allows the user to delete a breed by its ID. 
Exit: Exits the program. 
The user is prompted to enter a number corresponding to the action they want to take. For example, if they choose to search by ID, they will be asked to enter the breed’s ID, and the system will return the matching breed’s information. 

Here is how the menu is shown to the user: 

python 
Copy 
def show_menu(): 
    print("1. View All Breeds") 
    print("2. Search Breed by ID") 
    print("3. Search Breed by Name") 
    print("4. Update Breed") 
    print("5. Delete Breed") 
    print("6. Exit") 
 
The program loops and continuously prompts the user for input until they decide to exit. Each action is handled by the corresponding function that interacts with the database to either display data, modify it, or delete it. 

 
 
