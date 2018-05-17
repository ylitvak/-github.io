Section 08: Exercise States
:::::::::::::::::::::::::::

.. youtube:: pK1p0tdZ7jU
        :height: 315
        :width: 560
        :align: left

How did you specify the state, David? So, earlier when we were talking about our goal state, we had specified that we wanted our ceiling to be painted. And we wrote that as Painted (Ceiling). So if in this state the ceiling is painted, I'll write that as Painted (Ceiling). Earlier in the initial state, we said that the robot was on the floor. And now we know that the robot is on the ladder. So I'm going to say Robot On Ladder. And this is an and, so I'm going to join them with a conjunction right there. I wasn't giving any other information about the world, so I'm not including anything else in this state. That's good, David. In general, if there is information about the initial state, additional information for example dry ladder and dry ceiling, then those associations about the world can be propagated to the subsequent states, provided that no operator in the middle of this initial state and this state actually negates or deletes any of those assertions. We'll see more of this in just a minute.

