import ctypes as C
math=C.CDLL('./libClase3.so')
print math.add_int(5,6)
tres=C.c_int(3)
cuatro=C.c_int(4)
res1=C.c_int()
math.add_int_ref(C.byref(tres),C.byref(cuatro),C.byref(res1))
print res1.value
dos=C.c_float(2.5)
siete=C.c_float(7.2)
res2=C.c_float()
math.add_float_ref(C.byref(dos),C.byref(siete),C.byref(res2))
print res2.value
math.add_float.restype=C.c_float
print math.add_float(dos,siete)



