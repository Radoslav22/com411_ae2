def welcome():
    """
    Task 1: Display a welcome message.

    The welcome message should consist of the title 'Solar Record Management System' surrounded by dashes.
    The number of dashes before and after the title should be equal to the number of characters in the title 
    i.e. 30 dashes before and after.

    :return: Does not return anything.
    """
    title = 'Solar Record Management System'
    # Displaying the title surrounded by dashes
    print(len(title) * '-', title, len(title) * '-')


def menu():
    """
    Task 2: Display a menu of options and read the user's response.

    A menu consisting of the following options should be displayed:
    'Load Data', 'Process Data', 'Visualise Data', 'Save Data' and 'Exit'

    The user's response should be read in and returned as an integer corresponding to the selected option.
    For example, 1 for 'Load Data', 2 for 'Process Data' and so on.

    If the user enters a invalid option then a suitable error message should be displayed and the value
    None should be returned.

    :return: None if invalid selection otherwise an integer corresponding to a valid selection
    """
    # Displaying the main menu
    print("What would you like to do?")
    print("\n\t[1] Load Data")
    print("\t[2] Process Data")
    print("\t[3] Visualise Data")
    print("\t[4] Save Data")
    print("\t[5] Exit\n")
    # read the user response(integer)
    response = int(input())
    # Check if the response from the user is bigger than 5
    if response > 5:
        # Displaying error and return nothing
        error("There is no option with this number!")
        return None
    else:
        # Otherwise return the response from the user as an integer
        return response


def started(operation):
    """
    Task 3: Display a message to indicate that an operation has started.

    The function should display a message in the following format:
    '{operation} has started.'
    Where {operation} is the value of the parameter passed to this function

    :param operation: A string indicating the operation being started
    :return: Does not return anything
    """
    # Display the message
    print(f"{operation} has started.")


def completed(operation):
    """
    Task 4: Display a message to indicate that an operation has completed.

    The function should display a message in the following format:
    '{operation} has completed.'
    Where {operation} is the value of the parameter passed to this function

    :param operation: A string indicating the operation being completed
    :return: Does not return anything
    """
    # Display the message
    print(f"{operation} has completed.")


def error(error_msg):
    """
    Task 5: Display an error message.

    The function should display a message in the following format:
    'Error! {error_msg}.'
    Where {error_msg} is the value of the parameter passed to this function

    :param error_msg: A string containing an error message
    :return: Does not return anything
    """
    # Display the message
    print(f"Error! {error_msg}.")


def source_data_path():
    """
    Task 6: Retrieve a file path to the source data file.

    The function should prompt the user to enter the file path for a data file (e.g. 'data/sol_data.csv').
    If the file path entered by the user does not end in 'csv' then a suitable error message should be displayed
    and the value None should be returned.
    Otherwise, the file path entered by the user should be returned.

    :return: None if the file path does not end in 'csv' otherwise return the file path entered by the user
    """
    # Display a message and asking for the user response
    file_path = input("Please enter the file name:")
    # reading the last 4 character of the user response
    ext = file_path[-4:]
    # check if the user response end with ".csv"
    if ext == ".csv":
        # return the user response
        return file_path
    else:
        # Display error and return nothing
        error("Wrong file extension!")
        return None


def process_type():
    """
    Task 7: Display a menu of options for how the file should be processed. Read in the user's response.

    A menu should be displayed that contains the following options:
        'Retrieve entity', 'Retrieve entity details', 'Categorise entities by type',
        'Categorise entities by gravity', 'Summarise entities by orbit'

    The user's response should be read in and returned as an integer corresponding to the selected option.
    For example, 1 for 'Retrieve entity', 2 for 'Retrieve entity details' and so on.

    If the user enters a invalid option then a suitable error message should be displayed and the value
    None should be returned.

    :return: None if an invalid selection made otherwise an integer corresponding to a valid option
    """
    # Display menu for Process Data
    print("What would you like to do?")
    print("\n\t[1] Retrieve entity")
    print("\t[2] Retrieve entity details")
    print("\t[3] Categorise entities by type")
    print("\t[4] Categorise entities by gravity")
    print("\t[5] Summarise entities by orbit\n")
    # read the user response(integer)
    processing_data = int(input())
    # Check if the user response is less than or equal to 5
    if processing_data <= 5:
        # return the user response as an integer
        return processing_data
    else:
        # Display error message and return nothing
        error("There is no option with this number")
        return None


