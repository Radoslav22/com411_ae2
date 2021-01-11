import matplotlib.pyplot as plt
import matplotlib.animation as animation


def entities_pie(categories):
    """
    Task 24: Display a single subplot that shows a pie chart for categories.

    The function should display a pie chart with the number of planets and the number of non-planets from categories.

    :param categories: A dictionary with planets and non-planets
    :return: Does not return anything
    """
    # two empty list
    labels = []
    sizes = []
    # loop the dictionary items
    for key, value in categories.items():
        # append in lists
        labels.append(key)
        sizes.append(len(value))
    # title of the Pie chart
    plt.title("Planets vs Non-planets")
    plt.pie(sizes, labels=labels)
    plt.show()


def entities_bar(categories):
    """
    Task 25: Display a single subplot that shows a bar chart for categories.

    The function should display a bar chart for the number of 'low', 'medium' and 'high' gravity entities.

    :param categories: A dictionary with entities categorised into 'low', 'medium' and 'high' gravity
    :return: Does not return anything
    """
    # two empty list
    labels = []
    sizes = []
    # loop the dictionary items
    for key, value in categories.items():
        labels.append(key)
        sizes.append(len(value))
    # title of the Bar chart
    plt.title("Low, Medium and High gravity")
    plt.bar(labels, sizes, align='center')
    plt.show()


def orbits(summary):
    """
    Task 26: Display subplots where each subplot shows the "small" and "large" entities that orbit the planet.

    Summary is a nested dictionary of the form:
    summary = {
        "orbited planet": {
            "small": [entity, entity, entity],
            "large": [entity, entity]
        }
    }

    The function should display for each orbited planet in summary. Each subplot should show a bar chart with the
    number of "small" and "large" orbiting entities.

    :param summary: A dictionary containing the "small" and "large" entities for each orbited planet.
    :return: Does not return anything
    """
    labels = []
    size = []

    for key,value in summary.items():
        labels.append(key)
        size.append(len(value))

    fig, (ax1, ax2) = plt.suplots(1, 2)
    ax1.bar(labels, size, align='center')
    ax2.bar(labels, size, align='center')
    plt.show()



def gravity_animation(categories):
    """
    Task 27: Display an animation of "low", "medium" and "high" gravities.

    The function should display a suitable animation for the "low", "medium" and "high" gravity entities.
    E.g. an animated line plot

    :param categories: A dictionary containing "low", "medium" and "high" gravity entities
    :return: Does not return anything
    """

    labels = []
    sizes = []
    # loop the dictionary items
    for key, value in categories.items():
        labels.append(key)
        sizes.append(len(value))

    fig, ax = plt.subplots()
    ax.cla()
    ax.plot(labels, sizes)

    simple_animation = animation.FuncAnimation(labels, sizes, frames=100, interval=100)

    plt.show()
