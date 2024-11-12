import json


class JsonUtils:
    """
    A utility class for reading from and writing to JSON files.
    """
    @classmethod
    def read_json(cls, filename):
        """
        Read JSON data from a file.

        Args:
            filename (str): Path to the JSON file.

        Returns:
            dict: JSON data read from the file.
        """
        with open(filename, "r") as f:
            return json.load(f)

    @classmethod
    def write_json(cls, filename, data):
        """
        Write JSON data to a file.

        Args:
            filename (str): Path to the JSON file to be written.
            data (dict): JSON data to be written to the file.
        """
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    @classmethod
    def to_str(cls, filename: str) -> str:
        """
        Convert JSON data from a file to a formatted string.

        Args:
            filename (str): Path to the JSON file.

        Returns:
            str: Formatted JSON string representation.
        """
        return json.dumps(cls.read_json(filename=filename), indent=4)
