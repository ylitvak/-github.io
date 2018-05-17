Section 16: Exercise Partial Planning
:::::::::::::::::::::::::::::::::::::

.. youtube:: ZLR7AEzcdkE
        :height: 315
        :width: 560
        :align: left

Now that we have seen how a simple planner may work for this goal, let us see how the simple planner, the linear planner may work with the goal of painted ceiling. Pleas write down the operators in these boxes and the states that will be achieved after the application of these boxes in these bigger boxes.

.. fillintheblank:: Ch13_Q4

    .. blank:: blank41
        :correct: climb[-]ladder
        :feedback1: (".*", "Write one of the four operators -- climb-ladder, descend-ladder, paint-ceiling, paint-ladder")

        Operator: 

    .. blank:: blank42
        :correct: [O|o]n[(][R|r]obot[,][L|l]adder[)][^][D|d]ry[(][L|l]adder[)][^][D|d]ry[(][C|c]eiling[)]
        :feedback1: (".*", "")

        State: 

.. fillintheblank:: Ch13_Q4_2

    .. blank:: blank43
        :correct: paint[-]ceiling
        :feedback1: (".*", "Write one of the four operators -- climb-ladder, descend-ladder, paint-ceiling, paint-ladder")

        Operator: 

    .. blank:: blank44
        :correct: [O|o]n[(][R|r]obot[,][L|l]adder[)][^][D|d]ry[(][L|l]adder[)][^][~][D|d]ry[(][C|c]eiling[)][^][P|p]ainted[(][C|c]eiling[)]
        :feedback1: (".*", "")

        State: 

