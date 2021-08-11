#                                       Matrix Multiplier by Alpha_Cyberus (Luffy O'Brien)
class Matrix:
    def __init__(self, r, c):
        self.row = r
        self.col = c
        self.val = []

    def size(self):
        return '[%dx%d]' % (self.row, self.col)

    def printval(self):
        for r in range(len(self.val)):
            print(self.val[r])


mx_list = []
mx_result = Matrix(0, 0)
mxcomp = False


def main():
    for i in range(2):                 # mow many matrices to make
        mx_define(i + 1)
    mx_populate()
    mx_confirm()
    mx_multiply()
    print("The product of these matrices is:")
    mx_result.printval()


def mx_size_set(dim):                   # define size of single matrix dimension
    print("How many "+dim+"?")
    while True:
        try:
            n = int(input())
        except ValueError:
            print("That's not a number. Input a whole number.")
            continue
        if n <= 0:
            print("Number must at least 1.")
            continue
        else:
            break
    return n


def mx_size_confirm(mxnum, r, c):       # prompt user to confirm matrix dimension is correct
    print("Matrix %s's size is [%sx%s] \r\nIs this correct?" % (mxnum, r, c))
    while True:
        yn = input("[y/n]")
        if yn.lower() in ['y', 'yes']:
            print("confirmed yes")
            break
        elif yn.lower() in ['n', 'no']:
            print("confirmed no")
            mx_define(mxnum)
            break
        else:
            continue


def mx_define(mxnum):                     # instantiate empty matrix, add to mx_list
    print("Define Matrix %s's dimensions" % mxnum)
    r = mx_size_set("rows")
    c = mx_size_set("columns")
    # mx_size_confirm(mxnum, r, c)
    # compat_test()
    mx_list.append(Matrix(r, c))


def compat_test():                      # test matrix compatibility for multiplication
    global mxcomp
    if mxcomp:
        mxcomp = False
    if mx_list[0].col == mx_list[1].row:
        print("compatible!")
        mxcomp = True
    else:
        print("These matrices are incompatible and cannot be multiplied. Matrix 1's columns must be equal to Matrix 2's rows.")


def mx_populate():                      # allow user to populate matrices with values
    # loop all matrices
    print("Input values for each matrix one at a time. Values can be any whole number.")
    for imat in range(len(mx_list)):                # loop each matrix
        print("Matrix " + str(imat + 1) + ":")
        for irow in range(mx_list[imat].row):       # loop each row
            mx_list[imat].val.append([])
            for icol in range(mx_list[imat].col):   # loop each column
                print("Element " + str(irow + 1) + "," + str(icol + 1))
                while True:
                    try:
                        newval = int(input())
                    except ValueError:
                        print("That's not a number. Input a whole number.")
                        continue
                    else:
                        break
                mx_list[imat].val[irow].append(newval)


def mx_confirm():                       # display values in all matrices
    print("Values of each matrix are:")
    for imat in range(len(mx_list)):
        print("Matrix " + str(imat + 1) + ":")
        mx_list[imat].printval()


def mx_multiply():                      # multiply matrices together
    for i in range(mx_list[0].row):     # for each row in matrix a
        mx_result.val.append([])
        for j in range(mx_list[1].col):  # for each column in matrix b
            calc = 0
            for k in range(mx_list[1].row):  # for each row within each column in matrix b
                calc = calc + (mx_list[0].val[i][k] * mx_list[1].val[k][j])
            mx_result.val[i].append(calc)


main()
# Changelog v0.2.0a - added - matrix multiplication - improved - prompts
