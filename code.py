#staff username: barista
#staff password: biot
import sys
from datetime import datetime

cafedrink_name = ["Almond Coffe", "Spanish Latte", "Iced Mocha", "Espresso", "Americano Latte"]
cafedrink_price = [90.0, 90.0, 150.0, 90.0, 15.0]
cafedrink_servings = [15, 15, 10, 15, 30]
dessert_name = ["Caramel Cake", "Cheese Cake", "Tiramisu Cake"]
dessert_price = [55.0, 30.0, 30.0]
dessert_quantity = [15, 20, 20]
archive_cafedrinks = []
archive_price = []
archive_serving = []
archive_dessert = []
archive_dessert_price = []
archive_dessert_quantity = []
queue_number = 1
recorded_receipts = []
daily_sales = []          

STAFF_USER = "barista"
STAFF_PASS = "biot"

def main_menu():
    while True:
        print("==============================")
        print("          MAIN MENU")
        print("==============================")
        print("1. Staff")
        print("2. Customer")
        print("==============================")
        choice = input("(Enter 0 to exit) Enter your choice: ").strip()
        if choice == "0":
            username = input("Enter Username: ").strip()
            if username == STAFF_USER:
                password = input("Enter Password: ").strip()
                if password == STAFF_PASS:
                    print("Exiting program...")
                    sys.exit()
                else:
                    print("Incorrect password.")
            else:
                print("Incorrect Username.")
        elif choice == "1":
            staff_login()
        elif choice == "2":
            customer_menu()
        else:
            print("Invalid choice.")

def staff_login():
    while True:
        username = input("Enter Username: ").strip()
        if username != STAFF_USER:
            print("Incorrect Username.")
            continue
        password = input("Enter Password: ").strip()
        if password == STAFF_PASS:
            staff_menu()
            break
        else:
            print("Incorrect password.")

def staff_menu():
    while True:
        print("==============================")
        print("          STAFF MENU")
        print("==============================")
        print("1. View cafedrinks Menu")
        print("2. View desserts Menu")
        print("3. Add new cafedrink")
        print("4. Add new dessert")
        print("5. View out of stock / Archive")
        print("6. Edit Menu (Cafedrinks / Desserts)")
        print("7. View recorded receipts")
        print("8. Daily Sales Report / Summary")
        print("==============================")
        choice = input("(Enter 0 to logout) Enter your choice: ").strip()
        if choice == "0":
            y_n = input("Do you like to logout? (y/n): ").strip().lower()
            if y_n == "y":
                print("==============================")
                print("Returning to main menu...")
                return
            elif y_n == "n":
                continue
            else:
                print("Enter valid choice.")
        elif choice == "1":
            view_cafedrink_menu()
        elif choice == "2":
            view_dessert_menu()
        elif choice == "3":
            add_cafedrink()
        elif choice == "4":
            add_dessert()
        elif choice == "5":
            view_out_of_stock()
        elif choice == "6":
            edit()
        elif choice == "7":
            view_recorded_receipts()
        elif choice == "8":
            daily_sales_report()
        else:
            print("Invalid choice.")

def customer_menu():
    while True:
        print("==============================")
        print("        CUSTOMER MENU")
        print("==============================")
        print("1. View menu")
        print("2. Order")
        print("==============================")
        choice = input("(Enter 0 to exit) Enter your choice: ").strip()
        if choice == "0":
            y_n = input("Do you like to logout? (y/n): ").strip().lower()
            if y_n == "y":
                print("==============================")
                print("Returning to main menu...")
                return
            elif y_n == "n":
                continue
            else:
                print("Enter valid choice.")
        elif choice == "1":
            view_cafedrink_menu()
            print()
            view_dessert_menu()
        elif choice == "2":
            order()
        else:
            print("Invalid choice.")

def view_cafedrink_menu():
    print("=================================================================")
    print("                         CAFEDRINKS MENU")
    print("=================================================================")
    print(f"{'No.':<5} | {'CAFEDRINK NAME':<28} | {'PRICE':<12} | {'SERVINGS':<8}")
    print("-" * 65)
    if len(cafedrink_name) == 0:
        print("No Cafedrinks available.")
    else:
        for i in range(len(cafedrink_name)):
            print(f"{i+1:<5} | {cafedrink_name[i]:<28} | ₱{cafedrink_price[i]:<11.2f} | {cafedrink_servings[i]:<8}")
    print("=================================================================")

