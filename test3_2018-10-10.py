#One-way Decisions
#x = 5
#if x > 2 :
#   print('Bigger than 2')
#   print('Still bigger')
#print('Done witn 2')
#For i in range(5):
#  print(i)
#   if i > 2:
#     print('Bigger than 2')
#  print('Done with i',i)
#print('All Done')

#Nested Decisions
   #x = 42 
   #if x > 1:
    #  print('More than one ')
    #  if x < 100:
    #     print('Less than 100')
   #print('All done')

#Two-way Decisions

#x = 4
#if x > 2 :
#   print('Bigger')
#else:
#   print('Smaller')
#print('All done')

Mark = input("Enter your Mark:")
x = float(Mark)

if x >= 0.9 :
   print('A')
elif x >=0.8:
   print('B')
elif x >=0.7:
   print('C')
elif x >=0.6:
   print('D')
elif x <0.6:
   print('F')
elif x >1:
   print('Error')
elif x <0:
   print('Error')
print(x)

