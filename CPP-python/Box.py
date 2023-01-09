"""
Define an abstract class Box with a text label, a colour, a method providing the number of Boxes available and 
the pure virtual method getVolume computing the volume of a box.
Define the following cloasses inherited from the Box:
    * BrickBox representing the Box being a cubiod with a length, a width and a height
    * TubeBox representing the Box being a cylinder with a base radius and a height
    * BubbleBox representing the Box being a sphere with a radius.

Override, for each of the above classes, the virtual method getVolume, making it to return the volume of a box of the given class.
Implement all the constructors, destructors, getters, setters and exceptions which make the functionality of the classes complete, and all 
the other methods and exceptions necessary to run the code provided.


Define the class Store with a description, a total capacity and a dynamic list of het boxes stored. Implement
the following public methods of the class:
    * a one enabling to add a new box of an arbitrary type to the store list (with the control of the total capacity
    of the store, CapacityError should be thrown if the toatl capacity could be exceeded), 
    * a one enabling to remove the box (by its label) from the store list (throwing the NameError exception if it doesnt exist).
    * a one enabling to remove all teh boxes from the list, 
    * a method returning the summary volume of all the boxes stored in the store.
Overload the indexing operator ([]) for the Store to have a direct access to the item on the particular position in the 
store list (throwing the IndexError exception if it doesnt exist)
"""

import math

class Box:
    # Initialize number of boxes
    num_of_boxes = 0

    def __init__(self, text_label, colour) -> None:
        self.text_label = text_label
        self.colour = colour

    def getTextLabel(self):
        return self.text_label

    def getColor(self):
        return self.colour

    def getVolume(self):
        raise("The volumes are calculated in the various classes")

    def getNumofBoxes():
        return Box.num_of_boxes


class BrickBox(Box):
    def __init__(self, text_label, colour, length, width, height) -> None:
        super().__init__(text_label, colour)
        self.length = length
        self.width = width
        self.height = height
        Box.num_of_boxes += 1

    def getLength(self):
        return self.length

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getVolume(self):
        return self.length * self.width * self.height

class TubeBox(Box):
    def __init__(self, text_label, colour, base_radius, height) -> None:
        super().__init__(text_label, colour)
        self.base_radius = base_radius
        self.height = height
        Box.num_of_boxes += 1

    def getBaseRadius(self):
        return self.base_radius

    def getHeight(self):
        return self.height

    def getVolume(self):
        return math.pi * self.base_radius**2 * self.height


class BubbleBox(Box):
    def __init__(self, text_label, colour, radius) -> None:
        super().__init__(text_label, colour)
        self.radius = radius
        Box.num_of_boxes += 1

    def getRadius(self):
        return self.radius

    def getVolume(self):
        return 4/3 * math.pi * self.radius**3


    