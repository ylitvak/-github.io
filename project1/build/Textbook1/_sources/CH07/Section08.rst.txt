Section 08: Properties of Frames
:::::::::::::::::::::::::::::::::::::::::::::::::
.. youtube:: jNiNP3e4L3o
        :height: 315
        :width: 560
        :align: left

.. image:: ../../_static/Ch07/Slide08-01.png
        :height: 200px
        :width: 350px
        :alt: Class Goals
        :align: center

.. image:: ../../_static/Ch07/Slide08-02.png
        :height: 200px
        :width: 350px
        :alt: Class Goals
        :align: center

.. image:: ../../_static/Ch07/Slide08-03.png
        :height: 200px
        :width: 350px
        :alt: Class Goals
        :align: center

.. image:: ../../_static/Ch07/Slide08-04.png
        :height: 200px
        :width: 350px
        :alt: Class Goals
        :align: center

.. image:: ../../_static/Ch07/Slide08-05.png
        :height: 200px
        :width: 350px
        :alt: Class Goals
        :align: center

.. image:: ../../_static/Ch07/Slide08-06.png
        :height: 200px
        :width: 350px
        :alt: Class Goals
        :align: center

There are three cardinal properties of frames. The first property is that frames represents stereotypes. Now we all know about stereotypes. We deal with stereotypes all the time. Here’s a stereotype for the world eat or ate. And this particular stereotype, the slots are dealing with our stereotypical, my stereotypical notion of what happens when something is eaten. There is a subject and it is a frog. There is a location. There is a time. You may have a different set of stereotypes. In fact, stereotypes often are very culture specific. Second, frames provide default values. So not only do they have these slots which come from other notions of a stereotype of this particular word, but many of these slots may have values already filled in. As an example, I may already have a default value which says that after the object has been eaten, it is no longer alive. It is inside the subject’s stomach, and the subject’s mood is now happy. There are our default values. Of course, when you have default, you can also have exceptions to them. As an example, it may be that when Ashok ate a frog, it made him sad because frogs don’t suit him very well. Now the exception handling is both very powerful and a problem. It is powerful because I can have stereotypes or default values, and when needed, I can override the default values. But it’s also a problem, because you can see what will happen. The more in- stances that I have, the more times where I’ll be overriding some default value. And then I have to go to worry about how to manage all of this exceptional handling. Nevertheless, frames provide a very nice way of capturing both de- fault values and exception handling. The third cardinal property of frames is that they exhibit inheritance. So I can organize this frames in a frame hierarchy. Here is a frame for an animal, and then, that has two subclasses, a frame for an ant and a frame for a human. Note, I’m us- ing the language of classes and subclasses here. Now inheritance works, in that I may have some slot for the class animal, and then, I may specify for the ant more specific values for some of those slots. For example, number of legs is six or the number of arms is zero. But, the important thing is that I inherited these slots from the super-class. Of course, when I specify the sub- classes, when I go down this frame hierarchy, I may keep on adding additional slots. So for a human man, we may also add the job and the name. There’s classes then we have instances, as an example, Ashok is the name of the person and the job is a professor. And so, this instance is also inheriting all these slots and the slot values from the class. We can also see that when the frames provide default values, that’s very similar to a constructor when we’re dealing with object oriented programming that supplies some initial values when an object is first instantiated. So it seems like there’s actually a very rich connection between classes and frames here. David, that’s a very good point. In fact, there is a history to it. Frames and object-oriented programming came about the same time, the 1960s and the 1970s. And I’m sure they influenced each other in both directions.