from worth.models.idea import Idea
from worth.models.person import Person
from worth.utils import data
import json

def main():
    idea = data.load("idea",Idea)
    jeff = Person("Jeff")

    jeff.addIdea(idea)

    jeff.newIdea("Life's Worth", "Track your worth by the ideas you complete", 10)
    jeff.newIdea("Dress yourself", "Find some clothes", 4)

    print(jeff)
