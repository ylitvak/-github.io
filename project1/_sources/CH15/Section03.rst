Section 03: Primitive Actions
::::::::::::::::::::::::::::::::::::::::
.. youtube:: gXU4RC6w-Mo
        :height: 315
        :width: 560
        :align: left

.. image:: ../../_static/Ch15/Slide03-01.png
        :height: 200px
        :width: 350px
        :alt: Class Goals
        :align: center


.. image:: ../../_static/Ch15/Slide03-02.png
        :height: 200px
        :width: 350px
        :alt: Class Goals
        :align: center


David, that’s a good point. One way of capturing the meaning of that story in terms of these primitive actions is in, to use the move object primitive action. So, here about the object be- ing moved and the mover of the object is the same, I. So, I am moving myself one place to an- other place. And the nearest point here is that these primitive actions will be able to capture the meaning of some sentences in a very simple, logical, intuitive sense. And for some other sentences, it might be a little bit more involved. So let us see how this primitive actions may actually help an AI agent make sense of stories. So here is the first thing we can do. Recall there were large number of stories, each expressed by one sentence. Ashok ate a frog, Ashok devoured a frog and so on. So now, ate, devoured, consumed, ingest, partook. We can think that each one of them really is an instance of a primitive action called ingest. Here’s the primitive action Ingest. So Ashok ingested a frog here, Ashok ingested a frog here, Ashok ingested a frog here. Well, superficially these particular sentences are different. In terms of their deep meaning, the deep meaning is pretty much the same. But it’s true of course that the world may have a slightly differ- ent interpretation than dining. The [verb] might be something that I ravish with my hands for example, and dining might involve fine dining with silverware. nevertheless, ingest captures the basic meaning of these sentences. What is the basic meaning? The basic meaning again is that Ashok is an agent. Frog is the object that is getting eaten, ingested. Initially the frog was outside Ashok’s body, and probably dead or alive. We don’t know its state. After the ingestion has occurred, a devoured has occurred, a consumed has occurred, the frog is inside Ashok’s body, and it’s dead. And further, that Ashok probably is happy at the end of this particular ingestion. And where is all of that knowledge coming from? It’s buried inside the frame for ingest. So each of these primitive actions has a frame corresponding to it. And we have come across frame many times already in the class, so by now you should know what it means. And the frame has a large number of slots like agent, co-agent, object, beneficiary and so on, and those slots deal with still a difficult situations and have default values already put in there. So when a sentence comes like, Ashok ate a frog, then the verb ate here, pulls out the primitive action ingest, and the frame for this primitive action and the processing becomes top down, and they start thinking, where will Ashok go? Where will frog go? Who is the agent? Who is the object? And so on.