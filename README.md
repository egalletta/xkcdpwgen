# xkcdpwgen
Constructs complex, easy to use passwords


Created for CY 2550 at Northeastern as a part of analyzing password strengths, based on [xkcd #936](https://xkcd.com/936/)

usage: xkcdpwgen [-h] [-w WORDS] [-c CAPS] [-n NUMBERS] [-s SYMBOLS]

optional arguments:
  -h, --help 
  -w WORDS, --words WORDS  
                        include WORDS words in the password  
  -c CAPS, --caps CAPS  capitalize the first letter of CAPS random words  
  -n NUMBERS, --numbers NUMBERS  
                        insert NUMBERS random numbers in the password  
  -s SYMBOLS, --symbols SYMBOLS  
                        insert SYMBOLS random symbols in the password  
