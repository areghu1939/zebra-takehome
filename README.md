# CSV Combiner

The script `combine_csv.py` takes an input of CSV files and generates a combined output CSV with the desired schema.

## Setup
1. Have python3 and the latest pip installed on your machine.
2. To install requirements enter `python3 -m pip install -r requirements.txt`

## Run the program

- This script assumes you have Python installed on your machine
1. Clone this repository to your personal GitHub account.
2. Open the Zebra directory.
3. Place input csv files in the input folder.
4. In your terminal run `python3 combine_csv.py`. Make sure you are in the 'Zebra' directory you cloned.
5. Check the output folder to see the combined csv output file.

## Run Tests
1. In your terminal run `python3 ./tests/testCombine.py`.
The test checks if given two test input csv files the expected combined output is generated in its DataFrame format.

## Additional Thoughts
1. Additional tests could be written for the function which creates directories.
2. The test compares the equality of two DataFrame objects instead of the actual csv files. In addition the test prints out the lines with errors - which ideally should not be there.
3. Had testing been implemented using pytest - more thorough testing and mock data could have been created.