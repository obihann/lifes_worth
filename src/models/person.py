from idea import Idea
from utils.indent import Indent

class Person:
    def __init__(self, name):
        self._name = name
        self._ideas = []

    @property
    def name(self):
        return self._name

    @property
    def ideas(self):
        return self._ideas

    def newIdea(self, title, desc, diff):
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
        return self._findIdea(name)

    def __str__(self):
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
