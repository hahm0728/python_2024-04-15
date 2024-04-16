class Person:
  """사람을 나타내는 기본 클래스"""

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"이름: {self.name}, 나이: {self.age}"

class Manager(Person):
  """매니저를 나타내는 클래스"""

  def __init__(self, name, age, department):
    super().__init__(name, age)
    self.department = department

  def __str__(self):
    return f"매니저: {self.name}, 나이: {self.age}, 부서: {self.department}"

class Employee(Person):
  """직원을 나타내는 클래스"""

  def __init__(self, name, age, position):
    super().__init__(name, age)
    self.position = position

  def __str__(self):
    return f"직원: {self.name}, 나이: {self.age}, 직책: {self.position}"

class Alba(Person):
  """알바생을 나타내는 클래스"""

  def __init__(self, name, age, working_hours):
    super().__init__(name, age)
    self.working_hours = working_hours

  def __str__(self):
    return f"알바생: {self.name}, 나이: {self.age}, 근무 시간: {self.working_hours}"

# 예시 사용
person = Person("홍길동", 30)
print(person)

manager = Manager("김철수", 40, "영업")
print(manager)

employee = Employee("이영희", 25, "개발")
print(employee)

alba = Alba("박지영", 20, 10)
print(alba)