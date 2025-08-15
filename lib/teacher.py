#!/usr/bin/env python

from user import User
import random

class Teacher(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = [
            "str is a data type in Python",
            "a Python function can return itself",
            "Python is an interpreted language",
            "Python is dynamically typed",
            "Python supports multiple inheritance"
        ]

    def teach(self):
        return random.choice(self.knowledge)
