"""Use loops to make all the lyrics of "99 bottles of beer on the wall"  print on the screen. Adjust the last
two verses for correct grammar:"""

bottles = 99
for bottles in range(99, -1, -1):
    if bottles > 2:
        print(bottles, "bottles of beer on the wall")
        print(bottles, "bottles of beer")
        print("Take one down, pass it around")
        print(bottles - 1, "bottles of beer on the wall\n")
    elif bottles == 2:
        print(bottles, "bottles of beer on the wall")
        print(bottles, "bottles of beer")
        print("Take one down, pass it around")
        print(bottles - 1, "bottle of beer on the wall \n")
    elif bottles == 1:
        print(bottles, "bottle of beer on the wall")
        print(bottles, "bottle of beer")
        print("Take one down, pass it around")
        print(bottles - 1, "bottles of beer on the wall")
