Section 04: Defining Diagnosis
::::::::::::::::::::::::::::::


.. youtube:: ouQbt_fh1VA
	:height: 315
	:width: 560
	:align: left

|Defining Diagnosis| 
|Defining Diagnosis 1| 

We may define the task of diagnosis as determining what is wrong with a
malfunctioning device. Or more generally, what is the fault that is
responsible for a malfunctioning system. Given a system, we expect some
behavior from it. We expect it to do something. However, we may observe
that the system is doing something different. So there is the expected
behavior and there is the observed behavior, and there is a discrepancy
between them. When there is a discrepancy, we know that the system is
malfunctioning. The question then becomes what is the fault or the set
of faults responsible for the malfunctioning system. When we think of
diagnosis we typically think of medical diagnosis. But, of course
diagnosis can occur in a very large number of domains. Here are three
diagnostic domains with which all of us are familiar. The first figure
shows the engine of a car. When I insert the key into the ignition
system, I expect the engine to turn on. That is the expected behavior.
But suppose that I insert the key, and the engine doesn’t turn on.
That’s the observed behavior. There is a discrepancy between the
expected behavior and the observed behavior. When I insert the key into
the ignition, I expect the engine to turn on. That’s the expected
behavior. But then suppose that I put the key in, and the engine doesn’t
turn on. That’s the observed behavior. The discrepancy between the
expected behavior, turn the engine on, and the observed behavior, the
engine doesn’t turn on, so I know there is a malfunction. Given this
malfunction, the question becomes what is at fault, the force
responsible for it and that’s the diagnostic task. To address this
diagnostic task, I may use a rule which says that if the engine doesn’t
turn on when the key is inserted, check the carburetor. Suppose I go and
check the carburetor and everything is okay with the carburetor. Then I
[Thus, the] get activated. And let me say, if the engine doesn’t turn on
and everything is okay with the carburetor, go check the spark plugs.
And this way, I am going to use a production system to isolate the fault
of faults responsible for the malfunction. Something similar happens
with computer hardware repair. When we turn on a computer, there are few
behaviors that we expect of it. We expect it to boot up quickly, we
expect it to run fast, and we expect it to stay cool. Now, imagine we
turn a computer and notice it started to run at a much higher
temperature than we’re accustomed to. We might remember that the last
time we encountered this problem, there were problems with the fan. So
we might use that to then diagnose this a problem with the fan and
replace the fan. This happens at the software level too. If I’m writing
a program and the output differs from what I was expecting, I set about
debugging the program and finding the fault. One way of doing that is
called a rubber duck debugging, which involves explaining my model of
how my program works to the rubber duck so that I might uncover the
error by forcing myself through an explanation process. Note that we
discussed the same diagnostic task in three different domains. In each
domain there was a discrepancy between the expected and the observed
behaviors and we tried to identify the fault, or faults responsible for
it. Note also that we alluded to three different methods for doing
diagnosis. The matter of rule based reasoning, the matter of case based
reasoning, and the matter of model based reasoning. We haven’t talked a
lot about the matter of model based reasoning so far. We will do so when
we come to systems thinking later in the class. Of course we can use the
matter of rule based reasoning, not only for diagnosing car engines but
also for repairing computer hardware or for diagnosing computer
software. In this particular lesson our focus will be on the diagnostic
task. By now all of us are already familiar with many reasoning methods
that are potentially applicable to class.

.. |Preview| image:: ../../_static/Diagnosis/Slide01-01.PNG
.. |Preview 1| image:: ../../_static/Diagnosis/Slide01-02.PNG
.. |Exercise Diagnosing Illness| image:: ../../_static/Diagnosis/Slide02.PNG
.. |Exercise Diagnosing Illness 1| image:: ../../_static/Diagnosis/Slide03.PNG
.. |Defining Diagnosis| image:: ../../_static/Diagnosis/Slide04-01.PNG
.. |Defining Diagnosis 1| image:: ../../_static/Diagnosis/Slide04-02.PNG
.. |Data Space and Hypothesis Space| image:: ../../_static/Diagnosis/Slide05-01.PNG
.. |Data Space and Hypothesis Space 1| image:: ../../_static/Diagnosis/Slide05-02.PNG
.. |Data Space and Hypothesis Space 2| image:: ../../_static/Diagnosis/Slide05-03.PNG
.. |Data Space and Hypothesis Space 3| image:: ../../_static/Diagnosis/Slide05-04.PNG
.. |Data Space and Hypothesis Space 4| image:: ../../_static/Diagnosis/Slide05-05.PNG
.. |Problems with Diagnosis as Classification| image:: ../../_static/Diagnosis/Slide06-01.PNG
.. |Problems with Diagnosis as Classification 1| image:: ../../_static/Diagnosis/Slide06-02.PNG
.. |Problems with Diagnosis as Classification 2| image:: ../../_static/Diagnosis/Slide06-03.PNG
.. |Problems with Diagnosis as Classification 3| image:: ../../_static/Diagnosis/Slide06-04.PNG
.. |Problems with Diagnosis as Classification 4| image:: ../../_static/Diagnosis/Slide06-05.PNG
.. |Problems with Diagnosis as Classification 5| image:: ../../_static/Diagnosis/Slide06-06.PNG
.. |Deduction, Induction, Abduction| image:: ../../_static/Diagnosis/Slide07-01.PNG
.. |Deduction, Induction, Abduction 1| image:: ../../_static/Diagnosis/Slide07-02.PNG
.. |Deduction, Induction, Abduction 2| image:: ../../_static/Diagnosis/Slide07-03.PNG
.. |Criteria for Choosing a Hypothesis| image:: ../../_static/Diagnosis/Slide08-01.PNG
.. |Criteria for Choosing a Hypothesis 1| image:: ../../_static/Diagnosis/Slide08-02.PNG
.. |Criteria for Choosing a Hypothesis 2| image:: ../../_static/Diagnosis/Slide08-03.PNG
.. |Exercise Diagnosis as Abduction| image:: ../../_static/Diagnosis/Slide09.PNG
.. |Exercise Diagnosis as Abduction 1| image:: ../../_static/Diagnosis/Slide10.PNG
.. |Completing the Process| image:: ../../_static/Diagnosis/Slide11-01.PNG
.. |Completing the Process 1| image:: ../../_static/Diagnosis/Slide11-02.PNG
.. |Completing the Process 2| image:: ../../_static/Diagnosis/Slide11-03.PNG
.. |Assignment Diagnosis| image:: ../../_static/Diagnosis/Slide12.PNG
.. |Wrap Up| image:: ../../_static/Diagnosis/Slide13.PNG
