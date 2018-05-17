Section 05: Differences in State Spaces
::::::::::::::::::::::::::::::::::::::::
.. youtube:: ngVOPThLc2A
        :height: 315
        :width: 560
        :align: left

.. image:: ../../_static/Ch05/Slide05-01.png
        :height: 200px
        :width: 350px
        :alt: Class Goals
        :align: center

.. image:: ../../_static/Ch05/Slide05-02.png
        :height: 200px
        :width: 350px
        :alt: Class Goals
        :align: center

.. image:: ../../_static/Ch05/Slide05-03.png
        :height: 200px
        :width: 350px
        :alt: Class Goals
        :align: center

.. image:: ../../_static/Ch05/Slide05-04.png
        :height: 200px
        :width: 350px
        :alt: Class Goals
        :align: center

One way of thinking about this is to talk in terms of differences. This chart illustrates the differences between different states and the goal state. So, for example, if the current state was this one then this red line illustrates the difference from the goal state. So we should pick an operator that will help reduce the difference be- tween the current state and the goal state. So the reduction between the difference with the cur- rent state and the goal state is the end. The application of the operator is the means. That’s why it’s called the means-ends analysis. At any given state, I’m going to pick an operator that will help you deduce the difference between the current state and the goal state. Note in a way this problem is similar to the problem of part finding in robotics, where we have to design a robot that could go from one point to another point in some navigation space. ¿From my office to your office, for example, if all our offices were in the same building. There too we would use the notion of distances between offices. Here we using the notion of distance in a metaphorical sense, in a figurative sense, not in a physical sense. So I’ll sometimes use the word difference instead of distance but it’s the same idea. We are trying to deduce the distance or the difference but in an abstract space. So going back to an example of going from this initial state to this goal state. I can look at initial state and see that there are three differences between the initial state and the goal state. First, A is on table here, but A should be on B. B is on table here, but B should be on C. And third, C is on top of A here, the C should be on top, on table there. So three differences. Here the number of operations are available to us. Nine operations in particular. Let us do a means-end analysis. We can apply an operator that would put C on table. In which case the difference between the new state and the goal state will be two. We could apply an operator that will put C on top of B, in that case the difference between the current state and the goal state will still be three. Or we can ap- ply the operator putting B on top of C, in which case the distance between the current state and the goal state will be 2. Notice that the notion of reducing differences now leads to two possible choices. One could go with this state or with this one. Means-end analysis by itself does not help an AI agent decide between this course of action and that course of action. This is something that we will return to, both a little bit later in this lesson and even much more in detail when we come to planning in this course. For now, let us resume that we choose the top course of action just like they had done already there. So this chart illustrates the pot taken from the initial state to the goal state. And the important thing to notice here is that with each different move the distance between the current state and the goal state is decreasing, from three to two to one to zero. This is why means-end analysis comes up with this path because at each time it reduces a difference