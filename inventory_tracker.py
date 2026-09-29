import datetime
import json
import os


INVENTORY_FILE = "inventory.json"


def load_inventory():
    """Load inventory data, returning an empty list for a new project."""
    if not os.path.exists(INVENTORY_FILE):
        return []

    with open(INVENTORY_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, list):
        raise ValueError("inventory.json must contain a list of inventory items")

    return data


def save_inventory(inventory):
    with open(INVENTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(inventory, file, indent=4)
    print("Inventory saved successfully")


def create_inventory_item(inventory_id, description, quantity, price, category, status, supplier, timestamp):
    return {
        "id": inventory_id,
        "description": description,
        "quantity": quantity,
        "price": price,
        "category": category,
        "status": status,
        "supplier": supplier,
        "time_created": timestamp,
        "time_updated": timestamp,
    }


def add_inventory_item(inventory):
    description = input("Enter an inventory item's description: ").strip()
    quantity = input("Enter an inventory item's quantity: ").strip()
    price = input("Enter an inventory item's price: ").strip()
    category = input("Enter an inventory item's category: ").strip()
    status = input("Enter an inventory item's status: ").strip()
    supplier = input("Enter an inventory item's supplier: ").strip()

    if not all((description, quantity, price, category, status, supplier)):
        print("All inventory item fields are required")
        return

    try:
        quantity = int(quantity)
        price = float(price)
    except ValueError:
        print("Quantity must be a whole number and price must be a number")
        return

    next_id = max((item["id"] for item in inventory), default=0) + 1
    now = datetime.datetime.now().isoformat()
    inventory.append(create_inventory_item(
        next_id, description, quantity, price, category, status, supplier, now
    ))
    save_inventory(inventory)
    print("Inventory item added successfully")


def view_inventory_items(inventory):
    if not inventory:
        print("No inventory items found")
        return

    for inventory_item in inventory:
        print(json.dumps(inventory_item, indent=4))


def find_inventory_item(inventory):
    try:
        inventory_id = int(input("Enter the inventory item ID: "))
    except ValueError:
        print("Inventory item ID must be a number")
        return None

    for inventory_item in inventory:
        if inventory_item["id"] == inventory_id:
            return inventory_item

    print("Inventory item not found")
    return None


def update_inventory_item(inventory):
    inventory_item = find_inventory_item(inventory)
    if inventory_item is None:
        return

    fields = {
        "1": ("description", str),
        "2": ("quantity", int),
        "3": ("price", float),
        "4": ("category", str),
        "5": ("status", str),
        "6": ("supplier", str),
    }
    print("1. Description\n2. Quantity\n3. Price\n4. Category\n5. Status\n6. Supplier")
    choice = input("Choose a field to update: ")
    if choice not in fields:
        print("Invalid choice")
        return

    field, converter = fields[choice]
    new_value = input(f"Enter the new {field}: ").strip()
    if not new_value:
        print(f"{field.capitalize()} cannot be empty")
        return

    try:
        inventory_item[field] = converter(new_value)
    except ValueError:
        print(f"Invalid value for {field}")
        return

    inventory_item["time_updated"] = datetime.datetime.now().isoformat()
    save_inventory(inventory)
    print("Inventory item updated successfully")


def retrieve_inventory_item(inventory):
    inventory_item = find_inventory_item(inventory)
    if inventory_item is not None:
        print(json.dumps(inventory_item, indent=4))
        print("Inventory item retrieved successfully")


def delete_inventory_item(inventory):
    inventory_item = find_inventory_item(inventory)
    if inventory_item is None:
        return

    inventory.remove(inventory_item)
    save_inventory(inventory)
    print("Inventory item deleted successfully")


def main():
    inventory = load_inventory()

    while True:
        print("\nInventory Item Tracker")
        print("1. Add an inventory item")
        print("2. View all inventory items")
        print("3. Update an inventory item")
        print("4. Delete an inventory item by ID")
        print("5. Retrieve an inventory item by ID")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_inventory_item(inventory)
        elif choice == "2":
            view_inventory_items(inventory)
        elif choice == "3":
            update_inventory_item(inventory)
        elif choice == "4":
            delete_inventory_item(inventory)
        elif choice == "5":
            retrieve_inventory_item(inventory)
        elif choice == "6":
            print("Thank you for using Inventory Item Tracker")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
