Section 09: Variabilization
:::::::::::::::::::::::::::

.. youtube:: ijN249s6bvY
        :height: 315
        :width: 560
        :align: left

Let us look at the algorithm for incremental concept learning more systematical in more detail. This time, imagine that there is an AI program, and there is a teacher which is going to teach the AI program about the concept of an arch. So teaching this first example and suppose the teacher gives the example which has four bricks in it. Two vertical bricks that are not touching each other and there is a third brick on top of it and a fourth brick on top of it. To the AI program, the input may look a little bit like this, there are four bricks, A, B, C and D. And there are some relationships between these four blocks. So brick C is on left of brick D. Brick C supports brick B. Brick D supports brick B as well, and brick B supports brick A. This then is the input. What may the error program learn from this one, single example? Not very much. For this one single example, the AI program can only variablize. There were these constants here, brick A, brick B, brick C, brick D. Instead, the AI program may be able to variablize these constants and say, well, brick A is an instance of brick, and therefore, I just have brick here. Brick B is an instance of a brick. Therefore, I'll just have a brick here. So now, I can have any brick in these spaces as long as these relationships hold, it's an example of an arch. Note the first example was the positive example. Now we are going to see a series of positive and negative examples, and each time we see an example, the AI program will either generalize or specialize. If it sees a positive example, then it may generalize, if the positive example is not covered by a current concept definition. If it sees a negative example, it may specialize the current definition of the concept to exclude that negative example.

