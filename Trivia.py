import ui, json, requests, random, console
	
	
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

#ui.load_view('selection').present('sheet')

def displayStart(self):
	v = ui.load_view('Trivia').present('sheet')
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


def pressA(sender):
	global correct_letter
	if correct_letter == 'A':
		global score
		score += 1
		console.hud_alert('Correct!')
	else:
		console.hud_alert('Incorrect: ' + correct_answer, 'error')
	
	sender.superview['questionBox'].text = ''
	sender.superview['optionA'].text = ''
	sender.superview['optionB'].text = ''
	sender.superview['optionC'].text = ''
	sender.superview['optionD'].text = ''


def pressB(sender):
	global correct_letter
	if correct_letter == 'B':
		global score
		score += 1
		console.hud_alert('Correct!')
	else:
		console.hud_alert('Incorrect: ' + correct_answer, 'error')

def pressC(sender):
	global correct_letter
	if correct_letter == 'C':
		global score
		score += 1
		console.hud_alert('Correct!')
	else:
		console.hud_alert('Incorrect: ' + correct_answer, 'error')

def pressD(sender):
	global correct_letter
	if correct_letter == 'D':
		global score
		score += 1
		console.hud_alert('Correct!')
	else:
		console.hud_alert('Incorrect: ' + correct_answer, 'error')

v = ui.load_view()
v['questionBox'].text = question
v['optionA'].text = options[0]
v['optionB'].text = options[1]
v['optionC'].text = options[2]
v['optionD'].text = options[3]
v.present('sheet')
