# REGEX Tutorial

# syntax:
# re.match(pattern, string, flags = 0)
# Returns a match object on success, none on failure.
import re

line = "Cats are smarter than dogs"

matchObj = re.match( r'(.*) are (.*?).*', line , re.M|re.I)

if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))
else:
    print("No match!")

searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)

if searchObj:
   print("searchObj.group() : ", searchObj.group())
   print("searchObj.group(1) : ", searchObj.group(1))
   print("searchObj.group(2) : ", searchObj.group(2))
else:
   print("Nothing found!!")

#Search function
# Searches for the first occurence of RE pattern within string with optional flags.

# re.search(pattern, string, flags = 0)

#Match checks only at the beginning of the string, while search checks for a match anywhere in the string

# Search and replace
#re.sub(pattern, repl, string, max=0)
#This replaces all occurences of the RE pattern in a string with repl, unless max is provided.

phone = "2004-959-559 # This is phone number"

# Delete python-style comments
num = re.sub(r'#.*$', "", phone)
print("Phone num: ", num)

#Remove anyting other than digits
num = re.sub(r'\D',"",phone)
print("Phone num: ", num)

# Option flags
# re.I - Case insensitive matching
# re.L - Interprets words according to current locale
# re.M - Makes $ match the end of a line and makes ^ the start of any line
# re.S - makes a period match any character including a newline
# re.U - interprets letters according to the unicode character set.
# re.X - permits "cuter" regex syntax. Ignores whitespace, treats unescaped # as a comment marker.

# ^ Matches beginning of line
# $ End of line
# . any single character except newline
# [...] any single character in brackets
# [^...] any single char not in brackets
# re* matches 0 or more occurences
# re+ matches 1 or more occurences
# re? matches 0 or 1 occurences
# re{n} exactly n
# re{n,} n or more
# re{n,m} n or more and at most m
# a|b matches a or b
# \w word characters
# \W nonword characters
# \s whitespace
# \S non-whitespace
# \d matches digits
# \D matches non-digits
# \A matches beginning of string
# \G matches where last match finished

# Examples:

# [Pp]ython : Python or python
# rub[ye] : ruby or rube
# [aeiou] : any lowercase vowel
# [0-9] _ match any digit
# [^0-9] : match anything other than a digits
# ruby? : 'y' is Optional
# ruby+ : 'rub' + 1 or more y's
# python|perl : python or perl
# Python$ : match "Python" at the end of a string or line
