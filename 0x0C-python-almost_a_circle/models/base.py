#!/usr/bin/python3
"""The Base Class Module"""
import json
import csv


class Base:
    """The base class of all other classes
    Represents the "base" for all other classes in project 0x0C*.
    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a new base
        Args:
            id (int): the identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns str rep of a list of dict.
        Args:
            list_dictionaries (list): a list of dictionaries.
        """
        if list_dictionaries is not None or list_dictionaries != []:
            return json.dumps(list_dictionaries)
        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the json string rep of list_objs to a file
        Args:
            list_objs (list): list of class instances
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                temp_list = []
                for obj in list_objs:
                    temp_list += obj.to_dictionary()
                jsonfile.write(Base.to_json_string(temp_list))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string rep json_string
        Args:
            json_string (str): a string representing a list of dictionaries.
        """
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set
        Args:
            **dictionary (dict): key/value pairs of attributes to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances
        """
        try:
            filename = cls.__name__ + ".json"
            with open(filename, "r") as jsonfile:
                json_string = jsonfile.read()
                dicts_list = Base.from_json_string(json_string)
                return [cls.create(**d) for d in dicts_list]
        except IOError:
            return []

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.
        Reads from `<cls.__name__>.csv`.
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
