Section 31: A More Complex Proof
:::::::::::::::::::::::::::::::::::

.. youtube:: 5cLJPqvlK0g
        :height: 315
        :width: 560
        :align: left

.. image:: ../_static/LogicImages/Slide31-01.PNG
        :height: 200px
        :width: 350px
        :alt: A More Complex Proof 1
        :align: center

.. image:: ../_static/LogicImages/Slide31-02.PNG
        :height: 200px
        :width: 350px
        :alt: A More Complex Proof 2
        :align: center

.. image:: ../_static/LogicImages/Slide31-03.PNG
        :height: 200px
        :width: 350px
        :alt: A More Complex Proof 3
        :align: center

.. image:: ../_static/LogicImages/Slide31-04.PNG
        :height: 200px
        :width: 350px
        :alt: A More Complex Proof 4
        :align: center

.. image:: ../_static/LogicImages/Slide31-05.PNG
        :height: 200px
        :width: 350px
        :alt: A More Complex Proof 5
        :align: center

.. image:: ../_static/LogicImages/Slide31-06.PNG
        :height: 200px
        :width: 350px
        :alt: A More Complex Proof 6
        :align: center

.. image:: ../_static/LogicImages/Slide31-07.PNG
        :height: 200px
        :width: 350px
        :alt: A More Complex Proof 7
        :align: center

.. image:: ../_static/LogicImages/Slide31-08.PNG
        :height: 200px
        :width: 350px
        :alt: A More Complex Proof 8
        :align: center

.. image:: ../_static/LogicImages/Slide31-09.PNG
        :height: 200px
        :width: 350px
        :alt: A More Complex Proof 9
        :align: center

.. image:: ../_static/LogicImages/Slide31-10.PNG
        :height: 200px
        :width: 350px
        :alt: A More Complex Proof 10
        :align: center

Let us make this example a little bit more complicated. Complicated enough that it cannot be proven simply by applying one instance of modus ponens. Imagine that a robot proved to itself that this box is not liftable. And the humans in the factory who were trying to make fun of the robots said to the robot well, the reason it’s not liftable is not because it’s not movable, but because your battery is not working. So now the situation is more complicated, the robot must also check its battery. So now the robot begins with slightly different knowledge in this knowledge case. So suppose that the knowledge in its knowledge basis, cannot move and battery full means it’s not liftable. It finds from its concept. Again, it cannot move, so it checks its battery, and it checks its battery and it finds that the battery’s full. So then two new sentences that get written in the knowledge base. By the knowledge base contains three sentences. As earlier, the resolutions you’re improving, the agent must convert all these sentences, in its knowledge base into a conjunctive normal form. That means that the sentences can contain a literal or a disjunctional literal or a conjunction of disjunctional literals. So if we begin by removing the implication from sentence one, because an implication cannot occur in a conjunctive normal form. So when we remove implication from the first sentence we get this sentence. Where the sentence is not yet satisfactory, it is not yet a conjunctive normal form because this is a disjunction of conjunctions. And what we want are conjunctions of disjunctions. So we apply the deMorgan’s Law and now we get the following sentence. We’re simply taking the negation inside which flips the conjunction into a disjunction and now we have three liftables connected with disjunctions and this is a conjunctive normal form, disjunctional liftable. So now we have in the knowledge base, three sentences, all three of them in the conductor normal form, either literals or disjunctional literals. Recall that the robot wanted to prove not liftable. So it takes the negation of that, this is again proof by refutation, so it considers liftable. So now this knowledge base has four sentences. These four sentences coming from the negation of what it wants to prove. Once again the reasoning begins by the literal that it wants to prove, in this case liftable. It finds a sentence in which the negation of literal is true. So once again, we begin with the sentence, S4 because that is what we want to prove. And we find a sentence in the knowledge base which contains a literal which is a negation of the literal in this sentence S4 that we want to prove. We resolve on this because they both cannot be true, and resolution here simply means that we drop them. Now, in the sentence S1 that is under consideration currently, we have two literals. We can begin with either one of them. Let us begin with not battery full. We’ll try to find

