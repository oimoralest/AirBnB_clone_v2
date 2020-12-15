# AirBnB_clone

## Description

    Updated

## Requirements

    Python scripts
    
    - Allowed editors: vi, vim, emacs
    - All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3).
    - All your files should end with a new line
    - The first line of all your files should be exactly #!/usr/bin/python3.
    - A README.md file, at the root of the folder of the project, is mandatory.
    - Your code should use the PEP 8 style (version 1.7.*)
    - All your files must be executable
    - The length of your files will be tested using wc
    - All your modules should have documentation (python3 -c 'print(__import__("my_module").__doc__)')
    - All your classes should have documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
    - All your functions (inside and outside a class) should have documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
    - A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)


## Installation

    - Clone this repository
    - Access to AirBnb directory: cd AirBnb_clone
    - Run console (Interactive mode): ./console.py
    - Run (Non-interactive mode): echo "<command>" | ./console.py

## Using the console

    List of available commands:
    - quit and EOF: exits the console
        Example: (htbn) quit or (htbn) EOF
    - help: lists all available commands or the description for a command
        Example: (htbn) help or (htbn) ? or (htbn) help <command>
    - create: creates a new instance of a class
        Example: (hbtn) create <class>
            Available classes:
                - Amenity
                - BaseModel
                - City
                - Place
                - Review
                - State
                - User
    - show: prints the string representation of an instance
        Example: (hbtn) show <class> <id>
            The <id> could be readed from file.json or obtained from the command all
    - all: prints all string representation of all instances of a class or all instances
        Example: (htbn) all <class> or (htbn) all
    - update: updates an instance adding or updating an attribute (only once at time)
        Example: (htbn) update <class> <id> <attribute_name> <attribute_value>
    - destroy: deletes an instance
        Example: (htbn) destroy <class> <id>

## Content

| File | Description |
| --- | --- |
| [console.py](./console.py) | Console |

### Models directory

| File | Description |
| --- | --- |
| [\_\_init__.py](./models/__init__.py) | Init for models module. Links base_model and file_storage |
| [amenity.py](./models/amenity.py) | Module for Amenity class |
| [base_model.py](./models/base_model.py) | Module for BaseModel class. All other classes for models module inherit from this one |
| [city.py](./models/city.py) | Module for City class |
| [place.py](./models/place.py) | Module for Place class |
| [review.py](./models/review.py) | Module for Review class |
| [state.py](./models/state.py) | Module for State class |
| [user.py](./models/user.py) | Module for User class |

#### Models/Engine directory

| File | Description |
| --- | --- |
| [\_\_init__.py](./models/engine/__init__.py) | Init for engine module |
| [file_storage.py](./models/engine/file_storage.py) | Module for FileStorage class. Manages the storage of all objects |

### Tests directory

    Test suite fo this project

## Bugs

    No bugs at this time