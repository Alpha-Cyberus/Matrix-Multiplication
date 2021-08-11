#                                       Matrix Multiplier by Alpha_Cyberus (Luffy O'Brien)
class Matrix:
    def __init__(self, r, c):
        self.row = r
        self.col = c
        # values = []

    def size(self):
        return '[%dx%d]' % (self.row, self.col)


mx_list = []
mxcomp = False


def main():
    generate_matrices()
    compat_test()


def mx_size_set(dim):                   # define size of single matrix dimension
    print("How many "+dim+"?")
    while True:
        try:
            n = int(input(""))
        except ValueError:
            print("That's not a number. Input a whole number.")
            continue
        if n <= 0:
            print("Number must at least 1.")
            continue
        else:
            break
    return n


def mx_size_confirm(mxnum, r, c):       # confirm size of single matrix dimension
    print("Matrix %s's size is [%sx%s] \r\nIs this correct?" % (mxnum, r, c))
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


def mx_size(mxnum):                     # instantiate empty matrix, add to mx_list
    print("Configure Matrix %s's dimensions" % mxnum)
    r = mx_size_set("rows")
    c = mx_size_set("columns")
    mx_size_confirm(mxnum, r, c)
    mx_list.append(Matrix(r, c))


def generate_matrices():                # generate n matrices for multiplication
    i = int(1)
    while i <= 2:                       # mow many matrices to make
        mx_size(i)
        i = i+1
    for m in range(len(mx_list)):
        print("matrix " + str(m + 1) + " = " + mx_list[m].size())


def compat_test():                      # test matrix compatibility for multiplication
    global mxcomp
    if mxcomp:
        mxcomp = False
    if mx_list[0].col == mx_list[1].row:
        print("compatible!")
        mxcomp = True
    else:
        print("These matrices are incompatible and cannot be multiplied. Matrix 1's rows must be equal to Matrix 2's columns.")


main()

#                                       populate matrices with values
#                                       begin multiplication
#                                       iterate through matrices
#                                       output to result matrix
#                                       display results

#                                       MATRIX CALCULATION
#                                       compatibility = MX1.col = MX2.rows
#                                       result = MX1.row x MX2.col

# Changelog v0.0.3a - add matrix compatibility testing - fix negative numbers for matrix size - improve comment organization - improve fully dynamic matrix instantiation and referencing
