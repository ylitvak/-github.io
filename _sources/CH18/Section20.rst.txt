Section 20: Evaluation and Storage in Analogical Reasoning
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

.. youtube:: dDAqivFNyDU
        :height: 315
        :width: 560
        :align: left

.. image:: ../../_static/Ch18/Slide20-01.png
        :height: 200px
        :width: 350px
        :alt: Class Goals


.. image:: ../../_static/Ch18/Slide20-02.png
        :height: 200px
        :width: 350px
        :alt: Class Goals


.. image:: ../../_static/Ch18/Slide20-03.png
        :height: 200px
        :width: 350px
        :alt: Class Goals


Let us briefly talk about evaluation in storage. These evaluation and storage steps in analogical reasoning are very similar to the evaluation and storage steps in case based reasoning. Analogical reasoning by itself does not provide guarantees of correctness. So the solution that it proposes must be evaluated by some manner. For the down correlation problem, for example, we may evaluate the proposed solution by do- ing a simulation. Once the evaluation has been done, then the new problem and a solution can be encapsulated as a new case and stored back in memory for later potential reuse. To return to the down correlation problem, as an example. Once we have the solution of decomposing the laser beam into several smaller beams and sending them to a tumor at the same time from different directions, we can do a simulation of this solution and see whether they are successful. If it is, then we can encapsulate the target problem and the proposed solution as a case, and store it in memory. It might be useful later. It could potentially become a source case for a new target problem to come later. Once again, in this way, the AI agent learns incrementally. Each time it solves a problem, the new problem and its solution becomes a case for later reuse.