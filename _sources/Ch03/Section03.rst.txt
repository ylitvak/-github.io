Section 03: Introduction to Semantic Networks
:::::::::::::::::::::::::::::::::::::::::::::


.. youtube:: TWGTJyK2BJA
	:height: 315
	:width: 560
	:align: left


|Introduction to Semantic Networks| 
|Introduction to Semantic Networks 1| 
|Introduction to Semantic Networks 2| 

To understand semantic networks as a knowledge representation, let us
take an example. This is an example that we saw in a previous lesson.
This is A is to B as C is to D, and we have to pick one of the six
choices at the bottom that will go in D. How will we represent our
knowledge of A, B, C and the six choices at the bottom? Let us begin
with A and B. We’ll try to build semantics networks that can represent
our knowledge of A and B. Inside A is a circle, I’ll label it x. Also
inside x is a diamond, I’ll label it y. Here is a black dot, I’ll label
it z. We can similarly label the objects in B. So inside A are three
objects, x, y, and z. So the first thing we need to do in order to build
a semantic network for representing our knowledge of A is to represent
the object. So I have the object x, the object y, the object z, standing
for the circle, the diamond and the black dot. Now that we have
represented the objects in A, we want to represent the relationships
between these objects. So I have the objects x, y, z, and we’ll try to
represent the relationship between them by having links between the
nodes representing the objects. These links can be labeled. So I may say
that y is inside x because that is the relationship in the image A.
Similarly I may say that z is above y because z is above y in the image
A. I may also say that z is above x because z is above x in image A. In
this way, a semantic network representation of the image A captures both
the objects and the relationship between the objects. We can do exactly
the same thing for the image B. The objects and the relationships
between them, y is above x. Now that we have represented our knowledge
of image A and our knowledge of image B we want to capture somehow the
knowledge of the transformation from A to B because recall, A is to B as
C is to D. So we want to capture the relationship between A and B. The
transformation from A to B. To do that, to capture the transformation
from A to B, we’ll start building links between the objects in A and the
objects in B. Now, for x and y they are straightforward for z, but there
is no z in b. So we’ll have a dummy node here in b and we will see how
we can label the link here so that we can capture the idea that z
doesn’t occur in B. So we might say that x is unchanged because x the
circle here is the same as the circle here. Y on the other hand has
expanded. It was a small diamond here and it’s a much bigger diamond
there. Z, the black dot, has disappeared all together, so, we have,
let’s say, it’s deleted, it’s not there at B at all. I hope you can see
from this example how we constructed a semantic network for the
relationship between the images A and B. There were three parts to it.
The first part dealt with the objects in A and the object in B. The
second dealt with the relationships between the objects in A and the
relationship with the objects in B. The third party dealt with the
relationships between the objects in A and the relationships between the
objects in B. In principle, we can construct semantic networks for much
more complicated images, not just A and B. Here is another example of a
semantic network for another set of images. Once again, we have the
objects and the relationships. And then the relationship between the
objects in the first image and that in the second image.


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
