Section 05: The Challenge of Classification
:::::::::::::::::::::::::::::::::::::::::::

.. youtube:: jpURJK4sUpo
	:height: 315
	:width: 560
	:align: left

|The Challenge of Classification| 
|The Challenge of Classification 1| 
|The Challenge of Classification 2| 
|The Challenge of Classification 3| 
|The Challenge of Classification 4| 
|The Challenge of Classification 5| 
To see why classification is so powerful and so ubiquitous, and also to
understand what exactly is classification, let us go to our overall
cognitive architecture for an intelligent agent. This is a diagram that
we have come across many, many times. Let us imagine this particular
Cognitive System is dealing with a set of percepts. These percepts are
in the world. So as an example this Cognitive System may see some
object, some animal when the Cognitive System goes to the zoo. This
might be an AI agent, or perhaps your friend who goes to the zoo. And
look at some animals and there are a large number of percepts in that
environment. Has wings, Has feathers, talons, beak and so on. And for
the simplicity let’s assume that each of the percepts is binary, it’s
either true or false. So either the animal has wings or doesn’t have
wings. And depending upon the percepts and the combinations of this
percepts one might take different kind of actions. So if it’s a friendly
animal one might go and pet it, if it’s a unfriendly or dangerous animal
one might run away from it. So, all kind of actions are possible.
Imagine that there are some M actions that are possible. Send, we can
again imagine that there is a binary choice here. So, the total number
of combinations of actions, as 2 to the power m. So as an example. If I
have a, if I see a dangerous animal in a zoo, then I might both scream
and run away. If I see a friendly animal, I may approach the animal and
make cooing noise to the animal. So, a number of actions and
combinations of actions are possible. And if n is the number of percepts
then I have 2 to the power n. Combinations of percepts possible. So how
is the challenge that the cognitive agent faces? The challenges, that
the number of percepts and the number of actions multiplied by the
number of combinations of percepts and the number of combinations of
actions is very, very large. And we have to map these percepts,
combinations of percepts, actions, combinations of actions. This is a
very complex mapping. So imagine that only 10 percepts. Image at
environment, so I’m looking at an animal and let’s take 10 percepts that
I’m paying attention to. Then two to the power 10, the number of
combination of percepts is 1024, and doing it two to the power of 10
here because I’m assuming each percept has a binary value. If I had 100
percepts, I was not looking at one animal, but I was looking at a scene
of animals. Then I may have 100 percepts, in which case I have a much
larger number of combinations. And if I had something like 300 percepts,
which is not very large number. The number of combinations is, well it’s
a very large number. more than the combinations of atoms in the
universe. Now you and I, and AI agents more generally. Are constantly
faced with a complex environment where there are a large number of
percepts, and a large number of combinations that are possible. So let’s
go back to something earlier that we had considered in the class. We
defined earlier that, one way of talking what intelligent agent is to
think in terms of how can an intelligent agent map percepts into
actions. Intelligence is, in part, a lot part perhaps, according to this
definition, about action selection. The other aspect of this is. That if
the number of perceptions is large and the number of actions is large.
Then the mapping between them becomes very large and very complicated
quickly. But intelligent agents have only finite resources. How is it
then that we can select the right action. Or at least most of the time
select the right action. Even when the environment is very complex. And
do so in near real time.

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
