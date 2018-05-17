Section 22: Exercise Partial Order Planning II
::::::::::::::::::::::::::::::::::::::::::::::

.. youtube:: uPeEfd6CZe8
        :height: 315
        :width: 560
        :align: left

Now that we humans find addressing problems like this almost trivial, we know what to do here. Put D on the table, put B on the table, and so on. And then put C on top of D and so on. The question is, how can we write an AI program that can do it? And, by writing an AI program, how can we make things so precise that that will provide insight into human intelligence. To do this, let us start writing the operators that are available in this particular work. There are only two operators. I can either move block x to block y, which is the first operator here. Or I can move block x to the table. Note two things. First, instead of saying block A and block B, we have variabalized them, move block x to block y, where x could be A, B, C or D, and similary for block y. And this is just a more concised notation. Second, that in order to move block x to block y, both x and y must be clear. That is neither x nor y should have any of the block on top of them. Given this setup, please write down the specification of the first operator as well as the second operator.

