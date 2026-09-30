# Inventory Item Tracker

A beginner-friendly command-line inventory tracker written in Python. It supports adding, viewing, updating, retrieving, and deleting inventory items, with local JSON or CSV persistence.

## Features

- Add inventory items with descriptions, quantities, prices, categories, statuses, and suppliers
- View all saved items
- Update an item's fields by ID
- Retrieve a single item by ID
- Delete an item by ID
- Automatically assign the next available item ID
- Save inventory locally in `inventory.json`
- Create and switch between multiple JSON or CSV inventory files
- Track both sale price and item cost

## Requirements

- Python 3.9 or newer

## Run the tracker

```bash
python inventory_tracker.py
```

The program lets you load an existing JSON or CSV file, or create a new one. Inventory data files are intentionally ignored by Git because they contain local inventory data.

## Project layout

```text
inventory_tracker.py  # Application source
inventory*.json       # Local data files created at runtime (not committed)
inventory*.csv        # Local data files created at runtime (not committed)
```

## Learning context

This is a first project focused on Python functions, lists of dictionaries, loops, JSON/CSV persistence, input validation, and a menu-driven CLI.
