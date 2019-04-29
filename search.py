# USAGE
# python search.py --index index.csv --query queries/103100.png --result-path dataset

# import the necessary packages
from search.colordescriptor import ColorDescriptor
from search.searcher import Searcher
import argparse
import cv2
import numpy as np

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", required=True,
                help="Path to where the computed index will be stored")
ap.add_argument("-q", "--query", required=True,
                help="Path to the query image")
ap.add_argument("-r", "--result-path", required=True,
                help="Path to the result path")
args = vars(ap.parse_args())

# initialize the image descriptor
cd = ColorDescriptor((8, 12, 3))

# load the query image and describe it
query = cv2.imread(args["query"])
features = cd.describe(query)

# perform the search
searcher = Searcher(args["index"])
results = searcher.search(features)
print(results[0][1])

# return all the similar images from the dataset

similar_images = []

for i in range(len(results)):
    similar_images.append(results[i][1])

similar_images = np.asarray(similar_images)
print(similar_images)
# display the query
cv2.imshow("Query", query)

# TODO
# loop over the results
# Add here
