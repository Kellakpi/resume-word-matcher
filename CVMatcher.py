
resfile = input("What is the name of the resume file?") # Take user input
jobfile = input("What is the name of the job file?")

with open(resfile, "r") as fh:     # Open file that the user inputed
    resume_text = fh.read().lower() # read and force characters to be lower case
    wordrf = resume_text.split() # split the string
    

with open(jobfile, "r") as fh:
    job_text = fh.read().lower()
    wordjf = job_text.split() 


uselesswords = {"and", "the", "a", "an", "with", "in", "for", "to", "of", "on", "is","are", "looking", "rest", "we", "experience", "rest,"} # Words that the program should ignore and nor mention on the missing

filtered_resume = set(wordrf) - uselesswords # Filtered resume without the words above.
filtered_job = set(wordjf) - uselesswords

matches = filtered_resume & filtered_job
missing = filtered_job - filtered_resume

print("\nMatching Words:") # Print all the words that match togheter.
for word in sorted(matches):
    print("-", word)

print("\nMissing (in resume)") # Print all the words that are on the job description and not in the resume.
for word in sorted(missing):
    print("-", word)

with open("Review.txt", "w") as output:     #Opens a file with the results.
    output.write("\nMissing (in resume):\n")
    for word in sorted(missing):
        output.write(f"- {word}\n")
    output.write("Matching Words:\n")
    for word in sorted(matches):
        output.write(f"- {word}\n")


print("Resume:\n", resume_text)
print("\nJob Description:\n", job_text)