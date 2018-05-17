Section 02: Exercise The Block Problem
::::::::::::::::::::::::::::::::::::::::
.. youtube:: 9oBEadUpUSo 
        :height: 315
        :width: 560
        :align: left

.. image:: ../../_static/Ch05/Slide02-01.png
        :height: 200px
        :width: 350px
        :alt: Class Goals
        :align: center

.. image:: ../../_static/Ch05/Slide02-02.png
        :height: 200px
        :width: 350px
        :alt: Class Goals
        :align: center
        
Exercise 5.2
   
.. dragndrop:: Ex52
   :feedback: Incorrect. Try Again!
   :match_1: Move(A, B)|||Move(C, Table)
   :match_2: Move(B, C)|||Move(B, C)
   :match_3: Move(C, Table)|||Move(A, B)

   Drag the operators on the left in the correct order that will move the blocks into the goal state.

        

To understand a method of means and analysis. Let us look at this blocks word problem. This is a very famous problem in AI. It has occurred again and again. And almost every text- book in AI has this problem. You’re given a table on which there are three blocks. And A is on table, B is on table, and C is on A. This is the initial state. And you want to move these blocks, to the gold state. On this configuration, so that C is on table, B is on C and A is on B. The problem looks very simple listen, doesn’t it? Let’s introduce a couple of constraints. You may move only one block at a time, so you can’t pick both A and B together. And second, you may only move a block that has nothing on top of it. So, you cannot move block A in this configuration, because it has C on top of it. Let us also suppose that we’re given some operators in this world. These operators essentially move some object to some location. For example, we could move C to the table, or C onto B, or C onto A. Not all the operators may be applicable in the current state. C is already on A, but in principle, all these, all of these operators are available. Given these operators, and this initial state and this goal state, write a sequence of operations that will move the blocks from the initial state to the goal state.