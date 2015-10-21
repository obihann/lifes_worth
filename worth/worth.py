from worth.models.idea import Idea
from worth.models.person import Person
from worth.utils import data
import json

def main():
    jeff = Person("Jeff")
    jeff.addIdea(data.load("idea",Idea))

    print(jeff)
