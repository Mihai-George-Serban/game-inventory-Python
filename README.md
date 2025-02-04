# Game inventory

## Story

You just started to work at a game developer company named Eastwood Studios
and they decided to create a new text-based role-playing video game.
You are responsible for implementing the inventory system of the game which
will store, show and manage the acquired goods of the player.

As there are other developers on this project implementing other parts of the game
it's crucial to use the provided function names and conform with the requirements
to have a well-working final product.

## What are you going to learn?

You will learn and practice how to do the following things with Python:

- use loops,
- use the dictionary data structure,
- printing data on console in an organized way,
- work with files,
- handle errors.

## Tasks


1. Write a function named `display_inventory(inventory)` that would take any possible inventory as dictionary and display its contents.

    - Calling the function with a non-empty dictionary argument results in displaying each key, followed by a colon, then a space, then the corresponding value, then a newline
    - Calling the function with an empty dictionary results in displaying nothing

2. Write a function named `add_to_inventory(inventory, added_items)` that would add the contents of the `added_items` list to the `inventory` dictionary.

    - Calling the function with a dictionary and items which aren't in the inventory yet results in that the items are added to the inventory as keys and values are set to 1
    - Calling the function with a dictionary and items which are already in the inventory results in that those items' value are incremented by 1
    - The function could handle if the `added_items` argument contains multiple occurences of the same item, then dictionary values are incremented by the number of occurences

3. Write a function named `remove_from_inventory(inventory, removed_items)` that would remove the contents of the `removed_items` list from the `inventory` dictionary.

    - Calling the function with a dictionary and items which are already in the inventory results in that the values of the keys matching the items are decreased by 1
    - If any value in the dictionary becomes 0 or less after decreasing, the corresponding key is removed
    - The function could handle if the `removed_items` argument contains multiple occurences of the same item, then dictionary values are decreased by the number of occurences
    - Calling the function with a dictionary and items which aren't in the inventory results in no change in the dictionary

4. Write a function named `print_table(inventory, order)` that takes an inventory as parameter and displays it in an ordered, well-organized table with each column right-aligned.

    - Calling the function with a non-empty dictionary argument results
in displaying a two-column table with all the items, where the first
column contains the keys and the second column contains the values
as seen in the example below:

          -----------------
          item name | count
          -----------------
          gold coin |    45
              arrow |    12
              torch |     6
             dagger |     2
               rope |     1
               ruby |     1
          -----------------
    - The printing order can be set with the `order` parameter as follows:
      * empty (by default) means the table is unordered
      * `count,desc` means the table is ordered by count (of items in the inventory) in descending order
      * `count,asc` means the table is ordered by count in ascending order

5. Write a function named `import_inventory(inventory, filename)` which can import new inventory items from a CSV file.

    - The function can handle CSV files containing items in the following format:
`ruby,rope,ruby,gold coin,ruby,axe`
    - Calling the function with a dictionary and items in a file in comma separated format (e.g. `rope, torch, arrow`) which aren't in the inventory yet results in that the items are added to the inventory as keys and values are set to 1
    - Calling the function with a dictionary and items in a CSV file which are already in the inventory results in that those items' value are incremented by 1
    - The function could handle if the CSV file contains multiple occurences of the same item, then dictionary values are incremented by the number of occurences
    - If not specified, the `filename` argument is by default `import_inventory.csv`
    - If the file provided in the `filename` argument cannot be reached on the disk, then the error message `File '<filename>' not found!` is shown on the console output

6. Write a function named `export_inventory(inventory, filename)` which can export all inventory items to a CSV file.

    - Calling the function with a non-empty dictionary and a `filename` argument results in the dictionary keys to be saved in CSV format in the file
    - If there are keys in the dictionary with values greater than 1, then the key is saved into the file as many times as the value
    - If not specified, the `filename` argument is by default `export_inventory.csv`
    - The file denoted in the `filename` argument is automatically created if not exists, and is overwritten if already exists
    - If the user executing the function does not have write access in the folder where the script is executed then the error message `You don't have permission creating file '<filename>'!` is shown on the console output


## General requirements


None

## Hints

- You can use a for loop to loop through all the keys in a dictionary.
- You can use [F-strings](https://realpython.com/python-f-strings/) to print out
  variables mixed with text comfortably.
- Feel free to include any code in the main part of the program (outside of
  the functions) during development if you want to try out your functions.
  Make sure you remove these lines or protect them with an `if __name__ == "__main__":`
  [code snippet](https://docs.python.org/3/library/__main__.html) before pushing
  your code.
- This project has public tests that can check whether your functions are working
  as intended. Run the test file with `python3 game_inventory_test.py -v` to get a
  detailed output. Note that passing all tests not necessarily means passing all
  requirements!

## Starting repository

Follow [this link](https://journey.code.cool/v2/project/solo/blueprint/game-inventory/python) to create your project repository.

## Background materials

- :exclamation: [Working with Dictionaries, and more Collection types](https://learn.code.cool/full-stack/#/../pages/python/working-with-dictionaries-and-more-collection-types)
- :exclamation: [Working with Strings](https://learn.code.cool/full-stack/#/../pages/python/working-with-strings-string-functions-and-manipulators)
- :exclamation: [Working with Functions and their arguments, input parameters or default parameters](https://learn.code.cool/full-stack/#/../pages/python/working-with-functions-and-their-arguments-input-parameters-or-default-parameters)
- :exclamation: [Sorting](https://learn.code.cool/full-stack/#/../pages/python/sorting)
- :exclamation: [Error handling in Python](https://python-textbok.readthedocs.io/en/stable/Errors_and_Exceptions.html)
(until the heading **The `with` statement**, from that part the article is not
important for this project)
- :open_book: [Built-in Exceptions in Python](https://docs.python.org/3/library/exceptions.html#bltin-exceptions)
- :open_book: [Modifying objects in-place](https://learn.code.cool/full-stack/#/../pages/python/modifying-objects)
- :open_book: [Understanding Variable scope, lifetime, modifying values and type conversions](https://learn.code.cool/full-stack/#/../pages/python/variable-scopes-and-conversions)
