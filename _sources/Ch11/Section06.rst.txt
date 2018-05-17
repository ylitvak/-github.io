Section 06: Equivalence Classes
:::::::::::::::::::::::::::::::

.. youtube:: rI0q10J_VpE
	:height: 315
	:width: 560
	:align: left

|Equivalence Classes| 
|Equivalence Classes 1| 
|Equivalence Classes 2| 
Here is one way in which an intelligent agent can work and accomplish
environment with a large number of perception actions possible and yet
do so relatively efficiently. Suppose that this 2 to the power n
percepts, could be mapped into k concepts where each of these k concept
is an equivalence class with a large number of these combinations. So 2
to the power of n may be very, very large, but k is a much smaller
number. So these concepts are now equivalence classes or these percepts.
So now instead of indexing my actions on the combinations of percepts, I
index my actions on the equivalence classes that are called concepts,
and this happens all the time. You go to a doctor, for example and you
may go with some signs and symptoms and the doctor says, well, I have to
decide whether I’ll give you a blue liquid or a red liquid, assume that
those are the actions possible. And the actions are now indexed, not as
the signs and symptoms or the combination of signs and symptoms, which
are potentially very large for human beings, but it’s a small number of
concepts, the number of diseases, which compared to all the combinations
of signs and symptoms, is much smaller. Another example of this that
would come from computer programming would be that we might have a small
number of different ways in which a computer program can go wrong, by a
large number of different percepts that tell us what has actually gone
wrong. So, for example in my percepts, I might have whether or not I
received a null pointer error, whether or not I received a memory
allocation error, whether or not I received an index larger than size of
an array error. All of those are different percepts I might have, but it
might map the same underlying concept or something that has not yet been
initialized. So I’m taking the number of things that I can actually see
and mapping them to a smaller number of ways in which the program can
actually go wrong. Then instead of having to map each individual percept
to some number of actions, I know that if my error is that something has
not been initialized I need to find what hasn’t been initialized and
there’s a much smaller list of actions involved looking at each
individual variable and seeing where the initialization has not taken
place. Now we understand why classification is such an often-studied
topic in artificial intelligence. Almost every school of artificial
intelligence has studied classification extensively. If there were no
concept we were mapping this two to the power n combinations of percepts
and use two to the power m combinations of actions, then we could think
of an intelligent agent as one large, giant table. The rows of the table
are all the two to the n combinations of percepts that will be that many
rows and the columns are through the power m actions. Given a percept, I
know exactly what action to take if they would tell you that, and it’s
going to be a very large table. We don’t know how to use it, it will be
very costly to use it, and we don’t know how to build such a table. What
classification is doing is, it is breaking that large table into a large
number of small tables, and that’s the power of knowledge. When you have
knowledge, you can take some complex problem, and break it into a large
number of smaller, simpler problems.

.. |Preview| image:: ../../_static/Classification/Slide01-01.PNG
.. |Preview 1| image:: ../../_static/Classification/Slide01-02.PNG
.. |Exercise Concept Learning Revisited| image:: ../../_static/Classification/Slide02-01.PNG
.. |Exercise Concept Learning Revisited 1| image:: ../../_static/Classification/Slide02-02.PNG
.. |Exercise Concept Learning Revisited 2| image:: ../../_static/Classification/Slide03.PNG
.. |Classifying Birds| image:: ../../_static/Classification/Slide04.PNG
.. |The Challenge of Classification| image:: ../../_static/Classification/Slide05-01.PNG
.. |The Challenge of Classification 1| image:: ../../_static/Classification/Slide05-02.PNG
.. |The Challenge of Classification 2| image:: ../../_static/Classification/Slide05-03.PNG
.. |The Challenge of Classification 3| image:: ../../_static/Classification/Slide05-04.PNG
.. |The Challenge of Classification 4| image:: ../../_static/Classification/Slide05-05.PNG
.. |The Challenge of Classification 5| image:: ../../_static/Classification/Slide05-06.PNG
.. |Equivalence Classes| image:: ../../_static/Classification/Slide06-01.PNG
.. |Equivalence Classes 1| image:: ../../_static/Classification/Slide06-02.PNG
.. |Equivalence Classes 2| image:: ../../_static/Classification/Slide06-03.PNG
.. |Exercise Equivalence Classes| image:: ../../_static/Classification/Slide07.PNG
.. |Exercise Equivalence Classes 1| image:: ../../_static/Classification/Slide08.PNG
.. |Concept Hierarchies| image:: ../../_static/Classification/Slide09-01.PNG
.. |Concept Hierarchies 1| image:: ../../_static/Classification/Slide09-02.PNG
.. |Exercise Concept Hierarchies| image:: ../../_static/Classification/Slide10.PNG
.. |Exercise Concept Hierarchies 1| image:: ../../_static/Classification/Slide11.PNG
.. |Types of Concepts| image:: ../../_static/Classification/Slide12.PNG
.. |Axiomatic Concepts| image:: ../../_static/Classification/Slide13-01.PNG
.. |Axiomatic Concepts 1| image:: ../../_static/Classification/Slide13-02.PNG
.. |Prototype Concepts| image:: ../../_static/Classification/Slide14-01.PNG
.. |Prototype Concepts 1| image:: ../../_static/Classification/Slide14-02.PNG
.. |Prototype Concepts 2| image:: ../../_static/Classification/Slide14-03.PNG
.. |Prototype Concepts 3| image:: ../../_static/Classification/Slide14-04.PNG
.. |Exemplar Concepts| image:: ../../_static/Classification/Slide15-01.PNG
.. |Exemplar Concepts 1| image:: ../../_static/Classification/Slide15-02.PNG
.. |Order of Concepts| image:: ../../_static/Classification/Slide16.PNG
.. |Exercise Order of Concepts| image:: ../../_static/Classification/Slide17.PNG
.. |Exercise Order of Concepts 1| image:: ../../_static/Classification/Slide18.PNG
.. |Bottom-Up Search| image:: ../../_static/Classification/Slide19-01.PNG
.. |Bottom-Up Search 1| image:: ../../_static/Classification/Slide19-02.PNG
.. |Assignment Classification| image:: ../../_static/Classification/Slide20.PNG
.. |Wrap Up| image:: ../../_static/Classification/Slide21.PNG