def view_dessert_menu():
    print("=================================================================")
    print("                        DESSERTS MENU")
    print("=================================================================")
    print(f"{'No.':<5} | {'DESSERT NAME':<28} | {'PRICE':<12} | {'QUANTITY':<8}")
    print("-" * 65)
    if len(dessert_name) == 0:
        print("No dessert available.")
    else:
        for i in range(len(dessert_name)):
            print(f"{i+1:<5} | {dessert_name[i]:<28} | ₱{dessert_price[i]:<11.2f} | {dessert_quantity[i]:<8}")
    print("=================================================================")

def add_cafedrink():
    print("==============================")
    print("         ADD NEW CAFEDRINK")
    print("==============================")
    while True:
        new_cafedrink_name = input("Enter cafedrink name (Enter 0 to exit): ").strip()
        if new_cafedrink_name == "0":
            print("Exiting... Returning to Staff Menu.")
            return
        if new_cafedrink_name == "":
            print("Cafedrink name cannot be empty.")
            continue
        if any(char.isdigit() for char in new_cafedrink_name):
            print("Cafedrink name cannot contain numbers.")
            continue
        if not all(char.isalpha() or char.isspace() for char in new_cafedrink_name):
            print("Cafedrink name cannot contain special characters.")
            continue
        parts = new_cafedrink_name.split()
        if len(parts) > 1 and all(len(part) == 1 for part in parts):
            print("Invalid name format. Please enter a proper Cafedrink name.")
            continue
        if new_cafedrink_name.lower() in [d.lower() for d in cafedrink_name]:
            print("This cafedrink already exists... Try Again")
            continue
        break
    while True:
        try:
            new_cafedrink_price = float(input("Enter price: "))
            if new_cafedrink_price <= 0:
                print("Invalid price... Try Again.")
                continue
            break
        except ValueError:
            print("Enter a valid number...")
    while True:
        try:
            new_cafedrink_servings = int(input("Enter how many servings: "))
            if new_cafedrink_servings <= 0:
                print("Invalid serving... Try Again.")
                continue
            break
        except ValueError:
            print("Enter a whole number...")
    cafedrink_name.append(new_cafedrink_name)
    cafedrink_price.append(new_cafedrink_price)
    cafedrink_servings.append(new_cafedrink_servings)
    print(f'Cafedrink "{new_cafedrink_name}" added successfully.')

def add_dessert():
    print("==============================")
    print("         ADD NEW DESSERT")
    print("==============================")
    while True:
        new_dessert_name = input("Enter dessert name (Enter 0 to exit): ").strip()
        if new_dessert_name == "0":
            print("Exiting... Returning to Staff Menu.")
            return
        if new_dessert_name == "":
            print("Dessert name cannot be empty.")
            continue
        if any(char.isdigit() for char in new_dessert_name):
            print("Dessert name cannot contain numbers.")
            continue
        if not all(char.isalpha() or char.isspace() for char in new_dessert_name):
            print("Dessert name cannot contain special characters.")
            continue
        parts = new_dessert_name.split()
        if len(parts) > 1 and all(len(part) == 1 for part in parts):
            print("Invalid name format. Please enter a proper drink name.")
            continue
        if new_dessert_name.lower() in [d.lower() for d in dessert_name]:
            print("This dessert already exists... Try Again")
            continue
        break
    while True:
        try:
            new_dessert_price = float(input("Enter price: "))
            if new_dessert_price <= 0:
                print("Invalid price... Try Again.")
                continue
            break
        except ValueError:
            print("Enter a valid number...")
    while True:
        try:
            new_dessert_qty = int(input("Enter quantity: "))
            if new_dessert_qty <= 0:
                print("Invalid quantity... Try Again.")
                continue
            break
        except ValueError:
            print("Enter a whole number...")
    dessert_name.append(new_dessert_name)
    dessert_price.append(new_dessert_price)
    dessert_quantity.append(new_dessert_qty)
    print(f'Dessert "{new_dessert_name}" added successfully.')

