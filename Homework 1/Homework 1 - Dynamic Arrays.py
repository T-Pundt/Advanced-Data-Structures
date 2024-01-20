def main():
    import pandas as pd
    from pathlib import Path

    # This section of code creates the file pathway that is later used to open the csv file
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
