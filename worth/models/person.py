import json
from idea import Idea
from utils.indent import Indent

class Person:
    def __init__(self, data, ideas = []):
        """
        initialize a new person
        """

        self._name = data
        self._ideas = ideas

    @classmethod
    def load(cls, obj):
        try:
            return Person(obj["_name"])
        except ValueError:
            print "JSON is invalid"
        except KeyError as e:
            print "Invalid key: %s" % e

    @property
    def name(self):
        """
        return name of the person
        """
        return self._name

    @property
    def ideas(self):
        """
        return the list of ideas for the person
        """
        return self._ideas

    def newIdea(self, title, desc, diff):
        """
        add a new idea
        """
        self._ideas.append(Idea(title, desc, diff))

    def _findIdea(self, name, pos = 0):
        if len(self._ideas) == 0:
            return None
        elif self._ideas[pos].title == name:
            return self._ideas[pos]
        elif pos+1 >= len(self._ideas):
            return None
        else:
            return self._findIdea(name, pos+1)

    def findIdea(self, name):
        """
        return an idea by title
        """
        return self._findIdea(name)

    def __str__(self):
        """
        return the person in a formatted string
        """
        ideasStr = ""
        indent = Indent("   ")

        for pos, idea in enumerate(self._ideas):
            ideasStr += "(%d) %s\n" % (pos+1, idea)

        ideasStr = indent.block(ideasStr)

        score = 0
        for idea in self._ideas:
            score += idea.score()

        return """Name: %s
Score: %d
Ideas (%d): \n%s""" % (self._name, score, len(self._ideas), ideasStr)

    def __dict__(self):
        return dict(name=self._name)
