def algoritm():
  numbers = []
  for i in range(8):
    for j in range(i+1, 9):
      for k in range(j+1, 10):
        number = str(i)+str(j)+str(k)
        numbers.append(number)
  return(numbers) 


print(algoritm()) 