def show_current_order(order_items, total):
    print("\n=================================================================")
    print("                     YOUR CURRENT ORDER")
    print("=================================================================")
    
    if not order_items:
        print("No items in your order.")
    else:
        print(f"{'No.':<5} | {'ITEM':<28} | {'QTY':<6} | {'AMOUNT':<10}")
        print("-" * 65)
        
        for i, (item_type, name, qty, price) in enumerate(order_items, 1):
            line_total = qty * price
            item_label = f"{name} ({item_type})"
            # Keep it clean if the name is too long
            if len(item_label) > 28:
                item_label = item_label[:25] + "..."
            print(f"{i:<5} | {item_label:<28} | {qty:<6} | ₱{line_total:<9.2f}")
        
        print("-" * 65)
        print(f"{'':<5}  {'':<28} | {'TOTAL':<6} | ₱{total:<9.2f}")
    
    print("=================================================================\n")

def staff_verify_payment():
    print("\n    STAFF VERIFICATION REQUIRED TO COMPLETE PAYMENT    ")
    while True:
        username = input("Staff Username: ").strip()
        password = input("Staff Password: ").strip()
        if username == STAFF_USER and password == STAFF_PASS:
            print("Payment verified by staff. Thank you!\n")
            return True
        else:
            print("Incorrect credentials. Please try again.\n")

def order():
    global queue_number
    if len(cafedrink_name) == 0 and len(dessert_name) == 0:
        print("The menu is empty...")
        return
    total = 0.0
    order_items = []
    while True:
        print("\n==============================")
        print("      ORDERING OPTIONS")
        print("==============================")
        print("cd  - Order Cafedrinks")
        print("de  - Order Desserts")
        print("v   - View current order")
        print("0   - Proceed to Payment")
        print("==============================")
        choice = input("Enter your choice (cd / de / v / 0): ").strip().lower()
        if choice == "0":
            break
        elif choice == "v":
            show_current_order(order_items, total)
        elif choice == "cd":
            while True:
                print()
                view_cafedrink_menu()
                cafedrink_choice = input("Enter dish number (0 to go back): ").strip()
                if cafedrink_choice == "0":
                    break
                if not cafedrink_choice.isdigit():
                    print("Enter a valid number.")
                    continue
                cafedrink_num = int(cafedrink_choice)
                if cafedrink_num < 1 or cafedrink_num > len(cafedrink_name):
                    print("Invalid cafedrink number.")
                    continue
                idx = cafedrink_num - 1
                available = cafedrink_servings[idx]
                print(f"Available servings: {available}")
                qty_input = input("Enter quantity: ").strip()
                if not qty_input.isdigit():
                    print("Enter a valid quantity.")
                    continue
                quantity = int(qty_input)
                if quantity <= 0:
                    print("Quantity must be greater than zero.")
                    continue
                if quantity > available:
                    print(f"Not enough servings. Only {available} left.")
                    continue
                unit_price = cafedrink_price[idx]
                total += unit_price * quantity
                # Combine similar dishes
                found = False
                for i in range(len(order_items)):
                    if order_items[i][0] == "Dish" and order_items[i][1] == cafedrink_name[idx]:
                        old_qty = order_items[i][2]
                        order_items[i] = ("Cafedrink", cafedrink_name[idx], old_qty + quantity, unit_price)
                        found = True
                        break
                if not found:
                    order_items.append(("Cafedrink", cafedrink_name[idx], quantity, unit_price))
                cafedrink_servings[idx] -= quantity
                print(f"{quantity} x {cafedrink_name[idx]} added to your order.")
                show_current_order(order_items, total)   # show after every addition
                check_and_archive_cafedrink(idx)
        elif choice == "de":
            while True:
                print()
                view_dessert_menu()
                dessert_choice = input("Enter dessert number (0 to go back): ").strip()
                if dessert_choice == "0":
                    break
                if not dessert_choice.isdigit():
                    print("Enter a valid number.")
                    continue
                dessert_num = int(dessert_choice)
                if dessert_num < 1 or dessert_num > len(dessert_name):
                    print("Invalid dessert number.")
                    continue
                idx = dessert_num - 1
                available = dessert_quantity[idx]
                print(f"Available quantity: {available}")
                qty_input = input("Enter quantity: ").strip()
                if not qty_input.isdigit():
                    print("Enter a valid quantity.")
                    continue
                quantity = int(qty_input)
                if quantity <= 0:
                    print("Quantity must be greater than zero.")
                    continue
                if quantity > available:
                    print(f"Not enough stock. Only {available} left.")
                    continue
                unit_price = dessert_price[idx]
                total += unit_price * quantity
                # Combine similar drinks
                found = False
                for i in range(len(order_items)):
                    if order_items[i][0] == "Dessert" and order_items[i][1] == dessert_name[idx]:
                        old_qty = order_items[i][2]
                        order_items[i] = ("Dessert", dessert_name[idx], old_qty + quantity, unit_price)
                        found = True
                        break
                if not found:
                    order_items.append(("Dessert", dessert_name[idx], quantity, unit_price))
                dessert_quantity[idx] -= quantity
                print(f"{quantity} x {dessert_name[idx]} added to your order.")
                show_current_order(order_items, total)
                check_and_archive_dessert(idx)
        else:
            print("Invalid choice. Please type 'cd', 'de', 'v', or '0'.")
    if len(order_items) == 0:
        print("No orders placed.")
        return

    # Final review before payment
    print("\n =====   FINAL ORDER REVIEW   ===== ")
    show_current_order(order_items, total)
    confirm = input("Proceed to payment? (y/n): ").strip().lower()
    if confirm != "y":
        print("Order cancelled. Returning to Customer Menu.")
        return
    if not staff_verify_payment():
        print("Payment was not completed. Order cancelled.")
        return
    current_queue = queue_number
    queue_number += 1
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    receipt = {
        "queue": current_queue,
        "items": order_items,
        "total": total,
        "timestamp": timestamp,
        "paid": True
    }
    recorded_receipts.append(receipt)
    daily_sales.append(receipt)
    print("\n==============================")
    print(f"     QUEUE NUMBER: {current_queue:03d}")
    print("==============================")
    print("           RECEIPT")
    print("==============================")
    print(f"Date/Time : {timestamp}")
    for item_type, name, qty, price in order_items:
        line_total = qty * price
        print(f"{qty} x {name} ({item_type}) - ₱{line_total:.2f}")
    print("------------------------------")
    print(f"Total bill: ₱{total:.2f}")
    print(f"Your Queue Number is: {current_queue:03d}")
    print("Status: PAID")
    print("==============================")
    print("Please wait for your number to be called. Thank you!\n")

