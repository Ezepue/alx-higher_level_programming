#!/usr/bin/python3
""" 14-main """
from models.base import Base
from models.rectangle import Rectangle

if __name__ == "__main__":

    #r1 = Rectangle(10, 7, 2, 8)
    json_dictionary = Base.to_json_string([])
    print(json_dictionary)
    print(type(json_dictionary))
