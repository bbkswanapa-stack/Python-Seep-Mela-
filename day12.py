class School():
        def __init__(self, name, *marks):
        self.name = name
        self.marks = marks

        def avg(self):
            if len(self.marks) == 0:
                return "Zero division error", False
            return sum(self.marks) / len(self.marks), True
        
        def grade(self):
            grade_avg = self.avg()
         
            if grade_avg[1]:
                average = grade_avg[0]
                if average >=100:
                    return "A+"
                else:
                    return "F"
            else:
                