a sentence which contains a negation of this particle electrode. There is a sentence, S3, which is a negation of this so we resolve on this. Battery full and not battery full because they both cannot be true. We’ll drop them. Now in sentence S1 we are left with just one literal, can-move. We can try to find a sentence in the knowledge base which contains a negational judge literal. Here it is, and so we can resolve on them. And we resolve on them, we drop them. And once we drop them, then we have a null condition, which stands for a contradiction. So we reached a contradiction, therefore the assumption that this was liftable cannot be true, therefore not liftable is true, and we have just shown that resolution theorem proving in this case proves what the robot wanted to prove. One important point to note here is the issue of focus of attention. Often when the problem space is very complex, for example, when the number of sentences is really large, the sentences are very complex, it can become really hard for the logical agent to decide what to focus on. But because we have converted everything in a conjunctive normal form, and because resolution theorem proving is making use of resolution, therefore at any particular time, the logical agent knows exactly what to focus on. You always begin with this literal, you always try to find a sentence which contains this negation. You always resolve on that. You take the remaining literal in the sentence and proceed forward. This focus of attention, this computational efficiency of resolution theorem proving is arising because a [of what are called] called horn clauses. A horn clause, is a disjunction that contains at most one positive literal. This is happening in S1. This is a disjunction that contains at most one positive recall. This is a negative recall, this is a negative recall, and the fact that it contains just one positive recall, is a very powerful idea because that’s where the focus of attention comes from.

Section 32: Exercise: Proof I
:::::::::::::::::::::::::::::::::

.. youtube:: mzZLJBRVO4o
        :height: 315
        :width: 560
        :align: left

.. image:: ../_static/LogicImages/Slide32.PNG
        :height: 200px
        :width: 350px
        :alt: Exercise Proof I
        :align: center

Let us do an exercise together to make sure that we get rich solutions for improving. So consider this sentence if an animal has wings and does not have fur, it is a bird. Write this sentence down in formal logic. You can use the predicates, has-wings, has-fur, and bird.

Section 33: Exercise: Proof I
:::::::::::::::::::::::::::::::::

.. youtube:: NjDE4znrTaY
        :height: 315
        :width: 560
        :align: left

.. image:: ../_static/LogicImages/Slide33.PNG
        :height: 200px
        :width: 350px
        :alt: Exercise Proof I
        :align: center

David, what did you write? So starting at the beginning, has wings becomes the predicate has wings. We’re doing a conjunction so and, does not have fur, so not has fur, those two things imply that it’s a bird. That’s good, David. Now, let us put this in a form, in a conjunctive normal form that we can use in resolution theorem proving.

Section 34: Exercise: Proof II
::::::::::::::::::::::::::::::::::

.. youtube:: hhaeBmvhHrQ
        :height: 315
        :width: 560
        :align: left

.. image:: ../_static/LogicImages/Slide34.PNG
        :height: 200px
        :width: 350px
        :alt: Exercise Proof II
        :align: center

So since an indication cannot occur in a conducted normal form, we must eliminate the implication. So please eliminate the implication from this sentence, and rewrite it in this box.

Section 35: Exercise: Proof II
::::::::::::::::::::::::::::::::::

.. youtube:: RZnZaXTGZ98
        :height: 315
        :width: 560
        :align: left

.. image:: ../_static/LogicImages/Slide35.PNG
        :height: 200px
        :width: 350px
        :alt: Exercise Proof II
        :align: center

What did you get David? So this is a little bit more complicated. We know that from our earlier formula if a implies b, then to rewrite it with implicational elimination we write, not a or b. So or b is pretty straightforward, or bird. We take the not of the conjunction over here and say not has wings and not has fur. Now some of you may have jumped straight to writing this in full conjunctive normal form, but now we’re going to move on and do that last step.


