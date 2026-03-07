import random

def main():
  get_level() 
  
def get_level():
    while True:
      try:
        levelp = int(input("Choose Level 1 or 2: "))
        break
      except ValueError:
          continue
      except KeyboardInterrupt:
        print("If you want exit to it type exit")
    
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
          sum += i
        else:
           print("EEE")
           continue
      except ValueError:
          print("EEE")
          continue
      
      print(f"Score is {sum0}")
  elif b == 2:
    sum = 0
    for i in range(0,17):
      try:
        x = random.choice([1,2,3,4,5,6,7,8,9])
        y = random.choice([1,2,3,4,5,6,7,8,9])
        t = random.choice(["+", "-"])
        inputp= int(input(f"{x} {t} {y} = "))
        if t == "+":
           if x + y == inputp:
              sum0 = sum + i
              print(sum0)
        elif t == "-":
          if x - y == inputp:
            sum0 = sum + i
            print(sum0)
          else:
            print("EEE")
            continue
      except ValueError:
          print("EEE")
          continue
      except KeyboardInterrupt:
         print("Are you want to exit type 'exit")
      
      
    print(f"Score is {sum}")
       
if __name__ == "__main__":
    main()