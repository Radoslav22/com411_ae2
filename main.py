# Task 17: Import the modules csv, tui and visual
import csv
import tui
import visual

# Task 18: Create an empty list named 'records'.
# This will be used to store the date read from the source data file.
records = []


def run():
    # Task 19: Call the function welcome of the module tui.
    # This will display our welcome message when the program is executed.
    tui.welcome()

    while True:
        # Task 20: Using the appropriate function in the module tui, display a menu of options
        # for the different operations that can be performed on the data.
        # Assign the selected option to a suitable local variable
        operation = tui.menu()

        # Task 21: Check if the user selected the option for loading data.  If so, then do the following:
        # - Use the appropriate function in the module tui to display a message to indicate that the data loading
        # operation has started.
        # - Load the data (see below).
        # - Use the appropriate function in the module tui to display a message to indicate that the data loading
        # operation has completed.
        #
        # To load the data, it is recommended that you create and call one or more separate functions that do the
        # following:
        # - Use the appropriate function in the module tui to retrieve a file path for the CSV data file.  You
        # should appropriately handle the case where this is None.
        # - Read each line from the CSV file and add it to the list 'records'. You should appropriately handle the case
        # where the file cannot be found

        # Check if the selected option from the main menu is 1(Load Data)
        if operation == 1:
            tui.started("Loading data")

            file = f"data/{tui.source_data_path()}"
            with open(file, 'r') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=",")
                # Loop for row in csv file append the row in list records
                header = next(csv_reader)
                for row in csv_reader:
                    records.append(row)

            tui.completed("Loading data")
        # Task 22: Check if the user selected the option for processing data. If so, then do the following:
        # - Use the appropriate function in the module tui to display a message to indicate that the data processing
        # operation has started.
        # - Process the data (see below).
        # - Use the appropriate function in the module tui to display a message to indicate that the data processing
        # operation has completed.
        #
        # To process the data, it is recommended that you create and call one or more separate functions that do the
        # following:
        # - Use the appropriate function in the module tui to display a menu of options for processing the data.
        # - Check what option has been selected
        #
        #   - If the user selected the option to retrieve an entity then
        #       - Use the appropriate function in the module tui to indicate that the entity retrieval process
        #       has started.
        #       - Use the appropriate function in the module tui to retrieve the entity name
        #       - Find the record for the specified entity in records.  You should appropriately handle the case
        #       where the entity cannot be found.
        #       - Use the appropriate function in the module tui to list the entity
        #       - Use the appropriate function in the module tui to indicate that the entity retrieval process has
        #       completed.
        #
        #   - If the user selected the option to retrieve an entity's details then
        #       - Use the appropriate function in the module tui to indicate that the entity details retrieval
        #       process has started.
        #       - Use the appropriate function in the module tui to retrieve the entity details
        #       - Find the record for the specified entity details in records.  You should appropriately handle the
        #       case where the entity cannot be found.
        #       - Use the appropriate function in the module tui to list the entity
        #       - Use the appropriate function in the module tui to indicate that the entity details retrieval
        #       process has completed.
        #
        #   - If the user selected the option to categorise entities by their type then
        #       - Use the appropriate function in the module tui to indicate that the entity type categorisation
        #       process has started.
        #       - Iterate through each record in records and assemble a dictionary containing a list of planets
        #       and a list of non-planets.
        #       - Use the appropriate function in the module tui to list the categories.
        #       - Use the appropriate function in the module tui to indicate that the entity type categorisation
        #       process has completed.
        #
        #   - If the user selected the option to categorise entities by their gravity then
        #       - Use the appropriate function in the module tui to indicate that the categorisation by entity gravity
        #       process has started.
        #       - Use the appropriate function in the module tui to retrieve a gravity range
        #       - Iterate through each record in records and assemble a dictionary containing lists of entities
        #       grouped into low (below lower limit), medium and high (above upper limit) gravity categories.
        #       - Use the appropriate function in the module tui to list the categories.
        #       - Use the appropriate function in the module tui to indicate that the categorisation by entity gravity
        #       process has completed.
        #
        #   - If the user selected the option to generate an orbit summary then
        #       - Use the appropriate function in the module tui to indicate that the orbit summary process has
        #       started.
        #       - Use the appropriate function in the module tui to retrieve a list of orbited planets.
        #       - Iterate through each record in records and find entities that orbit a planet in the list of
        #       orbited planets.  Assemble the found entities into a nested dictionary such that each entity can be
        #       accessed as follows:
        #           name_of_dict[planet_orbited][category]
        #       where category is "low" if the mean radius of the entity is below 100 and "high" otherwise.
        #       - Use the appropriate function in the module tui to list the categories.
        #       - Use the appropriate function in the module tui to indicate that the orbit summary process has
        #       completed.

        # Check if the selected option from the main menu is 2(Process Data)
        if operation == 2:
            tui.started("Processing data")
            process = tui.process_type()

            # Check if the selected option from the Process data menu is 1
            if process == 1:
                tui.started("The entity retrieval process")
                entity_name = tui.entity_name()
                entity_details = []
                # Searching for the entity
                for record in records:
                    if entity_name == record[0]:
                        entity_details = record

                if entity_details:
                    print(entity_details)
                    tui.completed("The entity retrieval process")
                else:
                    tui.error("Entity not found!")

            # Process data/ entity details
            # Check if the selected option from the Process data menu is 2
            if process == 2:
                tui.started("The entity details retrieval process")
                entity_list = tui.entity_details()
                entity_name = entity_list[0]
                entity_indexes = entity_list[1]
                entity_details = []
                # Searching for the entity in records list
                for record in records:
                    if entity_name == record[0]:
                        entity_details = record

                # if entity details are found display the entity details
                if entity_details:
                    print(tui.list_entity(entity_details, entity_indexes))
                    tui.completed("The entity details retrieval process")
                else:
                    # Otherwise error message
                    tui.error("Entity not found!")

            # Check if the selected option from the Process data menu is 3
            if process == 3:
                tui.started("The entity type categorisation process")
                type_categories = {}
                planets = []
                non_planets = []
                for record in records:
                    if record[1] == "TRUE":
                        planets.append(record[0])
                    elif record[1] == "FALSE":
                        non_planets.append(record[0])
                type_categories['planets'] = planets
                type_categories['non-planets'] = non_planets
                tui.list_categories(type_categories)
                tui.completed("The entity type categorisation process")

            # Check if the selected option from the Process data menu is 4
            if process == 4:
                tui.started("The categorisation by entity gravity process")
                up_low_limits = tui.gravity_range()
                up_limit = float(up_low_limits[1])
                low_limit = float(up_low_limits[0])
                gravity_categories = {}
                for record in records:
                    current_gravity = float(record[8])
                    if current_gravity < low_limit:
                        gravity_categories['low'] = record[0]
                    elif (current_gravity > low_limit) and (current_gravity < up_limit):
                        gravity_categories['medium'] = record[0]
                    elif current_gravity > up_limit:
                        gravity_categories['high'] = record[0]
                tui.list_categories(gravity_categories)
                tui.completed("The categorisation by entity gravity process")

            # Check if the selected option from the Process data menu is 5
            if process == 5:
                tui.started("The orbit summary process")
                # empty dictionary
                orbits = {}
                # loop for record in records
                for record in records:
                    # check if there is no orbits
                    if record[21] != "NA":
                        # making mean radius float
                        mean_radius = float(record[10])
                        # empty dictionary
                        current_entity = {}
                        # check if mean radius is lower than 100 add to category low
                        if mean_radius < 100:
                            current_category = 'low'
                        # otherwise add to category high
                        else:
                            current_category = 'high'
                        # check if orbits are in orbits dictionary
                        if record[21] in orbits:
                            # adding the orbit name
                            current_entity = orbits[record[21]]
                        else:
                            # otherwise empty
                            current_entity['low'] = []
                            current_entity['high'] = []
                        # adding the names of the entity (eName)
                        current_entity[current_category].append(record[0])
                        # adding in dictionary orbit the dictionary current entity
                        orbits[record[21]] = current_entity
                # displaying the key and value of orbits dictionary
                tui.list_categories(orbits)
                tui.completed("The orbit summary process")
            tui.completed("Processing data")

        # Task 23: Check if the user selected the option for visualising data.  If so, then do the following:
        # - Use the appropriate function in the module tui to indicate that the data visualisation operation
        # has started.
        # - Visualise the data (see below).
        # - Use the appropriate function in the module tui to display a message to indicate that the data visualisation
        # operation has completed.
        #
        # To visualise the data, it is recommended that you create and call one or more separate functions that do the
        # following:
        # - Use the appropriate function in the module tui to retrieve the type of visualisation to display.
        # - Check what option has been selected
        #
        #   - if the user selected the option to visualise the entity type then
        #       - Use the appropriate function in the module tui to indicate that the entity type visualisation
        #       process has started.
        #       - Use your code from earlier to assemble a dictionary containing a list of planets and a list of
        #       non-planets.
        #       - Use the appropriate function in the module visual to display a pie chart for the number of planets
        #       and non-planets
        #       - Use the appropriate function in the module tui to indicate that the entity type visualisation
        #       process has completed.
        #
        #   - if the user selected the option to visualise the entity gravity then
        #       - Use the appropriate function in the module tui to indicate that the entity gravity visualisation
        #       process has started.
        #       - Use your code from earlier to assemble a dictionary containing lists of entities grouped into
        #       low (below lower limit), medium and high (above upper limit) gravity categories.
        #       - Use the appropriate function in the module visual to display a bar chart for the gravities
        #       - Use the appropriate function in the module tui to indicate that the entity gravity visualisation
        #       process has completed.
        #
        #   - if the user selected the option to visualise the orbit summary then
        #       - Use the appropriate function in the module tui to indicate that the orbit summary visualisation
        #       process has started.
        #       - Use your code from earlier to assemble a nested dictionary of orbiting planets.
        #       - Use the appropriate function in the module visual to display subplots for the orbits
        #       - Use the appropriate function in the module tui to indicate that the orbit summary visualisation
        #       process has completed.
        #
        #   - if the user selected the option to animate the planet gravities then
        #       - Use the appropriate function in the module tui to indicate that the gravity animation visualisation
        #       process has started.
        #       - Use your code from earlier to assemble a dictionary containing lists of entities grouped into
        #       low (below lower limit), medium and high (above upper limit) gravity categories.
        #       - Use the appropriate function in the module visual to animate the gravity.
        #       - Use the appropriate function in the module tui to indicate that the gravity animation visualisation
        #       process has completed.

        # Check if the selected option from the main menu is 3(Visualise Data)
        if operation == 3:
            tui.started("The data visualisation operation")
            visualise_data = tui.visualise()

            # Check if the selected option from the Visualise data menu is 1
            if visualise_data == 1:
                tui.started("The entity type visualisation process")
                visual.entities_pie(type_categories)
                tui.completed("The entity type visualisation process")

            # Check if the selected option from the Visualise data menu is 2
            if visualise_data == 2:
                tui.started("The entity gravity visualisation process")
                visual.entities_bar(gravity_categories)
                tui.completed("The entity gravity visualisation process")

            # Check if the selected option from the Visualise data menu is 3
            if visualise_data == 3:
                tui.started("The orbit summary visualisation process")
                visual.orbits(orbits)
                tui.completed("The orbit summary visualisation process")

            # Check if the selected option from the Visualise data menu is 4
            if visualise_data == 4:
                tui.started("The gravity animation visualisation process")
                visual.gravity_animation(gravity_categories)
                tui.completed("The gravity animation visualisation process")
            tui.completed("The data visualisation operation")

        # Task 28: Check if the user selected the option for saving data.  If so, then do the following:
        # - Use the appropriate function in the module tui to indicate that the save data operation has started.
        # - Save the data (see below)
        # - Use the appropriate function in the module tui to indicate that the save data operation has completed.
        #
        # To save the data, you should demonstrate the application of OOP principles including the concepts of
        # abstraction and inheritance.  You should create an AbstractWriter class with abstract methods and a concrete
        # Writer class that inherits from the AbstractWriter class.  You should then use this to write the records to
        # a JSON file using in the following order: all the planets in alphabetical order followed by non-planets 
        # in alphabetical order.

        # Check if the selected option from the main menu is 4(Save Data)
        if operation == 4:
            tui.started("Save data operation")
            saving_data = tui.save()
            if saving_data == 1:
                pass
            tui.completed("Save data operation")

        # Task 29: Check if the user selected the option for exiting.  If so, then do the following:
        # break out of the loop

        # Check if the selected option from the main menu is 5(Exit)
        if operation == 5:
            # break out of the loop
            break

        # Task 30: If the user selected an invalid option then use the appropriate function of the module tui to
        # display an error message

        # Check if the response is bigger than 5 print error message
        if operation > 5:
            tui.error("There is no option with this number!")


if __name__ == "__main__":
    run()
