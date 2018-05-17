Section 16: Exercise: Case Storage by Index II
::::::::::::::::::::::::::::::::::::::::::::::

.. youtube:: 2nArrX2yf1A
        :height: 315
        :width: 560
        :align: left

That's a good point David. Remember that we're trying to store things, because we want to retrieve things later. And if our storage mechanism is such that it doesn't not allow for efficient retrieval, then it's not a very good storage mechanism. And as you correctly point out, David, as the number of entries increase in this table, and the number of dimensions we are looking at increase also increases. This is going to be coming an inefficient for retrieval. Therefore, let's look at a second method called discrimination trees which provides an alternate way of storing these cases in memory.
