import string

def line(value, indent = "\t"):
    return "%s%s" % (indent, value)

def block(value, indent = "\t"):
    split = string.split(value, "\n")

    for x, row in enumerate(split):
        split[x] = line(row, indent)

    return string.join(split, "\n")

class Indent(object):
    def __init__(self, indent = "\t"):
        self._indent = indent

    def setIndent(self, indent):
        self._indent = indent

    def line(self, value):
        return line(value, self._indent)

    def block(self, value):
        return block(value, self._indent)
