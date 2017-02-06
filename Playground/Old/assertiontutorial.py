'''

Assertion and Exception tutorial

raise-if-not statement

Sanity check for code.

You can place them at the start of a function to check for valid input, and after a function to theck for valid output.

assert Expression[, Arguments]

If it fails, assertionerroris caught. Program terminates and produces a traceback.

'''

def KelvintoFahrenheit(Temperature):
    assert (Temperature >= 0), "Colder than absolutezero!"
    return ((Temperature-273)*1.8)+32

print(KelvintoFahrenheit(273))
print(KelvintoFahrenheit(50))
print(KelvintoFahrenheit(100))
#print(KelvintoFahrenheit(-5)) # Too cold!

'''
Exception handing

Exception - base class for all exceptions
SystemExit - raised by sys.exit() function
AssertionError
ImportError
KeyBoardInterrupt - User interrupts program, Cmd+c
KeyError - Key is not found in dictionary
IOError - input/output operation fails
SyntaxError
ValueError - wrong datatype Arguments

An exception is an event which occurs during the execution of a program that disrupts the normal flow of the programs instructions.

When a python script raises an exception, it must either handle it or it quits

If you are suspicious that your code may raise and exception, you can use a try: block

try:
    #code
except ExceptionI:
    If there is exceptionI, execute this block
    #code
else:
    If there is no exceptionI
    #code
'''
try:
   f = open("testfile", "w")
   f.write("This is my test file for exception handling!!")
except IOError:
   print("Error: can\'t find file or read data")
else:
   print("Written content in the file successfully")
   f.close()

#Trying to open a file without write permission
try:
   fh = open("testfile", "r")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print("Error: can\'t find file or read data")
else:
   print("Written content in the file successfully")

'''
Multiple exceptions in the same clause:

try:
   You do your operations here;
   ......................
except(Exception1[, Exception2[,...ExceptionN]]]):
   If there is any exception from the given exception list,
   then execute this block.
   ......................
else:
   If there is no exception then execute this block.

Finally: finally code block is always executed
try:
   You do your operations here;
   ......................
   Due to any exception, this may be skipped.
finally:
   This would always be executed.
   ......................
'''
try:
   fh = open("testfile", "w")
   try:
      fh.write("This is my test file for exception handling!!")
   finally:
      print("Going to close the file")
      fh.close()
except IOError:
   print("Error: can\'t find file or read data")
