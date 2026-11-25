

#Set Module. It containts program for basic mathematical Sets

class MathSet:

    def __init__(self, elements):
        self.elements = set(elements)

    def __repr__(self):
        return "{" + ", ".join(str(e) for e in self.elements) + "}"

    def __contains__(self, element):
        return element in self.elements
    
    def __or__(self, other):

        if not isinstance(other, MathSet):
            raise TypeError("Union requires other Set!")
        
        return MathSet(self.elements | other.elements)
    
    def __and__(self, other):
        return MathSet(self.elements & other.elements)
    
    def __sub__(self, other):
        return MathSet(self.elements - other.elements)
    
    def __mul__(self, other):
        return MathSet((a, b) for a in self.elements for b in other.elements)
