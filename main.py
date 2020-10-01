
def f1(a):
  absN=abs(a)
  return absN

def f2(n):
  sum=0
  for i in range (0,n):
    number=int(input("Enter an integer: "))
    sum+=f1(number)
  return sum 

def run():
  while(True):
    n= int(input("Enter an integer(must be equal or greater than 0): "))
    if n<=0:
      print("Error")
    else:
      break
  nn=f2(n)
  print(f"answer is {nn}.")


if __name__ == "__main__":
	run()