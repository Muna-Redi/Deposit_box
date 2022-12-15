#!/usr/bin/env python3
""" console to manage savings box """

import cmd
import json
from models import Storage
from models.money import Money

class Kolo_vest(cmd.Cmd):
    """ class that inherits from cmd """
    prompt = "(Kolo_record)"

    def do_EOF(self, line):
        """ recognises end of line """
        print()
        return True

    def do_quit(self, line):
        """ recognises CTRL D and terminates the program """
        print()
        return True

    def emptyline(self):
        """ handles empty line """
        pass

    def do_save(self, line):
        lines = line.split()
        if len(lines) >= 3:
            if lines[0] != "Money":
                print("unrecognised item: we only save money here,\n Thank u!")
                return
            if lines[1] not in ["10", "20", "50", "100", "200", "500", "100"]:
                print("not a valid denomination")
                return

            if not int(lines[2]) or int(lines[2]) < 1:
                print("not a valid count")
                return
            arg = dict()
            arg["value"] = lines[1]
            arg["count"] = lines[2]
            new_bill = Money(**arg)
            new_bill.save()
        else:
            print("some info are misding\nUsage: <save> <Money> <denomination> <count>")
            print("e.g save Money 200 1")

    def do_sum(self, line):
        """ gets total amount saved """
        lines = line.split()
        if len(lines) < 1 or lines[0] != "total":
            print("missing info\nUsage:<sum> <total>")
            return
        cash = 0
        obj = Storage.all()
        for key, val in obj.items():
            cash += (int(val.value) * int(val.count))
            print("cash is currently {} nsira".format(cash))
        print("Total amount saved so far is {} naira".format(cash))

if __name__ == "__main__":
    Kolo_vest().cmdloop()
