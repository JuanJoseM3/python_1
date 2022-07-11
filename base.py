from abc import ABC, abstractclassmethod

class DataAnalisis(ABC):

    """
    Abstract class to determine the methods that will be needed for the child classes obtained from this class.
    """

    @abstractclassmethod
    def open_csv_files(self):
        pass

    @abstractclassmethod
    def score_accumulator(self):
        pass

    @abstractclassmethod
    def all_students_accuracy(self, percentage):
        pass 

    @abstractclassmethod
    def top_students(self, number):
        pass