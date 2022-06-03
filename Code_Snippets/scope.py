#!/usr/bin/env python3

# scope order: => local => parent => global => python functions like sum()
a = 10
def parent():
    a = 6
    def child():
        a = 8
        return a
    return child()
    
    # return a
print(parent())
print(a)

b = 5
def simple():
    b = 1
    return b
print(b)
print(simple())