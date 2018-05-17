Section 05: Exercise Inferences About Foos
:::::::::::::::::::::::::::::::::::::::::::::

.. youtube:: pmyc-sZI0Qw
        :height: 315
        :width: 560
        :align: left

.. image:: ../_static/LogicImages/Slide05.PNG
	:height: 200px
	:width: 350px
	:alt: Exercise Inferences About Foos
	:align: center

What do you think, David? So, from the bottom, we have the brick has to support two blocks. Not necessarily two bricks. We know that those can be any kind of block. We also have that those two blocks cannot touch. So, that condition is important. And we also have that those two blocks must then support a brick. And when we learned earlier, it’s not sufficient for that to be any kind of block. The block on top has to be a brick as well. So, if these three conditions. Are as efficient to find a Foo in terms of logic. That is good David. So what we are learning here is given conceptual knowledge how can we translate it into the language of logic?

Section 06: Predicates
:::::::::::::::::::::::::

.. youtube:: YM39KJ088-c
        :height: 315
        :width: 560
        :align: left

.. image:: ../_static/LogicImages/Slide06.PNG
	:height: 200px
	:width: 350px
	:alt: Predicates
	:align: center

Recall that we said that a lot of this AI agent will have two parts to it, a knowledge base and then the rules of inference. We’ll come to the rules of inference a little bit later. First let us look at how can we construct a knowledge base in the language of logic. So what we are trying to do now is that an AI agent has some knowledge about the world and it is going to express it in the scheme of logic. In earlier schemes of knowledge representation, we discussed how there were objects and relationships between objects. And any knowledge representation scheme we need to capture both objects and relationships between those objects. Logic has a particular way of doing it. So consider an object like a bird. This object may have various arguments. We’ll define something called a predicate, which is a function that maps object arguments to either true or false. So let us consider an example. Here we have bluebird as the object and feathers as the predicate on this object. Let’s consider this example. Here, bluebird is the object and feathers is the predicate on this object. Feathers is now a function that can map either into true or into false. Either bluebird has feathers or bluebird doesn’t have feathers. In this particular case, feathers of bluebirds would be true, because bluebirds do have feathers. Now, just like we had bluebird as the object in the previous example, here we have animal as the object, the same predicate. Now, of course, not all animals will have feathers, so this particular predicate may be true or false, depending on the choice of the animal. In this sentence there are two predicates, one object, animal still, but there is a predicate feathers and a predicate bird. And we can capture the relationship between these two predicates, by saying that if feathers animal is true, then bird animal is also true. This example has two predicates. Here there’s one object, the animal. But the predicates are feathers and birds. And the sentence is capturing a relationship between the two predicates. If the animal has feathers, then the animal is a bird. In logic we call sentences like this as having an implication. This is an implicative relationship. So in logic, we’ll read this as Feathers(animal) implies Bird(animal). Or if the animal has feathers, then it implies that the animal is a bird.

Section 07: Conjunctions and Disjunctions
::::::::::::::::::::::::::::::::::::::::::::

.. youtube:: kG9LYOWoOJI
        :height: 315
        :width: 560
        :align: left

.. image:: ../_static/LogicImages/Slide07-01.PNG
	:height: 200px
	:width: 350px
	:alt: Conjunctions and Disjunctions-01
	:align: center

.. image:: ../_static/LogicImages/Slide07-02.PNG
	:height: 200px
	:width: 350px
	:alt: Conjunctions and Disjunctions-02
	:align: center

.. image:: ../_static/LogicImages/Slide07-03.PNG
        :height: 200px
        :width: 350px
        :alt: Conjunctions and Disjunctions-03
        :align: center

Now, consider another sentence that we have come across earlier. If an animal lays eggs, and it flies, then it is a bird. How do we write this in the language of logic, given that there is conjunction here. So this time, we can have two predicates again. There is a predicate of lays-eggs, coming from here. The predicate of flies, coming from here. And we can denote a conjunction between them. Which in the language of logic is often put in this form. Now we can re-write this sentence in the following form. If the animals lays eggs and the animal flies, then the animal is a bird. Remember again, this semi colon here, really is denoting implication for now. Remember again, that in logic, this really stands for an implication. Consider the slightly different sentence. Suppose if the sentence was if an animal lays eggs or it flies it is a bird. In that case, again, we’ll have two predicates, but this time we’ll have a disjunction between them. And the sentence would become or if animal lays eggs or animal flies, then the animal is a bird. And again, this is an implication. Let us continue with the our exercise in which we are learning how to write sentencable language of logic. It is under the sentence, if an animal flies and is not a bird. So, it is a negation here, then it is a bat. How do we write that in logic? So I’m still interested in writing the antecedent of this particular sentence, and I may be able to say that animal flies is a conjunction here, because it is an and here, and we have this negation symbol for this predicate, bird. Now we can write a complete sentence by saying that the animal flies, conjunction. Animal is not a bird, implies animal is a bat.

Section 08: Implies
:::::::::::::::::::::::

.. youtube:: Wp0zUlDcW4Y
        :height: 315
        :width: 560
        :align: left

.. image:: ../_static/LogicImages/Slide08.PNG
	:height: 200px
	:width: 350px
	:alt: Implies
	:align: center

Now, I have talking a little about implication. Let’s see how do we actually write, implication and logic. So here is a sentence, if animal lays eggs and animal flies, it is implication is that the animal is a bird. In logic we write this using the symbol, arrow symbol, or an indication, so if the animal lays eggs and animal flies, implication animal is a bird. So here is the left hand side of the implication, here is the left hand side of the implication. The left hand side of the implication, implies the right hand side.

Section 09: Notation Equivalency
:::::::::::::::::::::::::::::::::::

.. youtube:: 66MCL2rY0FQ
        :height: 315
        :width: 560
        :align: left

.. image:: ../_static/LogicImages/Slide09.PNG
        :height: 200px
        :width: 350px
        :alt: Notation Equivalency
        :align: center

Generally speaking, you won’t have these symbols on your keyboard. You can find them in your character map and you are welcome to use them if you’d like to. But for the exercises in the rest of this lesson and in the next lesson, feel free to use the symbols given over here. These are the symbols for AND, NOT, OR and Equals that come from Java or Python. So, feel free these when you are doing the exercises that you’ll come across in the rest of this lesson.

Section 10: Exercise: Practicing Formal Logic
::::::::::::::::::::::::::::::::::::::::::::::::

.. youtube:: gd1KvoJveqA
        :height: 315
        :width: 560
        :align: left

.. image:: ../_static/LogicImages/Slide10.PNG
        :height: 200px
        :width: 350px
        :alt: Exercise Practicing Formal Logic
        :align: center

So remember we are still trying to learn how to build a knowledge based on the language of logic. To put it all together, consider four exercises. Here is the sentence. Please put it in the language of logic. Similarly for this sentence, this sentence, this sentence.

.. .. fillintheblank:: fill1412

..	If an animal has feathers or has talons, it is a bird. 

.. .. blank:: blank52532
	:correct: \\bFeathers(animal) V Talons(animal) => Bird(animal)\\b
	:feedback1: (".*", "Feathers(animal) V Talons(animal) => Bird(animal)")

	


