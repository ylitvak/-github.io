Section 10: Exercise Operators
::::::::::::::::::::::::::::::

.. youtube:: v6zTfqhtEhc
        :height: 315
        :width: 560
        :align: left

Now that you have learned how to specify an operator, such as climb ladder. Let us do some exercises about how to specify other operators, like descend ladder, paint ceiling and paint ladder. In these boxes, please write down the pre-condition and the post-condition in the same notation

.. dragndrop:: Ch10_Q3
	:match_1: On(Robot,Ladder)^Dry(Ladder)|||descend-ladder precondition
	:match_2: On(Robot,Floor)|||descend-ladder postcondition
	:match_3: On(Robot,Ladder)|||paint-ceiling precondition
	:match_4: Painted(Ceiling)^~Dry(Ceiling)|||paint-ceiling postcondition
	:match_5: On(Robot,Floor)|||paint-ladder postcondition
	:match_6: Painted(Ladder)^~Dry(Ladder)|||paint-ladder postcondition

    Match



