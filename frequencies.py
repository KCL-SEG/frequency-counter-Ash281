"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for i in range(items):
        if items[i] in frequencies:
            frequencies[items[i]] += 1
        else:
            frequencies.update({items[i], 1})
    # Your code goes here
    return frequencies
