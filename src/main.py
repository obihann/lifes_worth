from models.person import Person

jeff = Person("Jeff")
jeff.newIdea("Life's Worth", "Track your worth by the ideas you complete", 10)
jeff.newIdea("Dress yourself", "Find some clothes", 4)
jeff.newIdea("Fear the Dice", "A D&D Helper", 8)

lWorth = jeff.findIdea("Life's Worth")
if lWorth != None:
    lWorth.start()

dress = jeff.findIdea("Dress yourself")
if dress != None:
    dress.finish()

print jeff
