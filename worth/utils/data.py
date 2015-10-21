import json

def load(src, cls):
    try:
        target = open("worth/data/%s.json" % src, 'r')
        data = target.read()

        return json.loads(data, object_hook=cls.load)
    except IOError as e:
        print("I/O error: {1}" % e.strerror)

def save(data, src):
    target = open("worth/data/%s.json" % src, 'w')
    target.write(json.dumps(data.as_dict()))
    target.close()
