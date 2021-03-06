""" ants3.py
    classic counting song
    further improvement with a list
"""

distraction = [
      "",
      "suck his thumb",
      "tie his shoe",
      "climb a tree",
      "shut the door"
      ]

def chorus():
    output = """
    ...and they all go marching
    down-
    to the ground-
    to get out-
    of the rain.
    Boom boom boom boom boom boom boom
    """
    return output

def verse(verseNum):

    problem = distraction[verseNum]
    output = """
    The ants go marching {0} by {0} hurrah, hurrah.
    The ants go marching {0} by {0} hurrah, hurrah.
    The ants go marching {0} by {0}.
    The little one stops to {1}
    """.format(verseNum, problem)

    return output

for verseNum in range(1, len(distraction)):
    print(verse(verseNum))
    print(chorus())
