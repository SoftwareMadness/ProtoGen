from protogen import *
def request_vdict():
    return value_dict
def request_pp():
    return prepro
width = Integer("Width")
height = Integer("Height")
A = Matrix("A")
B = Matrix("B")
Result = Matrix("Mat")
def logic():
    for y in prange(0,height):
        for x in prange(0,width):
            for xx in prange(0,width):
                iadd(at(Result,x,y),mul(at(A,xx,y),at(B,x,xx)))