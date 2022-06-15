import ConvertColorToPairNumber
MAJOR_COLORS = ['White', 'Red', 'Black', 'Yellow', 'Violet']
MINOR_COLORS = ["Blue", "Orange", "Green", "Brown", "Slate"]
def DisplayColorCodeReferenceManual():
  for i in MAJOR_COLORS:
      for j in MINOR_COLORS:
          pair_num = ConvertColorToPairNumber.get_pair_number_from_color(i,j)
          print(pair_num,"\t",i,"\t",j,"\n")
