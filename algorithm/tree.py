class tree():
    def __init__(self , value , position):
        self.children = []
        self.value = value
        self.X_position , self.Y_position = position
    
    def append(self , child):
        self.children.append(child)
    
    def get_children(self):
        return self.children

    def get_position(self):
        return [self.X_position , self.Y_position]
