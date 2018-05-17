Section 11: Tracks
::::::::::::::::::

.. youtube:: 8j-7Vo93pdc
	:height: 315
	:width: 560
	:align: left

|Tracks| 
Now, another part of the script was the track. And we really haven’t
talked a lot about track so far. So let’s talk a little bit more about
it. So here are four tracks with the restaurant script. That really
[events occur] to going to restaurant, four kinds. Here’s a coffeehouse,
fast food, casual dining, formal dining. You could add more if you
wanted to. Now in restaurants of all kinds, some even so common. You
have to go to a restaurant, you have to order some food. You eat that
food. You pay the bill. And then you leave. That is common to all of
them which is why all of them are part of the restaurant script. On the
other hand what happens in a Coffeehouse is quite different from what
happens in Formal Dining, which is quite different from what happens in
a Fast Food restaurant. So you may have specific cracks that correspond
to Coffeehouses and Fast Foods and so on. In effect, we are building a
semantic hierarchy or script. Here is a script for going to a
restaurant. Here is a script for going to a coffeehouse, going to fast
food. And this can be tracks in the overall script. Of course, we can
build a semantic hierarchy of something higher than this. We could think
about going to, for social events and [events occur] going to this
restaurant becomes part of going to a social event of various kind. Okay
now that we know something about the [events occur] representation
called script, the next question becomes how many AI agent actually use
these scripts? So imagine an AI agent that is hungry has some money and
decides to do something about it. So it may go into its long term memory
and find out the script that will be most useful for the current
situation. This really becomes a classification problem. In long term
memory a large number of scripts, and the agent is trying to classify
the current situation into one of those scripts. Let us suppose the
agent picks a restaurant script, and decides to execute it. As it enters
the restaurant, the scene it observes in the restaurant matches the
conditions of a fast food script. So it decides to invoke the fast food
script. This way the robot may walk down the semantic hierarchy, first
in working the restaurant script, then working the fast food script, and
so on. Now a robot could have taken a different stance. A robot could
have decided to do planning. Given some initial conditions, and cold
conditions, a robot may have used the operative that is available to it,
to generate a plan at one time. While the script is doing it, it is
giving it a plan in a compiled form. The robot doesn’t have to generate
this plan at runtime. It is already available in memory in a pre stored
form. This is very useful because one of the central conundrums that we
have been talking about is, how is it possible that AI agents can’t
address computationally complex problems with limited resources in near
real time? In a complex dynamic world, planning can take a lot of time.
But if I already have the store plans, then in working the script and
executing it is much faster.

.. |Preview| image:: ../../_static/Scripts/Slide01-01.PNG
.. |Preview 1| image:: ../../_static/Scripts/Slide01-02.PNG
.. |Exercise A Simple Conversation| image:: ../../_static/Scripts/Slide02.PNG
.. |Exercise A Simple Conversation 1| image:: ../../_static/Scripts/Slide03.PNG
.. |Story Understanding for AI Agents| image:: ../../_static/Scripts/Slide04.PNG
.. |Definition of Scripts| image:: ../../_static/Scripts/Slide06.PNG
.. |Parts of a Script| image:: ../../_static/Scripts/Slide07.PNG
.. |Constructing a Script| image:: ../../_static/Scripts/Slide08-01.PNG
.. |Constructing a Script 1| image:: ../../_static/Scripts/Slide08-02.PNG
.. |Constructing a Script 2| image:: ../../_static/Scripts/Slide08-03.PNG
.. |Form vs Content| image:: ../../_static/Scripts/Slide09-01.PNG
.. |Form vs Content 1| image:: ../../_static/Scripts/Slide09-02.PNG
.. |Using a Script to Generate Expectations| image:: ../../_static/Scripts/Slide10.PNG
.. |Tracks| image:: ../../_static/Scripts/Slide11.PNG
.. |Exercise Learning a Script| image:: ../../_static/Scripts/Slide12.PNG
.. |Exercise Learning a Script 1| image:: ../../_static/Scripts/Slide13.PNG
.. |Exercise Using a Script| image:: ../../_static/Scripts/Slide14.PNG
.. |Exercise Using a Script 1| image:: ../../_static/Scripts/Slide15.PNG
.. |Assignment Scripts| image:: ../../_static/Scripts/Slide16.PNG
.. |Wrap Up| image:: ../../_static/Scripts/Slide17.PNG
