Section 15: Actions and Resultant Actions
::::::::::::::::::::::::::::::::::::::::::::::::::
.. youtube:: twpOAnyOCJg
        :height: 315
        :width: 560
        :align: left

.. image:: ../../_static/Ch15/Slide15.png
        :height: 200px
        :width: 350px
        :alt: Class Goals
        :align: center


Earlier we had problems that will deal with sentences which have two verbs in it. So here are two verbs, told and throw. Maria told Ben to throw the ball. How may an AI agent make sense of this particular sentence? So once again, the processing starts on the left. Maria is not a verb, so let’s put in a concept list and for the time being ignore it. The processing goes to the second word which is told, which is a verb. And so the primitive action calls when the told is pulled out. The primitive action is speak, and so now we can start putting the fillers for the various slots. So the agent is Maria and the result is now we go to the second one. Here the primitive action is propel because we have a throw here. And the propulsion is being done by Ben and the object is ball and now we relate these two. This second frame is a result of the first frame’s action. So, if we go back to the previous sentence, Ashok enjoyed eating a frog. We can see how we can represent both verbs there in terms of action frames. So, Ashok enjoyed. That might be the frame here. The primitive action is feel. The agent is Ashok. Ashok ate a frog, that’s the primitive action of ingest, agent is Ashok, and the object that got eaten was a frog. And the result of that is this frame where Ashok had a feeling of enjoyment. Note that some problems still remain. It is too difficult to figure out exactly how represent a sentence like Ashok enjoyed eating a frog. It can be two representations with that particular sentence and see that those are two action frames or one action frame and one state of change frame. Some of these questions will get answered when we stop thinking in terms of stories that are only one sentence long, but stories that have a number of sentences. Stories based on a discourse. Because some of these ambiguities will get resolved when we know more about what happened when Ashok enjoyed eating the frog. What came before it, or what came after it.