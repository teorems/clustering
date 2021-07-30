from sklearn.cluster import DBSCAN
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

eps = evaluation(r.full)
  
##########

#best metrics

df_db_full = dbscan_res(r.full, 1, eps)

print(df_db)

#le meilleur parametrage se trouve avec n_voisis=1, qui donnera 23 clusters.

#####################################################################################################

#pays le plus proches à la France
df_db[df_db['label'] == 16]


  
