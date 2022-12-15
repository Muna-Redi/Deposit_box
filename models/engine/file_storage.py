#!/usr/bin/env python3
""" File storage engine"""

import json
from models.money import Money



class File_storage:
    """ defining class for storage """

    __bills = dict()
    file_path = "deposit_box.json"

    def all(self):
        """ returns all objects """
        return File_storage.__bills

    def new(self, obj):
        """ adds a new bill to the list"""
        key = "{}.{}".format(obj.to_dict()["__class__"], obj.id)

        File_storage.__bills[key] = obj

    def save(self):
        """ saves a bill"""
        new_dict = {}
        for key, value in File_storage.__bills.items():
            new_dict[key] = value.to_dict()

        with open(File_storage.file_path, 'w', encoding='utf-8') as f:
            json.dump(new_dict, f)

    def reload(self):
        """ reloads all objects of the class """
        try:
            with open(File_storage.file_path, "r", encoding="utf-8") as f:
                objects = json.load(f)
                for key, val in objects.items():
                    File_storage.__bills[key] = Money(**val)
        except FileNotFoundError:
            print("file not found")
