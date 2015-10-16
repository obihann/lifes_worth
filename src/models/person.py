from idea import Idea
from utils import indent

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

    def __str__(self):
        ideasStr = ""

        for idea in self.ideas:
            ideaStr = "%s" % idea
            ideasStr += ideaStr

        ideaStr = indent.indentBlock(ideaStr)

        return "Name: %s \nIdeas: \n%s" % (self._name, ideaStr)
