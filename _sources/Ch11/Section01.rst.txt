.. =====================
.. Chapter 11: Classification
.. =====================


Section 01: Preview
:::::::::::::::::::

  *Science is the systematic classification of experience.
  -- George Henry Lewes*


.. youtube:: CnWO-VrzdLI
	:height: 315
	:width: 560
	:align: left

|Preview| 
|Preview 1| 
Today we’ll talk about one of the most ubiquitous problems in AI called
classification. Classification is mapping sets of percepts in the world
into equals classes, so that we can take actions in the world in an
efficient manner. We could learn this concept through incremental
concept learning. We’ll talk about the nature of these equivalence
classes and how they can be organized into a hierarchy of concepts.
We’ll talk about different kinds of concepts, like axiomatic concepts
and prototypical concepts. Given a classification hierarchy, we’ll talk
about multiple processes for doing the classification, including both
bottom-up and top-down processes.

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
