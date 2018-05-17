Section 30: Hierarchical Task Network Planning
::::::::::::::::::::::::::::::::::::::::::::::

.. youtube:: 7L3tcoFMR7w
        :height: 315
        :width: 560
        :align: left

Our next topic in planning is called hierarchical planning. We'll introduce the idea to you. We'll also introduce the representation called hierarchical task network to you. HTN for hierarchical task network. To illustrate hierarchical planning, imagine that you are still in the box microworld. Here is the initial state. And here is the goal state. These states are more complicated than any initial state and goal state that we have encountered so far. So as previously, we can use partial order planning to come up with a plan to go from this initial state to goal state. Here is the final plan, and as you can see, it's pretty long and complicated, with a large number of operations in them. So the question then becomes, can we abstract some of these operations at a higher level? So that instead of thinking in terms of these slow level move operations, we can think in terms of high level macro operations. And those macro operations will then make the problems space much smaller, much simpler so that we can navigate it. And then we can expand those macro operators into the move operations.

