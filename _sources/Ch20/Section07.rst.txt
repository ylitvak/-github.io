Section 07: From Pixels to 3D
::::::::::::::::::::::::::::::

.. youtube:: NIoy8ecK9d0
	:height: 315
	:width: 560
	:align: left

|From Pixels to 3D| 
|From Pixels to 3D 1| 
|From Pixels to 3D 2| 
Let us look at the details of constraint propagation. To do so, we’ll
take a specific example from computer vision. Here’s an example of a 2D
image composed of a large number of pixels. The greyness at any one
pixel is a depiction of the intensity of light at that pixel. Now of
course, you and can immediately recognize that this is a cube. But how
do we do it, and how can we make a machine do it? [Miles] decompose a
task of 3D object recognition into several several sub-tasks. Miles said
in the first sub-task, a visual system detects edges, or lines as shown
here. At this particular point, no surfaces have been detected. In this
particular point, no 3D object has been fignized. Just these pixels have
been put into lines based on the intensities of light in different
pixels. According to Miles the second sub task of object recognition
consists of grouping these lines and the surfaces with orientations, as
indicated here. So now these four lines have been grouped into the
surface, and then orientation defined by the perpendicular the surface,
and similarly these four lines, and these four lines. In the third and
final phase of the object recognition task, according to Miles surfaces
are grouped into a complete 3D object. At this particular point, your
visual system recognizes that this is a cube. Miles theory has been very
influential in computer vision. It has actually also been influential in
AI as a whole. One of the lessons we can take away from Miles’ theory of
computer vision of object’s recognition is that before we get into our
guarded tones for addressing the task, we want to understand how a task
gets decomposed into sub tasks. Throughout this course, we have
emphasized task decomposition repeatedly. As an example, when we were
talking about understanding, a big task of understanding got decomposed
into a series of small tasks. Where surface level cues acted as probes
into memory and a frame was retrieved. The slice of the frames dented
expectations. Lexicon and grammatical analysts led to the identification
of objects and predicates that would satisfy those expectations. And the
fillers were put in. Problem reduction certainly is a general purpose
method for decomposing complex tasks into smaller tasks. This notion of
class decomposition is a powerful idea irrespective of what algorithm we
use for any of these specific sub tasks

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
