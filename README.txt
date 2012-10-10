Test Driven Development
=======================

Introduction
------------
    " [...] I had been a programmer for nearly thirty years before I was 
    introduced to TDD. I did not think anyone could teach me a low level 
    programming practice that would make a difference. Thirty years is a 
    lot of experience after all. But when I started to use TDD, I was 
    dumbfounded at the effectiveness of the technique."
    -- Robert Martin"
        As quoted in 'Test Driven Development in Python'
        Kevin Dahlhausen
        kevin.dahlhausen@keybank.com

Not a new idea.  Back in 1984 we used to develop COBOL programs. I was with the
premier COBOL training course of Van Zyl and Pritchard who employed a similar
idea of the 'dry run', where we wrote the test data and expected results
*before* the code, and then manually traced through the code using the test
data to see the if all the program code objectives are met.

A tedious process. Being a purely manual , it took *ages* - but it worked.  We
all prided ourselves (and were sold to the industry) as developers that who
developed systems that always worked first time - something quite unique.

Manual 'dry runs' are all very good and all, but because of the tedium 
involved, the practice soon falls into disuse,  gets forgotten and buggy 
code ensues.

However, *automating* the dry run - now that is a brilliant idea! It's a
philosophy or development approach rather than a technology, and very
do-able with modern and flexible languages such as Python.

How to Use
----------
If you buy into the idea of Test Driven Development, but have no starting
point, you are in the right place.

tests.py is a frame work, a starting point for any module or script that
is being developed.  As I have stated, TDD is a philosophy or approach as
much as a technology.

The idea is that you copy tests.py to your-script-name.py (along with the
excellent termcolor.py by Konstantin Lepa) into your working directory and
use it as the basis of your own program/module.

Define the modules and tests *first*, then start developing the def
functions and classes from that - beginning the development with a well
defined and coded End in Mind.

When you run your script, run with the parameter --test, and your test
cases with check the validity of the code you have just written. Test
frequently and throughout the development process.

*Important*.  Leave the test case code in the final script, because a
useful module seldom remains for unchanged for long.  When you need to
change or upgrade any of the code, update the test cases with any new
or changed results but otherwise leave the old ones intact.  Develop as
before.  If any of your modifications break old code, old test cases will
reveal that.

Author: Alexander Hughes <aebhughes@gmail.com>
