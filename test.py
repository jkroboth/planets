import glob
import numpy

filenames = glob.glob('inflammation*.csv')
filenames = filenames[0:3]


for f in filenames:
        print(f)
        
        data = numpy.loadtxt(fname=f, delimiter=',')
        print(data.shape)

