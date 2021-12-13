Data sets for the challenges should be stored here.

Naming convention follows the same pattern as script naming, but at '.txt' instead of '.py'
eg) day1a.txt, day1b.txt, day2a.txt, etc...

Most (if not all) challenges share data from challenge 'a' with challenge 'b'.
In this case it's recommended to create a symbolic link pointing to data from challenge 'a'.

Eg) In order to create a data file from 'day1a.py' for 'day1b.py', type the following from within './docs/data/'
    $ ln -s day1a.txt day1b.txt