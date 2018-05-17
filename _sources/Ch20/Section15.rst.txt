Section 15: Constraint Propagation for Natural Language Processing
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

.. youtube:: vM1lDp0oTPM
	:height: 315
	:width: 560
	:align: left

|Constraint Propagation for Natural Language Processing| 
|Constraint Propagation for Natural Language Processing 1| 
|Constraint Propagation for Natural Language Processing 2| 
Let us again written to the center. Colorless green ideas sleep
furiously. You and I can quickly recognize, that this sentence is
grammatically correct even as it is semantically meaningless. How do we
do it? Consider this mini-grammar. This is a small subset of the English
language grammar consisting of just three simple rules. The sentence can
go into a noun phrase, followed by a verb phrase. A noun phase can be,
optional adjectives, followed by a noun or a pronoun. The square bracket
here means, optional. A verb phrase, composed of a verb, followed by
optional adverb. The variables in this particular sentence, are the
words. The values we assign to them are elliptical categories like verb,
objective, noun and pronoun. If we can make a pastry for this, that
assigned values to this variables in a way that is consistent with this
grammar, then this particular sentence is grammatically correct. Let’s
try to make a pastry for this sentence. A sentence can a noun phrase, or
a word phrase. So we may say, that this is a noun phrase and this is
word phrase. Of course at this particular point we do not know, where we
should make this demarcation, what should go into the noun phrase, what
should go into the word phrase? We know whether or not, this demarcation
is correct depending upon whether or not this noun phrase, and word
phrase meet the low level lexical categories. So let’s look at colorless
green ideas. We know that a noun phrase can go into one or more
adjectives, followed by a noun or pronoun. So we can look at a lexicon,
and know that ideas are a noun, so we say that this is a noun. We can
look at a lexicon that tells us that colorless and green are adjectives,
and so colorless and green are adjectives here. We have satisfied this
part of the constraint. So I am ready for the verb phrase, a verb phrase
can be composed of a verb, followed by one or more optional adverbs. We
can look in the lexicon, and sleep is a verb, and furiously is an
adverb, so we have satisfied the constraints for this particular part.
Because we have satisfied the constraints, we know the top level
demarcation of this as a noun phrase, and this as a verb phrase was
correct. So the processing is not very top down here. It also has a
bottom up component. In this way we are able to decide, that this
particular sentence is grammatically correct because it satisfies the
constraints of [our mini] grammar. Know that we have used knowledge of
constraints, and the matter of constraint propagation, both for visual
processing and for language processing. This sentence method is very
general purpose in doing independent. Once we have done constraint
propagation, to derive the parse tree for the sentence, then we can do
additional processing. We can use this parse tree to support semantic
analysis to build an understanding, a semantic understanding, of the
sentence. Similarly, in visual processing, once we have used the
constraints for doing line labelling. And recognize the surfaces and
their orientations. We can then go on further and recognize the object
in its 3D form.


.. reveal:: revealcbrreading1
    :showtitle: Show Exercise
    :hidetitle: Hide Exercise

    .. activecode:: Generative Grammar
      
      """
      Random sentence generation using context-free generative grammars.
      Translated from chapter 2 of "Paradigms of Artificial Intelligence
      Programming" by Peter Norvig.
      """
      
      __author__ = 'Daniel Connelly'
      __email__ = 'dconnelly@gatech.edu'
      
      
      import random, sys
      
      
      SIMPLE_ENGLISH = {
          'verb': ['hit', 'took', 'saw', 'liked'],
          'noun': ['man', 'ball', 'woman', 'table'],
          'article': ['the', 'a'],
      
          'sentence': [['noun phrase', 'verb phrase']],
          'noun phrase': [['article', 'noun']],
          'verb phrase': [['verb', 'noun phrase']],
      }
      
      
      BIGGER_ENGLISH = {
          'prep': ['to', 'in', 'by', 'with', 'on'],
          'adj': ['big', 'little', 'blue', 'green', 'adiabatic'],
          'article': ['a', 'the'],
          'name': ['Pat', 'Kim', 'Lee', 'Terry', 'Robin'],
          'noun': ['man', 'ball', 'woman', 'table'],
          'verb': ['hit', 'took', 'saw', 'liked'],
          'pronoun': ['he', 'she', 'it', 'these', 'those', 'that'],
      
          'sentence': [['noun phrase', 'verb phrase']],
          'noun phrase': [['article', 'adj*', 'noun', 'pp*'],
                          ['name'],
                          ['pronoun']],
          'verb phrase': [['verb', 'noun phrase', 'pp*']],
          'pp*': [[], ['pp']],
          'adj*': [[], ['adj']],
          'pp': [['prep', 'noun phrase']],
      }
      
      
      def generate(grammar, phrase):
          """Recursively rewrites each subphrase until only terminals remain.
          grammar is a dictionary defining a context-free grammar, where each
          (key, value) item defines a rewriting rule.
          Each subphrase of phrase is recursively rewritten unless it does not
          appear as a key in the grammar.
          """
          if isinstance(phrase, list):
              phrases = (generate(grammar, p) for p in phrase)
              return " ".join(p for p in phrases if p)
          elif phrase in grammar:
              return generate(grammar, random.choice(grammar[phrase]))
          else:
              return phrase
          
      
      def generate_tree(grammar, phrase):
          """Generates a sentence from the grammar and returns its parse tree.
          
          The sentence is generated in the same manner as in generate, but the
          returned value is a nested list where the first element of each sublist
          is the name of the rule generating the phrase.
          """
          if isinstance(phrase, list):
              return [generate_tree(grammar, p) for p in phrase]
          elif phrase in grammar:
              rc = random.choice(grammar[phrase])
              if isinstance(rc, str):
                  print rc
              return [phrase] + generate_tree(grammar, rc)
          else:
              return [phrase]
      

      print generate_tree(BIGGER_ENGLISH, 'sentence')


