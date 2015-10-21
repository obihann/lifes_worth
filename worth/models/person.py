import json
from worth.models.idea import Idea
from worth.utils.indent import Indent

class Person(object):
    def __init__(self, data, ideas = []):
        """
        initialize a new person
        """
        self.name = data
        self.ideas = ideas

    @classmethod
    def load(cls, obj):
        """
        load json data
        """
        try:
            return Person(obj["name"])
        except ValueError:
            print("JSON is invalid")
        except KeyError as e:
            print("Invalid key: %s" % e)

    def addIdea(self, idea):
        """
        add an existing idea
        """
        self.ideas.append(idea)

    def newIdea(self, title, desc, diff):
        """
        add a new idea
        """
        self.ideas.append(Idea(title, desc, diff))

    def findIdea(self, name, pos = 0):
        """
        return an idea by title
        """
        if len(self.ideas) == 0:
            return None
        elif self.ideas[pos].title == name:
            return self.ideas[pos]
        elif pos+1 >= len(self.ideas):
            return None
        else:
            return self.findIdea(name, pos+1)

    def as_dict(self):
        dict = {}
        dict["name"] = self.name
        dict["ideas"] = []

        for idea in self.ideas:
            dict["ideas"].append(idea.as_dict())

        return dict

    def __str__(self):
        """
        return the person in a formatted string
        """
        ideasStr = ""
        indent = Indent("   ")

        for pos, idea in enumerate(self.ideas):
            ideasStr += "(%d) %s\n" % (pos+1, idea)

        ideasStr = indent.block(ideasStr)

        score = 0
        for idea in self.ideas:
            score += idea.score()

        return """Name: %s
Score: %d
Ideas (%d): \n%s""" % (self.name, score, len(self.ideas), ideasStr)

    def __dict__(self):
        return dict(name=self.name)
