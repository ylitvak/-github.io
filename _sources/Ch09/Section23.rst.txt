Section 23: Exercise: Retrieval by Index
::::::::::::::::::::::::::::::::::::::::

.. youtube:: -s_y6Gt9okw
        :height: 315
        :width: 560
        :align: left

Let us suppose that the case library is organized in the form of a table as shown here. Let us also suppose that we're given a new problem, how to go from this initial location to this goal location. Which case should be retrieved?

.. mchoice:: Ch09Ex6
   :answer_a: A
   :answer_b: B
   :answer_c: C
   :answer_d: D
   :correct: c
   :feedback_a: Route A matches the horizontal coordinate of the new problem, 10E, but it does not match the vertical, 4N. That means that if we can't find a route that matches both coordinates of the destination, we might choose route A. Here, however, is there a route that matches both coordinates of the destination?
   :feedback_b: The destination of Route B doesn't match either the x or the y coordinate of the new problem. Route B ends at (1E, 8N), while the new problem ends at (10E, 4N). Note that here, even though the coordinates are numeric, we're doing a straight string comparison. We're looking for the route that matches the greatest number of tags from the new problem.
   :feedback_c: Good job! The destination of route C was at 10E and 4N, which exactly matches this new problem. Note that here, even though the coordinates are numeric, we're doing a straight string comparison. We'd be looking for the route that matches the most tags, and route C matches two tags.
   :feedback_d: The destination of Route D doesn't match either the x or the y coordinate of the new problem. Route D ends at (2E, 1N), while the new problem ends at (10E, 4N). Note that here, even though the coordinates are numeric, we're doing a straight string comparison. We're looking for the route that matches the greatest number of tags from the new problem.

	What case should be retrieved and adapted? 
