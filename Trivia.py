import ui, json, requests, random, console, time

#Dummy variable to remember users last guess		
lastGuess = ''

def pressA(sender):
	global lastGuess
	lastGuess = 'A'

def pressB(sender):
	global lastGuess
	lastGuess = 'B'

def pressC(sender):
	global lastGuess
	lastGuess = 'C'

def pressD(sender):
	global lastGuess
	lastGuess = 'D'
	
	#Escape HTML
def format_text(text):
	text = text.replace('&quot;', '"', 15)
	text = text.replace('&amp;', '&', 15)
	text = text.replace('&#039;', '', 15)
	text = text.replace('&deg;', '°')
	text = text.replace('&euml;', 'ë')
	text = text.replace('&uuml;', 'ü')
	text = text.replace('&Eacute;', 'É')
	text = text.replace('&eacute;', 'é')
	text = text.replace('&oacute;', 'ó')
	text = text.replace('&sup2;', '²')
	return text

v = ui.load_view('Trivia')
v.present('sheet')

def askQuestion():
	global v
	v['questionBox'].text = question
	v['optionA'].text = options[0]
	v['optionB'].text = options[1]
	v['optionC'].text = options[2]
	v['optionD'].text = options[3]


#Download JSON data
url = 'https://www.opentdb.com/api.php?amount=10&type=multiple'

response = requests.get(url)
response.raise_for_status()

#Load JSON data into Python variable
trivia = json.loads(response.text)

score = 0
for i in range(10):
	options = []
	correct_answer = format_text(trivia['results'][i]['correct_answer'])
	options.append(correct_answer)
	for option in trivia['results'][i]['incorrect_answers']:
		options.append(format_text(option))
		
	random.shuffle(options)
	
	question = format_text(trivia['results'][i]['question'])
	
	if options.index(correct_answer) == 0:
		correct_letter = 'A'
	elif options.index(correct_answer) == 1:
		correct_letter = 'B'
	elif options.index(correct_answer) == 2:
		correct_letter = 'C'
	elif options.index(correct_answer) == 3:
		correct_letter = 'D'
		
	askQuestion()
	
	#Wait for user to make a guess
	while lastGuess == '':
		time.sleep(1)
	
	#Determine if user guessed correctly
	if correct_letter == lastGuess:
		score += 1
		console.hud_alert('Correct!')
	else:
		console.hud_alert('Incorrect: ' + correct_answer, 'error')
	lastGuess = ''
	
def calculatePercent(per, whole):
	return (int(per) / int(whole)) * 100
 
v['questionBox'].text = 'Final Score: ' + str(score) + '/' + str(10) + '\n'
percent = calculatePercent(score, 10)
v['questionBox'].text += str(percent) + '%\n'
if percent < 20.0:
	v['questionBox'].text += 'Ouch, go back to school!'
elif percent >= 20 and percent < 40.0:
	v['questionBox'].text += 'Hideous!!'
elif percent >= 40.0 and percent < 60.0:
	v['questionBox'].text += 'You need to try harder'
elif percent >= 60.0 and percent < 80.0:
	v['questionBox'].text += 'Ehh you did alright'
elif percent >= 80.0 and percent < 100.0:
	v['questionBox'].text += 'So close, yet so far'
elif percent == 100.0:
	v['questionBox'].text += 'You are a Trivia Master!'
		
		
