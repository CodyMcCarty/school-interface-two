from classes.staff import Staff
from classes.student import Student

class School:
  def __init__(self, name):
    self.name = name
    self.staff = Staff.objects()
    self.students = Student.objects()

  def list_students(self):
    for i,ppl in enumerate(self.students):
      print (f'{i + 1}. {ppl.name} {ppl.school_id} ')

  def find_student_by_id(self, id):
    for ppl in self.students:
      if ppl.school_id == id:
        return ppl
    return "ID not found"
