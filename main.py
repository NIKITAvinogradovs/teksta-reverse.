teksts = input ("Ievadi tekstu: ")
def reverseWords(teksts):
  sar1 = teksts.split()
  if len(sar1)>1:
    sar1.reverse()
    teksts=" ".join (sar1)
    print(teksts)
  else:
    teksts = "parak iss teikums"
    print(teksts)
  return teksts
reverseWords(teksts)