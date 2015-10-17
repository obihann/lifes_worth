import json
from models.person import Person
from models.idea import Idea

def main():
    jeff = Person("Jeff")
    jeff.newIdea("Life's Worth", "Track your worth by the ideas you complete", 10)
    jeff.newIdea("Dress yourself", "Find some clothes", 4)
    jeff.newIdea("Fear the Dice", "A D&D Helper", 8)

    print jeff
