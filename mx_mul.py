# title and declarations
class Matrix:
    def __init__(self, r, c):
        self.row = r
        self.col = c
        contents = []

    def size(self):
        # return '{}x{}'.format(self.row, self.col)
        return '[%dx%d]' % (self.row, self.col)


mx_list = []
# main menu

# define size of matrices


def mx_size_set(dim):

    print("How many "+dim+"?")
    while True:
        try:
            n = int(input(""))
        except ValueError:
            print("That's not a number. Input a whole number.")
            continue
        if n == 0:
            print("Number must not be 0.")
            continue
        else:
            break
    return n


def mx_size_confirm(mxnum, r, c):

    print("Matrix %s size is [%sx%s] \r\nIs this correct?" % (mxnum, r, c))
    while True:
        yn = input("[y/n]")
        if yn.lower() in ['y', 'yes']:
            print("confirmed yes")
            break
        elif yn.lower() in ['n', 'no']:
            print("confirmed no")
            mx_size(mxnum)
            break
        else:
            continue


def mx_size(mxnum):
    print("Configure Matrix %s" % mxnum)
    r = mx_size_set("rows")
    c = mx_size_set("columns")
    mx_size_confirm(mxnum, r, c)
    mx_list.append(Matrix(r, c))


def define_matrices():
    i = int(1)
    while i <= 2:
        mx_size(i)
        i = i+1
    print("matrix 1 = "+mx_list[0].size())
    print("matrix 2 = "+mx_list[1].size())


define_matrices()

#   confirm if matrices can be multiplied

#       if no return to menu

#       if yes carry on

# begin multiplication

#   iterate through matrices

#   call multiplication module

#   output to result matrix

# display results in eof menu

# multiplication module for single row
# multiplication module for single row
