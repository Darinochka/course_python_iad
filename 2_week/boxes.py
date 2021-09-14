box_first = [int(input()) for i in range(3)]
box_second = [int(input()) for i in range(3)]


if box_second == box_first:
    print("Boxes are equal")

elif all(x <= y for x, y in zip(box_first, box_second)):
    print("The first box is smaller than the second one")

elif all(x >= y for x, y in zip(box_first, box_second)):
    print("The first box is larger than the second one")

else:
    print("Boxes are incomparable")
