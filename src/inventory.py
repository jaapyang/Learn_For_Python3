# inventory.py

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
inv = {'gold coin': 12, 'dagger': 2, 'arrow': 1}
dragonLoot = ['gold coin','dagger','god coin','god coin','ruby']

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    # print(inventory['gold coin'])
    for k, v in inventory.items():
        print('   ' + str(v) + ' ' + k)
        item_total += v
    print('Total number of items:' + str(item_total))


displayInventory(stuff)
