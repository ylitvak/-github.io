Section 13: Semantic Networks for Guards and Prisoners
::::::::::::::::::::::::::::::::::::::::::::::::::::::


.. youtube:: jaCInn35DmQ
	:height: 315
	:width: 560
	:align: left


|Semantic Networks for Guards Prisoners| 

Let us try to construct a semantic network representation, for this
guards and prisoners problem, and see how we can use it to, do the
problem solving. So in this representation, I’m going to say that each
node is a state in the problem solving. In this particular state, there
happens to be one guard and one prisoner on the left side. The boat is
on the right side, and two of the prisoners and two of the guards are
also on the right side. So this is a node, one single node. So the node
captured, the lexicon of the semantic network. Now, we’ll add the
structural part. And the structural part has to do with the
transformation. That is going connect different nodes, into a more
complex sentence. We’ll label the links between the nodes, and these
labels then, will capture some of the semantics of this representation,
that will allow us to make interesting inferences, when it comes time to
do the problem solving. Here is a second node, and this node represents
a different state in the problem solving. In this case, there are two
guards and two prisoners on the left side. The boat is also on the left
side. There is one guard and one prisoner on the right side. So this
now, is a, semantic network. A node, another node, a link between them
and the link is labelled. Note that in this representation, I used icons
to represent objects, as well as icons to represent labels of the links
between the nodes. This is perfectly valid. You don’t have to use words.
You can use icons, as long as you’re capturing the nodes and the objects
inside each state, as well as the labels on the links between the
different nodes.

.. reveal:: revealcbrreading1
    :showtitle: Show Exercise
    :hidetitle: Hide Exercise

    .. activecode:: Guards_Prisoners
    
      from operator import sub

      class PrisonersandGuards(object):
        def __init__(self, ship=-1, near=[3,3], far=[0,0]):
          self.ship = ship
          self.near = near
          self.far = far
       
        def legal_state(self):
          ngn, npn = self.near
          ngf, npf = self.far	
          return ((ngn>=npn) or (ngn==0) or (npn==0)) and ((ngf>=npf) or (ngf==0) or (npf==0))
      
      def successors(pag_obj):
        successor_list = []
        if pag_obj.ship == -1:
          depart = pag_obj.near
        else:
          depart = pag_obj.far
        for possible_transfers in [[1,0],[0,1],[1,1],[2,0],[0,2]]:
          if min(map(sub, depart, possible_transfers)) >= 0:
            successor_list.append(possible_transfers)
        return successor_list
      
      pag = PrisonersandGuards()
      print successors(pag)

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
