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

## Contributors
KARABADJI Lina linakarabadji4@gmail.com
OUANES Sofia is_ouanes@esi.dz
MOUFFOK Tayeb Abderraouf raouf@yzr.ai
