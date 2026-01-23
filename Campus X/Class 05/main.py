# def insert_patient_data(name: str, age: int):

#     print(name)
#     print(age)
#     print('inserted into database')

# insert_patient_data('nitish', 30)

def insert_patient_data(name: str, age: int):
   
   

  if type(name) == str and type(age) == int:
    if age < 0:
      raise ValueError('Age cannot be negative')
    else:
     print(name)
     print(age)
     print('inserted into database')
  else :
    raise TypeError('Invalid data types for name or age')


insert_patient_data('nitish', 30)

def update_patient_data(name: str, age: int):

  if type(name) == str and type(age) == int:
    print(name)
    print(age)
    print('inserted into database')
  else :
    raise TypeError('Invalid data types for name or age')


insert_patient_data('nitish', 30)