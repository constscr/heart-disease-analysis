from pathlib import Path

import pandas as pd

from scripts.logger import setup_logger

# Initialization of the logger
logger = setup_logger(__name__)


def save_dataset(df: pd.DataFrame, dir_path: str, file_name: str) -> None:
    """
    Saves a DataFrame to the specified directory with the given file name.
    Creates the directory if it does not exist.

    Args:
        df (pd.DataFrame): The DataFrame to be saved.
        dir_path (str): Relative or absolute path to the target directory.
        file_name (str): Name of the file to save (e.g., 'dataset.csv').
    """
    target_dir = Path(dir_path)
    target_dir.mkdir(parents=True, exist_ok=True)

    # Construct the file path and save the data to a new CSV file
    file_path = target_dir / file_name
    df.to_csv(file_path, index=False)

    # Log the successful save result
    logger.info("Saving data...")
    logger.info(f"Data successfully saved to file: {file_path}")
    logger.info(f"Dataset dimensions: {df.shape[0]} rows, {df.shape[1]} columns.")
