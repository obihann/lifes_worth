import time
from worth.models.idea import Idea

def test_Idae():
    title = "Life's Worth"
    description = "Track your worth by the ideas you complete"
    difficulity = 10

    idea = Idea(title, description, difficulity)

    assert idea.title == title
    assert idea.desc == description
    assert idea.difficulty == difficulity

def test_start():
    title = "Life's Worth"
    description = "Track your worth by the ideas you complete"
    difficulity = 10

    idea = Idea(title, description, difficulity)
    idea.started = True

    assert type(idea.started) == type(time.time())

def test_complete():
    title = "Life's Worth"
    description = "Track your worth by the ideas you complete"
    difficulity = 10

    idea = Idea(title, description, difficulity)
    idea.completed = True

    assert type(idea.started) == type(time.time())
    assert type(idea.completed) == type(time.time())

#def test_score():

#def test_as_dict():

#def test_save():

#def test_load():
