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


class Storyboard:
    """
    The Storyboard class is to help with managing and organizing the notes.

     classes:
     add_notes
     search_by_filter
     search_by_title
     search_by_tag

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
        self.notes.append({"title": title, "tags": tags, "text": text})

    def search_by_title(self, title):
        """
        This function searches for note with the provided title.

        :param title: title of note
        :return: the note with the provided title
        """
        return [note for note in self.notes if note["title"] == title]

    def search_by_tag(self, tags):
        """
        This function searches for a note which has the provided tags in its tags.

        :param tags: possible tags of the note
        :return: the note with the provided tags
        """
        results = []
        for note in self.notes:
            if any(tag in note["tags"] for tag in tags):
                results.append(note)
        return result

    def search_by_text(self, text):
        """
        This function searches for a note which has the provided text in its contents.

        :param text: possible text of the note
        :return: the note with the provided text
        """
        return [note for note in self.notes if note["text"] == text]

    def delete_note(self, title: "", tags: "", text: ""):
        pass


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
result2 = storyboard_.search_by_tag({"unit test"})
assert len(result2) == 1
assert result2[0]["title"] == "Test Traceplayer"


# Search by text
result3 = storyboard_.search_by_text("Implement a unit test for the class Traceplayer of the spark core framework.")
assert len(result3) == 1

