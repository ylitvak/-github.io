Section 07: Exercise Block Problem I
::::::::::::::::::::::::::::::::::::::::::
.. youtube:: wTSvB34VZuQ
        :height: 315
        :width: 560
        :align: left

.. image:: ../../_static/Ch05/Slide07-01.png
        :height: 200px
        :width: 350px
        :alt: Class Goals
        :align: center

.. image:: ../../_static/Ch05/Slide07-02.png
        :height: 200px
        :width: 350px
        :alt: Class Goals
        :align: center


Exercise 5.7
   
Fill in the blank
   
.. fillintheblank:: Ex57

    .. blank:: blank571
        :correct: \\b(d|D)\\b
        :feedback1: (".*", "Try again")

        Fill in the blanks to make the following sentence: A on

    .. blank:: blank573
        :correct: \\b(c|C)\\b
        :feedback1: (".*", "Try again")

        B on
        
    .. blank:: blank574
        :correct: \\b(Table|TABLE|table)\\b
        :feedback1: (".*", "Try again")

        C on
        
    .. blank:: blank575
        :correct: \\b(b|B)\\b
        :feedback1: (".*", "Try again")

        D on  
        
        
.. fillintheblank:: Ex58

    .. blank:: blank581
        :correct: \\b(Table|TABLE|table)\\b
        :feedback1: (".*", "Try again")

        Fill in the blanks to make the following sentence: "A on"

    .. blank:: blank583
        :correct: \\b(c|C)\\b
        :feedback1: (".*", "Try again")

        "B on"
        
    .. blank:: blank584
        :correct: \\b(Table|TABLE|table)\\b
        :feedback1: (".*", "Try again")

        "C on"
        
    .. blank:: blank585
        :correct: \\b(a|A)\\b
        :feedback1: (".*", "Try again")

        "D on"  


.. fillintheblank:: Ex59

    .. blank:: blank591
        :correct: \\b(Table|TABLE|table)\\b
        :feedback1: (".*", "Try again")

        Fill in the blanks to make the following sentence: "A on"

    .. blank:: blank593
        :correct: \\b(c|C)\\b
        :feedback1: (".*", "Try again")

        "B on"
        
    .. blank:: blank594
        :correct: \\b(Table|TABLE|table)\\b
        :feedback1: (".*", "Try again")

        "C on"
        
    .. blank:: blank595
        :correct: \\b(Table|TABLE|table)\\b
        :feedback1: (".*", "Try again")

        "D on"  


To understand more deeply the properties of means and analysis, let us look at another, slightly more complicated example. In this example, there are four blocks instead of the three in the previous example. A, B, C, D. In the initial state, the blocks are arranged as shown here. The goal state is shown here on the right. The four blocks are arranged in a particular order. Now if you compare the configuration of blocks on the left with the configuration of blocks on the right, in the goal state, you can see there are three differences. First, A is on Table, where A is on B here. B is on C. That’s not a difference. C is on table. C is on D here, D’s on B, D’s on table here. So there are three differences. So, this is a heuristic measure of the difference between the initial state and the goal state. Once again, we’ll assume that the AI agent can move only one block at a time. Given the specification of the problem, what states are possible from the initial state? Please write down your answers in these boxes.