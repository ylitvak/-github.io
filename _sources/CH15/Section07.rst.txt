Section 07: Exercise Roles Primitive Actions
::::::::::::::::::::::::::::::::::::::::::::::::::
.. youtube:: e4I4OGHtuZs
        :height: 315
        :width: 560
        :align: left

.. image:: ../../_static/Ch15/Slide07.png
        :height: 200px
        :width: 350px
        :alt: Class Goals
        :align: center

Let’s do an exercise together. Here is a sentence. John took the book from Mary. For this sentence, first write down the primitive action that best captures the meaning of the sentence. And then write down the fillers for each of the slots of this primitive action.

.. fillintheblank:: Ch15S8

    .. blank:: blank15S8A
        :correct: \\b(move-possession|Move-possession)\\b
        :feedback1: (".*", "Try again")

        Primitive:

    .. blank:: blank15S8B
        :correct: \\b(John|john)\\b
        :feedback1: (".*", "Try again")

        agent:
        
    .. blank:: blank15S8C
        :correct: \\b(cart|Cart)\\b
        :feedback1: (".*", "Try again")

        coagent:
        
    .. blank:: blank15S8D
        :correct: \\b(book|Book)\\b
        :feedback1: (".*", "Try again")

        object:  
