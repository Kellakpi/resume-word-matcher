# Resume word matcher

A python script that compares a resume against a job description and highlights matching and missing keywords.

---

## Features

-  Reads `.txt` files for resume and job listing
-  Converts text to lowercase
-  Removes common stopwords
-  Finds matching keywords
-  Highlights missing job description keywords not found in the resume
-  Saves results to `Review.txt`

---

## How to use

1. Clone the repo:
>>bash
>>git clone https://github.com/Kellakpi/resume-word-matcher.git
>>cd resume-word-matcher
2. Run the script : >>"python matcher.py"
2. Add the resume and the job description on the right files
3. Run the program by adding the file names

---

## TODO

- Improve Useless word finder, to remove punctuation.
- Add GUI 
- Improve similarity scoring

---

Built by @Kellakpi
