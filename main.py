from statistician import *  

def main():
    # create a statistician object named s1
    s1 = statistician()

    # display a string representation of a s1
    print(s1)

    # give s1 the number 1.1
    s1.giveNextNum(1.1)

    # display a string representation of a s1
    print(s1)

    # give s1 the number -2.4
    s1.giveNextNum(-2.4)

    # display a string representation of a s1
    print(s1)

    # give s1 the number 0.8
    s1.giveNextNum(0.8)

    # display a string representation of a s1
    print(s1)

    # create a statistician object named s2
    s2 = statistician()

    # display a string representation of a s2
    print(s2)

    # display the result of testing if s1 is equal to s2
    print('Is s1 equal to s2?', s1.__eq__(s2))

    # give s2 the numbers 1.1, -2.4, and 0.8
    s2.giveNextNum(1.1)
    s2.giveNextNum(-2.4)
    s2.giveNextNum(0.8)

    # display a string representation of a s2
    print(s2)

    # display the result of testing if s1 is equal to s2
    print('Is s1 equal to s2?', s1.__eq__(s2))

    # set s2 equal to None
    s2 = None

    # display the result of testing if s1 is equal to s2
    print('Is s1 equal to s2?', s1.__eq__(s2))

    # test giveNextNum to ensure ValueError is being raised when appropriate
    try:
        s1.giveNextNum(5)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()