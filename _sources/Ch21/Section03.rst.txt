Section 03: Exercise: Designing a Basement
::::::::::::::::::::::::::::::::::::::::::

.. youtube:: eGyT72YDX18
        :height: 315
        :width: 560
        :align: left

Thanks, Isuke so right now, my wife and I are actually building a house and as part of that, we need to configure the basement for the house. I've taken a list of some of the requirements for this basement and listed them over here on the left. And on the right, I have the variables that we need to assign values to, we have things like the width of the utility closet, the length of the stairwell, we also had two additional rooms, each must have their own length and width. So try to configure our basement, such that we meet all the different requirements listed over here on the left, write a number in each of these blanks.

.. activecode:: ConfigurationEx1
   :nocanvas:
   :language: python

   def basement():
       height = 0
       total_width  = 0 
       total_length = 0
       util_closet_width  = 0 
       util_closet_length = 0
       stairwell_width  = 0
       stairwell_length = 0
       bathroom_width  = 0
       bathroom_length = 0

       room1_length = 0
       room1_width  = 0

       room2_length = 0
       room2_width  = 0

       # ------------
       total_area_equal = (total_width * total_length) == \
       							(room1_width * room1_length +
       							 room2_width * room2_length + 
       							 util_closet_width * util_closet_length +
       							 stairwell_width * stairwell_length +
       							 bathroom_width * bathroom_length)
       util_100ft   = (util_closet_width * util_closet_length) >= 100
       stair_100ft  = (stairwell_width * stairwell_length) >= 100
       greater_10ft = all(lw >= 10 for lw in [total_width, total_length,
       										 util_closet_width, util_closet_length,
       										 stairwell_width, stairwell_length,
       										 bathroom_width, bathroom_length,
       										 room1_width, room1_length,
       										 room2_width, room2_length])
       lw_constraints = (total_length == 44 and total_width == 30)
       bathroom_200ft = (bathroom_width * bathroom_length) >= 200
       room1_400ft = (room1_width * room1_length) >= 400
       room2_400ft = (room2_width * room2_length) >= 400

       assert(total_area_equal), 'Total area must equal sum of areas of individual rooms'
       assert(util_100ft and stair_100ft), 'Utility closet and stairwell must be at least 100 sqft'
       assert(greater_10ft), 'No length or width can be under 10 ft'
       assert(lw_constraints), 'Length is 44, width is 30'
       assert(bathroom_200ft), 'Bathroom must be at least 200 sqft'
       assert(room1_400ft and room2_400ft), 'Two other rooms must be at least 400 sqft'
   try:basement()
   except Exception as e: print(e)