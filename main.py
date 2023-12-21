# function troopSum
def troopSum(x):
   y = 0
   i = 0
   while i < len(x):
       y+= x[i]
       i+=1
   return y


# function troopLeadersSum
def troopLeadersSum(x):
   y = 0
   i = 0
   while i < len(x):
       if x[i] > x[0]:
           y += x[i]
       i += 1
   if y > 0:
       return y
   else:
       return -1

# function spyAttack
def spyAttack(x):
   y = 0
   i = 0
   while i < len(x)-1:
       if x[i] == x[-1]:
           return True
           break
       i += 1

   return False


# function commanderTracker
def commanderTracker(x):
   return min(x,key=x.count)


# function avgAttackStrength
def avgAttackStrength(x):
  x.sort()
  z = len(x)
  x.remove(x[0])

  y = 0
  i=0
  while i<len(x):
      y += x[i]
      i+=1
  return y/z

print(troopSum([-99,1,2,3,4,5,6,7,8,9,10,12345]))
print(troopLeadersSum([-99,1,2,3,4,5,6,7,8,9,10,5]))
print(spyAttack([-99,1,2,3,4,5,6,7,8,9,10,5]))
print(commanderTracker([-99,1,2,3,4,5,6,7,8,9,10,5]))
print(avgAttackStrength([-99,1,2,3,4,5,6,7,8,9,10,5]))
