import math
def newline():
  print()
print('Remember, quadratic equations ALWAYS take the form of ax² + bx + c = 0')

a = int(input('A = '))
b = int(input('B = '))
c = int(input('C = '))
newline()

#      _  /=========
# -b +- \/ b^2 -4ac
# --------------------
#          2a

if ((b)**2 - 4*a*c) < 0:
  print('No "real" solutions, since the discriminant is negative. If you try plugging it into your calculator, you get a math error.')
else:
  answerDec1 = -b + math.sqrt((b)**2 - 4*a*c) / 2*a
  answerDec2 = -b - math.sqrt((b)**2 - 4*a*c) / 2*a
  
  answerSurd = (b)**2 - 4*a*c

  if answerDec1 == answerDec2:
    print('Decimal Form:')
    print(answerDec1)
  else:
    print('Decimal Form:')
    print(answerDec1)
    print(answerDec2)
    newline()
  print('Surd Form:')
  if b < 0:
    print(b,'±√',answerSurd)
  print('-',b,'±√',answerSurd)
  print('--------')
  print('  ', 2*a, '  ')
