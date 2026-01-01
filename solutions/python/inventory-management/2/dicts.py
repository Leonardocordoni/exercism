"""Functions to keep track and alter inventory."""


def create_inventory(items):
    inventory = {}

    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
            
    return inventory


def add_items(inventory, items):
    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1

    return inventory


def decrement_items(inventory, items):
    for item in items:
        if item in inventory and inventory[item] > 0:
            inventory[item] -= 1
            
    return inventory


def remove_item(inventory, item):
    inventory.pop(item, None)
    return inventory


def list_inventory(inventory):
    return [(item, qty) for item, qty in inventory.items() if qty > 0]