def check_and_archive_cafedrink(index):
    if cafedrink_servings[index] <= 0:
        name = cafedrink_name[index]
        archive_cafedrinks.append(cafedrink_name[index])
        archive_price.append(cafedrink_price[index])
        archive_serving.append(cafedrink_servings[index])
        print(f'"{name}" (Cafedrink) is now out of stock and moved to archive.')

def check_and_archive_dessert(index):
    if dessert_quantity[index] <= 0:
        name = dessert_name[index]
        archive_dessert.append(dessert_name[index])
        archive_dessert_price.append(dessert_price[index])
        archive_dessert_quantity.append(dessert_quantity[index])
        print(f'"{name}" (Dessert) is now out of stock and moved to archive.')

def view_out_of_stock():
    print("\n==============================")
    print("     OUT OF STOCK / ARCHIVE")
    print("==============================")
    print("\n--- CAFEDRINKS ARCHIVE ---")
    if len(archive_cafedrinks) == 0:
        print("No cafedrinks are out of stock.")
    else:
        print(f"{'No.':<5} | {'Cafedrink Name':<25} | {'Price':<10} | {'Servings':<8}")
        print("-" * 58)
        for i in range(len(archive_cafedrinks)):
            print(f"{i+1:<5} | {archive_cafedrinks[i]:<25} | ₱{archive_price[i]:<9.2f} | {archive_serving[i]:<8}")
    print("\n--- DESSERTS ARCHIVE ---")
    if len(archive_dessert) == 0:
        print("No desserts are out of stock.")
    else:
        print(f"{'No.':<5} | {'Dessert Name':<25} | {'Price':<10} | {'Quantity':<8}")
        print("-" * 58)
        for i in range(len(archive_dessert)):
            print(f"{i+1:<5} | {archive_dessert[i]:<25} | ₱{archive_dessert_price[i]:<9.2f} | {archive_dessert_quantity[i]:<8}")
    print("==============================\n")

