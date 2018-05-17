Section 10: Exercise: Applying a Constraint
:::::::::::::::::::::::::::::::::::::::::::

.. youtube:: rDhTOSY3s_g
        :height: 315
        :width: 560
        :align: left

Let us do an exercise together. This exercise again deals with the configuration of a chair. The input specification is a chair that costs at most $16 to make, and has 100 grams metal seat. Please fill out the values of all of these boxes. Try to use a configuration process that we just described, and make a note of the process that you actually did use.

.. activecode:: ConfigurationEx1
   :nocanvas:
   :language: python

   prices = {'plastic': 0.01,
             'wood'   : 0.05,
             'metal'  : 0.10}

   def cost(size, material, count=1):
       assert(material in prices), '"%s" is not a valid material' % material
       return count * (size * prices[material])

   def chair():

       # Chair legs
       legs_number = 0
       legs_size   = 0
       legs_material = ''

       # Chair seat
       seat_size = 0
       seat_material = ''

       # Chair arms
       arms_size = 0
       arms_material = ''

       # Chair back
       back_size = 0
       back_material = ''

       chair_legs = cost(material=legs_material, size=legs_size, count=legs_number)
       chair_seat = cost(material=seat_material, size=seat_size)
       chair_arms = cost(material=arms_material, size=arms_size)
       chair_back = cost(material=back_material, size=back_size)

       assert((chair_legs + chair_seat + chair_arms + chair_back) <= 16), 'Chair must cost at most $16'
       assert(seat_size == 100 and seat_material == 'metal'), 'Seat must weight 100g and be made of metal'
       print('Correct!')
   try:chair()
   except Exception as e: print(e)