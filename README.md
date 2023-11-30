# Project Title: Text Clustering with Dimensionality Reduction
## Overview
This GitHub repository contains a collaborative project focused on developing a text clustering model using dimensionality reduction techniques such as Principal Component Analysis (ACP), Correspondence Analysis (AFC), and Uniform Manifold Approximation and Projection (UMAP). The goal is to create a tandem or sequential approach by combining text data (NG20 dataset with 2000 documents) with dimensionality reduction methods and clustering algorithms. In this project, we specifically use k-means as the clustering algorithm, but other clustering algorithms can be explored.

## Repository Structure
- README.md: This document provides an overview of the project, its objectives, and guidelines for collaboration.
- .gitignore: Specifies files and directories to be ignored by Git.
- main.py: Evaluates each approach (ACP+kmeans, AFC+kmeans, UMAP+kmeans) using performance metrics such as Normalized Mutual Information (NMI), Adjusted Rand Index (ARI), and Accuracy. It serves as the main execution script.
- experiments/: A folder to store individual approaches, each in a separate notebook.
- Dockerfile: Defines the Docker image specifications for running the main.py file and obtaining clustering results.
- requirements.txt: A file to stock all python libraries with their versions

## Docker
Docker plays a crucial role in providing a standardized and reproducible environment for developing and deploying the text clustering model. The Dockerfile defines the specifications for the Docker image, ensuring consistency in the Python version and required libraries across all collaborators. Local development is streamlined by running the Docker container with a mounted volume, allowing developers to work on the project in real-time while maintaining a shared Python environment. This collaborative approach minimizes compatibility issues and facilitates a seamless integration of individual contributions

the image is available at: 

## Bonus
• Développer le modèle en local avec docker et monter un volume sur le projet, ça vous permet de remplir le Dockerfile au fur et à mesure et de travailler ensemble sur la même version de python et des librairies : **We mounted a volume with our container. It allowed us to to modify our files and add methods both in the host and in the container which makes it much easier to push our changes. It also minimizes errors and keeps us from rebuilding the image each time.**

• Améliorer la qualité du rendu final, par exemple : permettre à l'utilisateur de choisir le(s) modèle(s) qu'il souhaite tester, ou bien executer le modèle dans un backend. Toute autre proposition sera appréciée : **We gave the user the choice to try any of the implemented methods or to run them all at once**

• Visualisation des données sur un plan à l'aide de l'ACP, l'AFC et UMAP. **We added the notebook where we presented insightfull visulizations**

• Rédaction d'une bonne documentation (README). **As you can see**

• Sauvegarder les données pour ne pas les télécharger à chaque instantiation d'un nouveau conteneur (ou bien les installer dans l'image docker). **We loaded and saved the embeddings and labels that we got from the model and this allowed us to save a lot of time building the image (at least  and also the runtime times less time). This also improved the runtime which became at least 3 times faster**

• Réaliser différentes initialisations et afficher la moyenne (et écart-type) des résultats. **We compared between  the methods and computed the average and standard deviation. This gives the user more insights about the methods and results obtained**

• Toute autre méthode de réduction de la dimension ou algorithme de clustering seraient très appréciés. **We used 04 methods in total : ACP, AFC, UMAP and TSNE**

## Contributors
KARABADJI Lina linakarabadji4@gmail.com
OUANES Sofia is_ouanes@esi.dz
MOUFFOK Tayeb Abderraouf raouf@yzr.ai
