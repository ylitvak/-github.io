Section 26: Choosing Matches by Weights
:::::::::::::::::::::::::::::::::::::::


.. youtube:: ykLlqKW0nck
	:height: 315
	:width: 560
	:align: left


|Choosing Matches by Weights| 
|Choosing Matches by Weights 1| 

So let us look at the semantic network representation of the
relationship between A and B. In one view of the transformation from A
to B, we can think of q, the outer circle, as remaining unchanged, and p
the inner circle, as getting deleted. Let’s look at another view of the
transformation from A to B. In this view, we can think of p as getting
expanded and q, the outer circle, as getting deleted. Both of these
views are valid views. If both of these views are valid, then how would
anyone decide? How would an AI agent decide which view to select? Let us
suppose that the AI agent had a metric by which it could decide upon the
ease of transformation from A to B. Let us suppose that, that metric
assigned different weights to different kind of transformations. You
will notice that these transformations like scaling, rotation,
reflection make for a fine transformations. In this scale, a larger
value like 5 points, means more ease of transformation and greater
similarity. A lower value means less ease of transformation and more
difficult transformation and less similarity. Given the scale, let us
calculate the weight of transformations for both transformation #1, and
transformation #2. In transformation #1, you can see that p is getting
deleted, which we gave a weight of 1. And q remains unchanged, which we
gave a weight of 5. So the total weight here is 6. In case of
transformation #2, the weight of p being expanded, we said will be 2,
scaled. And, q getting deleted is 1, so the total weight is 3. If you
prefer the first transformation over the second transformation, then we
can see why someone will answer the square is the correct answer, and
not the triangle. Let us return to this exercise. And now we can see why
both 3 and 5 are legitimate answers. We can also see why an AI agent may
prefer 5, given the similarity metric that we talked about in the last
shot.

.. |Preview| image:: ../../_static/SemanticNetworks/Slide01-01.PNG
.. |Preview 1| image:: ../../_static/SemanticNetworks/Slide01-02.PNG
.. |Representations| image:: ../../_static/SemanticNetworks/Slide02.PNG
.. |Introduction to Semantic Networks| image:: ../../_static/SemanticNetworks/Slide03-01.PNG
.. |Introduction to Semantic Networks 1| image:: ../../_static/SemanticNetworks/Slide03-02.PNG
.. |Introduction to Semantic Networks 2| image:: ../../_static/SemanticNetworks/Slide03-03.PNG
.. |Exercise Constructing Semantic Nets I| image:: ../../_static/SemanticNetworks/Slide04.PNG
.. |Exercise Constructing Semantic Nets I 1| image:: ../../_static/SemanticNetworks/Slide05.PNG
.. |Exercise Constructing Semantic Nets II| image:: ../../_static/SemanticNetworks/Slide06.PNG
.. |Exercise Constructing Semantic Nets II 1| image:: ../../_static/SemanticNetworks/Slide07.PNG
.. |Structure of Semantic Networks| image:: ../../_static/SemanticNetworks/Slide08.PNG
.. |Characteristics of Good Representations| image:: ../../_static/SemanticNetworks/Slide09.PNG
.. |Discussion Good Representations| image:: ../../_static/SemanticNetworks/Slide10.PNG
.. |Discussion Good Representations 1| image:: ../../_static/SemanticNetworks/Slide11.PNG
.. |Guards and Prisoners| image:: ../../_static/SemanticNetworks/Slide12-01.PNG
.. |Guards and Prisoners 1| image:: ../../_static/SemanticNetworks/Slide12-02.PNG
.. |Semantic Networks for Guards Prisoners| image:: ../../_static/SemanticNetworks/Slide13.PNG
.. |Solving the Guards and Prisoners Problem| image:: ../../_static/SemanticNetworks/Slide14-01.PNG
.. |Solving the Guards and Prisoners Problem 1| image:: ../../_static/SemanticNetworks/Slide14-02.PNG
.. |Solving the Guards and Prisoners Problem 2| image:: ../../_static/SemanticNetworks/Slide14-03.PNG
.. |Exercise Guards and Prisoners II| image:: ../../_static/SemanticNetworks/Slide18-01.PNG
.. |Exercise Guards and Prisoners II 1| image:: ../../_static/SemanticNetworks/Slide18-02.PNG
.. |Exercise Guards and Prisoners II 2| image:: ../../_static/SemanticNetworks/Slide18-03.PNG
.. |Exercise Guards and Prisoners III| image:: ../../_static/SemanticNetworks/Slide19-01.PNG
.. |Exercise Guards and Prisoners III 1| image:: ../../_static/SemanticNetworks/Slide20.PNG
.. |Represent Reason for Analogy Problems| image:: ../../_static/SemanticNetworks/Slide21-01.PNG
.. |Represent Reason for Analogy Problems 1| image:: ../../_static/SemanticNetworks/Slide21-02.PNG
.. |Exercise Represent Reason for Ravens| image:: ../../_static/SemanticNetworks/Slide22.PNG
.. |Exercise Represent Reason for Ravens 1| image:: ../../_static/SemanticNetworks/Slide23.PNG
.. |Exercise How do we choose a match| image:: ../../_static/SemanticNetworks/Slide24.PNG
.. |Exercise How do we choose a match 1| image:: ../../_static/SemanticNetworks/Slide25.PNG
.. |Choosing Matches by Weights| image:: ../../_static/SemanticNetworks/Slide26-01.PNG
.. |Choosing Matches by Weights 1| image:: ../../_static/SemanticNetworks/Slide26-02.PNG
.. |Discussion Choosing a Match by Weight| image:: ../../_static/SemanticNetworks/Slide27-01.PNG
.. |Assignment Semantic Nets| image:: ../../_static/SemanticNetworks/Slide30.PNG
.. |Wrap Up| image:: ../../_static/SemanticNetworks/Slide31.PNG
.. |Final Quiz| image:: ../../_static/SemanticNetworks/Slide34-01.PNG
.. |Final Quiz 1| image:: ../../_static/SemanticNetworks/Slide34-02.PNG
.. |Final Quiz 2| image:: ../../_static/SemanticNetworks/Slide34-03.PNG
.. |Final Quiz 3| image:: ../../_static/SemanticNetworks/Slide34-04.PNG
.. |Final Quiz 4| image:: ../../_static/SemanticNetworks/Slide34-05.PNG
.. |Final Quiz 5| image:: ../../_static/SemanticNetworks/Slide34-06.PNG
