#!/usr/bin/env python
# coding: utf-8
1.Why are functions advantageous to have in your programs?
ANS-->To reduce the need for duplicate code. 2.When does the code in a function run: when its specified or when its called?
ANS-->The code in a function executes when the function is called, not when the function is defined.3. What statement creates a function?
ANS-->def function(): this statement create function4. What is the difference between a function and a function call?
ANS-->Function is block of code that does some operation, and 
A function call is the code used to pass control to a function.5. How many global scopes are there in a Python program? How many local scopes?
ANS--> The scope of global variables is the entire program whereas the scope of local 
variable is limited to the function where it is defined.6. What happens to variables in a local scope when the function call returns?
ANS-->Each call of the function creates new local variables, and their lifetimes
expire when the function returns to the caller.7. What is the concept of a return value? Is it possible to have a return value in an expression?
ANS-->A return is a value that a function returns to the calling script or function when it completes its task. 
 we can use that value in a math expression or any other kind of expression in which the value has a logical or
coherent meaning.8. If a function does not have a return statement, what is the return value of a call to that function?
ANS-->If the function doesn't have any return statement, then it returns None
or it will return a default value9. How do you make a function variable refer to the global variable?
ANS-->By using global keyword
eg:
     def func():
        global a
        a = "RUTIK"
        print("my name is " + a)10. What is the data type of None?
#ANS-->
type(None)11. What does the sentence import areallyourpetsnamederic do?
ANS-->Give No module Error12. If you had a bacon() feature in a spam module, what would you call it after importing spam?
ANS-->This function can be called with spam. bacon().13. What can you do to save a programme from crashing if it encounters an error?
ANS-->Debugging by try and except code.14. What is the purpose of the try clause? What is the purpose of the except clause?
ANS-->try clause test the code block and except clause help to handle the error.