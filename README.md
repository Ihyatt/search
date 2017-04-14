Challenge.py
------------

Contains:

	Class: Search
	Methods within Search: 
	- less_than
	- less_than_equals
	- equals
	- greater_than_equals
	- greater_than

	Tests: 
	- Tests the time spent in each method
	- Displays the output of that function and time spent in terms of seconds

To run: 
	While in challenge.py file, only have the function that you would like to run uncommented. cd to the search directory within your terminal. Type 'python challenge.py' and press enter to run this file.

Output in Terminal(may vary by 1 second): 
	NotFound
	--- 2.31266021729e-05 seconds ---

	NotFound
	--- 2.88486480713e-05 seconds ---

	NotFound
	--- 2.09808349609e-05 seconds ---

	('FoundExact', '1')
	--- 2.31266021729e-05 seconds ---

	('FoundGreater', '2')
	--- 2.69412994385e-05 seconds ---


tests.py
--------
Contains:
 	unittest to check the output of the methods within the Search class. 

To run:
	cd to the search directory within your terminal. Type 'python tests.py' and press enter to run this file

Output in Terminal: 
	.....
	----------------------------------------------------------------------
	Ran 5 tests in 0.000s

	OK





