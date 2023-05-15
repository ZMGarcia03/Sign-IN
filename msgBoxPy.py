import msgBoxPy

msgBoxPy.infobox('Title', 'Here is my info message.') # Displays an information box with OK button
msgBoxPy.warningbox('Title', 'Here is my warning message!') # Displays a warning box with OK button
msgBoxPy.errorbox('Title', 'Here is my error message!') # Displays an error box with OK button

answer = msgBoxPy.integerbox(title='Your Age?', prompt='Enter your age: ') # Displays Integer Input
if answer == 'cancel': # Cancel button was selected
    msgBoxPy.errorbox(title='Error', message='Cancelled!')
else: # Integer was input and returned
    msgBoxPy.infobox(title='Your Age?', message='Your age is: {}'.format(answer))

answer = msgBoxPy.retrycancelbox(title='Title', message='Empty') # Displays Retry/Cancel box
if not answer: # Answer was False (Cancel button was selected)
    msgBoxPy.warningbox('Retry?', 'You have cancelled the retry!')
else: # Answer was True (Retry was selected)
    retryAgain()
    
# Displays Select Directory dialog starting at the initial directory "/etc"
myDirectory = msgBoxPy.selectdirectorybox(initialdir='/etc', mustexist=True)
if not myDirectory: # Cancel button was selected
    msgBoxPy.errorbox(title='Error', message='Cancelled!')
else: # Directory was selected and is returned 
    msgBoxPy.infobox(title='Your Directory', message=myDirectory)
    
# Displays a Listbox with the arguments passed and returns the selected argument
answer = msgBoxPy.listbox('Mother', 'Father', 'Brother', 'Sister')
if not answer: # Nothing was selected or window was closed
    msgBoxPy.errorbox(title='Listbox', message='You did not make a selection!')
elif answer == 'Mother':
    msgBoxPy.infobox(title='Listbox', message='Hi, Mom!')
else:
    msgBoxPy.infobox(title='Listbox', message='Hi, family member!')
