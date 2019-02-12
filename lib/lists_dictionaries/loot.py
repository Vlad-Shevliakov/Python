inventory = {
    'rope': 1,
    'torch': 6,
    'gold_coin': 42,
    'arrow': 12
}

def getIventory(obj):
    total = 0
    for key, value in obj.items():
        total += value
        print(key + ': ' + str(value))
    print('Number of items: ' + str(total))


getIventory(inventory)
inventory.setdefault
# add to inventory

loot = ['arrow', 'arrow', 'gold_coin', 'yad']

def add_inventory(loot_array, inventory):
    print('################################')
    for item in loot_array:
        inventory.setdefault(item, 0)
        inventory[item] = inventory[item] + 1
    getIventory(inventory)

add_inventory(loot, inventory)