import random
import math

def main():
  get_level() 
  
def get_level():
    while True:
      try:
        levelp = int(input("Choose Level 1 or 2 or 3: "))
        break
      except ValueError:
        continue
      except KeyboardInterrupt:
        print("You don't exit that easily complete the game first")
    
    generate_integer(levelp)

def generate_integer(b):
  if b == 1:
    sum = 0
    for i in range(1,17):
      try:
        x = random.choice([1,2,3,4,5,6,7,8,9])
        y = random.choice([1,2,3,4,5,6,7,8,9])
        inputp= int(input(f"{x} + {y} = "))
        if x+y == inputp:
          sum1 = sum + i
        else:
          print("EEE")
          continue
      except ValueError:
        print("EEE")
        continue
      except KeyboardInterrupt:
        print("You don't exit that easily complete the game first")
        continue
    print(f"Score is {sum1}")
  elif b == 2:
    sum = 0
    for i in range(1,18):
      try:
        x = random.choice([1,2,3,4,5,6,7,8,9])
        y = random.choice([1,2,3,4,5,6,7,8,9])
        t = random.choice(["+", "-"])
        inputp= int(input(f"{x} {t} {y} = "))
        if t == "+":
          if x + y == inputp:
            for j in range(1, 18):
              sum = sum + j
              break
          else:
            print("EEE")
            continue
        elif t == "-":
          if x - y == inputp:
            for j in range(1, 18):
              sum= sum + j
              break
          else:
            print("EEE")
            continue
      except ValueError:
        print("EEE")
        continue
      except KeyboardInterrupt:
        print("You don't exit that easily complete the game first")

    print(f"Score is {sum} ")
  elif b == 3:
    sum = 0
    for i in range(1, 18):
      try:
        x = random.choice([1,2,3,4,5,6,7,8,9])
        y = random.choice([1,2,3,4,5,6,7,8,9])
        t = random.choice(["+", "-", "*", "/"])
        inputp= int(input(f"{x} {t} {y} = "))
        if t == "+":
          if x + y == inputp:
            for j in range(1, 18):
              sum = sum + j
              break
          else:
            print("EEE")
            continue
        elif t == "-":
          if x - y == inputp:
            for j in range(1, 18):
              sum= sum + j
              break
          else:
            print("EEE")
            continue
        elif t == "*":
          if x * y == inputp:
            for j in range(1, 18):
              sum = sum + j
              break
          else:
            print("EEE")
            continue
        elif t == "/":
          print("Just put integer value of division")
          float(x)
          float(y)
          if x/y == float(inputp):
            for j in range(1, 18):
                sum= sum + j
                break
            else:
              print("EEE")
              continue
      except ValueError:
          print("EEE")
          continue
      except KeyboardInterrupt:
         print("You don't exit that easily complete the game first")

    print(f"Score is {sum} ")
       
if __name__ == "__main__":
    main()