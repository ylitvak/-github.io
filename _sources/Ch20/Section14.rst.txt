Section 14: More Complex Images
::::::::::::::::::::::::::::::::

.. youtube:: lOErkSy_Hyg
	:height: 315
	:width: 560
	:align: left

|More Complex Images| 
|More Complex Images 1| 
|More Complex Images 2| 
|More Complex Images 3| 
|More Complex Images 4| 
|More Complex Images 5| 
|More Complex Images 6| 
|More Complex Images 7| 
Now of course, some of us do see this as a 3D shape. You can think of
this as a paper folded here. One plane of the paper and another plane of
the paper. This looks kind of like an open book. This particular line
here then can be ignored, just being a line of these two planes, not
signifying a surface by itself. If you view this only as a line, and not
signifying a surface then it adverses David’s first problem. But how do
we address David’s second problem of this being a fold or a blade
depending upon where we started constraint propagation from? The answer
is that we actually have a much more complex ontology of disconnections.
The answer lies in the fact that we have so far used a very simple
ontology, just to demonstrate the constraint propagation process. In
reality the ontology risk constraints is more complicated. Let’s do
Y-constraint may not just fold, fold and fold, but it might also be
blade, blade and blade. And the L-constraint is not always blade and
blade and fold and fold. It could also be blade and fold and fold and
blade. Now we can see David’s second problem disappearing, because the Y
junction may have a blade and the L junction may also suggest a blade.
And there is then no conflict. Let me know that what we have shown here,
is still not a full anthology of the Y, W, L and T constraints. T
constraints in particular, may have additional complexity. The advantage
of having a more complete ontology is, that we can use that ontology to
interpret more complex scenes like this one, where there are two
rectangular objects, one being partially occluded by the other one. Of
course, the more complicated ontology is not without its own problems.
It now introduces ambiguities of a different kind. This particular
junction. Is it now a blade, blade, blade, or is it a fold, fold, fold?
Both of them are permissible in the new complete ontology. In order to
resolve some of these ambiguities, we can come up with additional
conventions. One convention is, that all of these edges that are next to
the background, we’ll consider them to be blades. So we’ll make this a
blade, blade, blade, blade. Once you make all these blades, then it’s
easy to propagate the constraints. Notice this W junction could have
been a fold, blade, fold, or a blade, fold, blade. But if we adopt the
convention of labeling all of these lines as blades, then, this W
junction can only be blade, fold, blade. But if this is a fold, this Y
junction can only be fold, fold, fold, and so on. And yet, helps us
resolve the ambiguity of what this junction could be. This task of image
interpretation is an instance of the abduction task. In abduction, we
try to come up with the best explanation for the data. This is the data,
we’re trying to interpret it in terms of an explanation. We’ll discuss
abduction in more detail when we come to diagnosis. Well now notice
that, we start with what we know. Blade, blade, blade. And that we
propagate the constraints, so that we can disambiguate between other
junctions.

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
