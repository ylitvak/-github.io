Section 06: Problems with Diagnosis as Classification
:::::::::::::::::::::::::::::::::::::::::::::::::::::


.. youtube:: bKf7jpbRBnc
	:height: 315
	:width: 560
	:align: left

|Problems with Diagnosis as Classification| 

|Problems with Diagnosis as Classification 1| 
|Problems with Diagnosis as Classification 2| 
|Problems with Diagnosis as Classification 3| 
|Problems with Diagnosis as Classification 4| 
|Problems with Diagnosis as Classification 5| 

Several factors conspire to make this process of classification much
more complicated. This is as you would expect in AI. If it was an easy
problem it would not be part of AI. The first factor that makes this
problem complicated is that one data point might be explained by
multiple hypotheses. So I go to the doctor with high fever, D5 here, and
several hypotheses about different diseases might explain my high fever.
Which of this hypotheses, then, is true? A second factor that
complicates things is that one hypotheses may explain multiple sets of
data. So the hypotheses that Ashok has influenza might explain not only
that he has fever, but also that he feels tired, and also that he is
shivering, and also that he can’t sleep at night. Go to your doctor with
two data items, one that have high fever and the other that I am tired.
Now the doctor may come up with a hypothesis, H3, that Ashok suffers
from flu. However, when H3 is present, then one can expect other
symptoms to be observed as well. However, the hypothesis of H3 may
generate expectations but additional data items. How, then, may a doctor
decide if H3 is true? Well, one possibility is that a doctor may ask
Ashok additional questions to collect additional data. Do you shiver at
night, the doctor may ask, if that is one of the expectations generated
by the hypothesis of having flu. because the mapping is not only from
the data space to the hypothesis space, the mapping is also from the
hypothesis space to the data space. Diagnosis entails not only mapping
data to hypothesis, but also to know the expectations of additional data
and, collecting that additional data. Of course, both of the first two
factors may be present at the same time. That is, one hypothesis may
explain multiple data items. And multiple hypothesis may explain the
same data item. So, in general, this is a M to M mapping, multiple
hypothesis, multiple sets of data. And, of course, this immediately
makes the diagnostic task harder. The fourth factor that makes the
diagnostic task hard is that these hypothesis could interact with each
other. One of the common interactions between hypotheses is called
mutual exclusion. Mutual exclusion occurs if one hypothesis present,
another hypothesis cannot be true. In this case, H3 explains D2, D3, D4.
And H6 expands D of 6, D of 7, D of 8. But if H3 is present, H6 cannot
be true. And if H6 is present, H3 cannot be true. This makes the
diagnostic task hard because if a patient goes to a doctor with symptoms
D3, D4 and D6, D7, then the question becomes whether to include H3 or to
include H6 to define our conclusion. A fifth factor that makes the
diagnostic test hard is called cancellation. Cancellation occurs when
two hypotheses interact relative to a particular data item. As an
example, I may have flu, which tends to increase a temperature, but I
may also have a lowered immune function, which tends not to show higher
temperature. As a result, I may not show high fever, but it’s not
because I don’t have flu. It’s much more because the symptoms of flu and
the symptoms of lowered immune function are cancelling out each other.
So, we also saw this in our initial exercise. We chose Thetadesis as the
most parsimonious hypothesis for these data. But imagine if we didn’t
have that as an option. If we didn’t have Thetadesis, we may have said
that it’s Betatosis, Iotalgia, and Kappacide, because the elevated A we
see in Iotalgia cancels out the reduced A we see in Kappacide, which
would account for our normal A levels. In general, cancel interactions
are very hard to account for. In order to address these factors that
make diagnosis so complex, it is useful to shift from the perspective of
diagnostics solely as classification to a perspective of diagnostics as
abduction.

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
