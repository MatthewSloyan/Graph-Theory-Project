# Graph-Theory-Project

Name: Matthew Sloyan
Student ID: G00348036

# Project statement
To write a program in the Python that can build a non-deterministic finite automaton (NFA) from a regular expression and can use the NFA to check if the regular expression matches any given string of text.

# How to run
* First, clone the repository using the following command `git clone https://github.com/MatthewSloyan/Graph-Theory-Project.git` 
* Traverse using the command line to the folder you have cloned using the cd command.
* From the command line run the following command to run the programs. `python GraphTheoryProject.py`

# User Guide
Below you’ll find a basic guide to the user interface, in the “How it works” section is a description of how this works in the code behind.

When running the program, the user is presented with a list of menu options listed below. To select a menu option, enter the corresponding number for your choice. E.g. 1 = menu option 1. Also, all other invalid inputs are handled.
### 1: Print predefined comparisons – This prints a list of pre-programmed infix expressions and strings.
### 2: Enter infix expressions and strings – This allows the user to enter their own list of infix expressions and strings. Each expression and string should be typed one after the other with a space between. E.g ca cat catt caat
### 3: Read from file – This allows the user to choose a file to read infix expressions and strings from. The full file path must be entered to the location of the file along with the file name and extension. E.g. C:\Users\Matthew\Desktop\New folder\TestInfix.txt
### 4: Exit - This allow the user to exit the program and return to the command line.

# Project Plan
* Week 1 - Initial research, setup of project and implementation of Infix to Postfix conversion using Shunting Yard Algorithm.
* Week 2 - Working with strings and creating small NFA's from parts of the regular expression in Python. These would then build and overall larger NFA's using Thompson's Construction.
* Week 3 - Main functionality and testing.
* Week 4 - Adding finishing touches, tidying up code, and adding extras.

