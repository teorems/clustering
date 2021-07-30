from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def evaluation(data):
  from sklearn.neighbors import NearestNeighbors
  
  X, cluster = data[['Dim.1','Dim.2']].values, data.clust

  neigh = NearestNeighbors(n_neighbors=2)
  nbrs = neigh.fit(X)
  distances, indices = nbrs.kneighbors(X)
  distances = np.sort(distances, axis=0)
  distances = distances[:,1]
  # _ = plt.plot(distances)
  # plt.show()
  # plt.clf()
  
  eps = np.quantile(distances, 0.9)

  from sklearn import metrics

  for _i in range(1,10):
    db= DBSCAN(eps = eps, min_samples= _i).fit(X)
    labels = db.labels_
    core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
    core_samples_mask[db.core_sample_indices_] = True
    labels = db.labels_

  # Number of clusters in labels, ignoring noise if present.
    n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
    n_noise_ = list(labels).count(-1)
    print(f'Metrics for {_i} min samples, eps : {eps}')
    print('Estimated number of clusters: %d' % n_clusters_)
    print('Estimated number of noise points: %d' % n_noise_)
    print("Homogeneity: %0.3f" % metrics.homogeneity_score(cluster, labels))
    print("Completeness: %0.3f" % metrics.completeness_score(cluster, labels))
    print("V-measure: %0.3f" % metrics.v_measure_score(cluster, labels))
    print("Adjusted Rand Index: %0.3f"
      % metrics.adjusted_rand_score(cluster, labels))
    print("Adjusted Mutual Information: %0.3f"
      % metrics.adjusted_mutual_info_score(cluster, labels))
    print("Silhouette Coefficient: %0.3f"
      % metrics.silhouette_score(X, labels))
    print("#################################")
    
  return eps

def dbscan_res(data, min_s, epsilon):
  
  X, cluster = data[['Dim.1','Dim.2']].values, data.clust
  db= DBSCAN(eps = epsilon, min_samples= min_s).fit(X)
  labels = db.labels_
  core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
  core_samples_mask[db.core_sample_indices_] = True
  n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
  n_noise_ = list(labels).count(-1)

  unique_labels = set(labels)

  colors = [plt.cm.Spectral(each) for each in np.linspace(0, 1, len(unique_labels))]

  for k, col in zip(unique_labels, colors):
      if k == -1:
          col = [0, 0, 0, 1]

      class_member_mask = (labels == k)

      xy = X[class_member_mask & core_samples_mask]
      plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),markeredgecolor='k', markersize=14)

      xy = X[class_member_mask & ~core_samples_mask]
      plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),markeredgecolor='k', markersize=6)

  plt.title('Estimated number of clusters: %d' % n_clusters_)

  plt.show()
  plt.clf()
  
  df_db = pd.DataFrame({"pays" : data.index, "label" : labels, 'clust': data.clust})
  
  return df_db


