Section 11: Nearest Neighbor in k-Dimensional Space
:::::::::::::::::::::::::::::::::::::::::::::::::::

.. youtube:: Wrgt4UnsIEA
        :height: 315
        :width: 560
        :align: left

Earlier we had this formula for calculating the Euclidean distance in two dimensions. Now we can generalize it to many dimensions. So here is a generalization of the previous formula computing nearest neighbor. In this new formula, both the case and the problem are defined in K dimensions. And we'll find the Euclidean distance between them in this K space. So this table summarizes Euclidean distance between the cases and the new problem in this multidimensional space where we are dealing both with the origin and the destination, and where the origin as well as the destination are specified by the x and y coordinates. Looking at this table, we can very quickly see that D and not B or E, is the closest case, your most similar case, linear problem Q. This method is called the KNN method where NN stands here for nearest neighbor, K nearest neighbor method. This is a probably method as simple as it is. Of course, it also has limitations. One limitations is that, in the real world, the number of dimensions in which I might want to compute the distance between the new problem and old cases might be very large, a high dimensional low space. In such a situation, deciding which of the stored cases is closest to the new problem may not be as simple as it appears here. A second difficulty with this method is, that even if the new problem isn't very close to an existing case, that does not mean that the existing cases solution can or should be darkly applied to the new problem. So, we need both alternative methods of retrieving cases from memory, and methods for adapting passed cases to fit the requirements of the new problem. That is called [UNKNOWN] and we will discuss that in the next lesson.


