Section 02: Guards and Prisoners
:::::::::::::::::::::::::::::::::

.. youtube:: dGUO-zTQtcA
        :height: 315
        :width: 560
        :align: center

Knowledge-based AI is a collection of three things. Knowledge representations, problem solving techniques and architectures. We have already look at one knowledge representation, semantic networks. We have not so far looked at problem solving methods or architectures. To- day, I'd like to start by talking about the problem solving method. Let us illustrate the problem solving method of generate and test with the same examples that we have discussed earlier. When we were discussing this example in the case of semantic networks, we simply came up with various states and pruned some of them without saying about how an AI agent would know what states to prune. So imagine that we have a generator that takes the initial state and from that initial or current state, generates all the possible successive states. For now, imagine it's not a very smart generator, it's a dumb generator. So it generates all the possible states. So the generator test method not only has a generator but also has a tester. The tester looks at all the possible states the generator has generated and removes some of them. For now, let's also assume that the tester is is dumb as well. And so the tester is removes only those states that are are clearly illegal based on the specific of the problem. Namely, that one cannot have more prisoners than guards on either back. So the first and the third states are removed by the tester.        