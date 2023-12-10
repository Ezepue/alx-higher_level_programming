#!/usr/bin/python3
"""Module containing base class"""
import json
import csv
import turtle


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiates Base object"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.
        list_dictionaries is a list of dictionaries.
        """
        if list_dictionaries in [[], None]:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.
        """
        filename = f"{cls.__name__}.json"

        with open(filename, 'w', encoding='utf-8') as file:
            if list_objs is None:
                file.write("[]")
            else:
                new_list = [obj.to_dictionary() for obj in list_objs]
                file.write(Base.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string.
        """
        if json_string in ["", None]:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set.
        """
        if not dictionary or dictionary == {}:
            return
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def create_from_list(cls, cls_as_list):
        """
        Returns an instance from list.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        c_as_l = tuple(cls_as_list)
        dummy.update(*c_as_l)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances.
        """
        result = []
        filename = f"{cls.__name__}.json"

        try:
            with open(filename, 'r', encoding='utf-8') as file:
                j_str = file.read()
                dict_list = cls.from_json_string(j_str)
                for item in dict_list:
                    result.append(cls.create(**item))
                return result
        except FileNotFoundError:
            return result

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes in CSV and writes to csv file"""
        result = []
        header = []
        filename = f"{cls.__name__}.csv"
        with open(filename, 'w', encoding='utf-8') as file:
            if list_objs in [[], None]:
                file.write("[]")
                return
            writer = csv.writer(file)
            if cls.__name__ == "Rectangle":
                header = ["id", "width", "height", "x", "y"]
            elif cls.__name__ == "Square":
                header = ["id", "size", "x", "y"]
            result.append(header)
            for obj in list_objs:
                result.append(obj.to_list())
            writer.writerow(result[0])
            writer.writerows(result[1:])

    @classmethod
    def load_from_file_csv(cls):
        """Reads CSV and deserializes"""
        filename = f"{cls.__name__}.csv"
        result = []
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    int_row = [int(element) for element in row]
                    result.append(cls.create_from_list(int_row))
                return result
        except IOError:
            return result

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
