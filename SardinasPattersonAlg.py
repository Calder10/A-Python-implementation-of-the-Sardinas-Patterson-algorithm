#Implementazione dell'algoritmo di Sardinas-Patterson

# Funzione che costruisce l'insieme S_i
import os
def compute_s_i(c,prec):
  s_i=[]
  for w in c:
    for x in prec:
      if x != w:
        if x.startswith(w):
          s_i.append(x[len(w):])

  for w in prec:
      for x in c:
        if x != w:
          if x.startswith(w):
            s_i.append(x[len(w):])
  s_i=set(s_i)
  s_i=list(s_i)
  s_i.sort()
  return s_i


# Funzione che verifica la prima condizione di arresto
def stop1(c,s_i):
  f=0
  for x in s_i:
    if x in c:
      f=1
      break
  return f

# Funzione che verifica la seconda condizione di arresto
def stop2(s_i):
  f=0
  if(len(s_i)==0):
    f=1
  return f

# Funzione che verifica la terza condizione di arresto
def stop3(S):
  x=len(S)-1
  f=0
  for i in range(x):
    if S[i]==S[x]:
      f=1
  return f

# Funzione che permette all'utente di inserire il codice da tastiera
def load_data():
  print("Inserisci le parole di codice separate da virgola--->")
  c=input()
  c=c.rstrip()
  c=c.lower()
  c=c.split(',')
  os.system('clear')
  return c

# Funzione per la stampa di un report finale
def print_report(S,ud):
  print ("C=" ,end = '')
  print(S[0])
  for i in range (len(S)):
    print("S_%d = "  %(i) ,end = '')
    print(S[i])
  if(ud==0):
    print("Il codice non è UD")
  else:
    print("Il codice è UD")

def spAlg():
  S=[]
  c=load_data()
  S.append(c)
  prev=c
  s_i=[]
  s1=0
  s2=0
  s3=0
  ud=0
  while True:
    curr=compute_s_i(c,prev)
    prev=curr
    S.append(curr)
    s1=stop1(c,curr)
    s2=stop2(curr)
    s3=stop3(S)
    if(s2==1):
      ud=1
      print_report(S,ud)
      break
    if(s1==1):
      ud=0
      print_report(S,ud)
      break
    if(s3==1):
      ud=1
      print_report(S,ud)
      break

#Main Routine
spAlg()