.. |Preview| image:: ../../_static/ConstraintPropagation/Slide01-01.PNG
.. |Preview 1| image:: ../../_static/ConstraintPropagation/Slide01-02.PNG
.. |Exercise Recognizing 3D Figures| image:: ../../_static/ConstraintPropagation/Slide02-01.PNG
.. |Exercise Recognizing 3D Figures 1| image:: ../../_static/ConstraintPropagation/Slide02-02.PNG
.. |Exercise Recognizing 3D Figures 2| image:: ../../_static/ConstraintPropagation/Slide03.PNG
.. |Exercise Gibberish Sentences| image:: ../../_static/ConstraintPropagation/Slide04.PNG
.. |Exercise Gibberish Sentences 1| image:: ../../_static/ConstraintPropagation/Slide05.PNG
.. |Constraint Propagation Defined| image:: ../../_static/ConstraintPropagation/Slide06.PNG
.. |From Pixels to 3D| image:: ../../_static/ConstraintPropagation/Slide07-01.PNG
.. |From Pixels to 3D 1| image:: ../../_static/ConstraintPropagation/Slide07-02.PNG
.. |From Pixels to 3D 2| image:: ../../_static/ConstraintPropagation/Slide07-03.PNG
.. |Line Labeling| image:: ../../_static/ConstraintPropagation/Slide08.PNG
.. |Constraints Intersections and Edges| image:: ../../_static/ConstraintPropagation/Slide09-01.PNG
.. |Constraints Intersections and Edges 1| image:: ../../_static/ConstraintPropagation/Slide09-02.PNG
.. |Constraints Intersections and Edges 2| image:: ../../_static/ConstraintPropagation/Slide09-03.PNG
.. |Exercise Assembling the Cube I| image:: ../../_static/ConstraintPropagation/Slide10.PNG
.. |Exercise Assembling the Cube I 1| image:: ../../_static/ConstraintPropagation/Slide11.PNG
.. |Exercise Assembling the Cube II| image:: ../../_static/ConstraintPropagation/Slide12.PNG
.. |Exercise Assembling the Cube II 1| image:: ../../_static/ConstraintPropagation/Slide13.PNG
.. |More Complex Images| image:: ../../_static/ConstraintPropagation/Slide14-01.PNG
.. |More Complex Images 1| image:: ../../_static/ConstraintPropagation/Slide14-02.PNG
.. |More Complex Images 2| image:: ../../_static/ConstraintPropagation/Slide14-03.PNG
.. |More Complex Images 3| image:: ../../_static/ConstraintPropagation/Slide14-04.PNG
.. |More Complex Images 4| image:: ../../_static/ConstraintPropagation/Slide14-05.PNG
.. |More Complex Images 5| image:: ../../_static/ConstraintPropagation/Slide14-06.PNG
.. |More Complex Images 6| image:: ../../_static/ConstraintPropagation/Slide14-07.PNG
.. |More Complex Images 7| image:: ../../_static/ConstraintPropagation/Slide14-08.PNG
.. |Constraint Propagation for Natural Language Processing| image:: ../../_static/ConstraintPropagation/Slide15-01.PNG
.. |Constraint Propagation for Natural Language Processing 1| image:: ../../_static/ConstraintPropagation/Slide15-02.PNG
.. |Constraint Propagation for Natural Language Processing 2| image:: ../../_static/ConstraintPropagation/Slide15-03.PNG
.. |Assignment Constraint Propagation| image:: ../../_static/ConstraintPropagation/Slide16.PNG
.. |Wrap Up| image:: ../../_static/ConstraintPropagation/Slide17.PNG
