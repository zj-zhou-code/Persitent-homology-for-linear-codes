import numpy as np
import pandas as pd
import galois





M = np.loadtxt(open("/home/zzj/persistent homology/Gxfx1_x5_n5.csv", "rb"), delimiter = ",", skiprows = 0)
#M = np.loadtxt(open("/home/zzj/persistent homology/RS2_1_21.csv", "rb"), delimiter = ",", skiprows = 0)
# rank = np.linalg.matrix_rank(M)
# print("rank(M) =",rank)
# shape = M.shape





#compute M^3
M3 = np.linalg.matrix_power(M, 3)
#trace of M^3
trace = np.trace(M3)
print("Trace(M3) =", trace/6)
# compute the number of `1` in M
count=np.sum(M==1)
print("Edge=", count/2)


#compute the 2-rank of M
Mmod2 = M.astype(int)
ff=2
Mmod2=galois.GF(ff)(Mmod2)
rank=np.linalg.matrix_rank(Mmod2)
print("2rank=", rank)

# #rank = Mmod2.rank()
# #print(M)
# #print(Mmod2)
# # #save as csv file
# # #np.savetxt('/home/zzj/RS2_1_2M3.csv', M, delimiter = ',')
# # '''
# # matrix = np.array([[1, 1], [0, 1]])

# # power = np.linalg.matrix_power(matrix, 3)
# # print(power)
# # '''