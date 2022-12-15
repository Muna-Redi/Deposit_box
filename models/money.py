#!/usr/bin/env python3
""" defining class Money """

import sys
import uuid
from datetime import datetime
import models

class Money:
    """class Money"""

    value = ""

    def __init__(self, **kwargs):
        """ instantiates an objct of the class Money
            args:
                value (int): monetary value
                id (str): unique id of the money

        """
        if kwargs is not None and len(kwargs) > 0:
            for key, val in kwargs.items():
                if key == "value":
                    self.value = kwargs["value"]

                if key == "id":
                    self.id = kwargs["id"]
                if key == "count":
                    self.count = val
                if key in ["date_saved"]:
                    tmp = datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")
                    self.date_saved = tmp

        if ("id", "date_saved") not in kwargs.keys():
            self.id = str(uuid.uuid4())
            self.date_saved = datetime.now()
        models.Storage.new(self)

    def to_dict(self):
        """ returns a dictionary representation of an instance
            of the class Money
        """
        new_dict = self.__dict__.copy()
        for key, value in new_dict.items():
            if key == "date_saved":
                new_dict["date_saved"] = self.date_saved.isoformat()

        new_dict["__class__"] = self.__class__.__name__
        return new_dict

    def save(self):
        """ saves money """
        self.date_saved = datetime.now()
        models.Storage.save()
        print("{} naira has been saved and recorded successfully".format(self.value))

