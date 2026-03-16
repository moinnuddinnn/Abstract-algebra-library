#Set Module. It containts program for basic mathematical Sets.

class MathSet:

    def __init__(self, elements):
        self.elements = set(elements)

    def __repr__(self):
        return "{" + ", ".join(str(e) for e in self.elements) + "}"

    def contains(self, element):
        return element in self.elements