# lt_pos – Basic Point of Sale (POS)

## Project Overview

`lt_pos` is a **very basic Point of Sale (POS) system** built using Python.
This project is designed for **learning and practicing core Python concepts** rather than building a production-ready POS system.

The application allows users to perform two simple operations:

* **Sale** – Process a product sale
* **Inventory** – View available items

⚠️ Note: This application **does not store data permanently**. All data is stored temporarily while the program is running.

---

## Features

### 1. Sale

* Select a product
* Enter quantity
* Calculate total price
* Display bill summary

### 2. Inventory

* Display available products
* Show product price and quantity

---

## Python Concepts Used

This project focuses on practicing the following Python topics:

### 1. Data Types

Used to store product details such as:

* `int`
* `float`
* `string`
* `list`
* `dictionary`

Example:

```python
product = {
    "name": "Apple",
    "price": 10,
    "quantity": 50
}
```

---

### 2. Loops

Loops are used to:

* Display menu repeatedly
* Iterate through product inventory
* Process user selections

Example:

```python
while True:
    print("1. Sale")
    print("2. Inventory")
```

---

### 3. Conditional Statements

Conditional statements help the program make decisions based on user input.

Example:

```python
if option == 1:
    sale()
elif option == 2:
    inventory()
```

---

### 4. Functions

Functions are used to organize the code into reusable blocks.

Example:

```python
def sale():
    print("Processing sale...")

def inventory():
    print("Showing inventory...")
```

---

### 5. List Comprehensions

Used to simplify loops when creating lists.

Example:

```python
product_names = [product["name"] for product in inventory]
```

---

### 6. Dictionary Comprehensions

Used to create dictionaries in a concise way.

Example:

```python
low_stock = {k:v for k,v in inventory.items() if v["quantity"] < 5}
```

---

## Project Structure

```
lt_pos/
├── main.py 
├── inventary.py  
├── Sale.py       
├── README.md     
```

---

## How to Run the Project

1. Clone the repository

```bash
git clone https://github.com/AlamManojKumar/Project-Three.git

```
2. Navigate to the project directory

```bash
cd lt_pos
```

3. Run the Python program

```bash
pythonpracticefolder\lt_pos>
```

---

## Example Menu

```
------ POS MENU ------

1. Sale
2. Inventory
3. Exit
```

---

## Learning Goal

The goal of this project is to practice:

* Writing clean Python code
* Using loops and conditions
* Working with lists and dictionaries
* Creating functions
* Understanding program flow

---

## Future Improvements

Possible improvements for future versions:

* Add file storage
* Add product creation option
* Add sales history
* Add user authentication
* Build a GUI version

---

## Author

Manoj Kumar Alam

Learning Python through small practical projects 🚀
