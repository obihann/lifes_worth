from utils import indent
import time

class Idea:
    def __init__(self, title, desc, diff):
        self._title      = title
        self._desc       = desc
        self._difficulty = diff
        self._started    = 0
        self._completed  = 0
        self._progress   = 0

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = val  

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value

    @property
    def difficulty(self):
        return self._difficulty

    @difficulty.setter
    def difficulty(self, value):
        self._difficulty = value

    @property
    def started(self):
        return self._started

    @started.setter
    def started(self, value):
        self._started = value

    @property
    def completed(self):
        return self._completed

    @completed.setter
    def completed(self, value):
        self._completed = value

    @property
    def progress(self):
        return self._progress

    @progress.setter
    def progress(self, value):
        if self._started == 0:
            self.start()

        self._progress = value

    def score(self):
        score = self._difficulty * 50
        
        if self._started != 0:
            score = score / 2

        if self._completed != 0:
            score = score * 2

        return score

    def start(self):
        self._started = time.time()

    def finish(self):
        if self._started == 0:
            self.start()

        self._progress = 100
        self._completed = time.time()

    def __str__(self):
        status = "not started"
        
        if self._started != 0 and self._completed != 0:
            status = "completed"
        elif self._started != 0:
            status = "started"

        ideas = indent.block("""+ Difficulity: %d 
+ Score: %d/%d
+ Description: %s
+ Status: %s""" % (self._difficulty, self.score(), self._difficulty * 100, self._desc, status), "   ")

        return "%s \n%s" % (self._title, ideas)
