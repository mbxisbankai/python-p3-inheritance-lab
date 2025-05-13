#!/usr/bin/env python

from user import User

class Student(User):
    knowledge = []
    
    def learn(self, string):
        return self.knowledge.append(string)
        pass