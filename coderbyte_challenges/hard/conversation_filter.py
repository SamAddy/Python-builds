"""
write a python function that filters a chat conversation by name or content of the message . the signature of your function should be depending on the language
def solve(conversation: str, name_filter: str="" content_filter: str 0 "") -> List
you may implement other functions called by your solve function if you wish
"""

from typing import List

def solve(converstion: str, name_filter: str = "", content_filter: str = "") -> list[str]:

    # Split the conversation received into lines of messages.
    lines = conversation.strip().split("\n")

    # Filter the message through by name and content
    filtered_lines = [line for line in lines if name_filter in line and content_filter in line]

    return filtered_lines
