def line(value, indent = "\t"):
    return "%s%s" % (indent, value)

def block(value, indent = "\t"):
    split = value.split("\n")

    for x, row in enumerate(split):
        split[x] = line(row, indent)

    return "\n".join(split)

class Indent(object):
    def __init__(self, indent = "\t"):
        self._indent = indent

    def setIndent(self, indent):
        self._indent = indent

    def line(self, value):
        return line(value, self._indent)

    def block(self, value):
        return block(value, self._indent)
