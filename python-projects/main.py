import random
import time
live = 0
blank = 0
liveblank = 0
bullets = 0
playerLives = 3
dealerLives = 3

print('They enter the chamber in a hidden sequence')
bullets = random.randint(3,8)
#print('bullets')
#print(bullets)
while live+blank != bullets:
	if random.randint(1,2) == 1:
		live += 1
		#print('live')
		#print(live)
	else:
		blank += 1
		#print('blank')
		#print(blank)
	liveblank += 1
	#print('liveblank')
	#print(liveblank)

print(live, 'live rounds..')
print(blank, 'blank rounds..')

while playerLives != 0 or dealerLives != 0:

	playerChoice = input('You or Dealer? Y/D \n')
	if playerChoice == ('Y'):
		print('You point the barrel towards yourself.')
		time.sleep(2)
		if random.randint(1,2) == 1:
			live -= 1
			print('Bang.')
			time.sleep(2)
			print('The defibrillator goes off.')
			playerLives -= 1
			print('Player lives left:')
			print(playerLives)
		else:
			blank -= 1
			print('Click.')
	elif playerChoice == ('D'):
		print('You point the barrel towards the dealer.')
		time.sleep(2)
		if random.randint(1,2) == 1:
			live -= 1
			print('Bang.')
			time.sleep(2)
			print('The defibrillator goes off.')
			dealerLives -= 1
			print('Dealer lives left:')
			print(dealerLives)
		else:
			blank -= 1
			print('Click.')