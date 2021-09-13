def input_param_box(box):
    for i in range(3):
        box.append(int(input()))
    return sorted(box)


box_first, box_second = [], []
box_first = input_param_box(box_first)
box_second = input_param_box(box_second)

if box_second == box_first:
    print("Boxes are equal")

elif all(x <= y for x, y in zip(box_first, box_second)):
    print("The first box is smaller than the second one")

elif all(x >= y for x, y in zip(box_first, box_second)):
    print("The first box is larger than the second one")

else:
    print("Boxes are incomparable")
