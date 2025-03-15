# Python - Data CRUD

This module contains functions to perform CRUD operations (Create, Read, Update, Delete) on a data list.

## Functions

### `create_data(value, data)`

- **Description:** Adds a new value to the data list.
- **Parameters:**
  - `value` (`str`): The value to be added to the data list.
  - `data` (`list`): The current data list to which the value will be appended.
- **Return:** The updated data list (with the newly added value).

### `read_data(data)`

- **Description:** Displays all stored values in the data list.
- **Parameters:**
  - `data` (`list`): The data list to be displayed.
- **Return:** The original data list (no modification).

### `update_data(index, new_value, data)`

- **Description:** Updates a value in the data list at the specified index.
- **Parameters:**
  - `index` (`int`): The index of the value to be updated.
  - `new_value` (`str`): The new value that will replace the current value at the specified index.
  - `data` (`list`): The current data list.
- **Return:** The updated data list with the modified value at the specified index.

### `delete_data(index, data)`

- **Description:** Removes a value from the data list at the specified index.
- **Parameters:**
  - `index` (`int`): The index of the value to be removed.
  - `data` (`list`): The current data list.
- **Return:** The updated data list with the specified value removed.

## Usage Example

```python
from crud import create_data, read_data, update_data, delete_data

data = []

# Create data
data = create_data("Sugarcane", data)
data = create_data("Tomato", data)

# Read data
read_data(data)

# Update data
data = update_data(0, "Modified Sugarcane", data)

# Delete data
data = delete_data(1, data)

# Read updated data
read_data(data)
```
