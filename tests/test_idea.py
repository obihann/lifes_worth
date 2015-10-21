from worth.models.idea import Idea

def test_Idae():
    title = "Life's Worth"
    description = "Track your worth by the ideas you complete"
    difficulity = 10

    idea = Idea(title, description, difficulity)

    assert idea.title == title
    assert idea.desc == description
    assert idea.difficulty == difficulity

