Section 12: Agents Doing Design
:::::::::::::::::::::::::::::::



.. youtube:: nbMxw9A6Ilo
	:height: 315
	:width: 560
	:align: left


|Agents Doing Design| 
|Agents Doing Design 1| 

As we have mentioned earlier, configuration is a kind of design, a kind
of routine design. And one material configuration is bound refinement.
In configuration, all the components of the design are already known,
but we are to find some arrangement with the components, and we assign
values to some of the variables of those components, to arrive at the
arrangement. Here is a design specification working it’s way. Here might
be a plan for designing a chair as a whole. And once we assign values to
some of the variables at the level of the chair, then we can refine the
plan for the chair into a plan for the chair legs, the chair seat, and
so on. All of this might be subject to some constraints. There are in
fact a number of AI systems, that do configuration design. Many of them
are being used in industry. Some of these AI systems use, matters like
brand refinement the way we are showing it here. Others use case based
reasoning. And various systems use a variety of methods, for doing
configuration design, including model based reasoning and rule based
reasoning. What about more creative kinds of design? Design in which not
all the parts are known in advance. Since we just discussed the
flashlight example, in the context of systems thinking, let us revisit
that example in the context of creative design. So this is a schematic
of the flashlight circuit. Here is the switch, the battery, the bulb, as
earlier. On the systems thinking, we discussed how structured behavior
function models capture the knowledge that when the switch is closed,
electricity flows from the battery to the bulb, and the bulb converts
the electrical energy into light energy. Let us suppose that this
particular electrical circuit use a 1.5 volt battery and created 10
lumens of light. Tomorrow someone comes to you and says, I want 20
lumens of light. Design a flashlight electrical circuit for me. How will
you do that? You might go to the structure, behavior function model for
this particular circuit and do some thinking. You may recognize, the
amount of light created in the bulb is directly proportional to the
voltage of the battery. Instead of creating 10 lumens of light you need
20 lumens of light, you might say, I’m going to use a 3 volt battery. So
far, so good. You’ve done system thinking in the context of design
thinking. But now let us add a wrinkle. Suppose that a 3.0 volt battery
is not available. At this point, a teacher tells you it’s okay if a 3.0
volt battery is not available. You can connect two 1.5 volt batteries in
series. Two 1.5 volt batteries connected in series will give you the
voltage of three volts. Accepting the teacher’s advice, you can now
create an electrical circuit that will use two 1.5 volt batteries in
series and create light of 20 lumens. But you’re not just creating this
particular design, you also learned something from it. Every design,
every experience is an opportunity for learning. In the 1990s, Sam
[propositional] here at Georgia Tech created a program called IDOL, IDOL
did creative design. In particular, IDOL would learn about design
patterns. >From simple design cases, the kind we just talked about. I’m
sure most of you are familiar with the notion of design pattern, design
patterns are a major construction software engineering. But design
patterns are not just in software engineering but in all kinds of
design, for example architecture and engineering and so on. There is
some way of capturing the design pattern that can be learned from the
previous case. A field of design of a device that changes the valuable
variable from one value to another value. And you want another design
that changes the value the same variable to some other value not the
same as the previous design. One way you in which you can create the new
design is. By replicating the behavior of the previous design. So not
just having behavior be one for the first design, but having this
behavior be one as many times as needed. Let us connect this to the
example we just saw. If you have a design of an electrical circuit that
can create 10 lumens of light, and you know how to do it through some
behavior B1. I need to design an electrical circuit that can create 20
lumens of light, but you don’t know the behavior of B2. Then this
behavior B2 is a replication of behavior B1 by connecting components and
series. Once Sam’s program IDOL had learned about this design pattern of
cascading, of replication, then, when it was given the problem of
designing a water pump of higher capacity than the one available. It
could create a new water pump by connecting several water pumps in
series. Thus, ideal, created new designs in one domain, the domain of
water pump, through analogical transfer of design patterns learned under
the domain, the domain of electrical circuits. You would form the
perspective of the new domain of water pumps initially did not know
about all the components about all the water pumps that will be needed.
With Sam’s program, IDOL is creative enough to know that the pattern of
problems here in the water pump is exactly the same pattern that was
also occurring in the domain of electrical circuits. Sam’s theory
provides a computational account of not only how design patterns can be
used, but also about how these design patterns can be learned and
transferred to new domains. There is of course a lot more to design. We
said earlier that design thinking engages problem solution, core
evolution. It’s not just that a solution evolves but the problem remains
fixed. But the problem evolves even as the solution evolves. It’s not
quite clear how humans do this kind of creative design, with this
problem solution co evolution. There is certainly a few AI systems
capable of problem solution coevolution at present

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
