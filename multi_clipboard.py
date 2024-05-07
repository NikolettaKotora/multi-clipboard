import sys
import clipboard
import json

SAVED_DATA = 'clipboard.json'

def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f, indent = 6)

def load_data(filepath):
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            return data
    except Exception as e:
        print("error in load", e)
        return {}
    
def file_chooser():
    pass
        


if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)
    
    if command == 'save':
        key = input('Enter a key: ')
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print("Data saved.")
    elif command == 'load':
        key = input('Enter a key: ')
        if key in data:
            clipboard.copy(data[key])
            print('Data copied to clipboard')
        else:
            print("Key doesn't exist.")
    elif command == 'list':
        print(data)
    
    # Delete something from json file / not deleting
    elif command == 'delete':
        key = input('Enter a key: ')
        try:
            if key in data:
                del data[key]
        except Exception as e:
            print("This has been already deleted", e)
        else:
            print('Data has been deleted.')

    else:
        print('Unknown command')
else:
    print('Please pass exactly one command.')
