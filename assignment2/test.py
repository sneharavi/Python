
"
[\s\-]
"
gmi
Match a single character present in the list below [\s\-]
\s matches any whitespace character (equal to [\r\n\t\f\v ])
\- matches the character - literally (case insensitive)
Global pattern flags
g modifier: global. All matches (don't return after first match)
m modifier: multi line. Causes ^ and $ to match the begin/end of each line (not only begin/end of string)
i modifier: insensitive. Case insensitive match (ignores case of [a-zA-Z])
Match 1
Full match	0-1		
Match 2
Full match	1-2		
Match 3
Full match	2-3		
Match 4
Full match	3-4		
Match 5
Full match	4-5		
Match 6
Full match	5-6		
Match 7
Full match	6-7		
Match 8
Full match	14-15	
Match 9
Full match	15-16	
Match 10
Full match	20-21	 
Match 11
Full match	23-24	 
Match 12
Full match	25-26	 
Match 13
Full match	30-31	 
Match 14
Full match	36-37	 
Match 15
Full match	40-41	 
Match 16
Full match	49-50	 
Match 17
Full match	58-59	 
Match 18
Full match	65-66	 
Match 19
Full match	68-69	 
Match 20
Full match	71-72	 
Match 21
Full match	75-76	 
Match 22
Full match	79-80	
Match 23
Full match	87-88	 
Match 24
Full match	89-90	 
Match 25
Full match	94-95	 
Match 26
Full match	97-98	 
Search reference
[\s\-]
                            PREFACE
​
This is a book about the computer language called C. If you are
seeking a book to increase your typing speed, expand on your
knowledge of word processing, or learn the secrets of chip
fabrication and design, this is not the one for you. However , if
you want to become thoroughly familiar with the C programming
language, then you have made a wise choice. For this book is devoted
to just that--to help you become proficient in C.
​
    It is one thing to read about a language; it is quite another to
get involved in it.. The best and most time-effective way to absorb
a language such as C is to have 1 terminal or computer available to
you , preferably at you fingertips. You will be exposed  to well
over 100 C programs in this book.
​
    You are encouraged to experiment with the programs illustrated
in this text. Omit keywords, change a comma to a period, ,
deliberately forget to terminate a statement with the required
semicolon, etc. You can do whatever you want without having to worry
about causing any damage to the computer, because you simply can't.
Play "what if" games to your heart's content. Familiarity with the
language will bring with it greater understanding ;the more you
understand about "C", the more you will enjoy it. ???
​
# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

regex = r"[\s\-]"

test_str = ("							PREFACE\n\n"
	"This is a book about the computer language called C. If you are\n"
	"seeking a book to increase your typing speed, expand on your\n"
	"knowledge of word processing, or learn the secrets of chip\n"
	"fabrication and design, this is not the one for you. However , if\n"
	"you want to become thoroughly familiar with the C programming\n"
	"language, then you have made a wise choice. For this book is devoted\n"
	"to just that--to help you become proficient in C.\n\n"
	"	It is one thing to read about a language; it is quite another to\n"
	"get involved in it.. The best and most time-effective way to absorb\n"
	"a language such as C is to have 1 terminal or computer available to\n"
	"you , preferably at you fingertips. You will be exposed  to well\n"
	"over 100 C programs in this book.\n\n"
	"	You are encouraged to experiment with the programs illustrated\n"
	"in this text. Omit keywords, change a comma to a period, ,\n"
	"deliberately forget to terminate a statement with the required\n"
	"semicolon, etc. You can do whatever you want without having to worry\n"
	"about causing any damage to the computer, because you simply can't.\n"
	"Play \"what if\" games to your heart's content. Familiarity with the\n"
	"language will bring with it greater understanding ;the more you\n"
	"understand about \"C\", the more you will enjoy it. ???\n")

matches = re.finditer(regex, test_str, re.MULTILINE | re.IGNORECASE)

for matchNum, match in enumerate(matches, start=1):
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.
Please keep in mind that these code samples are automatically generated and are not guaranteed to work. If you find any syntax errors, feel free to submit a bug report.
For a full regex reference for Python, please visit: https://docs.python.org/3/library/re.html
