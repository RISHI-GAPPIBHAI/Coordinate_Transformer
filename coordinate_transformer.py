#This program is to find the coordinate of given points in a transformed matrix whose transformations are dicided by the user and also the number of transformations will be decided by the user
#Transformations just follow a simple rule, they have to be linear and also origin is fundamental for all
def dimensions():
  while 1:
    try:
      number=int(input("Tell me the number of basic vectors/axes in your coordinate system"))
    except ValueError:
      print("What the heck DUDE!, give me a valid input")
      continue
    if number<=0:
      print("Number of axes have to be greater than 0")
      continue
    else:
      coordinates(number)
      break

def coordinates(number):
  print("Now, i'd want you to tell me the coordinates of your transformed axes")
  print("For now they are:")
  basis_vector=[[0 for j in range(number)] for i in range(number)]
  for i in range(0,number):
    basis_vector[i][i]=1
  for row in basis_vector:
    print(row)
  for i in range(0,number):
    print("Type in the values for basis vector",i+1)
    while 1:
      j=0
      try:
        while j<number:
          print("It currently looks like",basis_vector[i])
          basis_vector[i][j]=float(input(f"Matrix element [{i+1}][{j+1}] :"))
          print("Now, it looks like",basis_vector[i])
          choice=input("Are you satisfied??(Y/N)")
          if choice.upper().strip()=='Y':
            j=j+1
          else:
            pass
      except ValueError:
        print("What the heck DUDE!, give me a valid input")
        continue
      break
  print("Your transformed axes now look like: ")
  for row in basis_vector:
    print(row)
  transformer(basis_vector,number)


def transformer(axes,number):
  while 1:
    og_cood=input("Now, I'd want you to print the original coordinates of your point seperated by commas")
    og_cood=og_cood.split(",")
    for i in range(0,number):
      og_cood[i]=float(og_cood[i])
    totall=[]
    for i in range(0,number):
      total=0
      for j in range(0,number):
        total+=og_cood[j]*axes[i][j]
      totall.append(total)
    print("Your transformed coordinates are:")
    print(totall)
    choice=input("Are you done??(Y/N)")
    if choice.upper().strip()=='Y':
      break
    else:
      pass
dimensions()
