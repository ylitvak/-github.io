Section 08: Incremental Concept Learning
::::::::::::::::::::::::::::::::::::::::

.. youtube:: Ni-BnwKUicg
        :height: 315
        :width: 560
        :align: left

Here is the basic algorithm for incremental concept learning and David has created a visual illustration of this algorithm. We're given an example and we're also told whether it's a positive example or a negative example. If this is a positive example, then the algorithm comes to the left branch of this particular tree. And it asks does the current definition of the concept cover this positive example? We want to cover positive examples. If it already covers the positive example, we don't have to do anything. We don't have to devise a current definition of the concept. On the other hand, if the current definition of the concept does not cover the positive example then we must revise it in some way so that it does, so we will generalize it. On the other half of the tree, if this example is not a positive instance of the example, then we can ask ourselves does the current definition of the concept cover it? If it doesn't cover it, it shouldn't cover it. And if it doesn't cover it, then we don't have to do anything. On the other hand, if the example is a negative instance and if current definition does cover it, then we want to define our current definition to rule it out. So we'll specialize in a current definition. So, oftentimes, we see children committing overgeneralization or overspecialization. So, to take an example of this, we can imagine a child that has a concept of a cat, but the cat has to be black. The child has only ever been around black cats, so part of their definition, part of their concept of the cat is that cats are black. When she goes over to her friend's house, Is introduced to her friend's cat, and her friend's cat is orange. Right now, she's told that this is an example of a cat, but it does not fit her current definition of a cat so she needs to generalize her definition that cats can be different colors. Similarly, we can imagine another child that has only ever been exposed to dogs. Thus the child's concept of a dog is that a dog is anything that is furry, has four legs and that we keep as a pet. This child goes over to the same friend's house and is introduced to this orange cat. And right now, that orange cat fits his definition of a dog. It's furry, it has four legs, and they keep it as a pet. But he's told that this cat is not a dog. So he needs to specialize his concept of a dog to exclude this cat. That's good, David. It connects things with our everyday lives.

.. reveal:: revealcbrreading1
    :showtitle: Show Reading
    :hidetitle: Hide Reading

    .. raw:: html

        <center>
        <iframe height=600px width=800px src=../_static/readings/IncrementalConceptLearning/Winston_Ch16_p349-358.pdf>
        </iframe>
        </center>
        
or download :download:`here <../_static/readings/IncrementalConceptLearning/Winston_Ch16_p349-358.pdf>`
