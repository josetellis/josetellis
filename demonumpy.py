import numpy
# ar=numpy.array([12,3,56,6.7,'HCL'])
# ar1=numpy.array([2,3,4])
# # ar2=numpy.array([2,3,4])
# # ar=ar1*ar2
# ar3=numpy.array([[2,3,4],[5,6,7]])
# # print(ar3)
# # print(numpy.ndim(ar3))
# ar=ar1*ar3
# print(ar)
# l=list(range(1,10,3))
# # print(type(l))
# print(l)
# ar=numpy.arange(1,13).reshape(3,4)
# print(ar)
# 1,2,3,4
# 5,6,7,8
# 9,10,11,12
ar=numpy.arange(start=10,stop=-2,step=-3)
ar1=numpy.arange(10,dtype=numpy.int64)
# print(ar1)
print(ar1.dtype)
print(ar1.itemsize)