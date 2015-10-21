import json
from worth.utils import data
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
    def loadJSON(cls, obj):
        """
        load json data
        """

        if "__type__" in obj and obj["__type__"] == "Person":
            try:
                person =  Person(obj["name"])
                if "ideas" in obj:
                    for idea in obj["ideas"]:
                        person.addIdea(Idea.loadJSON(idea))

                return person
            except ValueError:
                print("JSON is invalid")
            except KeyError as e:
                print("Invalid key: %s" % e)

    @classmethod
    def load(cls, obj):
        """
        load from a file
        """
        try:
            target = open("worth/data/%s.json" % obj, "r")
            data = target.read()
            person = json.loads(data)
            person = Person.loadJSON(person)

            return person 
        except IOError as e:
            print("I/O error: {1}" % e.strerror)

    def save(self):
        data.save(self, self.name)

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
        custom_dict = {}
        custom_dict["__type__"] = "Person"
        custom_dict["name"] = self.name

        ideas = []

        for idea in self.ideas:
            ideas.append(idea.as_dict())

        custom_dict["ideas"] = ideas

        return custom_dict

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
