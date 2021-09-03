import pandas as pd
import glob
import pathlib
import os
import logging

this_file_path = pathlib.Path(__file__).resolve().absolute()
root_directory = this_file_path.parent


def makeDirectory(directory):
    """
    Creates a directory if it does not exist.

    :param directory: The directory to create.
    """

    output_dir = pathlib.Path(directory)
    exists = output_dir.is_dir()
    if not exists:
        output_dir.mkdir(parents=True)

def combineInputs(csvs):
    """
    Creates a combined DataFrame from input csvs.

    :param csvs: The list of input csvs.
    """
    # Only keep columns needed for final schema format.
    col_list = ["Provider Name", "CampaignID", "Cost Per Ad Click", "Redirect Link", "Phone Number", "Address", "Zipcode"]

    # Lambda functions to convert csv input types.
    cast_to_string = lambda x: (str(x))
    cast_to_float = lambda x: (float(x.replace('"', '')))

    # Read input csv files and convert to expected types for the
    # Phone Number and Cost Per Ad columns.
    df_from_each_file = (pd.read_csv(f, index_col=False, header=0, usecols=col_list, converters={'Phone Number':cast_to_string, 'Cost Per Ad Click':cast_to_float})[col_list] for f in csvs)

    # The csvs as a concatenated DataFrame.
    concatenated_df = pd.concat(df_from_each_file, ignore_index=True)

    # Print the rows in the DataFrame which contain 'NaN' values - excluding
    # the 'Phone Number' column which is nullable.
    null_df = concatenated_df[concatenated_df.isnull().any(axis=1)]
    logging.error(f"The following rows contained 'NaN' values for non-nullable columns:\n {null_df}")
    # Drop rows with NaN values in nullable columns.
    nan_removed = concatenated_df.dropna(subset=['Provider Name','CampaignID','Cost Per Ad Click','Redirect Link','Address','Zipcode'])
    return nan_removed


def main():
    """
    For a given input of CSVs, combines the CSVs and returns a unified CSV
    in the expected schema.

    :return: Combined CSV file in expected schema format.
    """
    # Gather input csv files as list.

    input_dir = f"{root_directory}/inputs"
    input_files = glob.glob(f"{input_dir}/*.csv")

    combined_df = combineInputs(input_files)

    # Create output directory
    directory = os.path.join(root_directory, "output")
    makeDirectory(directory)

    final_path = os.path.join(
        directory,
        "output.csv",
    )

    # Write output csv to output directory.
    combined_df.to_csv(final_path)


if __name__ == "__main__":
    main()