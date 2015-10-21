from worth.utils import data
from worth.utils import indent
import json
import time

class Idea(object):
    def __init__(self, title, desc, diff):
        """
        initialize a new idea
        """
        self.title       = title
        self.desc        = desc
        self._difficulty = diff
        self._started    = None
        self._completed  = None

    @classmethod
    def loadJSON(cls, obj):
        if "__type__" in obj and obj["__type__"] == "Idea":
            try:
                return Idea(obj["title"], obj["desc"], obj["_difficulty"])
            except ValueError:
                print("JSON is invalid")
            except KeyError as e:
                print("Invalid key: %s" % e)

    def save(self):
        data.save(self, self.title)

    @classmethod
    def load(cls, obj):
        """
        load from a file
        """
        try:
            target = open("worth/data/%s.json" % obj)
            person = json.load(target, object_hook=cls.loadJSON)
            return person 
        except IOError as e:
            print("I/O error: {1}" % e.strerror)

    @property
    def difficulty(self):
        """
        return the difficulty of the idea
        """
        return self._difficulty

    @difficulty.setter
    def difficulty(self, value):
        """
        set the difficulty of the idea
        """

        if value >= 0 and value <= 10:
            self._difficulty = value
        else:
            raise ValueError("difficulty should be between 0 and 10")

    @property
    def started(self):
        """
        return the started date of the idea
        """
        return self._started

    @started.setter
    def started(self, value):
        """
        set the stated date of the idea
        """
        if value is True:
            if self._started is None:
                self._started = time.time()
        elif value is False:
            self._started = None
        else:
            raise ValueError("expected True or False")

    @property
    def completed(self):
        """
        return the completed date of the idea
        """
        return self._completed

    @completed.setter
    def completed(self, value):
        """
        set the completed date of the idea
        """
        if value is True:
            if self._started is None:
                self._started = time.time()

            if self._completed is None:
                self._completed = time.time()
        elif value is False:
            self._completed = None
        else:
            raise ValueError("expected True or False")

    def score(self):
        """
        return the current score of the idea
        """
        score = self._difficulty * 50
        
        if self._started != None:
            score = score / 2

        if self._completed != None:
            score = score * 2

        return score

    def as_dict(self):
        custom_dict = self.__dict__
        custom_dict["__type__"] = "Idea"

        return custom_dict

    def __str__(self):
        """
        return the idea in a formatted string
        """
        status = "not started"
        
        if self._started != None and self._completed != None:
            status = "completed"
        elif self._started != None:
            status = "started"

        ideas = indent.block("""+ Difficulity: %d 
+ Score: %d/%d
+ Description: %s
+ Status: %s""" % (self.difficulty, self.score(), self.difficulty * 100, self.desc, status), "   ")

        return "%s \n%s" % (self.title, ideas)
