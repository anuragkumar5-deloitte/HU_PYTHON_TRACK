#write a decorator which will take a function and execute it twice.
#Function is -
#def multiply(num1, num2):
#    print(num1 * num2)

def do_twice(func):
  def inner(num1,num2):
    if num1<num2:
      num1,num2=num2 ,num1
      func(num1,num2)
      return func(num1,num2)
  return inner

@do_twice
def multiply(num1,num2):
  print(num1*num2)

multiply(4,5)
