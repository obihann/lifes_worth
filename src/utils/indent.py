import string

def indentBlock(block):
    split = string.split(block, "\n")

    for x, line in enumerate(split):
        line = "\t%s" % line
        split[x] = line

    return string.join(split, "\n")
