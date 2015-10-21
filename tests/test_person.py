from worth.models.person import Person

def test_Person():
    name = "Jeff"
    person = Person(name)

    assert person.name == name

def test_newIdea():
    person = Person("Jeff")
    title = "Dress yourself"

    person.newIdea(title, "Find some clothes", 4)

    idea = person.findIdea(title)

    assert idea.title == title

#def test_as_dict():

#def test_save():

#def test_load():
