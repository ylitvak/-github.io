Section 15: Exercise: Production System in Action
:::::::::::::::::::::::::::::::::::::::::::::::::

.. youtube:: o6uX8ncr4wo
	:height: 315
	:width: 560
	:align: left

|Exercise Production System in Action I| 
Okay, given these productions in the procedural part of sol’s long term
memory. And given these are the contents of the working memory which
capture the current set of percepts and the current goal. What operator
do you think sol will select? Note that one of the choices here is none,
the system cannot decide.

.. reveal:: revealcbrreading1
    :showtitle: Show Exercise
    :hidetitle: Hide Exercise

    .. activecode:: Production Systems
    
      p = {"inning":7, "portion":"top", "runners":(2,3), "outs":2, 
    	"batter":"Prado", "average":.256, "bats": "r", "score":(3,2),
    	"goal":"escape","strikes":0}
    
      selected_operators = []
    
      #(r1)
      if p["goal"] == "escape" and p["outs"] == 2 and 2 in p["runners"] and 1 not in p["runners"]:
    	p["goal"] = "intentional_walk"
    
      #(r2)
      if p["goal"] == "escape" and (p["outs"] < 2 or 1 in p["runners"] or (2 not in p["runners"]) or p["runners"] == ()):
    	p["goal"] = "pitch"
    
      #(r3)
      if p["goal"] == "intentional_walk":
    	selected_operators.append("intentional-walk")
    
      #(r5)
      if p["goal"] == "pitch" and p["strikes"] < 3:
    	selected_operators.append("throw-curve-ball")
    
      #(r6)
      if p["goal"] == "pitch" and p["strikes"] < 3 and p["bats"] == "l":
    	selected_operators.append("throw-fast-ball")
    
      #(r7)
      if len(selected_operators) == 1:
    	print("Selected action: " + selected_operators[0])
      else:
            print("No action selected")

.. |Preview| image:: ../../_static/ProductionSystems/Slide01-01.PNG
.. |Preview 1| image:: ../../_static/ProductionSystems/Slide01-02.PNG
.. |Exercise A Pitcher| image:: ../../_static/ProductionSystems/Slide02-01.PNG
.. |Exercise A Pitcher 1| image:: ../../_static/ProductionSystems/Slide02-02.PNG
.. |Exercise A Pitcher 2| image:: ../../_static/ProductionSystems/Slide03.PNG
.. |Function of a Cognitive Architecture| image:: ../../_static/ProductionSystems/Slide04.PNG
.. |Levels of Cognitive Architectures| image:: ../../_static/ProductionSystems/Slide05-01.PNG
.. |Exercise Levels of Architectures| image:: ../../_static/ProductionSystems/Slide06.PNG
.. |Exercise Levels of Architectures 1| image:: ../../_static/ProductionSystems/Slide07.PNG
.. |Assumptions of Cognitive Architectures| image:: ../../_static/ProductionSystems/Slide08.PNG
.. |Architecture Content Behavior| image:: ../../_static/ProductionSystems/Slide09-01.PNG
.. |Architecture Content Behavior 1| image:: ../../_static/ProductionSystems/Slide09-02.PNG
.. |A Cognitive Architecture for Production Systems| image:: ../../_static/ProductionSystems/Slide10-01.PNG
.. |A Cognitive Architecture for Production Systems 1| image:: ../../_static/ProductionSystems/Slide10-02.PNG
.. |Return to the Pitcher| image:: ../../_static/ProductionSystems/Slide11-01.PNG
.. |Return to the Pitcher 1| image:: ../../_static/ProductionSystems/Slide11-02.PNG
.. |Return to the Pitcher 2| image:: ../../_static/ProductionSystems/Slide11-03.PNG
.. |Action Selection| image:: ../../_static/ProductionSystems/Slide12-01.PNG
.. |Action Selection 1| image:: ../../_static/ProductionSystems/Slide12-02.PNG
.. |Putting Content in the Architecture| image:: ../../_static/ProductionSystems/Slide13.PNG
.. |Bringing in Memory| image:: ../../_static/ProductionSystems/Slide14-01.PNG
.. |Bringing in Memory 1| image:: ../../_static/ProductionSystems/Slide14-02.PNG
.. |Exercise Production System in Action I| image:: ../../_static/ProductionSystems/Slide15.PNG
.. |Exercise Production System in Action I 1| image:: ../../_static/ProductionSystems/Slide16.PNG
.. |Exercise Production System in Action II| image:: ../../_static/ProductionSystems/Slide17.PNG
.. |Exercise Production System in Action II 1| image:: ../../_static/ProductionSystems/Slide18.PNG
.. |Exercise System in Action III| image:: ../../_static/ProductionSystems/Slide19.PNG
.. |Exercise System in Action III 1| image:: ../../_static/ProductionSystems/Slide20.PNG
.. |Chunking| image:: ../../_static/ProductionSystems/Slide21.PNG
.. |Exercise Chunking| image:: ../../_static/ProductionSystems/Slide22.PNG
.. |Exercise Chunking 1| image:: ../../_static/ProductionSystems/Slide23.PNG
.. |Assignment Production Systems| image:: ../../_static/ProductionSystems/Slide25.PNG
.. |Wrap Up| image:: ../../_static/ProductionSystems/Slide26.PNG
.. |The Cognitive Connection| image:: ../../_static/ProductionSystems/Slide27-01.PNG
.. |The Cognitive Connection 1| image:: ../../_static/ProductionSystems/Slide27-02.PNG
.. |The Cognitive Connection 2| image:: ../../_static/ProductionSystems/Slide27-03.PNG
