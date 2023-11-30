from sklearn.metrics.cluster import normalized_mutual_info_score, adjusted_rand_score
import numpy as np
from sklearn.cluster import KMeans
import umap
import pandas as pd
from prince import CA, PCA
from sklearn.manifold import TSNE
import pickle

import warnings
warnings.filterwarnings("ignore")

def dim_red(mat, p, method):
    '''
    Perform dimensionality reduction

    Input:
    -----
        mat : NxM list 
        p : number of dimensions to keep 
    Output:
    ------
        red_mat : NxP list such that p<<m
    '''
    if method=='ACP':
        if isinstance(mat, np.ndarray):
            mat = pd.DataFrame(mat)

        pca = PCA(n_components=p)
        red_mat = pca.fit_transform(mat)
        
    elif method=='AFC':
        df = pd.DataFrame(mat)

        df_positive = df + np.abs(df.min().min())

        ca = CA(n_components=p)
        ca.fit(df_positive)
        red_mat = ca.row_coordinates(df_positive)
        
    elif method=='UMAP':
        reducer = umap.UMAP(n_components=p)
        red_mat = reducer.fit_transform(mat)

    elif method =='TSNE':
        tsne = TSNE(n_components = p)
        red_mat = tsne.fit_transform(mat)
        
    else:
        raise Exception("Please select one of the three methods : APC, AFC, UMAP")
    
    return red_mat


def clust(mat, k):
    '''
    Perform clustering

    Input:
    -----
        mat : input list 
        k : number of cluster
    Output:
    ------
        pred : list of predicted labels
    '''
    kmeans = KMeans(n_clusters=k)
    pred = kmeans.fit_predict(mat)

    return pred

# import data
embeddings = pickle.load(open('embeddings.pkl', 'rb'))
labels = pickle.load(open('labels.pkl', 'rb'))
k = len(set(labels))

print("Data loaded\n\n")

choice = input('Choose the methods to use:  1. ACP   2. AFC   3. UMAP   4. TSNE   5. All\n')

if choice == '1':
    methods = ['ACP']
elif choice == '2':
    methods = ['AFC']
elif choice == '3':
    methods = ['UMAP']
elif choice == '4':
    methods = ['TSNE']
elif choice == '5':
    methods = ['ACP', 'AFC', 'UMAP', 'TSNE']
else:
    print("Choice not valid, running all methods")
    methods = ['ACP', 'AFC', 'UMAP', 'TSNE']

for method in methods:
    nmi_scores = []
    ari_scores = []
    for _ in range(3):
        # Perform dimensionality reduction
        red_emb = dim_red(embeddings, 3, method)

        # Perform clustering
        pred = clust(red_emb, k)

        # Evaluate clustering results
        nmi_score = normalized_mutual_info_score(pred, labels)
        ari_score = adjusted_rand_score(pred, labels)

        nmi_scores.append(nmi_score)
        ari_scores.append(ari_score)

    mean_nmi = np.mean(nmi_scores)
    std_nmi = np.std(nmi_scores)
    mean_ari = np.mean(ari_scores)
    std_ari = np.std(ari_scores)

    # Print results
    print(f'Method: {method}\nNMI: {mean_nmi:.2f} (+/- {std_nmi:.2f})\nARI: {mean_ari:.2f} (+/- {std_ari:.2f})\n')
