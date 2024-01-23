using System;
using Microsoft.VisualBasic.FileIO;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;

/* 
    This program was made entirely with chat gpt.
    The prompts used to make this program were:
        -What is a dynamic array in c#
        -How can you read multiple rows and collumns of data into a dynamic array in c# 
        -As a csv file
        -How could I sort the data alphabetically based on a specified data
        -How could I easily find the length of the dynamic array
*/


class Program
{
    static void Main()
    {
        // Specify the path to your CSV file
        string csvFilePath = @"D:\DSU classes\Spring 2024\Advanced Data Structures\Advanced-Data-Structures\Homework 1\us-contacts (2).csv";

        // Creating a dynamic array to store CSV data
        List<List<string>> contacts = ReadCsvFile(csvFilePath);

        // Sorting the dynamic array alphabetically based on the first column
        Sortcontacts(contacts, columnIndex: 1);

        // Accessing and printing the CSV data
        PrintCsvData(contacts);
    }

    static List<List<string>> ReadCsvFile(string filePath)
    {
        List<List<string>> contacts = new List<List<string>>();

        using (TextFieldParser parser = new TextFieldParser(filePath))
        {
            parser.TextFieldType = FieldType.Delimited;
            parser.SetDelimiters(",");

            while (!parser.EndOfData)
            {
                string[] fields = parser.ReadFields();
                List<string> row = new List<string>(fields);
                contacts.Add(row);
            }
        }

        return contacts;
    }

    static void Sortcontacts(List<List<string>> contacts, int columnIndex)
    {
        contacts.Sort((a, b) => string.Compare(a[columnIndex], b[columnIndex], StringComparison.OrdinalIgnoreCase));
    }


    static void PrintCsvData(List<List<string>> contacts)
    {
        // Printing the CSV data starting at the 50th eleement and printing every 50 after that 
        int i = 49;

        while (i <= contacts.Count)
        {
            foreach (string field in contacts[i])
            {
                Console.Write($"{field} ");
            }
            Console.WriteLine();
            i += 50;
        }
    }
}
