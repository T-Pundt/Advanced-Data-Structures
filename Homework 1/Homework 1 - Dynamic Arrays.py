# This program was made with chatgpt and a reference to a subreddit
# The link to the reddit post is
# https://www.reddit.com/r/learnpython/comments/xjn9pq/opening_a_text_file_in_the_same_directory/
# The rest of the program was made with chat gpt
# The prompts used to make the program were:
#   -what is a dynamic array in python
#   -How to read a excel file with multiple rows and columns into a list in python
#   -will this work with a csv file
#   -I did that, and it works besides it excludes the first row of data which is located in cell 1A to 1H
#   -How would I sort the data in the list of lists in alphabetical order of a select portion of data
#   -Why lamdbda

def main():
    import pandas as pd
    from pathlib import Path

    # This section of code creates the file pathway that is later used to open the csv file
    # Reference to reddit post was made here
    root_dir = Path(__file__).parent
    file = root_dir / 'us-contacts (2).csv'

    # reads in the data from the csv file, Header = None is to make sure the first line of data is read in
    dataframe = pd.read_csv(file, header=None)

    # converts the csv data stored in dataframe to a list of lists (Dynamic Array)
    contacts = dataframe.values.tolist()

    # sorts the contacts in alphabetical order according to the 1 (technically 2nd) item in the list
    contacts.sort(key=lambda x: x[1])

    i = 49
    while i <= len(contacts):
        print(contacts[i])
        i += 50


if __name__ == '__main__':
    main()
