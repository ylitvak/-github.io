Section 12: Guards and Prisoners
::::::::::::::::::::::::::::::::


.. youtube:: byYZx_fbqSE
	:height: 315
	:width: 560
	:align: left


|Guards and Prisoners| 
|Guards and Prisoners 1| 

Let us now look at a different problem, not a 2 by 1 matrix problem but
a problem called the guards and prisoners problem. Actually this problem
goes by many names, Cannibals and missionaries problem, the jealous
husbands problem and so on. It was first seen in a math text book about
880 and has been used by many people in AI for discussing problem
representation. Imagine that there are three guards and three prisoners,
on one bank of the river and they must all cross to the other bank.
There is one boat, just one boat and they can only take one or two
people at a time, not more and the boat cannot travel alone. On either
bank, prisoners can never outnumber the guards, if they do they will
overpower the guards. So, the number of guards must at least be equal to
the number of prisoners on each bank. We’ll assume these are good
prisoners. They won’t runaway if they’re left alone. Although they might
beat up the guards if they outnumber them. That’s the beauty of this
class. We lead with real problems, practical problems. We also make up
problems to help illustrate specific things. I think you’re going to
have fun with this one.

.. reveal:: revealcbrreading1
    :showtitle: Show Exercise
    :hidetitle: Hide Exercise

    .. activecode:: Guards_Prisoners
    
      class PrisonersandGuards(object):
        def __init__(self, ship=-1, near=[3,3], far=[0,0]):
          self.ship = ship
          self.near = near
          self.far = far
       
        def legal_state(self):
          ngn, npn = self.near
          ngf, npf = self.far	
          return ((ngn>=npn) or (ngn==0) or (npn==0)) and ((ngf>=npf) or (ngf==0) or (npf==0))
      
      pag = PrisonersandGuards()
      print pag.legal_state()

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
