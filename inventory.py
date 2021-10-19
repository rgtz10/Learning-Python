# inventory.py
stuff = {'gold coin': 42, 'rope': 1}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        # Fill this part in
        print(str(v) + " " + k)
        item_total = item_total + v
    print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):
    for l in addedItems:
        inventory.setdefault(l,0)
        inventory[l] = inventory[l] + 1
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inventory = addToInventory(stuff, dragonLoot)
displayInventory(stuff)
