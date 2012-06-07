from matplotlib.pyplot import show
from hcluster import pdist, linkage, dendrogram

#from scipy.spatial.distance import squareform

data =[
		[0.2, 0],
		[0.1,0.5],
		[0 ,-0.3],
		[-1, 1 ],
		[0.1,-0.1]
		]

Y = pdist(data)
Z = linkage(Y)
print Z
dendrogram(Z)

show()
