# In this exercise we want to design a Storyboard. Our version of the Storyboard
#
# contains arbitrary many notes (imagine it like putting sticky notes on a board).
# Every note has a title, a text and a set of tags. E.g.
#                        - title: "Test Traceplayer"
#
#                         - text: "Implement a unit test for the class Traceplayer of the spark core framework."
#
#                         - tags: {"unit test", "traceplayer", "testing", "spark core"}
#
#
#
# Our Storyboard should enable us to search for notes by title, text and tags.
#  E.g.:
#
#      searchByTitle("Test Traceplayer")
#      searchByTag({"testing", "unit test"})
#      searchByText("Implement a unit test for the class Traceplayer of the spark core framework.")
#
# For the sake of simplicity we don't want to do any similiarity or prefix matching when
#
# searching for a title, tag or text. Only an exact match should give results.
#
#
# The skeleton code below can be used as a starting point but doesn't have to.
#
# The comments "fill in" are placeholders where you definitely have to put in some code when
#
# you use this skeleton code. But this doesn't mean that you shouldn't or can't put code anywhere else.
#
# Also write some simple unit tests to show how you would test the functionality of the Storyboard.
# Don't use any testing framework. Simple if-statements are sufficient for this exercise.
#
#
# Hint: Think about performance versus memory tradeoffs in your design, so you can give good
#
#       reasons for your decision.
#
#
#
#
# class Note
#
# {
#
#                              /*fill in*/
#
# };
#
# class Storyboard
#
# {
#
# public:
#
#                              void addNote(/*fill in*/);
#
#                              void deleteNote(/*fill in*/);
#
#                              /*fill in*/ searchByTitle(/*fill in*/);
#
#                              /*fill in*/ searchByText(/*fill in*/);
#
#                              /*fill in*/ searchByTag(/*fill in*/);
#
#
#
# private:
#
#                              /*fill in*/
#
# };
import time


start_time = time.time()


class Note:
    """
    This class serves as a note which takes in three parameters
    """
    def __init__(self, title, tags, text):
        self.title = title
        self.tags = tags
        self.text = text


class Storyboard:
    """
    The Storyboard class is to help with managing and organizing the notes.

     classes:
     add_notes
     search_by_filter
     search_by_title
     search_by_tag
     delete_note_by_title

    """

    def __init__(self):
        self.notes = []

    def add_notes(self, title, tags, text):
        """
        This function adds notes to the storyboard

        :param
        title - title of note
        tags - possible tags for the note
        text - content of the note
        """
        note = Note(title, tags, text)
        self.notes.append(note)

    def search_by_title(self, title):
        """
        This function searches for note with the provided title.

        :param title: title of note
        :return: the note with the provided title
        """
        return [note for note in self.notes if note.title == title]

    def search_by_tag(self, tags):
        """
        This function searches for a note which has the provided tags in its tags.

        :param tags: possible tags of the note
        :return: the note with the provided tags
        """
        # results = []
        # for note in self.notes:
        #     if any(tag in note["tags"] for tag in tags):
        #         results.append(note)
        # return result

        return [note for note in self.notes if set(tags).issubset(note.tags)]

    def search_by_text(self, text):
        """
        This function searches for a note which has the provided text in its contents.

        :param text: possible text of the note
        :return: the note with the provided text
        """
        return [note for note in self.notes if note.text == text]

    def delete_note_by_title(self, title):
        """
        This function searches through the notes for the provided title and deletes the
        note with the particular title.

        :param title: title of note to be deleted.
        :return: true or false
        """
        for note in self.notes:
            if self.note.title == title:
                self.notes.remove(note)
                return True
        return False


# Making a storyboard for testing
# Create an instance of Storyboard
storyboard_ = Storyboard()

# Add notes to the storyboard
storyboard_.add_notes("Test Traceplayer", {"unit test", "traceplayer", "testing", "spark core"}, "Implement a unit test for the class Traceplayer of the spark core framework.")

# Search by title
result = storyboard_.search_by_title("Test Traceplayer")
assert len(result) == 1
assert result[0]["title"] == "Test Traceplayer"

# Search by tags
result = storyboard_.search_by_tag({"testing" "unit test"})
assert len(result) == 1
assert result[0]["title"] == "Test Traceplayer"

# Search by text
result = storyboard_.search_by_text("Implement a unit test for the class Traceplayer of the spark core framework.")
assert len(result) == 1

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")


"""
Reasons

The code is written this way to provide a simple implementation of the Storyboard class that allows adding 
notes and searching for them by title, text, and tags. The implementation uses a list of dictionaries to store the notes, 
with each dictionary representing a single note and containing the note's title, text, and tags.

The search_by_title, search_by_tag, and search_by_text methods use list comprehensions to filter the list of 
notes based on the search criteria. These methods return a list of all notes that match the search criteria.

This implementation strikes a balance between memory usage and performance, as it stores the notes in a simple data 
structure (a list of dictionaries) that doesn't require a lot of memory, while also providing efficient search methods 
that can quickly find notes that match the search criteria. The implementation also allows for easy extensibility, 
as new search methods could be added by simply adding a new method that uses a list comprehension to filter the list of 
notes based on the new search criteria.
"""