def view_recorded_receipts():
    print("\n==============================")
    print("      RECORDED RECEIPTS")
    print("==============================")
    if len(recorded_receipts) == 0:
        print("No receipts have been recorded yet.")
        print("==============================\n")
        return
    for receipt in recorded_receipts:
        print(f"\nQueue Number : {receipt['queue']:03d}")
        print(f"Date/Time    : {receipt.get('timestamp', 'N/A')}")
        print(f"Status       : {'PAID' if receipt.get('paid') else 'UNPAID'}")
        print("------------------------------")
        for item_type, name, qty, price in receipt["items"]:
            line_total = qty * price
            print(f"  {qty} x {name:<22} ({item_type}) ₱{line_total:>8.2f}")
        print("------------------------------")
        print(f"  TOTAL{' ' * 30} ₱{receipt['total']:>8.2f}")
        print("==============================")
    print(f"\nTotal recorded orders: {len(recorded_receipts)}")
    print("==============================\n")

def daily_sales_report():
    print("\n==================================================")
    print("           DAILY SALES REPORT / SUMMARY")
    print("==================================================")
    if not daily_sales:
        print("No paid sales recorded yet today.")
        print("==================================================\n")
        return
    total_revenue = 0.0
    total_orders = len(daily_sales)
    item_count = {}          
    item_revenue = {}        
    for sale in daily_sales:
        total_revenue += sale["total"]
        for item_type, name, qty, price in sale["items"]:
            key = f"{name} ({item_type})"
            item_count[key] = item_count.get(key, 0) + qty
            item_revenue[key] = item_revenue.get(key, 0.0) + (qty * price)
    print(f"Total Paid Orders : {total_orders}")
    print(f"Total Revenue     : ₱{total_revenue:.2f}")
    print("--------------------------------------------------")
    print("ITEM BREAKDOWN")
    print(f"{'Item':<30} | {'Qty Sold':<10} | {'Revenue':<12}")
    print("-" * 58)
    for name in sorted(item_count.keys()):
        print(f"{name:<30} | {item_count[name]:<10} | ₱{item_revenue[name]:<11.2f}")
    print("--------------------------------------------------")
    print("DETAILED ORDERS")
    for sale in daily_sales:
        print(f"  Queue {sale['queue']:03d} | {sale['timestamp']} | ₱{sale['total']:.2f}")
    print("==================================================\n")

def edit():
    while True:
        print("\n==============================")
        print("          EDIT MENU")
        print("==============================")
        print("0. Go back")
        print("1. Edit Cafedrink Price")
        print("2. Edit Cafedrink Servings")
        print("3. Rename Cafedrink")
        print("4. Edit Dessert Price")
        print("5. Edit Dessert Quantity")
        print("6. Rename Dessert")
        print("==============================")
        choice = input("Enter choice: ").strip()
        if choice == "0":
            return
        elif choice == "1":
            edit_cafedrink_price()
        elif choice == "2":
            edit_cafedrink_servings()
        elif choice == "3":
            rename_cafedrink()
        elif choice == "4":
            edit_dessert_price()
        elif choice == "5":
            edit_dessert_quantity()
        elif choice == "6":
            rename_dessert()
        else:
            print("Invalid choice.")

def edit_cafedrink_price():
    view_cafedrink_menu()
    if not cafedrink_name:
        return
    choice = input("Enter cafedrink number to edit price (0 to cancel): ").strip()
    if choice == "0" or not choice.isdigit():
        return
    idx = int(choice) - 1
    if idx < 0 or idx >= len(cafedrink_name):
        print("Invalid number.")
        return
    current_price = cafedrink_price[idx]
    while True:
        try:
            new_price = float(input(f"New price for {cafedrink_name[idx]} (current: ₱{current_price:.2f}): "))
            if new_price <= 0:
                print("Price must be greater than 0.")
                continue
            if new_price == current_price:
                print("New price cannot be the same as the current price.")
                continue
            cafedrink_price[idx] = new_price
            print("Price updated.")
            break
        except ValueError:
            print("Enter a valid number.")

