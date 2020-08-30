import numpy as np 
from scipy.spatial.distance import euclidean

class KNearestNeighbors:
    def __init__(self, num_neighbors = 3):
        self.num_neighbors = num_neighbors
    
    def fit(self, X, y):
        # store array  and labels
        self.X = X
        self.y = y


    def predict(self, query):        
        d = self._get_distance(query)

        # dict to keep count of class votes
        labels = {label:0 for label in set(self.y)}

        result = {}
        for key,val in d.items():
            # keep count of class votes, reset each pass
            labels = {label:0 for label in set(self.y)}

            for i, _ in val:
                # use x_idx to determine class in y
                vote = self.y[i]

                # increment vote count for that label
                labels[vote] += 1

            #find max and add to result dict
            result[key] = max(labels, key=labels.get)

        # sort results dict by keys to return based on query order
        return [result[key] for key in sorted(result.keys())]


    def _get_distance(self, query):
        d = {}
        x_idx = 0 # keep track of self.X index
        q_col = 0 # keep track of the columns in query

        # helper for sorting
        def get_key(item):
            return item[1]

        # deal with cases where the query is a single item
        if len(np.shape(query)) == 1:
            d[q_col] = [] 

            # find distance from each row and track its index
            for row in self.X:
                d[q_col].append([x_idx, euclidean(query,row)])
                x_idx += 1

            # return k items from list sorted by distance 
            d[q_col] = sorted(d[q_col], key = getkey)[:num_neighbors]
            return d
        
        # same as above but also track query column 
        for q in query:
            d[q_col] = []

            for row in self.X:
                d[q_col].append([x_idx, euclidean(q,row)])
                x_idx += 1
            
            #increment column and reset index
            q_col += 1
            x_idx = 0
        
        # sort items in dict by distance
        for k in d.keys():
            d[k] = sorted(d[k], key = getkey)[:num_neighbors]
        
        return d        
