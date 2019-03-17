# Graph-Theory-Project

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
I plan to implement other operators such as "+" and "?".

# References
* https://en.wikipedia.org/wiki/Nondeterministic_finite_automaton
* http://www.oxfordmathcenter.com/drupal7/node/628
* https://swtch.com/~rsc/regexp/regexp1.html
