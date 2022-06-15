import ConvertColorToPairNumber
import ConvertPairNumberToColor
import TestColorCodeConversion
if __name__ == '__main__':
  MAJOR_COLORS = ['White', 'Red', 'Black', 'Yellow', 'Violet']
  MINOR_COLORS = ["Blue", "Orange", "Green", "Brown", "Slate"]
  for i in MAJOR_COLORS:
    for j in MINOR_COLORS:
      pair_num = ConvertColorToPairNumber.get_pair_number_from_color(i,j)
      print("Color Code Reference Manual: \n")
      print(pair_num,"\t",i,"\t",j,"\n")
  TestColorCodeConversion.test_number_to_pair(4, 'White', 'Brown')
  TestColorCodeConversion.test_number_to_pair(5, 'White', 'Slate')
  TestColorCodeConversion.test_pair_to_number('Black', 'Orange', 12)
  TestColorCodeConversion.test_pair_to_number('Violet', 'Slate', 25)
  TestColorCodeConversion.test_pair_to_number('Red', 'Orange', 7)
  print('Done :)')