# Research & Development
#### Start of Semester to 04-03-19
Each week I watched the various videos posted and read the Python documentation (https://docs.python.org/3/), along with researching online to get a grasp of the language. This has really helped me with this project and will be a valuable skill going forward in my career. 

#### Week of 04-03-19 to 11-03-19
I initially began to look up related information online that could help me. I also watched the videos and read the information posted on Learnonline regarding the project. To get it clear in my head I drew out some diagrams and workings with help from the videos. From this I developed a function that converts Infix regular expression to Postfix using the Shunting Yard Algorithm, which is the first step of the project. I tested this with various infix expressions which was a success.

#### Week of 11-03-19 to 18-03-19
With the shunting algorithm implemented and working I moved onto working with creating NFA's from this postfix expression. This is achieved using Thompson's construction. It works by breaking the postfix expression down one character at a time into smaller NFA's, these NFA's are then combined to create and overall larger NFA which the string will be run through. To achieve this, I initially looked up information online that could help me and tried some things myself. I also watched the videos and read the information posted on Learnonline (linked below). This helped me develop a function which creates an NFA using Thompson's construction. I couldn't test this properly however till the matching function was implemented as it would just return the memory address.

To get the basic functionality working a matching function had to be implemented. To achieve this, I watched the videos on Learnonline, and developed a function which runs a string through the NFA adding each possible state every character could be in to a set by following the e edges. Once completed if the final set contains the accept state then the string is accepted otherwise it returns false.

#### Week of 18-03-19 to 25-03-19
With the main functionality completed, I wanted to add additional extras such as the ‘+’ and ‘?’ operators. To achieve this, I first began to see what they do, and found that the ‘?’ operator equals Zero or one. For example ab?c will match ‘abc’ and ‘ac’, but nothing else. Also, the + operator means One or more, so ab+c would match ‘abc’ and abbc but not ‘ac’. Lastly, they both have the same priority as the Kleene star and | operator. With this in mind I began to draw them out to visualise how they work in my head (Drawings can be found in the "Drawings" folder above or in the links below). This really gave me a great start, so I wasn't coding blind.

I then began to implement the ‘?’ operator which works by first popping the current NFA’ off the stack and setting up an initial/accept state. Then connect initial state edge1 to the popped NFA’s initial state and connect initial edge two to the accept state. Finally set nfa1 edge1 to the accept state to create the one or zero relationship. Create a new NFA from this and add back on the stack. Once I had this working, I tested it with a few regular expressions which worked correctly.

After I began to implement the + operator which works like the ‘?’ operator at first and then like the Kleene star by joining edge1 from nfa1 accept state to the nfa1 initial state creating a loop on itself for the "or more" option. Then setting the other edge to the accept state for the "one" option. Lastly create a new NFA from this and push on the stack. Once I had this working, I tested it with a few regular expressions.

I have also cut down the lines of code significantly by putting related lines together on one line which also improves readability.

#### Week of 25-03-19 to 31-03-19
For the last week of the project I decided to work on finalising the project, finishing off this readme document, adding extras to the project and getting it ready for submission. 

# How it works
### infix to postfix conversion using Shunting Yard Algorithm (infixConversion function)
* It starts by looping through the passed in infix string. 
* If the first character is a ‘(‘ add to the stack signifying the start of a group. 
* If a ‘)’ is encountered add what’s on the stack until ‘(‘ is encountered and then remove the ‘(‘. 
* If the character is one of the special characters (operators) E.g. * + ? . | which are order of precedence, push from top of stack to postfix output if priority is lower or equal to. Note: * + and ? carry the same precedence.
* If neither of the above add the character to the postfix output, E.g. the character “a”.
* After, remove additional characters from the stack and return completed postfix string.

### Thompsons construction algorithm implementation (compile function)
It starts by iterating through the passed in postfix expression. It then checks for each operator (* + ? . |) and creates a small NFA to add to the overall NFA stack. These work by setting up initial and accepts states using the NFA class and constructor. Below is a quick description how each operator works.
#### Concatenation operator ‘.’
Pop both NFA’s from the stack to concatenate and set the first NFA accept state to the second NFA initial state to connect them up.
#### Or operator ‘|’ 
Pop both NFA’s from the stack and create a new initial and accept state. Set edge one for the new initial state to the initial state of NFA one. Set the second edge to the initial state of NFA two. Connect the accept state of both NFA one and two to the new accept state created to finish and append to the stack.
#### Kleene Star Operator (Zero or more)
Pop one NFA’s from the stack and create a new initial and accept state. Set edge one for the new initial state to the initial state of the NFA. Set the second edge to the new accept state (Zero option). Set edge one of the accept state in the NFA back to the initial state of the NFA to loop back on itself. Set the second edge to the accept state to complete and append to stack.
#### ? Operator (Zero or one)
Pop one NFA’s from the stack and create a new initial and accept state. Set edge one for the new initial state to the initial state of the NFA. Set the second edge to the new accept state (Zero option). Set edge one of the accept state in the NFA to the final accept state (One option). 
#### + Operator (One or more)
Pop one NFA’s from the stack and create a new initial and accept state. Set edge one of the new initial state to the initial state of the NFA. Set edge one for the new initial state to the initial state of the NFA. Set edge one of the accept state in the NFA back to the initial state of the NFA looping it back on itself. (Or more option). Set edge two of the accept state in the NFA to the final accept state (One option). 

### Matching Algorithm (match function)
This function converts an infix regular expression, coverts it to postfix and checks if the regular expression matches the given string of text.
First get the postfix expression by calling the the infixConversion() function described in detail above, which returns a postfix expression. Then compile the postfix expression into a non-deterministic finite automaton to compare the string with using the compile() function which is described above too. Create a new set for both the current set of states and the set of next states. Sets work like lists in other programming languages however their values must be unique. E.g. you can’t add the same value to a set twice. Using the union operator add all the possible states you could travel to by following the e arrows to the current set. This is implemented using the followEs function which is described below. For each character in the string iterate through the current set to check if the set contains the character, if so, add the next states you could travel to using this edge. At the end if the current set contains the accept state then it returns true, if not then returns false and the string doesn’t match the NFA.

### Traverse through all possible e edges (FollowEs function)
Helper function, which returns set of states that can be reached from the state following e arrows. If it encounters an e arrow (state.label is None) it will check both edges and follow them if possible. If it can follow it uses recursion and starts the process again from that current edge until it can follow no more edges.

# References
* https://en.wikipedia.org/wiki/Nondeterministic_finite_automaton
* http://www.oxfordmathcenter.com/drupal7/node/628
* https://swtch.com/~rsc/regexp/regexp1.html
* http://www.boost.org/doc/libs/1_56_0/libs/regex/doc/html/boost_regex/syntax/basic_extended.html#boost_regex.syntax.basic_extended.operator_precedence
* https://www.gnu.org/software/gcal/manual/html_node/Regexp-Operators.html
