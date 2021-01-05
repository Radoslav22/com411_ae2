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
        if (operation == 1):
            tui.started("Loading data")

            file= f"data/{tui.source_data_path()}"
            with open(file, 'r') as csv_file:
                for line in csv_file.readlines():
                    records.append(line.strip())
            tui.completed("Loading data")






        # Task 22: Check if the user selected the option for processing data.  If so, then do the following:
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
        if(operation == 2):
            tui.started("Processing data")
            process= tui.process_type()
            if (process == 1):
                tui.started("The entity retrieval process")
                nameofentity=tui.entity_name()
                if f"{nameofentity}" in records:
                    print (nameofentity.row)

                tui.completed("The entity retrieval process")
            if (process == 2):
                tui.started("The entity details retrieval process")
                entity_list = tui.entity_details()
                tui.list_entity(entity_list[0],entity_list[1])
                tui.completed("The entity details retrieval process")
            if (process == 3):
                tui.started("The entity type categorisation process")
                for record in records:
                    pass
                tui.completed("The entity type categorisation process")
            if(process == 4):
                tui.started("The categorisation by entity gravity process")
                tui.gravity_range()
                gravity_categories = {}
                for record in records:
                    if line[0]:
                        pass
                tui.completed("The categorisation by entity gravity process")
            if(process == 5):
                tui.started("The orbit summary process")
                orbits = tui.orbits()
                categories = {}
                for record in records:
                    if record == "orbits":
                        categories[planet_orbited][category]
                        pass

                tui.list_categories(categories)
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
        if (operation == 3):
            tui.started("The data visualisation operation")
            visualise_data = tui.visualise()
            if (visualise_data == 1):
                tui.started("The entity type visualisation process")
                visual.entities_pie(categories)
                tui.completed("The entity type visualisation process")
            if (visualise_data == 2):
                tui.started("The entity gravity visualisation process")
                visual.entities_bar(categories)
                tui.completed("The entity gravity visualisation process")
            if (visualise_data == 3):
                tui.started("The orbit summary visualisation process")
                visual.orbits(summary)
                tui.completed("The orbit summary visualisation process")
            if (visualise_data == 4):
                tui.started("The gravity animation visualisation process")
                visual.gravity_animation(categories)
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
        if (operation == 4):
            tui.started("Save data operation")
            tui.save()
            tui.completed("Save data operation")

        # Task 29: Check if the user selected the option for exiting.  If so, then do the following:
        # break out of the loop
        if (operation == 5):
            break

        # Task 30: If the user selected an invalid option then use the appropriate function of the module tui to
        # display an error message


        if (operation > 5):
            tui.error("There is no option with this number!")


if __name__ == "__main__":
    run()