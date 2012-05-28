from matplotlib.pyplot import show

from hcluster import pdist, linkage, dendrogram
import numpy
from numpy.random import rand
from scipy.spatial.distance import squareform
'''
X=[
[0.0, 0.81, 1.21, 0.6], 
[0.81, 0.0, 1.64, 0.22],
[1.21, 1.64, 0.0, 1.56],
[0.6, 0.22, 1.56, 0.0]
]
'''
data =[
		[0.2, 0],
		[0.1,0.5],
		[0 ,-0.3],
		[-1, 1 ],
		[0.1,-0.1]
		]
Y = pdist(data)
#Y = squareform(X)
Z = linkage(Y)
print Z
dendrogram(Z)

show()
