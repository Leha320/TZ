import random

def generate_math_question(a, b):
    
    num1 = random.randint(a, b)
    num2 = random.randint(a, b)
    operation = random.choice(['+', '-', '*', '/'])
    return f"{num1} {operation} {num2}" 
  

def check_answer(question, user_answer):
  try:
     user_answer = float(user_answer)
  except ValueError:
     return False

  return user_answer == eval(question)
    

    
def eval(question):
  
  num1, operator, num2 = question.split()
  num1 = float(num1)
  num2 = float(num2)
  
  if operator == '+':
    return num1 + num2
  elif operator == "-":
    return num1 - num2
  elif operator == "*":
    return num1 * num2
  elif operator == "/":
    return num1 / num2
  
     
    
  
    
      
def math_quiz(number_of_questions=5):
  correct_answers = 0
  print("Добро пожаловать в математический тест!")
  for _ in range(number_of_questions):
      question = generate_math_question(a=1, b=5)
      user_answer = input(question + ' = ')
      if check_answer(question, user_answer):
          correct_answers += 1
  percentage_correct = (correct_answers / number_of_questions) * 100
  if percentage_correct >= 80:
      percentage_correct = 'Хорошо! Вы получаете оценку A.'
  elif percentage_correct >= 60 and percentage_correct < 80:
      percentage_correct = 'Хорошо! Вы получаете оценку B.'
  else:
      percentage_correct = 'Хорошо! Вы получаете оценку C.'
  print("Тест завершен.")
  print(f"Вы правильно решили {correct_answers} из {number_of_questions} вопросов.")
  print(percentage_correct)

math_quiz(7)
