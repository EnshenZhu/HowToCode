"""
https://www.youtube.com/watch?v=7tCNu4CnjVc&ab_channel=Computerphile

<tree in python>

We are going to convert the expression of 3*(y+x) and 3*y+x into the tree format

"""


class Expr:
    pass


class Times(Expr):
    def __init__(self, l, r):  # l is left and r is right
        self.l = l
        self.r = r

    def __str__(self):
        return str(self.l) + "*" + str(self.r)

    def eval(self, env):
        return self.l.eval(env) * self.r.eval(env)


class Plus(Expr):
    def __init__(self, l, r):
        self.l = l
        self.r = r

    def __str__(self):
        return "(" + str(self.l) + "+" + str(self.r) + ")"

    def eval(self, env):
        return self.l.eval(env) + self.r.eval(env)


class Const(Expr):
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return str(self.val)

    def eval(self, env):
        return self.val


class Var(Expr):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def eval(self, env):
        return env[self.name]


e1 = Times(Const(3), Plus(Var("y"), Var("x")))
e2 = Plus(Times(Const(3), Var("y")), Var("x"))

env = {"x": 2, "y": 4}

print(e1)
print(e1.eval(env))

print(e2)
print(e2.eval(env))
