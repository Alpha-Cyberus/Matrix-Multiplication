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


mx_list = []                            # collection of every matrix user will generate
mx_result = Matrix(0, 0)                # matrix to hold results


def main():
    mx_count = 2                        # controls how many matrices should be generated
    compatible = False
    while not compatible:
        for i in range(mx_count):
            mx_define(i + 1)
        compatible = compat_test()
    mx_populate()
    mx_confirm()
    mx_multiply()
    print("The product of these matrices is:")
    mx_result.printval()


def mx_define(mxnum):                   # instantiate empty matrix, add to mx_list
    print("Define Matrix %s's dimensions" % mxnum)
    correct = False
    while not correct:
        r = mx_size_set("rows")
        c = mx_size_set("columns")
        correct = mx_size_confirm(mxnum, r, c)
    mx_list.append(Matrix(r, c))
    print("Matrix %s saved" % mxnum)


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


def mx_size_confirm(mxnum, r, c):       # prompt user to confirm matrix dimensions are correct
    print("Matrix %s's dimensions are [%sx%s]. \r\nIs this correct?" % (mxnum, r, c))
    while True:
        yn = input("[y/n]")
        if yn.lower() in ['y', 'yes']:
            return True
        elif yn.lower() in ['n', 'no']:
            break
        else:
            continue


def compat_test():                      # test matrix compatibility
    if mx_list[0].col == mx_list[1].row:
        return True
    else:
        for i in range(len(mx_list)):
            mx_list.pop()
        print("These matrices are incompatible and have been deleted. Matrix 1's columns Matrix 2's rows must be equal values.\r\nExample: [?x3]x[3x?]")


def mx_populate():                      # allow user to populate matrices with values
    print("Input values for each matrix one at a time. Values can be any whole number.")
    for imat in range(len(mx_list)):                # for each matrix
        print("Matrix " + str(imat + 1) + ":")
        for irow in range(mx_list[imat].row):       # for each row
            mx_list[imat].val.append([])
            for icol in range(mx_list[imat].col):   # for every column within each row
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
    print("Each matrix's values are:")
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
