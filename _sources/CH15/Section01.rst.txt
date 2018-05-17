.. ====================================
.. Chapter 15: Common Sense Reasoning
.. ====================================

.. image:: ../../_static/Ch15/Slide00.png
        :height: 200px
        :width: 350px
        :alt: Intro Sphere
        :align: center

*Believe nothing, no matter where you read it or who has said it, not even if I have said it, unless it agrees with your own reason and your own common sense.*
 
*– Buddha.*

*Common sense is not so common.*
 
*– Voltaire.*

*Inferences of Science and Common Sense differ from those of deductive logic and mathematics in a very important respect, namely, when the premises are true and the reasoning correct, the conclusion is only probable.*
 
*– Bertrand Russell.*



Section 01: Preview
:::::::::::::::::::::::
.. youtube:: rmby_NOApI4
        :height: 315
        :width: 560
        :align: left

.. image:: ../../_static/Ch15/Slide01-01.png
        :height: 200px
        :width: 350px
        :alt: Preview
        :align: center

.. image:: ../../_static/Ch15/Slide01-02.png
        :height: 200px
        :width: 350px
        :alt: Preview
        :align: center

Today we’ll talk about common sense reasoning. You and I, as cognitive individuals, are very good at common sense reasoning. We can make natural, obvious inferences about the world. How can we help AI agents make similar common sensical inferences about the world? Suppose I had a robot, and I asked a robot, find the weather outside. I don’t want the robot to jump out of the window to see whether it’s raining outside but, why should the robot not jump out of the window? What tells it that it’s not a very common sensical thing to do? We’ll talk about common sense reasoning using a frame representation. We’ll start talking about certain small set of primitive actions. There are only 14 of them, but they bring a lot of power because they organize a lot of knowledge. These primitive actions can be organized into hierarchies of sub actions. These actions can result in changes in the state. This is important, because that is what allows the robot to infer that if I were to take this action, that result might occur. That state might be achieved. So then it decides not to jump out of the window, because it might get hurt.