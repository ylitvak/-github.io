Section 04: State Spaces
::::::::::::::::::::::::::::::::::::::::
.. youtube:: eliEyu_10kQ 
        :height: 315
        :width: 560
        :align: left

.. image:: ../../_static/Ch05/Slide04-01.png
        :height: 200px
        :width: 350px
        :alt: Class Goals
        :align: center

.. image:: ../../_static/Ch05/Slide04-02.png
        :height: 200px
        :width: 350px
        :alt: Class Goals
        :align: center

So, we can imagine problem solving as occurring in a state space. Here is the initial state, here is the goal state. And the state space consists of all of the states that could be potentially produced from the initial state by iterative application of the various operators in this micro world. I want to come up with a path in the state space, takes me from initial state to the goal state. There is one path, this is not the only path, but this is one path to go from the initial state to the goal state. The question then becomes, how might an AI agent derive this path that may take it from the initial state to the goal state. Let us see how this notion of path finding applies to our blocks world problem. ¿From the initial state, here it is one path of going to the goal state. First, we put C on the table. Then we put B on top C. And then we put A on top of B. Which is exactly the answer that David had given. This is one sequence, one path from the initial state to the goal state. The question then becomes, how does AI method know what operation to select in a given state? Consider this state, for example. There are several operations possible here. One could put C on top of B or B on top of A. How does the AI agent know which operation to select at this particular state?