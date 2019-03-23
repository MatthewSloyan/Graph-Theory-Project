# Graph-Theory-Project

# How to run
To run the program run the follow command below.
python GraphTheoryProject.py

# Project Plan
* Week 1 - Initial research, setup of project and implementation of Infix to Postfix conversion using Shunting Yard Alogorithm.
* Week 2 - Working with strings, and creating small NFA's from parts of the regular expression in Python. These would then build and overall larger NFA's using Thompson's Contruction.
* Week 3 - Main functionality and testing.
* Week 4 - Adding finishing touches, tidying up code, and adding extras.

# Research & Development
#### Start of Semester to 04-03-19
Each week I watched the various videos posted and read the Python documents, along with researching online to get a grasp of the language. This has really helped me with this project and will be a vauable skill going forward in my career.

#### Week of 04-03-19 to 11-03-19
I intially began to look up related information online that could help me. I also watched the videos and read the information posted on Learnonline regarding the project. To get it clear in my head I drew out some digrams and workings with help from the videos. From this I developed a function that converts Infix regular expression to Postfix using the Shunting Yard Algorithm, which is the first step of the project. I tested this with various infix expressions which was a success.

#### Week of 11-03-19 to 18-03-19
With the shunting algorithm implemented and working I moved onto working with creating NFA's from this postfix expression. This will be achieved using Thompson's contruction. It works by breaking the postfix expression down one character at a time into smaller NFA's, these NFA's are then combined to create and overall larger NFA which the string will be run through. To achieve this I intially looked up information online that could help me and tried some things myself. I also watched the videos and read the information posted on Learnonline (linked below). This helped me develop a function which creates a NFA using Thompson's contruction. I couldn't test this properly however till the matching function was implemented as it would just return the memory address.

To get the basic functionality working a matching function had to be implemented. To achive this I watched the videos on Learnonline, and developed a function which runs a string through the NFA adding each possible state every character could be in to a set. Once completed if the final set contains the accept state then the string is accepted otherwise it returns false.

#### Week of 18-03-19 to 25-03-19
With the main funcionality completed, I wanted to add additional extras such as the "+" and "?" operators. To achieve this I first began to see what they do, and found that the ? operator equals Zero or one. For example ab?c will match ‘abc’ and ‘ac’, but nothing else. Also the + operator means One or more, so ab+c would match ‘abc’ and abbc but not ‘ac’. Lastly they both have the same priorty as the kleene star and | operator. With this in mind I began to draw them out to visualise how they work in my head (Drawings can be found in the "Drawings" folder above or in the links below). This really gave me a great start so I wasn't coding blind.

I then began to implement the ? operator which works by first popping the current nfa off the stack and setting up an initial/accept state. Then connect intial state edge1 to the popped nfa's intial state, and connect intial edge two to the accept state. Finally set nfa1 edge1 to the accept state to create the one or zero relationship. Create a new nfa from this and add back on the stack. Once I had this working I tested it with a few regular expressions which worked correctly.

After I began to implement the + operator which works similar to the ? operator at first and then similar to the kleene star by joining edge1 from nfa1 accept state to the nfa1 inital state creating a loop on itself for the "or more" option. Then setting the other edge to the accept state for the "one" option. Lastly create a new nfa from this and push on the stack. Once I had this working I tested it with a few regular expressions.

#### Week of 25-03-19 to 31-03-19

# References
* https://en.wikipedia.org/wiki/Nondeterministic_finite_automaton
* http://www.oxfordmathcenter.com/drupal7/node/628
* https://swtch.com/~rsc/regexp/regexp1.html
* https://www.gnu.org/software/gcal/manual/html_node/Regexp-Operators.html
