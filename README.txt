PREP
Open the python files in your IDE.
In the terminal, type each one of the following in turn and press enter. 
pip install pywin32
pip install pypiwin32

This installs the relevant library into the folder containing the scripts. 

START
Run coffee_routlette.py

The terminal will print the pairs recommended.

EMPTY LIST
If the list in the terminal is empty ->Run the script again 4 or 5 times as all pairs maybe exhausted or it may just need a few more attempts to populated. 
(I already have it looping 10 times to generate a maximum number of pairs)

LIST POPULATED
If the list in the terminal is populated then it will auto append the PreviousPairs.csv and overwrite NewPair.csv. 
Do not run coffee_routlette.py script again. 
You must run coffee_roulette_send_email.py to send the emails as it uses the NewPair.csv as the source.

IMPORTANT
Do not lose PreviousPairs.csv cause that is the tracking for all previous meetings that is appended with new meetings each time.
In fact, do not ever open it !

JOINERS/ LEAVERS
Just delete and appened their names to the bottom of listofnames.xlsx
However, coffee_roulette.py will only work with an "even number" of people on listofnames.xlsx
Take your own email out or put back in to make it an even number. 

EMAIL
You can change the email content in coffee_routlette_send_email.py
 



 