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
* 1: Print predefined comparisons – This prints a list of pre-programmed infix expressions and strings.
* 2: Enter infix expressions and strings – This allows the user to enter their own list of infix expressions and strings. Each expression and string should be typed one after the other with a space between. E.g ca cat catt caat
* 3: Read from file – This allows the user to choose a file to read infix expressions and strings from. The full file path must be entered to the location of the file along with the file name and extension. E.g. C:\Users\Matthew\Desktop\New folder\TestInfix.txt
* 4: Exit - This allow the user to exit the program and return to the command line.

# Project Plan
* Week 1 - Initial research, setup of project and implementation of Infix to Postfix conversion using Shunting Yard Algorithm.
* Week 2 - Working with strings and creating small NFA's from parts of the regular expression in Python. These would then build and overall larger NFA's using Thompson's Construction.
* Week 3 - Main functionality and testing.
* Week 4 - Adding finishing touches, tidying up code, and adding extras.

# Research & Development
Please note all links used for research can be found in the References section below under their respective week, as I wanted to keep them from cluttering up the descriptions below.

#### Start of Semester to 04-03-19
Each week I watched the various videos posted on Moodle and read the Python documentation. I also researched online to get a grasp of the language as we hadn’t worked with python much before. I looked at various things like the way functions, classes, variables, loops etc. work and wrote basic test programs to help me understand it all. This has really helped me with this project and will be a valuable skill going forward in my career. 

#### Week of 04-03-19 to 11-03-19
I initially began to look up related information online that could help me. I also watched the videos and read the information posted on Learnonline regarding the project. To get it clear in my head how to convert infix expressions to postfix expressions I drew out some diagrams and workings with help from the videos and resources listed in the References section. From this I developed a function that converts Infix regular expression to Postfix using the Shunting Yard Algorithm, which is the first step of the project. I tested this with various infix expressions which was a success.

#### Week of 11-03-19 to 18-03-19
With the shunting algorithm implemented and working I moved onto working with creating NFA's from this postfix expression. This is achieved using Thompson's construction. It works by breaking the postfix expression down one character at a time into smaller NFA's, these NFA's are then combined to create and overall larger NFA which the string will be run through. To achieve this, I initially looked up information online that could help me and tried some things myself by drawing out each operator with sample inputs (Shown below). I also watched the videos and read the information posted on Learnonline. This helped me develop a function which creates an NFA using Thompson's construction. I couldn't test this properly however till the matching function was implemented as it would just return the memory address.

