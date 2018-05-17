Section 10: Quiz: Discussion Smart Generators and Testers
::::::::::::::::::::::::::::::::::::::::::::::::::::::

.. youtube:: TykwL-Qflbc
        :height: 315
        :width: 560
        :align: center

Recall that we had this state as a kind of hanging state. It had no successes state. And we said that, well this state can be dismissed, but here is a question. Who will dismiss it, the generator or the tester? What do you think, David? So I think the tester would do it. We could have the tester basically say any state where there is only one person on the side of the river that has the boat can be pruned off , because the only way to get into that state is to send that person over. And the only way to get out of that state is to undo the previous move. So my rule would be for the tester, any time only one person is on the side of the river with the boat, throw out that state. What does everyone else think? Is David right about this?

.. mchoice:: Ch10Ex2
   :answer_a: Yes, this is the only way to throw out that state
   :answer_b: Yes, but there is a rule to prevent the state from being generated in the first place
   :answer_c: No, because the rule should apply only to the right coast as we are trying to move everyone to the right
   :answer_d: No, because the rule would throw out some valid states as well
   :correct: b
   :feedback_a: David's method does work, but is there really no other way to decide to throw out this state? Could our generator be equipped with the ability to never generate this state in the first place?
   :feedback_b: That's right! It's true that David's rule would work, but we could have avoided generating the invalid state in the first place.
   :feedback_c: While that makes sense, it isn't actually necessary. The way the problem is set up, there is no way for only one person to be on either coast unless they took the boat over by themselves. So, it's fine to throw out states that meet these conditions on either coast.
   :feedback_d: Actually, there is no valid state that this rule would ignore. If you can think of one, though, let us know on the forums!

   Is David right?    