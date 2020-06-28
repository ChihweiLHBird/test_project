import numpy

class testClass(object):
    def testArr(self):
        return numpy.array([1,2,3])

def runtest():
    obj = testClass()
    print(obj.testArr())