![]( https://github.com/MatthewSloyan/Graph-Theory-Project/blob/master/Drawings/Concat%2C%20Kleene%20Star%20and%20Or%20operator%20sketch.jpg)

To get the basic functionality working a matching function had to be implemented. To achieve this, I watched the videos on Learnonline, and developed a function which runs a string through the NFA adding each possible state every character could be in to a set by following the e edges. Once completed if the final set contains the accept state then the string is accepted otherwise it returns false.

#### Week of 18-03-19 to 25-03-19
With the main functionality completed, I wanted to add additional extras such as the ‘+’ and ‘?’ operators. To achieve this, I first began to see what they do, and found that the ‘?’ operator equals Zero or one. For example ab?c will match ‘abc’ and ‘ac’, but nothing else. Also, the + operator means One or more, so ab+c would match ‘abc’ and abbc but not ‘ac’. Lastly, they both have the same priority as the Kleene star and | operator which I found from research. With this in mind I began to draw them out to visualise how they work in my head (Drawings can be found in the "Drawings" folder or as shown below). This really gave me a great start, so I wasn't coding blind.

![]( https://github.com/MatthewSloyan/Graph-Theory-Project/blob/master/Drawings/Plus%20and%20Question%20mark%20operator%20sketch.jpg)

(Extra) I then began to implement the ‘?’ operator which works like the Kleene star however instead it doesn’t have a e arrow connecting back on itself from the NFA accept state to the initial state. Drawing these out really helped me visualise what was going on and how to implement it. More information of how it works can be found in the “How it works” section.

(Extra) After I implemented the + operator which again works similar to the Kleene star however instead it doesn’t have a e arrow connecting from the initial state to the accept state. More information of how it works can be found in the “How it works” section. Once I had this working, I tested it with a few regular expressions.

I have also cut down the lines of code significantly by putting related lines together on one line which also improves readability.

#### Week of 25-03-19 to 31-03-19
For the last week of the project I decided to work on finalising the project, finishing off this readme document, adding extras to the project and getting it ready for submission. 

Even though the main functionality was completed the research and work wasn’t over. I began by thinking what I could do to improve the program, and what came to mind was adding more features & functionality along with making it more user friendly. I started with the latter by adding an easy to user menu which allows the user to select the option they want by entering just a corresponding number. Each menu option would correspond with functionality which I added incrementally. 

(Extra) I started with allowing the user to enter their own infixes and strings. With research of the python documentation I found the split method which allowed me to easily add all the inputs into the list in one line rather than having a loop (Description of how this works below). 

(Extra) After I implemented the ability to read infixes and strings from files. From what I learned from the user input and how strings can be added easily into lists, I researched how file opening and reading works. I found it requires no external packages and can be opened with a simple `open(filePath, "r")`. However, when adding this to the list like in the user entry function it would include the \n character which was a problem. To solve this, I researched a way to strip characters from a string and found the rstrip method here “https://www.w3schools.com/python/ref_string_rstrip.asp” and how to user it. It strips all characters to the right of a string. I then needed to figure out how to loop through the document and remove each line where I found a similar implementation here https://qiita.com/visualskyrim/items/1922429a07ca5f974467 which I modified it and improved  to be this `[line.rstrip() for line in open(filePath, "r")]`. However I noticed from testing it would leave an empty string from the end of the file, so to fix this I instead swapped it to `open(filePath, "r").read().splitlines()` which handles this. 

# How it works
### Infix to postfix conversion using Shunting Yard Algorithm (infixConversion function)
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

### UI Functions
#### print_predefined()
Prints a predefined list of infix expressions and strings already in the program and calls print_results().
#### user_entry()
This function takes in any number of inputs for both infixes and strings. It splits the line and adds each input delimited by a space to a list using the split() method. Both entries are then passed into the print_results() function for comparison.
#### file_entry()
This function allows the user to input the path to a file for infix expressions and strings. If the file is found it reads it line by line stripping out the \n character and adds to a list, otherwise it returns a FileNotFoundError and returns.
#### print_results() 
Takes in list of infix expressions and strings looping through them and calling the match function which returns either true or false. It also prints out the results in a formatted table for readability.

# References
#### Start of Semester to 04-03-19
* https://docs.python.org/3/
* https://www.tutorialspoint.com/python/
* https://en.wikipedia.org/wiki/Nondeterministic_finite_automaton
#### Week of 04-03-19 to 11-03-19
* http://www.cs.man.ac.uk/~pjj/cs212/fix.html
* http://interactivepython.org/runestone/static/pythonds/BasicDS/InfixPrefixandPostfixExpressions.html
* http://www.oxfordmathcenter.com/drupal7/node/628
* https://web.microsoftstream.com/video/a29536d4-e975-4172-a470-40b4fe28866e?referrer=https:%2F%2Flearnonline.gmit.ie%2Fcourse%2Fview.php%3Fid%3D467
#### Week of 11-03-19 to 18-03-19
* https://swtch.com/~rsc/regexp/regexp1.html
* https://en.wikipedia.org/wiki/Thompson%27s_construction
* https://web.microsoftstream.com/video/29de6c7c-9379-46d3-99e8-8a3dbafe391f
* https://web.microsoftstream.com/video/5e2a482a-b1c9-48a3-b183-19eb8362abc9
#### Week of 18-03-19 to 25-03-19
* http://www.boost.org/doc/libs/1_56_0/libs/regex/doc/html/boost_regex/syntax/basic_extended.html#boost_regex.syntax.basic_extended.operator_precedence
* https://www.gnu.org/software/gcal/manual/html_node/Regexp-Operators.html
* http://www.delorie.com/gnu/docs/regex/regex_11.html
#### Week of 25-03-19 to 31-03-19
* https://docs.python.org/3/tutorial/inputoutput.html
* https://www.w3schools.com/python/ref_string_rstrip.asp
* https://qiita.com/visualskyrim/items/1922429a07ca5f974467

