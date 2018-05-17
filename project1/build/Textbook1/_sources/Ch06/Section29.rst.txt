Section 29: Conclusions and Monkeys and Bananas
:::::::::::::::::::::::::::::::::::::::::::::::

.. youtube:: HDXfrkoB8tk
	:height: 315
	:width: 560
	:align: left



This lesson covers the fundamentals of Production Systems which are
similar to Expert Systems and based on rules known to domain experts.
Production Systems helps map percepts in the world into actions. When
the production system reaches an impasse, it uses chunking to learn a
new rule to overcome that impasse.

Source: 1. Winston P., Artificial Intelligence,Chapter 7, Pages 119-137.
http://courses.csail.mit.edu/6.034f/ai3/rest.pdf.

Exercise 1:

In the classical Monkey & Bananas problem, a monkey is faced with the
problem of reaching bananas hanging from the ceiling. But a box is
available that will enable the monkey to reach the bananas if he climbs
on it. Initially the monkey is at location A, bananas at B, and the box
at C. The bananas are at height Y, the monkey and the box have height X
such that if the monkey climbs on the box, it too will be at height Y.

R1: If My-location = Bananas-location AND My-height = Bananas-height,
Then Grasp Bananas

R2: If NOT (My-location = Bananas-location) AND My-height =
Bananas-height, Then Walk to Bananas-location

R3: If My-location = Box-location AND Box-location = Bananas-location
AND My-height < Bananas-height,Then Climb Box to Bananas-height

R4: If My-location = Box-location AND NOT (Box-location =
Bananas-location) AND My-height < Bananas-height,Then Push Box to
Bananas-location

.. reveal:: revealcbrreading1
    :showtitle: Show Code Example
    :hidetitle: Hide Code Example

    .. activecode:: Production Systems

        My = {'height':0, 'location':'A'}

        Bananas = {'height':1, 'location':'B'}

        Box = {'height':0, 'location':'C'}

        def grasp_bananas():
            print "Bananas grasped"

        def walk_to(walker, destination):
            print "Walked to {}".format(str(destination))
            walker['location'] = destination

        def climb_box(climber, destination):
            print "Climbed to {}".format(str(destination))
            climber['height'] = destination

        def push_box(box, destination):
            print "Pushed box to {}".format(str(destination))
            box['location'] = destination
        
        def productions():
            if My['location'] == Bananas['location'] and My['height'] == Bananas['height']:
                grasp_bananas()
                return False
            if My['location'] != Bananas['location'] and My['height'] == Bananas['height']:
                walk_to(My, Bananas['location'])
            if My['location'] == Box['location'] and Box['location'] == Bananas['location'] and My['height'] < Bananas['height']:
                climb_box(My, Bananas['height'])
            if My['location'] == Box['location'] and Box['location'] != Bananas['location'] and My['height'] < Bananas['height']:
                push_box(Box, Bananas['location'])
            if My['location'] != Box['location'] and My['height'] < Bananas['height']:
                walk_to(My, Box['location'])
            return True

        while productions():
            pass
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        


.. |Preview| image:: ../../_static/ProductionSystems/Slide01-01.PNG
.. |Preview 1| image:: ../../_static/ProductionSystems/Slide01-02.PNG
.. |Exercise A Pitcher| image:: ../../_static/ProductionSystems/Slide02-01.PNG
.. |Exercise A Pitcher 1| image:: ../../_static/ProductionSystems/Slide02-02.PNG
.. |Exercise A Pitcher 2| image:: ../../_static/ProductionSystems/Slide03.PNG
.. |Function of a Cognitive Architecture| image:: ../../_static/ProductionSystems/Slide04.PNG
.. |Levels of Cognitive Architectures| image:: ../../_static/ProductionSystems/Slide05-01.PNG
.. |Exercise Levels of Architectures| image:: ../../_static/ProductionSystems/Slide06.PNG
.. |Exercise Levels of Architectures 1| image:: ../../_static/ProductionSystems/Slide07.PNG
.. |Assumptions of Cognitive Architectures| image:: ../../_static/ProductionSystems/Slide08.PNG
.. |Architecture Content Behavior| image:: ../../_static/ProductionSystems/Slide09-01.PNG
.. |Architecture Content Behavior 1| image:: ../../_static/ProductionSystems/Slide09-02.PNG
.. |A Cognitive Architecture for Production Systems| image:: ../../_static/ProductionSystems/Slide10-01.PNG
.. |A Cognitive Architecture for Production Systems 1| image:: ../../_static/ProductionSystems/Slide10-02.PNG
.. |Return to the Pitcher| image:: ../../_static/ProductionSystems/Slide11-01.PNG
.. |Return to the Pitcher 1| image:: ../../_static/ProductionSystems/Slide11-02.PNG
.. |Return to the Pitcher 2| image:: ../../_static/ProductionSystems/Slide11-03.PNG
.. |Action Selection| image:: ../../_static/ProductionSystems/Slide12-01.PNG
.. |Action Selection 1| image:: ../../_static/ProductionSystems/Slide12-02.PNG
.. |Putting Content in the Architecture| image:: ../../_static/ProductionSystems/Slide13.PNG
.. |Bringing in Memory| image:: ../../_static/ProductionSystems/Slide14-01.PNG
.. |Bringing in Memory 1| image:: ../../_static/ProductionSystems/Slide14-02.PNG
.. |Exercise Production System in Action I| image:: ../../_static/ProductionSystems/Slide15.PNG
.. |Exercise Production System in Action I 1| image:: ../../_static/ProductionSystems/Slide16.PNG
.. |Exercise Production System in Action II| image:: ../../_static/ProductionSystems/Slide17.PNG
.. |Exercise Production System in Action II 1| image:: ../../_static/ProductionSystems/Slide18.PNG
.. |Exercise System in Action III| image:: ../../_static/ProductionSystems/Slide19.PNG
.. |Exercise System in Action III 1| image:: ../../_static/ProductionSystems/Slide20.PNG
.. |Chunking| image:: ../../_static/ProductionSystems/Slide21.PNG
.. |Exercise Chunking| image:: ../../_static/ProductionSystems/Slide22.PNG
.. |Exercise Chunking 1| image:: ../../_static/ProductionSystems/Slide23.PNG
.. |Assignment Production Systems| image:: ../../_static/ProductionSystems/Slide25.PNG
.. |Wrap Up| image:: ../../_static/ProductionSystems/Slide26.PNG
.. |The Cognitive Connection| image:: ../../_static/ProductionSystems/Slide27-01.PNG
.. |The Cognitive Connection 1| image:: ../../_static/ProductionSystems/Slide27-02.PNG
.. |The Cognitive Connection 2| image:: ../../_static/ProductionSystems/Slide27-03.PNG
