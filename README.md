 # Ordering and Payment System

A simple console-based cafe ordering system written in Python.  
It supports **Staff** and **Customer** modes with menu management, ordering, stock tracking, receipts, and daily sales reports.

---

## Features

### Main Menu
- **Staff** – login required
- **Customer** – no login
- Exit program (requires staff credentials)

### Staff Menu
1. View Cafedrinks Menu  
2. View Desserts Menu  
3. Add new cafedrink  
4. Add new dessert
5. View out of stock / Archive  
6. Edit Menu (price, servings/quantity, rename)  
7. View recorded receipts  
8. Daily Sales Report / Summary  

### Customer Menu
1. View menu (cafedrinks + desserts)  
2. Order  
   - Order cafedrinks or desserts  
   - View current order  
   - Stock is reduced in real time  
   - Items that reach 0 stock are moved to archive  
   - Final order review → staff payment verification → receipt with queue number  

---

## Default Login (Staff)

| Username | Password |
|----------|----------|
| `barista`  | `biot`    |

---

## Default Menu

### Cafedrinks
| Dish                | Price   | Servings |
|---------------------|---------|----------|
| Almond Coffee       | ₱90.00  | 15       |
| Spanish Latte       | ₱90.00  | 15       |
| Iced Mocha          | ₱150.00 | 10       |
| Espresso            | ₱90.00  | 15       |
| Americano Latte     | ₱15.00  | 30       |

### Desserts
| Dessert         | Price  | Quantity |
|-----------------|--------|----------|
| Caramel Cake    | ₱55.00 | 15       |
| Cheese Cake     | ₱30.00 | 20       |
| Tiramisu Cake   | ₱30.00 | 20       |

---

## How to Run

1. Make sure you have **Python 3** installed.
2. Save the code as a `.py` file (e.g. `restaurant.py`).
3. Run it:

```bash
python restaurant.py
```

or

```bash
python3 restaurant.py
```

---

## Key Behaviors

- **Stock management**: When a cafedrinks or desserts reaches 0 servings/quantity, it is automatically moved to the archive.
- **Order combining**: Ordering the same item multiple times merges the quantities.
- **Payment verification**: A staff member must enter the correct username and password before an order is marked as paid.
- **Queue numbers**: Each successful paid order gets an incrementing queue number (001, 002, …).
- **Receipts & Sales**: All paid orders are stored and can be viewed later. The Daily Sales Report shows total revenue and item breakdown.
- **Input validation**: Names cannot contain numbers or special characters. Prices and quantities must be positive numbers.

---

## Project Structure (Single File)

All data is kept in memory using Python lists:

- `cafedrink_name`, `cafedrink_price`, `cafedrinks_servings`
- `dessert_name`, `dessert_price`, `dessert_quantity`
- Archive lists for out-of-stock items
- `recorded_receipts` and `daily_sales` for transaction history

No external libraries or database are required — only the Python standard library (`sys` and `datetime`).

---

## Notes

- Data is **not persisted**. Everything resets when you close the program.
- This is a console / terminal application (text-based interface).
- Designed for simple classroom / project demonstration purposes.

---

## Author

- Gumapac, Ezekiel A.
- Sarip, Abbas Abdullah C.
