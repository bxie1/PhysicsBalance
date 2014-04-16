import sys
import random

class NoveltySearch:
    """
    Implementation of novelty search.
    """

    def __init__(self, k, limit, threshold):

      self.k = k
      self.limit = limit
      self.threshold = threshold
      self.archive = []
    
    # return the distance from p1 to p2
    def distance(self, p1, p2):
      dist = 0
      for i in range(len(p1)):
        dist += (p2[i] - p1[i])**2


      return dist**(.5)
    
    # compute the distance of point p from it k nearest neighbors
    def distFromkNearest(self, p):
      neigh = []
      
      # for each item in archive, we add the dist from p to i to neigh
      for i in self.archive:
        neigh.append(self.distance(p, i))
      
      neigh.sort()
      
      dist = 0
      
      # compute the sum of the dists.
      for n in range(min(self.k, len(neigh))):
        dist += neigh[n]

      return dist
    
    # return sparseness
    def sparseness(self, p):
      return self.distFromkNearest(p)/self.k
    
    # add point p to archive based on sparseness and current size of archive
    def addToArchive(self, p):
      # if length of archive is less than k, always add the point
      if len(self.archive) < self.k:
        self.archive.append(p)
        return 0.1
      #else if the sparseness of p is high enough, add the point
      elif self.sparseness(p) > self.threshold:
        self.archive.append(p)
        #if the archive is bigger than the limit, pop the oldest element
        if len(self.archive) > self.limit:
          self.archive.pop(0)

      return self.sparseness(p)
    
    def getArchiveSize(self):
      return len(self.archive)

    def saveArchive(self, filename):
      f = open(filename, "w")
      # get the dimension of the vector 
      numDim = len(self.archive[0])
      # for each of the items in archive...
      for i in range(len(self.archive)):
        for j in range(numDim):
          pointDim = self.archive[i][j]
          f.write("%f " %(pointDim))
        f.write("\n")



def main():
    """
    Test of novelty search class.
    """

    args = sys.argv
    if len(args) < 4:
      print "Usage error: program requires 3 arguments."

    k = int(args[1])
    limit = int(args[2])
    threshold = float(args[3])
    
    # create the object
    n = NoveltySearch(k,limit,threshold)
    
    # generate random points and add them to archive
    for i in range (100):
      x = random.random()
      y = random.random()
      p = (x,y)
      n.addToArchive(p)

    print "Size of archive: ", n.getArchiveSize()

    print "\nSparseness Point (0.5, 0.5): %f\n" %n.sparseness((.5,.5))
    print "Sparseness Point (1, 1): %f\n" %n.sparseness((1,1))
    print "Sparseness Point (2, 2): %f\n" %n.sparseness((2,2))
    print "Sparseness Point (5,5): %f\n" %n.sparseness((5,5))
    
    # generate more random points between 0 and .5
    for i in range (100):
      x = random.random()*.5
      y = random.random()*.5
      p = (x,y)
      n.addToArchive(p)

    print "Size of archive: ", n.getArchiveSize()

    n.saveArchive("test.dat")




if __name__ == '__main__':
    main()
