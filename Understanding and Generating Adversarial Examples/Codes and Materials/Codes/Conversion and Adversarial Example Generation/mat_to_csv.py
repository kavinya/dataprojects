import scipy.io
import numpy as np

data = scipy.io.loadmat("mnist_data.mat")

for i in data:
	if '__' not in i and 'readme' not in i:
		np.savetxt(("mnist_csv/"+i+".csv"),data[i],delimiter=',',fmt='%f')
