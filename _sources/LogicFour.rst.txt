Section 16: Exercise: Truth Tables II
::::::::::::::::::::::::::::::::::::::::

.. youtube:: M0FhGwTp7Rk
        :height: 315
        :width: 560
        :align: left

.. image:: ../_static/LogicImages/Slide16.PNG
        :height: 200px
        :width: 350px
        :alt: Exercise Truth Tables II
        :align: center

.. codelens:: Truth_Tables_II

	a = True; b = True; c = False;
	exp1 = a or (b and not c)

	a = False; b = True; c = False;
	exp1 = a or (b and not c)

	a = False; b = True; c = True;
	exp1 = a or (b and not c)
	
David, what did you come up with? From the beginning, we start with A or something. So as long as A is true, then we know the result is true. We don’t even care about the rest of it. When A is false, then we need to look at B and the not C. Because this is an and, we need both B and not C to both be true. So, when B is false, we can go ahead and say this is false over here. And when not C is false, we can go ahead and say this is false over here. Not C is false, if C is true, so this is also false. So, our only other answer that’s true is that row right there. So, as you can see, this can become very complicated very quickly. But David did get the answer to the truth value of this particular sentence, based on the truth values of the predicates that are inside the sentences. So in principle now, we can see how we can compute the truth value of very, very complicated sentences returning logic.

Section 17: Exercise: Commutative Property
:::::::::::::::::::::::::::::::::::::::::::::

.. youtube:: JqYx2yvmJwU
        :height: 315
        :width: 560
        :align: left

.. image:: ../_static/LogicImages/Slide17.PNG
        :height: 200px
        :width: 350px
        :alt: Exercise Commutative Property
        :align: center

The construction of these truth tables, allows us to illustrate certain important properties of logical predicates. To see those properties, let us do an exercise together. So here we have the predicate A, and the predicate B. And here we have A and B, and B and A. Please fill these boxes, the truth values of A and B, the truth values of B and A.

Section 18: Exercise: Commutative Property
:::::::::::::::::::::::::::::::::::::::::::::

.. youtube:: Ms9Xj61JWMM
        :height: 315
        :width: 560
        :align: left

.. image:: ../_static/LogicImages/Slide18.PNG
        :height: 200px
        :width: 350px
        :alt: Exercise Commutative Property 2
        :align: center

That’s good, David. And as you know, this property is called the commutative property. The commutative property says that the truth value for A and B is the same as the truth value for B and A. So whenever I have A and B, and can re-write it as B and A.

Section 19: Exercise: Distributive Property
::::::::::::::::::::::::::::::::::::::::::::::

.. youtube:: Ir8OoFj9qsw
        :height: 315
        :width: 560
        :align: left

.. image:: ../_static/LogicImages/Slide19.PNG
	:height: 200px
        :width: 350px
        :alt: Exercise Distributive Property
        :align: center

Let us try a slightly more complicated exercise. This time, we have three variables, A, B, and C. And here are the combinations of the truth values of A, B, and C. Here on the right are two formulas. The first one says, A and parenthesis B or C parenthesis closed. The second says parenthesis A and B parenthesis closed or parenthesis A and C parenthesis closed. Please write down the truth values for these two formulas.

.. codelens:: Distributive_Property
	
	a = True; b = False; c = True;
	exp1 = a and (b or c)
	exp2 = (a and b) or (a and b)

	a = False; b = True; c = True;
	exp1 = a and (b or c)
	exp2 = (a and b) or (a and b)

Section 20: Exercise: Distributive Property
::::::::::::::::::::::::::::::::::::::::::::::

.. youtube:: rvVHGZQTUIg
        :height: 315
        :width: 560
        :align: left

.. image:: ../_static/LogicImages/Slide20.PNG
        :height: 200px
        :width: 350px
        :alt: Exercise Distributive Property 2
        :align: center

Did you write down the truth values for these two formulas, David? I did. And on the one on the left, we find it’s little bit easier because it starts with A and, which means anytime A is false, we can go ahead and write that this is false. When A is true, that means we can ignore it and evaluate solely based on B or C. Whenever either of them is true, the result is true. And only when both of them are false, is the result false. So the one on the right is a little bit more complicated because for each of them we need to look at both A and B and A and C. But because there’s an or in the middle, that means that once we discover that one of them is true, we don’t need to really worry about the other one. A and B is true whenever both A and B are true, and so A and B are true here and here, meaning we can go ahead and say that those are true. We don’t need to look at A and C here. Similarly, A and C are true here. So we can go ahead and say that this one is true as well. For all the ones at the bottom, A is false which means it’s going to go ahead and render both of them false. And for the fourth one, B and C are both false, meaning each individually is going to become false. So what we see here is that the truth values for these two formulas actually end up the same, so I guess they’re equivalent as well. Good, David. So this property’s called the distributive property. The distributive property says that these two formulas have the same truth values. And in particular, if there is B and C inside the parentheses with a disjunction between them, and A is outside the parentheses with a conjunction between them, then we can move A inside the parentheses by first writing A and B and then writing A and C and taking the disjunction of the two. We can also think of this as distributing the part outside of both the predicate and the operator into both the ones on the inside. We take the A and apply it to B, so A and B. We take the A and apply it to C, so A and C. And we preserve the operator in between B and C in between the two new parenthesis. So if this had been A or B or C, this would become A or B, or B or C. This would become A and B and C and would be all the operators here.


