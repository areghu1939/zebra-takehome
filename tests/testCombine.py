import sys
import pathlib
import os
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)
import combine_csv
import glob
import pandas as pd


this_file_path = pathlib.Path(__file__).resolve().absolute()
test_directory = this_file_path.parent

def testCombineCSV():
    # Gather input csv files as list.
    input_dir = f"{test_directory}/mock_data"
    input_files = glob.glob(f"{input_dir}/*.csv")

    cast_to_string = lambda x: (str(x))
    expected_df = pd.read_csv(f"{test_directory}/expected.csv",converters={'Phone Number':cast_to_string})

    actual_df = combine_csv.combineInputs(input_files)

    if actual_df.equals(expected_df):
        print("Combine CSV test passed!")
    else:
        print("Combine CSV test failed!")
    # return


testCombineCSV()
