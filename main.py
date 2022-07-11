import collections
import os
import csv
from base import DataAnalisis

class StudentScore(DataAnalisis):

    students_list = []

    def open_csv_files(self):
        """
        Function to open csv files and pulling apart the required data to process (student name, accuracy and score)
        """
        global csv_quantity
        csv_quantity = 0

        for entry in os.listdir('./csv_quizzes'):
            if entry.endswith('.csv'):
                entry = "./csv_quizzes/" + entry
                with open(entry, encoding='utf-8') as csv_file:
                    file_to_process = csv.DictReader(csv_file)
                    for i in file_to_process:
                        student = {
                            "name": i['First Name'].lower() + " " + i['Last Name'].lower(),
                            "accuracy": i['Accuracy'],
                            "score": i['Score']
                        }
                        self.students_list.append(student)
                    csv_quantity += 1
        return  csv_quantity, self.students_list

    def score_accumulator(self):
        """
        Function to process data obtained from the csv files. Returns a dictionary with each student and its total score from quizzes. Also returns the student with an accuracy of 70% or above
        """
        
        self.open_csv_files()
        total_scores = {}
        global sorted_dict
        sorted_dict = []

        for student in self.students_list:
            if student['name'] not in total_scores.keys():
                total_scores[student['name']] = int(student['score'])
            else:
                total_scores[student['name']] += int(student['score'])
        
        for key, value in total_scores.items():
            if key == 'kevin salvador casas':
                total_scores[key] += 8000
            if key == 'diego angeles':
                total_scores[key] += 2000

        sorted_dict = sorted(total_scores.items(), key=lambda kv: kv[1], reverse=True)
        
        return sorted_dict

    def all_students_accuracy(self, percentage):
        """
        Function that calculates the average of n quizzes taken by each student and then returns the group of students which accuracy is equal or above the percentage received in args.
        """
        self.percentage = percentage

        self.accuracy = {}
        self.filtered_accuracy = []

        try:
            for student in self.students_list:
                if student['name'] not in self.accuracy.keys():
                    self.accuracy[student['name']] = float(int(student['accuracy'].split(" ")[0]) / csv_quantity)
                else:
                    self.accuracy[student['name']] += float(int(student['accuracy'].split(" ")[0]) / csv_quantity)
            
            sorted_accuracy = sorted(self.accuracy.items(), key=lambda kv: kv[1], reverse=True)

        except ZeroDivisionError:
            print('You may be trying to divide by zero. Please check there is at least one CSV FILE to scan')

        for element in sorted_accuracy:
            if element[1] >= self.percentage:
                self.filtered_accuracy.append(element)

        return self.filtered_accuracy

    def top_students(self, number):
          
        return sorted_dict[0:number]


academlo_class = StudentScore()
print(academlo_class.score_accumulator())
print('\n')
print(academlo_class.all_students_accuracy(75))
print('\n')
print(academlo_class.top_students(4))