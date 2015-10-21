from worth.models.idea import Idea

def test_newIdea():
    title = "Life's Worth"
    description = "Track your worth by the ideas you complete"
    difficulity = 10

    idea = newIdea(title, desc, description)

    assert idea.title == title