def entity_name():
    """
    Task 8: Read in the name of an entity and return the name.

    The function should ask the user to enter the name of an entity e.g. 'Earth'
    The function should then read in and return the user's response.

    :return: the name of an entity
    """
    # Display a message
    print("What is the name of the entity:")
    # Reading the user response
    name_of_entity = input()
    # return the user response
    return name_of_entity


def entity_details():
    """
    Task 9: Read in the name of an entity and column indexes. Return a list containing the name and indexes.

    The function should ask the user to enter the name of an entity e.g. 'Earth'
    The function should also ask the user to enter a list of integer column indexes e.g. 0,1,5,7
    The function should return a list containing the name of the entity and the list of column
    indexes e.g. ['Earth', [0,1,5,7]]

    :return: A list containing the name of an entity and a list of column indexes
    """
    # empty list
    entity_cols = []
    # using the input from another function
    entity_input = entity_name()
    # append into the list
    entity_cols.append(entity_input)
    # Display message
    print("Please enter a list of integer column indexes:")
    # Read and split by comma the user response
    indexes = input().split(",")
    # empty list for the column indexes(integer)
    indexes_int = []
    # loop for every index from the user response(indexes)
    for index in indexes:
        # append the user response index as an integer in the list indexes_int
        indexes_int.append(int(index))
    # Combine the entity name and the cols list into one list
    entity_cols.append(indexes_int)
    # return the list e.g. ["Entity", [0,1,2,3]]
    return entity_cols


def list_entity(entity, cols=[]):
    """
    Task 10: Display an entity. Only the data for the specified column indexes will be displayed.
    If no column indexes have been specified, then all the data for the entity will be displayed.

    The entity is a list of values corresponding to particular Solar System space entity
    E.g. ['Earth', TRUE, 9.8].
    The function should only display those values from the entity list that correspond to the column
    indexes provided as part of cols.
    E.g. if cols is [0, 2] then for the entity ['Earth', TRUE, 9.8] the following will be displayed
    ['Earth', 9.8]
    E.g. if cols is an empty list then all the values will be displayed i.e. ['Earth', TRUE, 9.8]

    :param entity: A list of data values related to an entity
    :param cols: A list of integer values that represent column indexes
    :return: does not return anything
    """
    # Check if cols is not equal to nothing
    if cols is None:
        cols = []
    if cols:
        # empty list
        entity_data = []
        # loop for each column in columns
        for col in cols:
            # Check if entity has columns
            if entity[col]:
                # appending to the list entity_data
                entity_data.append(entity[col])
        # check if the list is not empty
        if entity_data:
            # return the list with the data in it
            return entity_data
        # if the list is empty
        else:
            # return nothing
            return None
    # if the cols is equal to nothing
    else:
        # return the whole entity
        return entity


def list_entities(entities, cols=[]):
    """
    Task 11: Display each entity in entities. Only the data for the specified column indexes will be displayed.
    If no column indexes have been specified, then all the data for an entity will be displayed.

    The function should have two parameters as follows:
    entities    which is a list of entities where each entity itself is a list of data values
    cols        this is a list of integer values that represent column indexes.
                the default value for this is an empty list i.e. []

    You will need to add these parameters to the function definition.

    The function should iterate through each entity in entities and display the entity.
    An entity is a list of values e.g. ['Earth', TRUE, 9.8]
    Only the columns whose indexes are included in cols should be displayed for each entity.
    If cols is an empty list then all values for the entity should be displayed.

    :param entities: A list of data values related to an entity
    :param cols: A list of integer values that represent column indexes
    :return: Does not return anything
    """
    # empty list
    entities_data = []
    # loop for entity in entities
    for entity in entities:
        # append into the list using the list_entity function
        entities_data.append(list_entity(entity, cols))
    # return the list about entities data
    return entities_data


