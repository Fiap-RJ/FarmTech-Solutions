def create_data(value, data):
    """
    Adds a new value to the data list.
    """
    data.append(value)
    print(f"Data added: {value}")

    return data

def read_data(data):
    """
    Displays all stored values in the data list.
    """
    if not data:
        print("No data stored.")
    else:
        print("Stored data:")
        i = 0
        while i < len(data):
            print(f"{i}: {data[i]}")
            i += 1

    return data

def get_data(index, data):
    """
    Retrieves a value from the data list based on the given index.
    """
    if index < 0 or index >= len(data):
        print("Invalid index!")
        return None

    return data[index]


def update_data(index, new_value, data):
    """
    Updates a value in the data list based on the given index.
    """
    if index < 0 or index >= len(data):
        print("Invalid index!")
    else:
        data[index] = new_value
        print(f"Data updated at index {index}: {new_value}")

    return data

def delete_data(index, data):
    """
    Removes a value from the data list based on the given index.
    """
    if index < 0 or index >= len(data):
        print("Invalid index!")
    else:
        removed_value = data.pop(index)
        print(f"Data removed: {removed_value}")

    return data

