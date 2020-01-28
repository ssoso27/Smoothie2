class Item:
    def __init__(self, name, idx):
        self.name = name
        self.idx = idx

    def is_a_key(self):
        if self.name == 'key':
            return True
        return False

    def is_a_box(self):
        if self.name == 'box':
            return True
        return False

class Box(Item):
    def __init__(self, idx, items=[]):
        super().__init__("box", idx)
        self.items = items

    def make_a_pile(self):
        return Pile(self.items)


class Key(Item):
    def __init__(self, idx):
        super().__init__('key', idx)

class Pile:
    def __init__(self, boxs):
        self.boxs = boxs

    def grab_a_box(self):
        return self.boxs.pop()

    def is_empty(self):
        if len(self.boxs) <= 0:
            return True
        return False

    def append(self, box):
        self.boxs.append(box)

def find_key_while(main_box):
    print('반복문')
    pile = main_box.make_a_pile()
    while not pile.is_empty():
        box = pile.grab_a_box()
        print('grap a box' + str(box.idx))
        for item in box.items:
            if item.is_a_box():
                print('this is box' + str(item.idx))
                pile.append(item)
            elif item.is_a_key():
                print('this is key' + str(item.idx))

def find_key_recursion(box):
    print('재귀')
    for item in box.items:
        if item.is_a_box():
            print('this is box' + str(item.idx))
            find_key_recursion(item)
        elif item.is_a_key():
            print('this is key' + str(item.idx))
            return

my_box = Box(1, [Box(2, [Box(5, [])]), Box(3, [Key(6)]), Box(4, [])])
# my_box = Box([Box([Box(), Box()]), Box([Box([Box(), Key()]), Box()]), Box()])
find_key_while(my_box)
# find_key_recursion(my_box)