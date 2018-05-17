Section 06: Visuospatial Reasoning: Another Example
:::::::::::::::::::::::::::::::::::::::::::::::::::


.. youtube:: RLm2qIArsVc
	:height: 315
	:width: 560
	:align: left


|Visuospatial Reasoning Another Example| 

We just saw an example where visual spatial knowledge by itself,
suffices too in our logical reasoning under certain conditions. Now let
us look at a different problem. There suddenly are situations where we
might want AI agents to be able to extract [propositional]
presentations. Your projects one, two, and three did exactly that. One
task, where AI agent might want build proper [propositional]
representations out of regional spatial knowledge is when an AI is given
a design drawing. So here is a vector graphics drawing of a simple
engineering system. Perhaps some of you can recognize what is happening
here. This is a cylinder and this a piston. This is the rod of the
piston. The piston moves. Left and right. The other end of the rod is
connected to a crankshaft. As this piston moves left and right, this
particular crankshaft starts moving anticlockwise. This device
translates linear motion into rotational motion. I just gave you a
causal account. Although because [propositional] only implicit in this
[propositional] spatial knowledge. You and I were able to extract a
causal account out of this. How did we do it? How can we help AI agents
do it? At present if you were to make a CAD drawing using any CAD tool
that you want, the machine does not understand the drawing. But can
machines of tomorrow understand drawings by automatically building these
causal models out of them? Put it another way. There is a story that has
been captured in this particular diagram. Can a machine automatically
extract the story from this diagram? In 2007, Patrick Yaner built an AI
program called Archytas. Archytas was able to extract causal models out
of vector graphics drawings of the kind that I just showed you. This
figure is coming from paper and Archytas and hence the form of the
figure. We’ll have a pointer to the paper in the notes. This is how
Archytas works. It began with a library of source drawings. These were
drawings that we already knew about. For each drawing order it knew
about it already had done the segmentation. The basic shapes for example
might be things like circles and the composite shapes which were then
labeled like piston and cylinder. Then a behavioral model or a causal
model which said what happens when the piston moves in and out, namely
the crankshaft turns. And then a functional specification we’ve said
this particular system can work in linear motion into rotational motion.
So there was a lot of knowledge with each previous drawing that Archytas
already had seen. All of this knowledge was put into a library. When a
new drawing was input into Archytas then it generated line segments and
arcs and intersections from it. And then, it started mapping them to the
lines and segments and arcs of previously known drawings. Retrieve the
drawing that was the closest match in drawing to the new drawing. And
then started transferring basic shapes, and then composite shapes, and
it transferred each element through this abstraction hierarchy all the
way up to the functional level. As an example, if Archytas library
contains piston and crankshaft drawings like this along with causal
functional models for them, then given a new drawing of a piston and
crankshaft device Archytas will then be able to assemble a causal
functional model for the new drawing. Thus Archytas extracted causal
information from which spatial presentations to analogical reasoning.

.. |Visuospatial Reasoning Introduction| image:: ../../_static/AdvancedTopics/Slide02-01.PNG
.. |Visuospatial Reasoning Introduction 1| image:: ../../_static/AdvancedTopics/Slide02-02.PNG
.. |Visuospatial Reasoning Introduction 2| image:: ../../_static/AdvancedTopics/Slide02-03.PNG
.. |Visuospatial Reasoning Introduction 3| image:: ../../_static/AdvancedTopics/Slide02-04.PNG
.. |Two Views of Reasoning| image:: ../../_static/AdvancedTopics/Slide03-01.PNG
.. |Two Views of Reasoning 1| image:: ../../_static/AdvancedTopics/Slide03-02.PNG
.. |Two Views of Reasoning 2| image:: ../../_static/AdvancedTopics/Slide03-03.PNG
.. |Two Views of Reasoning 3| image:: ../../_static/AdvancedTopics/Slide03-04.PNG
.. |Visuospatial Reasoning An Example| image:: ../../_static/AdvancedTopics/Slide05.PNG
.. |Visuospatial Reasoning Another Example| image:: ../../_static/AdvancedTopics/Slide06.PNG
.. |Ravens Progressive Matrices| image:: ../../_static/AdvancedTopics/Slide07-01.PNG
.. |Ravens Progressive Matrices 1| image:: ../../_static/AdvancedTopics/Slide07-02.PNG
.. |Systems Thinking Introduction| image:: ../../_static/AdvancedTopics/Slide08-01.PNG
.. |Systems Thinking Introduction 1| image:: ../../_static/AdvancedTopics/Slide08-02.PNG
.. |Systems Thinking Connections| image:: ../../_static/AdvancedTopics/Slide09-01.PNG
.. |Systems Thinking Connections 1| image:: ../../_static/AdvancedTopics/Slide09-02.PNG
.. |Structure-Behavior-Function| image:: ../../_static/AdvancedTopics/Slide10-01.PNG
.. |Structure-Behavior-Function 1| image:: ../../_static/AdvancedTopics/Slide10-02.PNG
.. |Structure-Behavior-Function 2| image:: ../../_static/AdvancedTopics/Slide10-03.PNG
.. |Design Introduction| image:: ../../_static/AdvancedTopics/Slide11-01.PNG
.. |Design Introduction 1| image:: ../../_static/AdvancedTopics/Slide11-02.PNG
.. |Design Introduction 2| image:: ../../_static/AdvancedTopics/Slide11-03.PNG
.. |Agents Doing Design| image:: ../../_static/AdvancedTopics/Slide12-01.PNG
.. |Agents Doing Design 1| image:: ../../_static/AdvancedTopics/Slide12-02.PNG
.. |Creativity Introduction| image:: ../../_static/AdvancedTopics/Slide13-01.PNG
.. |Creativity Introduction 1| image:: ../../_static/AdvancedTopics/Slide13-02.PNG
.. |Creativity Introduction 2| image:: ../../_static/AdvancedTopics/Slide13-03.PNG
.. |Exercise Defining Creativity I| image:: ../../_static/AdvancedTopics/Slide14-01.PNG
.. |Exercise Defining Creativity I 1| image:: ../../_static/AdvancedTopics/Slide14-02.PNG
.. |Exercise Defining Creativity I 2| image:: ../../_static/AdvancedTopics/Slide15.PNG
.. |Defining Creativity II| image:: ../../_static/AdvancedTopics/Slide16.PNG
.. |Exercise Defining Creativity III| image:: ../../_static/AdvancedTopics/Slide17.PNG
.. |Exercise Defining Creativity III 1| image:: ../../_static/AdvancedTopics/Slide18.PNG
.. |Exercise Defining Creativity IV| image:: ../../_static/AdvancedTopics/Slide19.PNG
.. |Exercise Defining Creativity IV 1| image:: ../../_static/AdvancedTopics/Slide20.PNG
.. |AI Ethics| image:: ../../_static/AdvancedTopics/Slide21.PNG
.. |Open Issues| image:: ../../_static/AdvancedTopics/Slide22.PNG
.. |Final Quiz| image:: ../../_static/AdvancedTopics/Slide23.PNG
