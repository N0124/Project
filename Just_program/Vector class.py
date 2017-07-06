class Vector:
    def __init__(self, coordinates):
        self.coord = coordinates

    def check(self, vector):
        if len(self.coord)!= len(vector.coord):
            return 'Error'

    def add(self, vector):
        if self.check(vector) != None:
            return self.check(self, vector)
        coord = [self.coord[i]+vector.coord[i] for i in range(len(self.coord))]

        return Vector(coord)

    def subtract (self,vector):
        if self.check(vector) != None:
            return self.check(self, vector)
        coord = [self.coord[i]-vector.coord[i] for i in range(len(self.coord))]
        return Vector(coord)

    def dot (self,vector):
        if self.check(vector) != None:
            return self.check(self, vector)
        coord = [self.coord[i]*vector.coord[i] for i in range(len(self.coord))]
        return sum(coord)

    def norm (self):

        coord = [self.coord[i]**2 for i in range(len(self.coord))]
        return sum(coord)**0.5

    def __str__(self):
        answer = str(tuple(self.coord))

        return answer.replace(' ', '')

    def equals(self, vector):
        return all([self.coord[i]==vector.coord[i] for i in range(len(self.coord))])


a = Vector([1,2])
b = Vector ([3,4])


print (a.add(b))