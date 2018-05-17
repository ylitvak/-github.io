Section 41: Exercise: Proof V
:::::::::::::::::::::::::::::::::

.. youtube:: tqDzsVzvsys
        :height: 315
        :width: 560
        :align: left

.. image:: ../_static/LogicImages/Slide41-01.PNG
        :height: 200px
        :width: 350px
        :alt: Exercise: Proof V
        :align: center

.. image:: ../_static/LogicImages/Slide41-02.PNG
        :height: 200px
        :width: 350px
        :alt: Exercise Proof V 2
        :align: center

What do you think David? So in resolution theorem proving, we start with whatever it is we assumed and look for the negation of that in an earlier sentence. Here we find not bird, and bird in S1. So we’re going to resolve on not bird and bird and leave both of those out. That’s good.

Section 42: Exercise: Proof VI
::::::::::::::::::::::::::::::::::

.. youtube:: NYN1e2rhWDg
        :height: 315
        :width: 560
        :align: left

.. image:: ../_static/LogicImages/Slide42.PNG
        :height: 200px
        :width: 350px
        :alt: Exercise Proof VI
        :align: center

So what shall we do next? What should we resolve on next?

Section 43: Exercise: Proof VI
::::::::::::::::::::::::::::::::::

.. youtube:: Y8yy1QJV5I8
        :height: 315
        :width: 560
        :align: left

.. image:: ../_static/LogicImages/Slide43-01.PNG
        :height: 200px
        :width: 350px
        :alt: Exercise Proof VI
        :align: center

.. image:: ../_static/LogicImages/Slide43-02.PNG
        :height: 200px
        :width: 350px
        :alt: Exercise Proof VI 2
        :align: center

.. image:: ../_static/LogicImages/Slide43-03.PNG
        :height: 200px
        :width: 350px
        :alt: Exercise Proof VI 3
        :align: center

Out of four choices, which one did you pick, David? So, I picked the first one, but I think there’s actually two correct answers. What we’re looking for is something else in S1 that has a negation in another sentence. Not has wings has a negation in S2, so we could resolve on S2 with the not has wings portion of S1. Has fur also has a negation in S3. So we could also resolve on S3 and the has fur portion of S1. This is right, David. At the end of this, we’re left with null, which is a contradiction. Therefore, an assumption that is not bird is false. Therefore, it must be a bird and the robot has just proved that this must be a bird. Note what we have done. We have mechanized parts of logic. And sort of coming up with large truth tables. And it’s sort of coming up with complex chains of inference based on modus ponens and modus tollens. We have found in our garden resolutions are improving, which is a efficient way of proving sentences and the truth values. This is how it works. Take all the sentence and the knowledge base, convert them into conjecture novel form. Take what you want to prove and its negation. Put that as a new sentence. Now, starting with this particular sentence, a new sentence. Find the literal in another sentence on which you can resolve, and keep on doing it until you find a null condition, which is a contradiction. If you don’t find a null condition, if you don’t find a contradiction, that means that what you started with cannot be proved.

Section 44: Assignment: Logic
:::::::::::::::::::::::::::::::::

.. youtube:: XKRY4OXfL5c
        :height: 315
        :width: 560
        :align: left

.. image:: ../_static/LogicImages/Slide44.PNG
        :height: 200px
        :width: 350px
        :alt: Exercise Proof VI 3
        :align: center

So how would you use formal logic to develop an agent that can solve Raven’s progressive matrices? As with production systems, we can kind of face this at two different levels. One, you could use formal logic to represent the overall algorithm the agent uses to solve any new problem. Or secondly, the agent could use formal logic to develop its understanding of a new problem that just came in. It could then use those formal rules to develop the transformations that occur within the problem and transfer those transformations into the new answer. Alternatively, you could also use formal logic to allow your agent to prove why it’s answer to a particular problem is correct. Then if the answer is actually incorrect, the agent may have the information necessary to go back and repair it’s reasoning and do better next time.

Section 45: Wrap Up
:::::::::::::::::::::::

.. youtube:: o_tNdgOC138
        :height: 315
        :width: 560
        :align: left

.. image:: ../_static/LogicImages/Slide45.PNG
        :height: 200px
        :width: 350px
        :alt: Wrap Up
        :align: center

So today, we’ve talked about formal logic in order to set up a kind of formal language for us to reason with going forward. We started off by talking about formal notation, including conjunctions and disjunctions, so that we can write sentences in formal logic. We use that to then talk about truth tables, and exam some of the properties that we need going forward, like De Morgan’s law. Using that, we investigated some of the inferences that we can draw using formal logic. And finally, we looked at proof by reputation which kind of capitalizes on everything we’ve talked about so far. Next time, we’ll be discussing planning, which leverages the formal logic that we’ve developed in this lesson. It allows agents to reason more formally about initial and goal states. Interestingly, planning actually has its history in the kinds of proofs we’ve developed here. Originally, agents would prove that a particular plan would work, so that’s why we talk about formal logic before we talk about planning.