def edit_cafedrink_servings():
    view_cafedrink_menu()
    if not cafedrink_name:
        return
    choice = input("Enter cafedrink number to edit servings (0 to cancel): ").strip()
    if choice == "0" or not choice.isdigit():
        return
    idx = int(choice) - 1
    if idx < 0 or idx >= len(cafedrink_name):
        print("Invalid number.")
        return
    while True:
        try:
            new_serv = int(input(f"New servings for {cafedrink_name[idx]}: "))
            if new_serv < 0:
                print("Cannot be negative.")
                continue
            cafedrink_servings[idx] = new_serv
            print("Servings updated.")
            break
        except ValueError:
            print("Enter a whole number.")

def rename_cafedrink():
    view_cafedrink_menu()
    if not cafedrink_name:
        return
    choice = input("Enter cafedrink number to rename (0 to cancel): ").strip()
    if choice == "0" or not choice.isdigit():
        return
    idx = int(choice) - 1
    if idx < 0 or idx >= len(cafedrink_name):
        print("Invalid number.")
        return
    old = cafedrink_name[idx]
    while True:
        new_name = input(f"New name for '{old}': ").strip()
        if not new_name:
            print("Name cannot be empty.")
            continue
        if any(char.isdigit() for char in new_name):
            print("Cafedrink name cannot contain numbers.")
            continue
        if not all(char.isalpha() or char.isspace() for char in new_name):
            print("Cafedrink name cannot contain special characters.")
            continue
        parts = new_name.split()
        if len(parts) > 1 and all(len(part) == 1 for part in parts):
            print("Invalid name format. Please enter a proper dish name.")
            continue
        if new_name.lower() in [d.lower() for d in cafedrink_name]:
            print("Name already exists.")
            continue
        cafedrink_name[idx] = new_name
        print(f'Renamed to "{new_name}"')
        break

def edit_dessert_price():
    view_dessert_menu()
    if not dessert_name:
        return
    choice = input("Enter dessert number to edit price (0 to cancel): ").strip()
    if choice == "0" or not choice.isdigit():
        return
    idx = int(choice) - 1
    if idx < 0 or idx >= len(dessert_name):
        print("Invalid number.")
        return
    current_price = dessert_price[idx]
    while True:
        try:
            new_price = float(input(f"New price for {dessert_name[idx]} (current: ₱{current_price:.2f}): "))
            if new_price <= 0:
                print("Price must be greater than 0.")
                continue
            if new_price == current_price:
                print("New price cannot be the same as the current price.")
                continue
            dessert_price[idx] = new_price
            print("Price updated.")
            break
        except ValueError:
            print("Enter a valid number.")

def edit_dessert_quantity():
    view_dessert_menu()
    if not dessert_name:
        return
    choice = input("Enter dessert number to edit quantity (0 to cancel): ").strip()
    if choice == "0" or not choice.isdigit():
        return
    idx = int(choice) - 1
    if idx < 0 or idx >= len(dessert_name):
        print("Invalid number.")
        return
    while True:
        try:
            new_qty = int(input(f"New quantity for {dessert_name[idx]}: "))
            if new_qty < 0:
                print("Cannot be negative.")
                continue
            dessert_quantity[idx] = new_qty
            print("Quantity updated.")
            break
        except ValueError:
            print("Enter a whole number.")

def rename_dessert():
    view_dessert_menu()
    if not dessert_name:
        return
    choice = input("Enter dessert number to rename (0 to cancel): ").strip()
    if choice == "0" or not choice.isdigit():
        return
    idx = int(choice) - 1
    if idx < 0 or idx >= len(dessert_name):
        print("Invalid number.")
        return
    old = dessert_name[idx]
    while True:
        new_name = input(f"New name for '{old}': ").strip()
        if not new_name:
            print("Name cannot be empty.")
            continue
        if any(char.isdigit() for char in new_name):
            print("Dessert name cannot contain numbers.")
            continue
        if not all(char.isalpha() or char.isspace() for char in new_name):
            print("Dessert name cannot contain special characters.")
            continue
        parts = new_name.split()
        if len(parts) > 1 and all(len(part) == 1 for part in parts):
            print("Invalid name format. Please enter a proper drink name.")
            continue
        if new_name.lower() in [d.lower() for d in dessert_name]:
            print("Name already exists.")
            continue
        dessert_name[idx] = new_name
        print(f'Renamed to "{new_name}"')
        break

main_menu()
