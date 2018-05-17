Section 27: Exercise Partial Order Planning IV
::::::::::::::::::::::::::::::::::::::::::::::

.. youtube:: myMbVQnqA58
        :height: 315
        :width: 560
        :align: left

What ordering did you come up with David? So what we see is that each goal actually clobbers the next goal in its last step. So the post condition of move A, B is that A is now on B. But a precondition for move B, C is that B is clear. Because A is on B, B is no longer clear, so we can't move B to C, so this plan has clobbered this plan. Similarly, if we move B to C, we no longer can move C on top of D because C is no longer clear, so this plan has clobbered this plan. So we're going to need to do this plan first, then this plan, then this plan. Good, David.

