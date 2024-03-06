# Rat24S Language Lexer

## Overview

This project implements a lexer (lexical analyzer) for the Rat24S language. The lexer scans the source code of a Rat24S program and converts it into a series of tokens, which are meaningful for the language. These tokens can later be used by a parser to understand the structure of the code.

## How to Use

1. Clone the repository to your local machine with `git clone github.com/JeremiahHerring/Lexical-Analyzer`
2. Navigate to the Lexical Analyzer directory.
3. Run the command `python3 LexerFSM/main.py`.
4. The lexer will run based on the three input files inside the input folder, and the corresponding output will be placed in the output folder.
5. If you want to test your own test cases, you can replace one of the three input files, and the output will again be placed in the corresponding output folder. Note that the names of the input and output files are hardcoded.

## Design

The project repository is organized into several sections: Documents, FSM diagrams, and the code for the lexer. The code for the lexer is divided into classes that each hold a finite state machine (FSM). There are separate files for identifiers, integers, and real numbers, each containing the main FSM code that determines if we are in an accepting or non-accepting state. 

Each class exports a class that holds the states that we are traversing with our FSMs. Each class also has specific functions that help determine the current state. The main part of all these classes is their `validate_x` functions. These functions are passed the current character from the main lexer and return a state and a Boolean value that tells us if the current token was terminated. We update the `input_char_terminates_token` Boolean if we get to the end of the token and make sure that we still return a proper state that we can use in our lexer to properly identify the token and separate the lexeme. 

Each of our files that contain our classes also has individual testing code that only gets run if you run those files individually. This code was used for testing the individual FSMs to verify they were working. 

In our FSMs, we included transition tables to determine what state to go to given certain inputs, which is the main driver of all our functions along with `validate_x` which uses the FSMs to return the state and terminated-token status. These transition tables came from us converting our non-deterministic FSMs into deterministic FSMs for easier code implementations. 

For separators, operators, and keywords, we didn’t implement FSMs, but we did implement a buffer to determine if the input string matched one of these. Each of these three internally tracked the characters they were receiving and added them to a buffer. If the elements in the buffer matched with any of the items we had in lists, then it would correctly identify that as the token and lexeme. 

In our main file, we import all the classes that we need, define the main lexer function, and then call it given the content of the input file as an argument. Our lexer iterates over all the characters in our input file until it reaches the end. One of the first things that it does is check if there are any comments to skip them so they don’t get fed into our FSMs. Next, the character is fed through all the FSMs and the buffer functions. If any of them return true for the state and the input character terminates the token, then the token gets selected, and the lexeme is created, and both are appended to the output file. We also have code that traverses whitespace after a lexeme has been created so we don’t have to feed that into each FSM.
