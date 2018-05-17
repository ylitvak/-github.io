Section 21: Chunking
::::::::::::::::::::

.. youtube:: 0CY0s-M-Mqc
	:height: 315
	:width: 560
	:align: left

|Chunking| 
So for this situation source cognitive architectures selected not one
goal but to. So this SOAR theory this is called an impasse. An impasse
occurs when the decision maker cannot make a decision either because not
enough knowledge is available or because multiple courses of action
there are being selected and the agent cannot decide among them. In this
case two actions have been selected and the agent cannot decide between
them. Should the pitch throw a curve ball or a fast ball? At this point
SOAR will attempt to learn a rule that might break the impasse. If the
decision maker has a choice between the fast ball and the curve ball and
it cannot decide it, might there be a way of learning a rule that
decides between what to throw in a particular situation given the choice
of the fast falling curve ball. For this now SOAR will invoke episodic
knowledge. Let’s see how SOAR does that and how it can help SOAR learn
the rule that results in the breaking of the impasse. So imagine that
SOAR had episodic knowledge about the previous event, about the previous
instance of an event. And this previous instance of an event in another
game it was a fifth inning bottom of the fifth inning, if the weather
was windy it was the same batter though, Parra, who bats left handed. It
was a similar kind of situation and the pitcher threw a fastball and
Parra hit a homerun out of it. Now we want to avoid that. The current
pitcher wants to avoid it. So given this episodic knowledge about this
even set occurred earlier, SOAR has learning mechanism that allows it to
encapsulate knowledge from this event into the form of a production rule
that can be used as part of the procedural knowledge. And the learned
rule is, if two operators are suggested, and threw a fast ball is one of
those operators, and the batter is Parra, then dismiss throw-fast-ball
operator. This is the process of learning called chunking. So, chunking
is a process, a learning technique that’s SOAR uses to learn rules that
can break impasse. First note, that chunking is triggered when impasse
occurs. In this situation, the impasse is that two rules got activated
and there is no way of resolving between them. So the impasse imagery
tells the process of chunking, what the goal of chunking is. Find a rule
that can break the impasse. SOAR now searches for the episodic memory
and finds an event that has some knowledge that may break the impulse.
In particular, it looks like a perceptual current situation that we had
in previous shot. And compared to the perceptions of previous
situations, of the event memory, the episodic memory, and find that any
information available of the current batter. If some information is
available that tells, SOAR the result of some previous action that also
occurs in the current impasse, then SOAR picks that event. So now it
tries to encapsulate the result of the previous event, in the form of a
rule. In this case, it wants to avoid the result of a homerun, and
therefore it says dismiss that particular operator. If it wanted that
particular result, it would have said throw that particular operator. We
said earlier that in cognitive systems, reasoning, learning and memory
are closely connected. Here is an example of that. We’re dealing with
memory, procedural memory, we’re dealing with memory that can deal with
procedural knowledge and episodic knowledge. Dealing with reasoning,
decision making. We’re also dealing with learning, chunking. If you want
to learn more about chunking then the reading by Lehman Leodon
Rosenblum, and the further readings at the end of this lesson gives lot
many more details.

.. |Preview| image:: ../../_static/ProductionSystems/Slide01-01.PNG
.. |Preview 1| image:: ../../_static/ProductionSystems/Slide01-02.PNG
.. |Exercise A Pitcher| image:: ../../_static/ProductionSystems/Slide02-01.PNG
.. |Exercise A Pitcher 1| image:: ../../_static/ProductionSystems/Slide02-02.PNG
.. |Exercise A Pitcher 2| image:: ../../_static/ProductionSystems/Slide03.PNG
.. |Function of a Cognitive Architecture| image:: ../../_static/ProductionSystems/Slide04.PNG
.. |Levels of Cognitive Architectures| image:: ../../_static/ProductionSystems/Slide05-01.PNG
.. |Exercise Levels of Architectures| image:: ../../_static/ProductionSystems/Slide06.PNG
.. |Exercise Levels of Architectures 1| image:: ../../_static/ProductionSystems/Slide07.PNG
.. |Assumptions of Cognitive Architectures| image:: ../../_static/ProductionSystems/Slide08.PNG
.. |Architecture Content Behavior| image:: ../../_static/ProductionSystems/Slide09-01.PNG
.. |Architecture Content Behavior 1| image:: ../../_static/ProductionSystems/Slide09-02.PNG
.. |A Cognitive Architecture for Production Systems| image:: ../../_static/ProductionSystems/Slide10-01.PNG
.. |A Cognitive Architecture for Production Systems 1| image:: ../../_static/ProductionSystems/Slide10-02.PNG
.. |Return to the Pitcher| image:: ../../_static/ProductionSystems/Slide11-01.PNG
.. |Return to the Pitcher 1| image:: ../../_static/ProductionSystems/Slide11-02.PNG
.. |Return to the Pitcher 2| image:: ../../_static/ProductionSystems/Slide11-03.PNG
.. |Action Selection| image:: ../../_static/ProductionSystems/Slide12-01.PNG
.. |Action Selection 1| image:: ../../_static/ProductionSystems/Slide12-02.PNG
.. |Putting Content in the Architecture| image:: ../../_static/ProductionSystems/Slide13.PNG
.. |Bringing in Memory| image:: ../../_static/ProductionSystems/Slide14-01.PNG
.. |Bringing in Memory 1| image:: ../../_static/ProductionSystems/Slide14-02.PNG
.. |Exercise Production System in Action I| image:: ../../_static/ProductionSystems/Slide15.PNG
.. |Exercise Production System in Action I 1| image:: ../../_static/ProductionSystems/Slide16.PNG
.. |Exercise Production System in Action II| image:: ../../_static/ProductionSystems/Slide17.PNG
.. |Exercise Production System in Action II 1| image:: ../../_static/ProductionSystems/Slide18.PNG
.. |Exercise System in Action III| image:: ../../_static/ProductionSystems/Slide19.PNG
.. |Exercise System in Action III 1| image:: ../../_static/ProductionSystems/Slide20.PNG
.. |Chunking| image:: ../../_static/ProductionSystems/Slide21.PNG
.. |Exercise Chunking| image:: ../../_static/ProductionSystems/Slide22.PNG
.. |Exercise Chunking 1| image:: ../../_static/ProductionSystems/Slide23.PNG
.. |Assignment Production Systems| image:: ../../_static/ProductionSystems/Slide25.PNG
.. |Wrap Up| image:: ../../_static/ProductionSystems/Slide26.PNG
.. |The Cognitive Connection| image:: ../../_static/ProductionSystems/Slide27-01.PNG
.. |The Cognitive Connection 1| image:: ../../_static/ProductionSystems/Slide27-02.PNG
.. |The Cognitive Connection 2| image:: ../../_static/ProductionSystems/Slide27-03.PNG
