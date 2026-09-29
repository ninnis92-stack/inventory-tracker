# Inventory Item Tracker

A beginner-friendly command-line inventory tracker written in Python. It supports adding, viewing, updating, retrieving, and deleting inventory items, with local JSON persistence.

## Features

- Add inventory items with descriptions, quantities, prices, categories, statuses, and suppliers
- View all saved items
- Update an item's fields by ID
- Retrieve a single item by ID
- Delete an item by ID
- Automatically assign the next available item ID
- Save inventory locally in `inventory.json`

## Requirements

- Python 3.9 or newer

## Run the tracker

```bash
python inventory_tracker.py
```

The first time the program saves an item, it creates `inventory.json` in the project directory. That file is intentionally ignored by Git because it contains local inventory data.

## Project layout

```text
inventory_tracker.py  # Application source
inventory.json        # Local data file created at runtime (not committed)
```

## Learning context

This is a first project focused on Python functions, lists of dictionaries, loops, JSON persistence, input validation, and a menu-driven CLI.
