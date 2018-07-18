class Mammals:

    def __init__(self):
        self.members = ['Tiger', 'Elephant', 'Wild Cat']

    def printmembers(self):
        print("Printing members of mammale class")
        for member in self.members:
            print("\t %s" % member)
