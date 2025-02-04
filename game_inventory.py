import os
# This is the file where you must work.
# Write code in the functions (and create new functions) so that they work
# according to the requirements.

# a = "food"
# b = "armor"
# c = "gold coin"
# d = "arrow"
# e = "torch"
# f = "dagger"
# g = "rope"
# h = "ruby"
added_items = []
removed_items = []


def main_menu():
    menu_dict = {
        "Add item": 1,
        "Remove item": 2,
        "Display inventory": 3,
        "Display fancy inventory": 4,
        "Import inventory from CSV file": 5,
        "Export inventory to CSV file": 6
        }
    print("\n" "What action do you want to perform?")
    print("1. Add item")
    print("2. Remove item")
    print("3. Display inventory")
    print("4. Display fancy inventory")
    print("5. Import inventory from CSV file")
    print("6. Export inventory to CSV file")
    x = input("")
    for k, v in menu_dict.items():
        if int(x) == 1:
            os.system("cls")
            update_added_items()
            add_to_inventory(inventory, added_items)
            main_menu()
        elif int(x) == 2:
            os.system("cls")
            remove_from_inventory(inventory, removed_items)
            main_menu()
        elif int(x) == 4:
            os.system("cls")
            print_table(inventory, "count,desc")
            main_menu()
        elif int(x) == 3:
            os.system("cls")
            display_inventory(inventory)
            main_menu()
        elif int(x) == 5:
            os.system("cls")
            import_inventory(inventory, filename="test_inventory.csv")
            main_menu()
        elif int(x) == 6:
            os.system("cls")
            export_inventory(inventory, filename="test_inventory.csv")
            main_menu()


def create_inventory():
    global inventory
    inventory = {
        "gold coin": 45,
        "arrow": 12,
        "torch": 6,
        "dagger": 2,
        "rope": 1,
        "ruby": 1
        }
    return inventory


def update_added_items():
    # all_items = [k for k, v in inventory.items()]
    print("\n" "What item do you want to add?")
    x = input("")
    if x.isnumeric():
        print("\n" "Only letters please")
        update_added_items()
    else:
        print("\n" "How many of those should i add?")
        y = input("")
        for i in range(int(y)):
            added_items.append(x)
    return added_items


def display_inventory(inventory):
    # """Display the contents of the inventory in a simple way."""
    print("\n")
    for k, v in inventory.items():
        print(k, ": ", v)
    print("\n")
    return inventory


def add_to_inventory(inventory, added_items):
    # """Add to the inventory dictionary a list of items from added_items."""
    for i in added_items:
        inventory.setdefault(i, 0)
        inventory[i] = inventory[i] + 1
    return inventory


def remove_from_inventory(inventory, removed_items):
    # """Remove from the inventory dictionary a list of items from removed_items."""
    print("\n" "What item do you want to remove?")
    x = input("")
    if x.isnumeric():
        print("\n" "Only letters please")
        remove_from_inventory(inventory, removed_items)
    for k, v in inventory.items():
        if x in k:
            print("\n" "How many of those should i remove?")
            y = input("")
            if y.isnumeric():
                inventory[k] -= int(y)
                if inventory[k] == 0:
                    del inventory[k]
                    return inventory
                else:
                    main_menu()
            else:
                print("\n" "Only numbers please")
                remove_from_inventory(inventory, removed_items)
        elif x not in k:
            print("\n" "That item isn't in your inventory")
            remove_from_inventory(inventory, removed_items)


def print_table(inventory, order):  # Not mine, don't like it, too huge
    # """
    # Display the contents of the inventory in an ordered, well-organized table with
    # each column right-aligned.
    # """
    print("Inventory:")
    total_amount = []
    item_strings = []
    space = " "
    sepparator = " |"
    if order == "count,desc":
        max_length = max(len(x) for x in inventory)
        count = 2 * space + "count"
        item_name = (int((max_length / 2)) * space + "item name")
        headline = count + sepparator + item_name
        print(headline + "\n" + "-" * len(headline))
        for items, amount in sorted(inventory.items(), key=lambda x: x[1], reverse=True):
            print((7 - len(str(amount))) * space + str(amount) + sepparator + space * (len(item_name) - len(str(items))) + str(items))
            total_amount.append(amount)
            item_strings.append(items)
        print("-" * len(headline))
    if order == "count,asc":
        max_length = max(len(x) for x in inventory)
        count = 2 * space + "count"
        item_name = (int((max_length / 2)) * space + "item name")
        headline = count + item_name
        print(headline + "\n" + "-" * len(headline))
        for items, amount in sorted(inventory.items(), key=lambda x: x[1]):
            print(
                (7 - len(str(amount))) * space + str(amount) + space * (len(item_name) - len(str(items))) + str(items))
            total_amount.append(amount)
            item_strings.append(items)
        print("-" * len(headline))
    if order is None:
        max_length = max(len(x) for x in inventory)
        count = 2 * space + "count"
        item_name = (int((max_length / 2)) * space + "item name")
        headline = count + item_name
        print(headline + "\n" + "-" * len(headline))
        for items, amount in inventory.items():
            print(
                (7 - len(str(amount))) * space + str(amount) + space * (len(item_name) - len(str(items))) + str(items))
            total_amount.append(amount)
            item_strings.append(items)
        print("-" * len(headline))

    total_amount = sum(total_amount)
    print("Total number of items: {0}".format(total_amount) + "\n")


def import_inventory(inventory, filename="test_inventory.csv"):
    # """Import new inventory items from a CSV file."""
    content = open(filename).readlines()
    new_string = str(content)
    new_string = new_string.replace("'", "")
    new_string = new_string.replace("[", "")
    new_string = new_string.replace("]", "")
    new_string = new_string.split(",")
    add_to_inventory(inventory, new_string)
    print("Import succesful")


def export_inventory(inventory, filename="export_inventory.csv"):
    # """Export the inventory into a CSV file."""
    newstring = ""
    for x in inventory:
        newstring += (x + ",") * inventory[x]
    with open(filename, "w") as myfile:
        myfile.write(newstring.strip(""))
    print("Export succesful")


def main():
    create_inventory()
    main_menu()
    # display_inventory(inventory)
    # update_added_items()
    # add_to_inventory(inventory, added_items)
    # display_inventory(inventory)


main()
