Section 25: Exercise: Retrieval by Discrimination Tree
::::::::::::::::::::::::::::::::::::::::::::::::::::::

.. youtube:: 4o9Is5kIlog
        :height: 315
        :width: 560
        :align: left

Let's repeat this exercise, but this time using discrimination tree for organizing the case memory. So here is a discrimination tree, containing the cases currently in the case memory. And here is the, new problem. You could go to the initial location, to the goal location. Given this problem, what case would be retrieved from this discrimination tree?

.. mchoice:: Ch09Ex6
   :answer_a: A
   :answer_b: B
   :answer_c: X
   :answer_d: Y
   :correct: d
   :feedback_a: Not quite. You're right that we'd answer 'Yes' to 'Is the origin North of 5N?'; 'No' to 'East of 5E?'; and 'No' to 'East of 3E?'. However, to retrieve case A, we'd have to answer 'Yes' to 'Is the origin East of 2E?' The origin is at the far West side of the map, so it isn't East of anything except 0E.
   :feedback_b: Not quite. You're right that we'd answer 'Yes' to 'Is the origin North of 5N?' and 'No' to 'East of 5E?'. However, to retrieve case X, we'd have to answer 'Yes' to 'Is the origin East of 3E?' The origin is at the far West side of the map, so it isn't East of anything except 0E.
   :feedback_c: Good job! The destination of route C was at 10E and 4N, which exactly matches this new problem. Note that here, even though the coordinates are numeric, we're doing a straight string comparison. We'd be looking for the route that matches the most tags, and route C matches two tags.
   :feedback_d: That's right! Traversing the tree from top to bottom, we say 'Yes' to 'Is the origin North of 5N?'; 'No' to 'East of 5E?'; 'No' to 'East of 3E?'; and 'No' to 'East of 2E?'. So, we retrieve case Y.

	What case should be retrieved and adapted? 
