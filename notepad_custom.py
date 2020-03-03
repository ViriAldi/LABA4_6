import datetime


last_id = 0

class Note:
    """
    Class for representation of a single note with memo
    """

    def __init__(self, memo, tags=''):
        """
        Initializes a note with memo and tags (remembers creation date)
        """
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()

        global last_id

        last_id += 1
        self.id = last_id

    def match(self, filt):
        """
        Checks if in note there is matches with given tags
        """
        return filt in self.memo or filt in self.tags


class Notebook:

    def __init__(self):
        """
        Initializes a Notebook with a empty list of notes
        """
        self.notes = []

    def new_note(self, memo, tags=''):
        """
        Creates a new note with memo in notebook
        """
        self.notes.append(Note(memo, tags))

    def _find_note(self, note_id):
        """
        Finds a note by note id
        """
        for note in self.notes:
            if note.id == note_id:
                return note

    def modify_memo(self, note_id, memo):
        """
        Modifies a memo in notebook by id
        """
        note = self._find_note(note_id)

        if note:
            self._find_note(note_id).memo = memo
            return 1

    def modify_tags(self, note_id, tags):
        """
        Modifies a tegs in notebook by id
        """
        note = self._find_note(note_id)

        if note:
            self._find_note(note_id).tags = tags
            return 1

    def search(self, filt):
        """
        Returns a list of notes which matches a filter
        """
        return [note for note in self.notes if 
                note.match(filt)]
