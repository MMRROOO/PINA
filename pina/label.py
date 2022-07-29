
class Label():
    def __init__(self, comp, derivs, order):
        self._comp = comp
        self._derivs = derivs
        self._order = order
    
    def addorder(self, dir):
        if not dir in self._deriv:
            self._deriv.append(dir)
            self._order.append(1)
        else:
            self._order[self._deriv.index(dir)] +=1
    
    def __str__(self):
        totalorder = 0
        for i in self._order:
            totalorder += i 
        s = 'd' + totalorder
        for i, deriv in enumerate(self._derivs):
            s += 'd' + self._order[i] + deriv
        return s