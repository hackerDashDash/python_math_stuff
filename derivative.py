import re
import string
import os
alph = string.ascii_lowercase+string.ascii_uppercase
def checkvar(s):
    s = s.replace("+","")
    s = s.replace("-","")
    s = s.replace("/","")
    s = s.replace("*","")
    if re.sub("[^0-9]","",s) == s:
        return False
    else:
        return True
def removespaces(s):
    return s.replace(" ","")
def isStr(s):
    if s in list(alph):
        return True
    else:
        return False
def clear():
  return os.system("clear")
def getco(t):
    co = ""
    for i in list(alph):
        if i in t:
            co += i
    number = t.replace(co,"")
    if number == "":
      number = "1"
    return number

def derive(s):
    s = removespaces(s)
    terms = re.split(", |/|\-|\*|\+",s)
    st = ""
    for i in terms:
        if checkvar(i):
            if i.find("^"):
                variable = i.split("^")[0]
                if len(i.split("^"))>=2:
                    exp = str(int(getco(i.split("^")[0])) * int(i.split("^")[1]))+"x"
                    expm1 = "^"+str(int(i.split("^")[1]) - 1)
                    
                else:
                    exp = str(int(getco(i.split("^")[0])) * 1)
                    expm1 = "^0"
                if expm1 == "^1":
                    expm1 = ""
                if expm1 == "^0":
                    variable = re.sub("[^0-9]","",variable)
                    expm1 = ""
                if len(list(s.partition(i)[2]))>=1:
                    operation = list(s.partition(i)[2])[0]
                else:
                    operation = ""
                if exp == "1":
                    exp = ""
                if not checkvar(s.partition(i)[2]):
                    operation = ""
                st += exp+expm1+operation
    return st
