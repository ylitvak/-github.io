Section 06: Constraint Propagation Defined
:::::::::::::::::::::::::::::::::::::::::::

.. youtube:: vQ7ucWQOQ4s
	:height: 315
	:width: 560
	:align: left

|Constraint Propagation Defined| 
This brings us to the definition of constraint propagation. Constraint
propagation is a method of inference that assigns values to variables
characterizing a problem in such a way that some conditions are
satisfied. So if you have any problem, that problem is going to be
characterized by some variables. And the task is to give specific values
to each variable in such a way that some global constraints have been
satisfied. So given a problem, some problems are characterized by a set
of variables, each variable may locally take on some values. So probably
the question is, how can we locally assign values to variables in such a
way that some global constraints are satisfied? As an example, let us
return to this figure. Here is a figure, drawn on a 2D surface, and the
problem is whether or not it represents a 3D object. The variables here
are the surfaces and the orientations. One could consider this to be a
single, two dimensional surface with some lines drawn on it.
Alternatively, one can think of this as having four surfaces, one, two,
three, four, where each surface has a particular orientation. The
orientation can be specified by the perpendicular of that surface. The
method of constraint propagation is going to help identify the surfaces
and their orientations. The constraints here are defined by these
junctions. For trihedral objects where three surfaces meet at a
particular point, these junctions have certain properties. No matter how
we assign these surfaces and their orientations, the assignment must
satisfy all of those constraints. We’ll look at the details of
constraint propagation in a minute. But first notice that there are two
possible interpretations to this particular 3D object. One can look at
it as if one were looking inside a box. Alternatively, one can look at
it as if one were looking at a building. This means that constraint
propagation need not necessarily always succeed in this ambiguity
between different kind of assignments of surfaces in the orientation.
Sometimes multiple interpretations can simultaneously satisfy all the
constraints. It is also possible that no assignment of values with
variables will satisfy all the constraints, in which case interpretation
becomes very difficult. As another example, let us examine this
sentence. Colorless green ideas sleep furiously. All of us can recognize
that this is semantically meaningless, but grammatically correct. How
did we know that this is grammatically correct? The variables here are
the various lexical categories, like words and nouns and some different
predicates. The values are the assignments we make to these various
words here. Is green a noun? Is green a verb? Green a determiner? Is it
part of a subject or part of a predicate? The constraints here are
defined with the rules of English language grammar. As we assign values
to the various variables here, that assignment must satisfy the
constraints of the English language grammar so that as we assign values
to these variables, those assignments must satisfy the constraints of
the English language grammar before we can accept this sentence to be
grammatically correct. If this sentence was grammatically not correct,
then we will not be able to assign values to all the variables in a way
that will satisfy the constraints imposed by the English language
grammar. So we’ve actually come across this idea of constraints in
English language grammar before. During our lesson on understanding we
talked about how a preposition, for example, can constrain the meaning
of the word that follows it. If we see the word from, for example, we
expect what comes after it to be some kind of source for the sentence.
There we used grammatical constraints in service of some kind of
semantic analysis. Here we’re just using grammatical constraints to
figure out if a sentence is grammatically correct or not. There’s
another connection here to understanding as well. Ashok talked about how
we can interpret this shape as either popping out towards us or down
into the screen. We talked about two simultaneously accurate
interpretations of the same thing and understanding with regard to
sentences that can be read as puns. So for example, when I said, it’s
hard to explain puns to kleptomaniacs because they always take things
literally. The word take can simultaneously be interpreted as interpret
and physically remove, while satisfying all the constraints of the
sentence.

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
