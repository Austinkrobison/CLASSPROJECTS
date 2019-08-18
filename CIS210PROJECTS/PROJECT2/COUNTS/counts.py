"""
counts.py: Counts the number of occurrences of each major code in a file.
Authors: Austin Robison

Input is a file in which major codes (e.g., "CIS", "UNDL", "GEOG")
appear one to a line. Output is a sequence of lines containing major code
and count, one per major.
"""

import argparse

def count_codes(majors_file):
    """
    Retrieves a text file containing a list of major codes,
    inserts each code into a list, sorts the codes in alphabetical order,
    counts each unique major code and prints the tally
    by the major code
    """
    majors = [ ]

    for line in majors_file:
        majors.append(line.strip())

    majors = sorted(majors)

    prior = 0
    for major in majors:
        count = majors.count(major)
        if prior != major:
            prior = major
            print(major, count)

def main( ):
    """
    Interaction if run from the command line.
    Usage:  python3 counts.py  majors_code_file.txt
    """
    parser = argparse.ArgumentParser(description="Count major codes")
    parser.add_argument('majors', type=argparse.FileType('r'),
                        help="A text file containing major codes, one major code per line.")
    args = parser.parse_args()  # gets arguments from command line
    majors_file = args.majors
    count_codes(majors_file)
    
    
if __name__ == "__main__":
    main( )
