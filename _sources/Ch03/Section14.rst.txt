Section 14: Solving the Guards and Prisoners Problem
::::::::::::::::::::::::::::::::::::::::::::::::::::


.. youtube:: 2RZXMOMOVNY
	:height: 315
	:width: 560
	:align: left


|Solving the Guards and Prisoners Problem| 
|Solving the Guards and Prisoners Problem 1| 
|Solving the Guards and Prisoners Problem 2| 

There’s an old saying in AI, which goes like, if you have the right
knowledge representation, problem solving becomes very easy. Let’s see
whether that also works here. We now have a knowledge representation for
this problem of guards and prisoners. Does this knowledge representation
immediately afford effective problem solving? So, here we are in the
first node, the first state. There are three guards and three prisoners
in the boat, all in the left-hand side. Let us see what moves are
possible from this initial state. Now, using this representation, we can
quickly figure out that there are five possible moves from the initial
state. And the first move, we move only guard to the right. On the
second move, we move a guard and a prisoner to the right. In the third
move, we can move two guards, or two prisoners. Or, in the fifth move,
just one prisoner to the right. Five possible moves. Of course, we know
that some of these moves are illegal and some of them are likely to be
not very productive. Will the semantic network allow us to make
inferences about which moves are productive and which moves are not
productive? Let’s see further. So, let’s look at the legal moves first.
So we can immediately make out from this representation, that the first
move is not legal because we are not allowed to have more prisoners than
guards on one side, of the river. Similarly, we know that the third move
is illegal for the same reason. So, we can immediately rule out the
first and the third moves. The fifth move, too, can be ruled out. Let’s
see how. We have one prisoner on the other side. But the only way to go
back would be to take the prisoner to the, back to the previous side.
And if we do that, we reach the initial state. So we did not make any
forward progress. Therefore, we can rule out this move as well. This
leaves us with two possible moves that are both legal and productive.
The, we have already removed the moves that were not legal and not
productive. Later, we will see how AI programs can use various methods
to figure out what moves are productive and what moves are unproductive.
For the time being, let’s go along with our problem solving.

.. |Preview| image:: ../../_static/SemanticNetworks/Slide01-01.PNG
.. |Preview 1| image:: ../../_static/SemanticNetworks/Slide01-02.PNG
.. |Representations| image:: ../../_static/SemanticNetworks/Slide02.PNG
.. |Introduction to Semantic Networks| image:: ../../_static/SemanticNetworks/Slide03-01.PNG
.. |Introduction to Semantic Networks 1| image:: ../../_static/SemanticNetworks/Slide03-02.PNG
.. |Introduction to Semantic Networks 2| image:: ../../_static/SemanticNetworks/Slide03-03.PNG
.. |Exercise Constructing Semantic Nets I| image:: ../../_static/SemanticNetworks/Slide04.PNG
.. |Exercise Constructing Semantic Nets I 1| image:: ../../_static/SemanticNetworks/Slide05.PNG
.. |Exercise Constructing Semantic Nets II| image:: ../../_static/SemanticNetworks/Slide06.PNG
.. |Exercise Constructing Semantic Nets II 1| image:: ../../_static/SemanticNetworks/Slide07.PNG
.. |Structure of Semantic Networks| image:: ../../_static/SemanticNetworks/Slide08.PNG
.. |Characteristics of Good Representations| image:: ../../_static/SemanticNetworks/Slide09.PNG
.. |Discussion Good Representations| image:: ../../_static/SemanticNetworks/Slide10.PNG
.. |Discussion Good Representations 1| image:: ../../_static/SemanticNetworks/Slide11.PNG
.. |Guards and Prisoners| image:: ../../_static/SemanticNetworks/Slide12-01.PNG
.. |Guards and Prisoners 1| image:: ../../_static/SemanticNetworks/Slide12-02.PNG
.. |Semantic Networks for Guards Prisoners| image:: ../../_static/SemanticNetworks/Slide13.PNG
.. |Solving the Guards and Prisoners Problem| image:: ../../_static/SemanticNetworks/Slide14-01.PNG
.. |Solving the Guards and Prisoners Problem 1| image:: ../../_static/SemanticNetworks/Slide14-02.PNG
.. |Solving the Guards and Prisoners Problem 2| image:: ../../_static/SemanticNetworks/Slide14-03.PNG
.. |Exercise Guards and Prisoners II| image:: ../../_static/SemanticNetworks/Slide18-01.PNG
.. |Exercise Guards and Prisoners II 1| image:: ../../_static/SemanticNetworks/Slide18-02.PNG
.. |Exercise Guards and Prisoners II 2| image:: ../../_static/SemanticNetworks/Slide18-03.PNG
.. |Exercise Guards and Prisoners III| image:: ../../_static/SemanticNetworks/Slide19-01.PNG
.. |Exercise Guards and Prisoners III 1| image:: ../../_static/SemanticNetworks/Slide20.PNG
.. |Represent Reason for Analogy Problems| image:: ../../_static/SemanticNetworks/Slide21-01.PNG
.. |Represent Reason for Analogy Problems 1| image:: ../../_static/SemanticNetworks/Slide21-02.PNG
.. |Exercise Represent Reason for Ravens| image:: ../../_static/SemanticNetworks/Slide22.PNG
.. |Exercise Represent Reason for Ravens 1| image:: ../../_static/SemanticNetworks/Slide23.PNG
.. |Exercise How do we choose a match| image:: ../../_static/SemanticNetworks/Slide24.PNG
.. |Exercise How do we choose a match 1| image:: ../../_static/SemanticNetworks/Slide25.PNG
.. |Choosing Matches by Weights| image:: ../../_static/SemanticNetworks/Slide26-01.PNG
.. |Choosing Matches by Weights 1| image:: ../../_static/SemanticNetworks/Slide26-02.PNG
.. |Discussion Choosing a Match by Weight| image:: ../../_static/SemanticNetworks/Slide27-01.PNG
.. |Assignment Semantic Nets| image:: ../../_static/SemanticNetworks/Slide30.PNG
.. |Wrap Up| image:: ../../_static/SemanticNetworks/Slide31.PNG
.. |Final Quiz| image:: ../../_static/SemanticNetworks/Slide34-01.PNG
.. |Final Quiz 1| image:: ../../_static/SemanticNetworks/Slide34-02.PNG
.. |Final Quiz 2| image:: ../../_static/SemanticNetworks/Slide34-03.PNG
.. |Final Quiz 3| image:: ../../_static/SemanticNetworks/Slide34-04.PNG
.. |Final Quiz 4| image:: ../../_static/SemanticNetworks/Slide34-05.PNG
.. |Final Quiz 5| image:: ../../_static/SemanticNetworks/Slide34-06.PNG
