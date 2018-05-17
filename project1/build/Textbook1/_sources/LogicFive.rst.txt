Section 21: Exercise: Associative Property
:::::::::::::::::::::::::::::::::::::::::::::

.. youtube:: cLYLpeilAVI
        :height: 315
        :width: 560
        :align: left

.. image:: ../_static/LogicImages/Slide21.PNG
        :height: 200px
        :width: 350px
        :alt: Exercise Associative Property
        :align: center

Let us do one of their exercising in two tables illustrate one of the property of logical predicate. Again here are three predicates, and here are two formulas. It should be a simple exercise. Please write down the truth values, of the two formulas, in these boxes.

Section 22: Exercise: Associative Property
:::::::::::::::::::::::::::::::::::::::::::::

.. youtube:: 01fnPPGO1bc
        :height: 315
        :width: 560
        :align: left

.. image:: ../_static/LogicImages/Slide22.PNG
        :height: 200px
        :width: 350px
        :alt: Exercise Associative Property 2
        :align: center

What did you get, David? So like before, because this is an or, as soon as we see that A is true, we can go ahead and write down true for all of these. When A is false, we just need to evaluate B or C. When B is true, we know it’s already true. And then if B is false we need to look at C. If C is true, then it’s still true, and if C is false, then all three are false and that’s the only time it’s false. Over here, we’ve moved the parentheses but really, we’re not changing what we do. We can think of it as stating at the bottom with C being true. Anytime C is true, the entire thing is true. So C is true here, here, here, and here. If that evaluates to false, we need to look at A or B, and so on. So we end up doing the exact same process. That’s good, David. And this property is called the associative property. The associative property simply says that we can change the location of the parentheses here, A or parentheses B or C, parenthesis close, has the same value as A or B parenthesis close or C. So that we can change the location of the parentheses. The same would have been true if these were both conjunctions. So if it was A conjunction parentheses B conjunction C or A conjunction B, conjunction C, it would have had the same values. The difference between these formulas and the ones we were doing before are the values of these operators. Associative property works when it’s both ors or both ands. Distributive property worked when there was a mixture of operators.

.. codelens:: assocProp
	
	a = True; b = True; c = True;
	
	assocExp1 = a or (b or c)
	assocExp2 = (a or b) or c

	a = True; b = False; c = False;

	assocExp1 = a or (b or c)
	assocExp2 = (a or b) or c

	a = False; b = False; c = False;

	assocExp1 = a or (b or c)
	assocExp2 = (a or b) or c

	a = False; b = False; c = True;
	
	assocExp1 = a or (b or c)
	assocExp2 = (a or b) or c

Section 23: Exercise: de Morgan's Law
::::::::::::::::::::::::::::::::::::::::

.. youtube:: ozqoSVWQZ5w
        :height: 315
        :width: 560
        :align: left

.. image:: ../_static/LogicImages/Slide23.PNG
        :height: 200px
        :width: 350px
        :alt: Exercise de Morgan's Law
        :align: center

One other property of logical predicates that we will see very soon in action is called de Morgan’s law. So this time there are two predicates A and B. Here are their truth values. And here are two formulas. Remember this is a negation. Please write down the truth values of these two formulas in these boxes.

.. codelens:: deMorgans_Example_1

	a = True; b = True;
	
	deMorgExp1 = not(a and b)
	deMorgExp2 = not a or not b

	a = True; b = False;
	deMorgExp1 = not(a and b)
	deMorgExp2 = not a or not b

	a = False; b = True;
	deMorgExp1 = not(a and b)
	deMorgExp2 = not a or not b

	a = False; b = False;
	deMorgExp1 = not(a and b)
	deMorgExp2 = not a or not b
 
Section 24: Exercise: de Morgan's Law
::::::::::::::::::::::::::::::::::::::::

.. youtube:: CYJKuDSQo_Q
        :height: 315
        :width: 560
        :align: left

.. image:: ../_static/LogicImages/Slide24.PNG
        :height: 200px
        :width: 350px
        :alt: Exercise de Morgan's Law 2
        :align: center

That’s good David. So the de Morgan’s law is saying that when we try to distribute negation over the predicate inside the parentheses that are connected with a conjunction, then the conjunction becomes a disjunction between the negations of the pre, predicates. The same would have been true if we had a disjunction here. When we distribute the negation, it would have become a conjunction here. David, before we go ahead further, let’s remember why we are trying to do all of this. So do you recall we said in the beginning of the lesson that a logical agent will have a knowledge base, and then formal rules of inference that will apply on these sentences as knowledge base. The knowledge base itself may be coming from many places. Some sentences in the knowledge base may be boot strapped into the logical agent. Other sentences may be coming from perception. Now when we’re trying to apply these rules of inferences to the synthesis of the knowledge base it is sometimes very useful to rewrite the sentences in different forms. And that’s what we are trying to do. These properties will allow us to rewrite the sentences in such a way that we can in fact apply the rules of inferences that we will see in a minute.

Section 25: Truth of Implications
::::::::::::::::::::::::::::::::::::

.. youtube:: DfuSV65BXVs
        :height: 315
        :width: 560
        :align: left

.. image:: ../_static/LogicImages/Slide25.PNG
        :height: 200px
        :width: 350px
        :alt: Truth of Implications
        :align: center

So it can be a little bit weird to talk about the truth value of an implication sentence. What we’re really saying here is, whether or not this implication actually holds true. So let’s take three different implications to see this. First let’s think of the implication, feathers implies bird. All birds have feathers and only birds have feathers. So, we know that if an animal has feathers, then it is a bird. That’s true. On the other hand, let’s take the implication, if scales then bird. Lots of animals with scales aren’t birds and in fact no animals with scales are birds. So the implication, scales implies birds. Would be False. For our third example, let’s take the implication, flight implies bird. If we have a penguin, flight is False. But the penguin is still a bird. So, flight can be false and bird can still be true, meaning the implication can still be true here. On the other hand, if we have a cat, flight if False. And bird is False. So, the implication can still be true. So in this case, if flight was false, we can’t actually make a determination on whether or not the animal is a bird.

.. codelens:: Implication_Equivalent

	a = True; b = False
	aImpliesb = not a or b

	a = False; b = False
	aImpliesb = not a or b

