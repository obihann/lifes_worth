import json, sys
import urwid

from worth.models.idea import Idea
from worth.models.person import Person
from worth.utils import data
from worth.boxes import CascadingBoxes

import worth.menu as Menu

class Worth(object):
    _placeholder = urwid.SolidFill()
    _palette = [
            ('banner', 'dark green', 'black'),
            ('background', 'dark blue', 'dark gray'),
            ('controls', 'light blue', 'black'),]

    def __init__(self):
        # define main loop and widgets
        self._loop = urwid.MainLoop(self._placeholder, self._palette, handle_mouse=False, unhandled_input=self.controls)
        self._loop.widget = urwid.AttrMap(self._placeholder, 'background')
        self._loop.widget.original_widget = urwid.Pile([])

        pile = self._loop.widget.base_widget

        # define controls and control map
        controls = urwid.Text(u"q - quit\n", align='center')
        controlsMap = urwid.AttrMap(controls, 'controls')

        # define top menu
        menu_top = Menu.menu(u'Main Menu', [
            Menu.sub_menu(u'Users', [
                Menu.menu_button(u'Load User', Menu.item_chosen),
                Menu.menu_button(u'New User', Menu.item_chosen),
                ]),
            Menu.sub_menu(u'Ideas', [
                Menu.menu_button(u'Load Idea', Menu.item_chosen),
                Menu.menu_button(u'New Idea', Menu.item_chosen),
                ]),
            Menu.menu_button(u'Quit', Menu.item_chosen),
        ])

        top = CascadingBoxes(menu_top)

        # define header
        title = urwid.Text(u"%s - %s" % (Main.name, Main.version), align='center')
        titleMap = urwid.AttrMap(title, 'banner')

        # add everything to the pile
        pile.contents.append((titleMap, pile.options('pack')))
        pile.contents.append((top, pile.options()))
        #pile.contents.append((urwid.SolidFill(), pile.options()))
        #pile.contents.append((controlsMap, pile.options('pack')))

        #top.focus()

        self._loop.run()

    def controls(self, key):
        if key in ('q', 'Q'):
            raise urwid.ExitMainLoop()

class Main(object):
    version = "0.0.1"
    name = "LIFES WORTH" 

    def __init__(self):
        print("""%s %s
https://github.com/obihann/lifes-worth/
This tool is protected by the GNU General Public License v2.
Copyright Jeffrey Hann 2015
------------------------------------------------------------""" % (self.name, self.version))

        try:
            self.worth = Worth() 
        except KeyboardInterrupt:
            sys.exit()

    #print("""(1) List users

    #command = input("Command: ")

    #if command == "2":
        #name = input("Name: ")
        #person = Person.load(name)
    #elif command == "3":
        #name = input("Name: ")
        #person = Person(name)
    #else:
        #return

    #if person is not None:
        #print(person)

    #print("""(1) List ideas
#(2) Load idea
#(3) New idea
#(4) Save user
#(q) Quit""")

    #command = input("Command: ")

    #if command == "3":
        #title = input("Title: ")
        #desc = input("Description: ")
        #diff = int(input("Difficulty: "))
        #idea = Idea(title, desc, diff)
        #print(idea)

        #confirm = input("Correct [y/n]: ")

        #if confirm == "y":
            #person.addIdea(idea)
            #print(person)
    #elif command == "4":
        #person.save()
    #else:
        #return
