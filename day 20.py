#global
# x=10
# print("outside fn",x)
#
# def fn():
#     print("inside fn",x)
# fn()


#local
# def f():
#     x=10
#     print("inside fn",x)
# f()
#print("outside fn",x) --> this will be error since x is local and not global


# def f():
#     global x #used to change local scope into global
#     x=20
#     print("inside f fn",x)
#
# def g():
#     print(x)
#     y=20
#     print("inside g fn",y)
#
# f()
# g()

#non local
def outer():
    x=20 #--> it can be accessed by both inner and outer fn
    print(x)

    def inner():
        print(x)
        return

    inner()
outer()

#built in
