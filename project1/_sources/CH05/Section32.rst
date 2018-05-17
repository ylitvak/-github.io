Section 32: Summary and Exercise
::::::::::::::::::::::::::::::::::::::::::::::::::::

This lesson cover the following topics:
    1. The knowledge representation of Semantic networks works well with Generate and Test, Means-Ends Analysis and Problem Reduction. These are examples of Universal AI methods.
    2. Means-ends analysis uses a heuristic to guide the search from the initial state to the goal state. Convergence is not guaranteed. Optimality is not guaranteed. Computational efficiency is not guaranteed.
    3. Problem reduction is used along with Means-ends analysis to help overcome problems with means-ends analysis.
    4. The Universal methods have weak coupling between the methods and the knowledge representation and hence are called Weak methods since they make little use of knowledge. Strong AI methods are knowledge-intensive and use knowledge of the world to come up with good solutions in an efficient manner.

References
:::::::::::

    1. Winston P., Artificial Intelligence, Chapter 3.

Optional Reading
:::::::::::::::::

    `1. Winston Chapter 3, pp. 50-60; <http://courses.csail.mit.edu/6.034f/ai3/ch3.pdf>`_
    
Exercises
:::::::::::

Exercise 1:
The workers installed a new wall-to-wall carpet in your bedroom and left. Later you discover that the bedroom door will not close unless you trim off about 1/8 inch off the carpet at the bottom of the door. Construct a difference-operator table relating simple instruments such as a saw, a plane, and a file. Now show how the method of mean-ends analysis would use the difference-operator table to address the carpet problem in your bedroom.

Exercise 2:
In the Monkey & Bananas problem, a monkey is faced with the problem of reaching bananas hanging from the ceiling. But a box is available that will enable the monkey to reach the bananas if he climbs on it. Initially the monkey is at location A, bananas at B, and the box at C. The bananas are at height Y, the monkey and the box have height X such that if the monkey climbs on the box, it too will be at height Y.
Invent operators Walk, Push, Climb, and Grasp, for walking to a location, pushing the box to a location, climbing up on the box, and grasping bananas, respectively. Show the preconditions and postconditions of each operator.

Write down the initial and final states in propositional form.
Show how the monkey may used means-ends analysis to form a plan to get the bananas in the above problem.