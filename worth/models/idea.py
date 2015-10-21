from utils import indent
import json
import time

class Idea:
    def __init__(self, title, desc, diff):
        """
        initialize a new idea
        """
        self._title      = title
        self._desc       = desc
        self._difficulty = diff
        self._started    = None
        self._completed  = None

    @classmethod
    def load(cls, obj):
        try:
            return Idea(obj["_title"], obj["_desc"], obj["_difficulty"])
        except ValueError:
            print "JSON is invalid"
        except KeyError as e:
            print "Invalid key: %s" % e

    @property
    def title(self):
        """
        return the title of the idea
        """
        return self._title

    @title.setter
    def title(self, value):
        """
        set the title of the idea"
        """
        self._title = val  

    @property
    def desc(self):
        """
        return the description of the idea
        """
        return self._desc

    @desc.setter
    def desc(self, value):
        """
        set the description of the idea
        """
        self._desc = value

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
        self._difficulty = value

    @property
    def started(self):
        """
        return the started date of the idea
        """
        return self._started

    @property
    def completed(self):
        """
        return the completed date of the idea
        """
        return self._completed

    def start(self):
        if self._started == None:
            self._started = time.time()

    def complete(self):
        self.start()

        if self._completed == None:
            self._completed = time.time()

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
+ Status: %s""" % (self._difficulty, self.score(), self._difficulty * 100, self._desc, status), "   ")

        return "%s \n%s" % (self._title, ideas)
