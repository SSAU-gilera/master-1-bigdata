import warnings
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore")

data = pd.read_csv('imports-85.data', header=None)[[5, 10, 11]].rename(
    columns={5: 'num-of-doors', 10: 'length', 11: 'width'})


kmeans = KMeans(n_clusters=2, init="k-means++").fit(data[['length', 'width']])
data['cluster'] = kmeans.labels_


plt.scatter('length', 'width', data=data,
            c=[0 if i == 'two' else 1 if i == 'four' else 2 for i in data['num-of-doors'].values])
plt.title('Кластеризация по классам (two, four)')


plt.scatter('length', 'width', data=data,
            c=data['cluster'])
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c=['red', 'red'], marker='x', )
plt.title('Кластеризация методом k-mean с центрами (x)')

data['sqrt_distances'] = data.apply(lambda x: ((kmeans.cluster_centers_[0,0] - x['length']) ** 2 + (kmeans.cluster_centers_[0,1] - x['width']) ** 2) ** 0.5  if x['cluster'] == 0 else ((kmeans.cluster_centers_[1,0] - x['length']) ** 2 + (kmeans.cluster_centers_[1,1] - x['width']) ** 2) ** 0.5, 1)
data