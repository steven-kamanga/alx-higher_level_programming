#!/usr/bin/python3
"""The Base Class"""


import json
import os
import csv
import turtle


class Base:
    """The Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class initialization"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == {}:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        content = []
        if list_objs is not None:
            for item in list_objs:
                content.append(item.to_dictionary())
        with open(filename, 'w', encoding="utf-8") as f:
            return f.write(cls.to_json_string(content))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if dictionary != {}:
            if cls.__name__ == 'Rectangle':
                new_instance = cls(1, 1)
            if cls.__name__ == 'Square':
                new_instance = cls(1)
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        if not os.path.isfile(filename):
            return []
        with open(filename, 'r', encoding="utf-8") as f:
            content = f.read()
            formattedContent = (cls.from_json_string(content))
            return [cls.create(**item) for item in formattedContent]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__ + ".csv"
        content = ""
        if list_objs is not None:
            content += ','.join(list_objs[0].to_dictionary().keys())
            content += '\n'
            for lst in list_objs:
                content += ','.join(
                    map(str, lst.to_dictionary().values())
                )
                content += '\n'

        with open(filename, mode="w", encoding="utf-8") as f:
            return f.write(content)

    @classmethod
    def load_from_file_csv(cls):
        """load from csv"""
        filename = cls.__name__ + ".csv"
        object_created = []

        with open(filename, 'r') as f:
            header = f.readline().replace('\n', '').split(',')
            for el in f.readlines():
                values = map(int, el.replace('\n', '').split(','))
                data = dict(zip(header, values))
                object_created.append(cls.create(**data))

        return object_created

    @classmethod
    def draw(cls, list_rectangles, list_squares):
        """draw the figure
        """
        window = turtle.Screen()
        pen = turtle.Pen()
        figures = list_rectangles + list_squares

        for fig in figures:
            pen.up()
            pen.goto(fig.x, fig.y)
            pen.down()
            pen.forward(fig.width)
            pen.right(90)
            pen.forward(fig.height)
            pen.right(90)
            pen.forward(fig.width)
            pen.right(90)
            pen.forward(fig.height)
            pen.right(90)

        window.exitonclick()
