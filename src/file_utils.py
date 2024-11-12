from typing import List
import os


class FileUtils:
    """
    A utility class for file operations.
    """
    @classmethod
    def read_file(cls, file_name: str) -> str:
        """
        Read content from a file.

        Args:
            file_name (str): Name of the file to read.

        Returns:
            str: Content read from the file.
        """
        with open(file_name, 'r') as f:
            return f.read()

    @classmethod
    def write_file(cls, file_name: str, content: str) -> None:
        """
        Write content to a file.

        Args:
            file_name (str): Name of the file to write.
            content (str): Content to write to the file.
        """
        with open(file_name, 'w') as f:
            f.write(content)

    @classmethod
    def read_multiple_files(cls, file_names: List[str]) -> List[str]:
        """
        Read content from multiple files.

        Args:
            file_names (List[str]): List of file names to read.

        Returns:
            List[str]: List of contents read from the files.
        """
        return [cls.read_file(file_name) for file_name in file_names]

    @classmethod
    def get_company_data_files_list(cls) -> list:
        """
        Get a list of company data files from the 'data/json' directory.

        Returns:
            list: List of file names starting with 'company_' in 'data/json' directory.
        """
        file_list = []
        for file in os.listdir("data/json"):
            if file.startswith("company_"):
                file_list.append(file)

        return file_list
