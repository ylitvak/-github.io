Section 02: Exercise Identifying a Foo I
::::::::::::::::::::::::::::::::::::::::

.. youtube:: 9I4qta2zeqU
        :height: 315
        :width: 560
        :align: left

Let us try to do a problem together on incremental concept learning. I'm going to give you a series of examples, and we will see what kind of concept one can learn from it. I'll not tell you what the concept really is, for the time being I'm just going to call it foo. Here is the first example. In this first example, there are four bricks. A brick at the bottom, horizontal brick at the bottom, or horizontal brick at the top. And two vertical bricks on the side. Here is a second example. And this time I'll tell you that this particular example is not a positive instance of the concept foo. Once again, we have four bricks, a brick at the bottom, a brick at the top, and two bricks on the side. This time the two bricks aren't touching each other. Here's a third example of the concept foo. This is a positive example. This is a foo. Again we have four blocks. This time they are two bricks, and instead of having two bricks, vertical bricks, we have two cylinders. They are not touching each other. So I showed you three examples of the concept foo. And I'm sure, you learned some concept definition out of it. Now I'm going to show you another example and ask you, does this example fit your current definition of concept foo, what do you think?

.. mchoice:: Ch10_Q1
   :answer_a: Yes
   :answer_b: No
   :answer_c: -
   :answer_d: -
   :correct: a
   :feedback_a: That's what we said, too. We're thinking that the shape of the support doesn't matter, so the arches on the sides here are fine. A big part of this lesson is talking about generalization and specialization. You seem to have generalized that any supports are fine, regardless of shape.
   :feedback_b: It looks like your model of a foo differs from ours: you seem to think arches can't be the supports on the sides. That's completely fine, though -- we haven't seen enough examples to be confident either way. All we can do here is infer. A big part of this lesson is talking about generalization and specialization. You seem to have a more specialized notion of a foo, that it can only have cylinders or bricks on the sides instead of arches.
   :feedback_c: -
   :feedback_d: -

   Is this a foo?