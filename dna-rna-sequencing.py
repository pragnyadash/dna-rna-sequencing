
def shippingLabel(seq):
  res=""
  i=1
  if len(seq)<3:
    return None

  while(i<len(seq)):
    if seq[i+1]=="d":
      if len(res)>0 and res[len(res)-1]=="]":
        res = res[:-1]+seq[i]+"]"
      else:
        res=res+"["+seq[i]+"]"
    else:
      res=res+seq[i]
    i=i+4
  return res
  
  
print(shippingLabel(seq))


baseMassMap = {"A":1, "G":2, "C":3, "T":4, "U":5, "R":6, "Y":7, "S":8, "W":9, "K":10, "M":11, "B":12, "D":13, "H":14, "V":15, "N":16}

linkageMassMap = {"o":1, "s":2}

def countSeq(seq):
  linkage=0
  bases=0
  lcount=0
  bcount=0
  
  i=1
  if len(seq)<2:
    return None
  while(i<len(seq)):
    bcount += baseMassMap[seq[i]]
    bases += 1
    try:
      seq[i+2]
    except:
      pass
    else:
      lcount += linkageMassMap[seq[i+2]]
      linkage += 1
    i += 4
  return linkage,lcount,bases,bcount
  
  
print(countSeq(seq))


modifiers= ["-", "m", "b", "d"]
bases = ['A', 'G', 'C', 'T', 'U', 'R', 'Y', 'S', 'W', 'K', 'M', 'B', 'D', 'H', 'V', 'N']
sugars = ['d', 'r', 'e', 'm', 'y', 'l', 'k', 'o']
linkages = ['o', 's']

def confirmSeq(seq):
  i=0
  flag = "Success"
  if len(seq)%4 != 3:
    return "Failure"
  while(i<len(seq)):
    #Check modifier
    if seq[i] in modifiers:
      pass
    else:
      flag = "Failure"
      break
    #Check base
    try:
      seq[i+1]
    except:
      break
    if seq[i+1] in bases:
      pass
    else:
      flag = "Failure"
      break
    #Check sugars
    try:
      seq[i+2]
    except:
      break
    if seq[i+2] in sugars:
      pass
    else:
      flag = "Failure"
      break
    #Check linkages
    try:
      seq[i+3]
    except:
      break
    if seq[i+3] in linkages:
      pass
    else:
      flag = "Failure"
      break
    i += 4
  return flag
  
  
print(confirmSeq(s))

