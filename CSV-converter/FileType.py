"""
Abstract class for both CSV and JSON classes
"""
from abc import abstractmethod


class File:
    def __init__(self, *args, **kwargs):  # real signature unknown
        pass

    @abstractmethod
    def __str__(self, *args, **kwargs):  # real signature unknown
        pass

    @abstractmethod
    def ParseInput(self, *args, **kwargs):  # real signature unknown
        """
        Function where parsing should be performed
        :param args:
        :param kwargs:
        :return:
        """
        pass

    @abstractmethod
    def WriteOutput(self, *args, **kwargs):  # real signature unknown
        """
        Function where file opened in mode=write should be performed
        :param args:
        :param kwargs:
        :return:
        """
        pass

    @staticmethod
    def ReadFile(name):
        # Retrieving the input from the file as list of lists
        with open(name, 'r') as Read:
            data = Read.readlines()

        try:
            # Raising error if no data obtained or only header
            if len(data) == 1 or not len(data):
                raise ValueError("No values in csv file, terminating...")
        except ValueError as v:
            raise SystemExit(v)

        return data
