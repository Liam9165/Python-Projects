print('Welcome to my computer quiz!')

playing = input('Do you want to play? ')

if playing.lower() != 'yes':
    quit()

print('Okay! lets play you get 3 tires! for every question')
score = 0


for x in range(3):
  answer = input('What does CPU stand for? ')

  if answer.lower() == 'central processing unit':
    print('Correct!')
    score += 1
    break
    
  else:
    print('Try again!')


for x in range(3):
  answer = input('What does GPU stand for? ')

  if answer.lower() == 'graphics processing unit':
    print('Correct!')
    score += 1
    break
    
  else:
    print('Try again!')


for x in range(3):
  answer = input('What does RAM stand for? ')

  if answer.lower() == 'random access memory':
    print('Correct!')
    score += 1
    break
    
  else:
    print('Try again!')


for x in range(3):
  answer = input('What does PSU stand for? ')

  if answer.lower() == 'power supply':
    print('Correct!')
    score += 1
    break
    
  else:
    print('Try again!')

print('you got ' + str(score) + ' questions correct!')
print('you got ' + str((score /  4) * 100) + '%.')