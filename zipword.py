import zipfile
import time

folderpath = input('Path to the file: ')
zipf = zipfile.ZipFile(folderpath)

global result
result = 0
global tried
tried = 0
c = 0

if not zipf :
  print("The zipped file/folder is not password protected! You can successfully open it!")
else :
  startTime = time.time()
  wordlistFile = open('wordlist.txt', 'r', errors='ignore')
  body = wordlistFile.read().lower()
  words = body.split('\n')

for i in range(len(words)) :
  word = words(i)
  password = word.encode('utf-8').strip()
  c = c + 1
  print('Trying to decode password by: {}'.format(word))

  try :
    with zipfile.ZipFile(folderpath, 'r') as zf :
      zf.extractall(pwd=password)
      print("Success! The password is " + word)
      endTime = time.time()
      result = 1
      break
  except :
    pass

duration = endTime - startTime
if result == 0 :
  print("We took {c} tries in {duration} seconds and we failed to crack the password.")
elif result == 1 :
  print("We successfully cracked the password! This took {c} tries in {duration} seconds.")