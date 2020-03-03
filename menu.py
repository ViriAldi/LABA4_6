import sys
from notepad_custom import Notebook, Note


class Menu:
    """
    Class that representates menu object for
    our notepad program
    """
    def __init__(self):
        """
        Initializes menu with choises and notebook
        """
        self.notebook = Notebook()
        self.choices = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.quit
            }

    def display_menu(self):
        """
        Prints menu (choises options)
        """
        print("""
        Notebook Menu
        1. Show all Notes
        2. Search Notes
        3. Add Note
        4. Modify Note
        5. Quit
        """)

    def run(self):
        """
        Runs menu, accepts choises and refreshes page
        """
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)

            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def show_notes(self, notes=None):
        """
        Prints all selected notes
        """
        if not notes:
            notes = self.notebook.notes

        for note in notes:
            print("{0}: {1}\n{2}".format(
                note.id, note.tags, note.memo))

    def search_notes(self):
        """
        Searches and returns notes in notebook
        """
        filt = input("Search for: ")
        notes = self.notebook.search(filt)
        self.show_notes(notes)

    def add_note(self):
        """
        Adds a note to a notebook
        """
        memo = input("Enter a memo: ")
        self.notebook.new_note(memo)
        print("Your note has been added.")

    def modify_note(self):
        """
        Modifies a note from notebook by id with memo
        """
        ID = input("Enter a note id: ")
        memo = input("Enter a memo: ")
        tags = input("Enter tags: ")

        if memo:
            self.notebook.modify_memo(ID, memo)
        if tags:
            self.notebook.modify_tags(ID, tags)

    def quit(self):
        """
        Stops menu continious running
        """
        print("Thank you for using your notebook today.")
        sys.exit(0)

if __name__ == "__main__":
    Menu().run()
