import json

def load(src, cls):
    try:
        target = open("worth/data/%s.json" % src)
        return json.load(target, object_hook=cls.loadJSON)
    except IOError as e:
        print("I/O error: {1}" % e.strerror)

def save(data, src):
    target = open("worth/data/%s.json" % src, 'w')
    json.dump(data.as_dict(), target)