def list_categories(categories):
    """
    Task 12: Display the contents of the dictionary categories.

    The function should take a single parameter categories which is a dictionary containing category names
    and a list of entities that belong to the category.

    You will need to add the parameter categories to the function definition.

    :param categories: A dictionary containing category names and a list of entities that are part of that category
    :return: Does not return anything
    """
    for key, value in categories.items():
        print(f"{key}: {value}")


def gravity_range():
    """
    Task 13: Ask the user for the lower and upper limits for gravity and return a tuple containing the limits.

    The function should prompt the user to enter the lower and upper limit for a range of values related to gravity.
    The values will be floats e.g. 5.1 for lower limit and 9.8 for upper limit.
    The function should return a tuple containing the lower and upper limits

    :return: a tuple with the lower and upper limits
    """
    # empty list
    up_low_limit = []
    print("Please enter a lower and upper limits for gravity!")
    # output from user and split using comma
    limits = input().split(",")
    # loop for every element in limits appending in the list as float
    for index in limits:
        up_low_limit.append(float(index))
    # converting from list to tuple
    up_low_limit = tuple(up_low_limit)
    # return a tuple
    return up_low_limit


def orbits():
    """
    Task 14: Ask the user for a list of entity names and return the list.

    The function should prompt the user to enter a list of entity names e.g. Jupiter,Earth,Mars
    The list represents the entities that should be orbited.
    The user may enter as many entity names as they desire.
    The function should return a list of the entity names entered by the user.

    :return: a list of entity names
    """
    # empty list
    entity_names_orbit = []
    # Display message
    print("Please enter a list of entity names!")
    # Reading the user response
    names = input()
    # append the user response into the list
    entity_names_orbit.append(names)
    # return the list
    return entity_names_orbit


def visualise():
    """
    Task 15: Display a menu of options for how the data should be visualised. Return the user's response.

    A menu should be displayed that contains the following options:
        'Entities by type', 'Entities by gravity', 'Summary of orbits', 'Animate gravities'

    The user's response should be read in and returned as an integer corresponding to the selected option.
    For example, 1 for 'Entities by type', 2 for 'Entities by gravity' and so on.

    If the user enters an invalid option, then a suitable error message should be displayed and the value
    None should be returned.

    :return: None if an invalid selection is made otherwise an integer corresponding to a valid option
    """
    # Display menu for Visualise Data
    print("How would you like to visualise the data?")
    print("\n\t[1] Entities by type")
    print("\t[2] Entities by gravity")
    print("\t[3] Summary of orbits")
    print("\t[4] Animate gravities\n")
    # reading the user response(integer)
    visualise_data = int(input())
    # Check if the user response is bigger than 4 printing error message and return nothing
    if visualise_data > 4:
        error("\nThere is no option with this number!")
        return None
    else:
        # return the user response as an integer
        return visualise_data


def save():
    """
    Task 16: Display a menu of options for how the data should be saved. Return the user's response.

    A menu should be displayed that contains the following option:
         'Export as JSON'

    The user's response should be read in and returned as an integer corresponding to the selected option.

    If the user enters a invalid option then a suitable error message should be displayed and the value
    None should be returned.

    :return: None if an invalid selection is made otherwise an integer corresponding to a valid option
    """
    # Display menu for Save data
    print("How would you like to export the file?")
    print("\n\t[1] Export as JSON")
    # Read the user response as an integer
    saving_data = int(input())
    # Check if the user response is equal to 1 return the response
    if saving_data == 1:
        return saving_data
    else:
        # Otherwise return nothing and displaying error message
        error("Invalid option")
        return None
