"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for i in range(len(items)):
        if str(items[i]) not in frequencies:
            frequencies.update({str(items[i]) : 1})
        else:
            frequencies[str(items[i])] += 1
    # Your code goes here
    return frequencies
