

layers = [0,1,3,4,5,6]

class Number:
    def __init__(self,layer_number,y):
        self.layer_number = layer_number
        self.y = y


lay1 = Number(layer_number=layers[0],y=int(layers[0]))
lay2 = Number(layer_number=layers[1],y=int(layers[1]))
lay3 = Number(layer_number=layers[2],y=int(layers[2]))


sprite = [lay1,lay2,lay3]

MAX_SPREAD = 10

for i in range(len(sprite)):
    for spread in range(MAX_SPREAD):
        print(sprite[i].y)
        sprite[i].y +=1

