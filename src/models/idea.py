class Idea:
    def __init__(self, title, desc, diff):
        self._title = title
        self._desc  = desc
        self._diff  = diff

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
    def diff(self):
        return self._diff

    @diff.setter
    def diff(self, value):
        self._diff = value

    def __str__(self):
        return "Idea: %s \nDifficulity: %d \nDescription: %s" % (self.title, self.diff, self.desc)
