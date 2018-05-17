Section 09: Constraints: Intersections and Edges
:::::::::::::::::::::::::::::::::::::::::::::::::

.. youtube:: TnFHkhiGetw
	:height: 315
	:width: 560
	:align: left

|Constraints Intersections and Edges| 
|Constraints Intersections and Edges 1| 
|Constraints Intersections and Edges 2| 
So let’s take the notion of constraints. Consider this cube again.
You’ll notice this cube has junctions, and these junctions have
different kind of shapes. For example, this looks like a Y junction,
this looks like an L junction, this also looks like an L junction, it’s
just that this arm of the L is coming in the other direction. This also
looks like an L junction. This junction, on the other hand, looks a
little bit like a W junction. So, junctions of various kinds. Here are
the kind of junctions that can occur, in the world of trihedral objects
like cubes. Y junction, W junction, T junction, L junction. We can say a
little bit more about each of these junctions. Let us look at the Y
junction first. If we examine the various kinds of Y junctions that get
formed in the world of trihedral optics, then we find that whenever
there is a Y junction formed, then each of these lines represents a
fold, where a fold is a line where two surfaces meet. Now, the important
thing about this is. That if we can infer, that this is a Y junction and
that this line represents a fold, then an image that follows, this line
must also represent a fold, and this line must also represent a fold.
Actually I should tell you quickly, that in the world of trihedral
objects. Y junctions can have multiple kind of constraints. But right
now, let’s just look at this one single constraint. So in the case of an
L junction, which has a shape like this, in the world of trihedral
objects, an L junction is characterized by this being a blade, and this
being a blade, where a blade is a line, well we cannot infer that two
surfaces are getting connected with each other. Again, the L-Constraint
can actually have many more formulations. But right now, we’re keeping
it simple just looking at one single constraint for the L junction.
Similarly, in the world of trihedral objects, one of the ways in which a
double junction gets characterized is through a blade, fold, blade. In
effect, we’re defining a spatial grammar here, for the world of
trihedral objects. The equivalent of this, in case of grammar of natural
language sentences might be that a sentence can have a non phrase,
followed by their verb phrase, followed by a propositional phrase, and
so on. Given this set of very simple constraints for the world of
trihedral objects, let us see how these constraints actually can be
propagated, to group edges and to surfaces

.. |Preview| image:: ../../_static/ConstraintPropagation/Slide01-01.PNG
.. |Preview 1| image:: ../../_static/ConstraintPropagation/Slide01-02.PNG
.. |Exercise Recognizing 3D Figures| image:: ../../_static/ConstraintPropagation/Slide02-01.PNG
.. |Exercise Recognizing 3D Figures 1| image:: ../../_static/ConstraintPropagation/Slide02-02.PNG
.. |Exercise Recognizing 3D Figures 2| image:: ../../_static/ConstraintPropagation/Slide03.PNG
.. |Exercise Gibberish Sentences| image:: ../../_static/ConstraintPropagation/Slide04.PNG
.. |Exercise Gibberish Sentences 1| image:: ../../_static/ConstraintPropagation/Slide05.PNG
.. |Constraint Propagation Defined| image:: ../../_static/ConstraintPropagation/Slide06.PNG
.. |From Pixels to 3D| image:: ../../_static/ConstraintPropagation/Slide07-01.PNG
.. |From Pixels to 3D 1| image:: ../../_static/ConstraintPropagation/Slide07-02.PNG
.. |From Pixels to 3D 2| image:: ../../_static/ConstraintPropagation/Slide07-03.PNG
.. |Line Labeling| image:: ../../_static/ConstraintPropagation/Slide08.PNG
.. |Constraints Intersections and Edges| image:: ../../_static/ConstraintPropagation/Slide09-01.PNG
.. |Constraints Intersections and Edges 1| image:: ../../_static/ConstraintPropagation/Slide09-02.PNG
.. |Constraints Intersections and Edges 2| image:: ../../_static/ConstraintPropagation/Slide09-03.PNG
.. |Exercise Assembling the Cube I| image:: ../../_static/ConstraintPropagation/Slide10.PNG
.. |Exercise Assembling the Cube I 1| image:: ../../_static/ConstraintPropagation/Slide11.PNG
.. |Exercise Assembling the Cube II| image:: ../../_static/ConstraintPropagation/Slide12.PNG
.. |Exercise Assembling the Cube II 1| image:: ../../_static/ConstraintPropagation/Slide13.PNG
.. |More Complex Images| image:: ../../_static/ConstraintPropagation/Slide14-01.PNG
.. |More Complex Images 1| image:: ../../_static/ConstraintPropagation/Slide14-02.PNG
.. |More Complex Images 2| image:: ../../_static/ConstraintPropagation/Slide14-03.PNG
.. |More Complex Images 3| image:: ../../_static/ConstraintPropagation/Slide14-04.PNG
.. |More Complex Images 4| image:: ../../_static/ConstraintPropagation/Slide14-05.PNG
.. |More Complex Images 5| image:: ../../_static/ConstraintPropagation/Slide14-06.PNG
.. |More Complex Images 6| image:: ../../_static/ConstraintPropagation/Slide14-07.PNG
.. |More Complex Images 7| image:: ../../_static/ConstraintPropagation/Slide14-08.PNG
.. |Constraint Propagation for Natural Language Processing| image:: ../../_static/ConstraintPropagation/Slide15-01.PNG
.. |Constraint Propagation for Natural Language Processing 1| image:: ../../_static/ConstraintPropagation/Slide15-02.PNG
.. |Constraint Propagation for Natural Language Processing 2| image:: ../../_static/ConstraintPropagation/Slide15-03.PNG
.. |Assignment Constraint Propagation| image:: ../../_static/ConstraintPropagation/Slide16.PNG
.. |Wrap Up| image:: ../../_static/ConstraintPropagation/Slide17.PNG
