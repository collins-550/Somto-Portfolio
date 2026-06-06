# Python OOP — Restaurant Ordering System
 
## Overview
A Python Object-Oriented Programming project that simulates a restaurant
ordering system. Demonstrates core OOP concepts including classes,
objects, methods, and instance attributes applied to a real-world
business scenario.
 
## Tools & Technologies
- Python 3
- OOP principles
 
## Features
- Dynamic menu display
- Add items to order
- Real-time bill calculation
- Final bill summary
- Input validation (checks if item is on the menu)
- Continuous ordering loop until customer is done
 
## How to Run
```bash
python restaurant.py
```
 
## Sample Output
```
===== Somto's Kitchen MENU =====
Jollof Rice: ₦1500
Fried Rice: ₦1800
Chicken: ₦1000
Pepsi: ₦500
Water: ₦200
=================================
 
Enter item to order (or 'done' to finish): Jollof Rice
Jollof Rice added! ₦1500
 
===== YOUR ORDER =====
- Jollof Rice: ₦1500
TOTAL: ₦1500
======================
```
 
## OOP Concepts Demonstrated
| Concept | Implementation |
|---------|---------------|
| Class | `Restaurant` class |
| Constructor | `__init__` with name, menu, order, total |
| Methods | `show_menu()`, `add_order()`, `show_bill()` |
| Instance attributes | `self.name`, `self.menu`, `self.order`, `self.total` |
| Object creation | `resto = Restaurant("Somto's Kitchen")` |
 
## Skills Demonstrated
- Object-Oriented Programming (OOP)
- Python classes and methods
- Dictionary and list manipulation
- While loops and user input
- Real-world application design
 
## Author
Somto Collins | Cybersecurity Student | NOUN | Early Code Institute, Abuja
