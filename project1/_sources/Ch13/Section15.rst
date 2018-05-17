Section 15: Partial Planning
::::::::::::::::::::::::::::

.. youtube:: cwjbtxddJt8
        :height: 315
        :width: 560
        :align: left

Now let us see how partial order planning, sometimes also called nonlinear planning, may work for our ladder and ceiling problem. So here is a goal state, painted ladder. There is the initial state. We can now use the goal knowledge as control knowledge to select between different operators available in this world. The only operator whose post conditions match the goal condition of painted ladder. And whose preconditions are compatible with the initial status, paint-ladder. So we'll select that operator. When we think of applying the operator paint-ladder to the initial state, we get this as a successor state. Painted ladder and not dry ladder are coming from the post conditions of paint-ladder. Robot and floor, and ceiling, dry, have been propagated from the initial state. We changed dry ladder to not dry ladder because that was the post condition of paint-ladder. We did not change the on robot floor and dry ceiling because pain ladder was silent about them.

