Section 09: Operators
:::::::::::::::::::::

.. youtube:: 2PyyQt1Vcmg
        :height: 315
        :width: 560
        :align: left

Now that we have learned how to specify states in planning, let us look at how to specify the operators. So consider the operator, climb-ladder. You might specify the climb-ladder operator, and any other operator in general, to a set of preconditions, and post-conditions. So for the climb-ladder operator, the precondition might be that the robot is on the floor and the ladder is dry. Notice that these are being written in the language of propositional logic. And the postcondition for the climb-ladder operator might be that the robot is on the ladder. This captures the notion that the robot has climbed the ladder. It was earlier on the floor and later it's on the ladder. Several things to note here. First, by convention the precondition does not have any negative leg holds. All the leg holds in the precondition are positive. Post conditions of operators may have negative leg holds. Second, the meaning of this pre-condition, and post conditions is that, these assertions are true in the world before this operator can be applied. And that these assertions become true in the world after this operator has been applied. This captures the syntax of the operator climb-ladder. The semantics of this operator is that this operator can be applied if and only if the preconditions of the operator are true in the world. It cannot be applied if the preconditions are not true in the world

