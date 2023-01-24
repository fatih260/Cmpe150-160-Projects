
# return img, nested list
def read_ppm_file(f):
    fp = open(f)
    fp.readline()  # reads P3 (assume it is P3 file)
    lst = fp.read().split()
    n = 0
    n_cols = int(lst[n])
    n += 1
    n_rows = int(lst[n])
    n += 1
    max_color_value = int(lst[n])
    n += 1
    img = []
    for r in range(n_rows):
        img_row = []
        for c in range(n_cols):
            pixel_col = []
            for i in range(3):
                pixel_col.append(int(lst[n]))
                n += 1
            img_row.append(pixel_col)
        img.append(img_row)
    fp.close()
    return img, max_color_value


# Works
def img_printer(img):
    row = len(img)
    col = len(img[0])
    cha = len(img[0][0])
    for i in range(row):
        for j in range(col):
            for k in range(cha):
                print(img[i][j][k], end=" ")
            print("\t|", end=" ")
        print()


filename = input()
operation = int(input())


# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
if operation == 1:
    minimum = int(input())
    maximum = int(input())


    img, old_max = read_ppm_file(filename)

    old_min=0
    # verilen formülle değerleri değiştiriyorum
    for i in img:
        for j in i:
            for n in range(len(j)):
                j[n] = float('{:.4f}'.format(((j[n]-old_min)/(old_max-old_min))*(maximum-minimum)+minimum))
    img_printer(img)



if operation == 2:
    img, max_color_val = read_ppm_file(filename)
    # her bir channel için verilen formülleri uyguladım
    for w in range(3):
        n = len(img[0])
        sum=0
        for i in img:
            for j in i:
                sum += j[w]
        mean = sum/(n**2)
        befdeviation=0
        for i in img:
            for j in i:
                befdeviation += (j[w]-mean)**2
        deviation=(befdeviation/(n**2))**0.5 + 10**(-6)
        for i in img:
            for j in i:
                j[w] = float('{:.4f}'.format((j[w]-mean)/deviation))
    img_printer(img)

if operation == 3:
    img, max_color_val = read_ppm_file(filename)
    # ortalamayı üç channel'a da yazıyorum
    for i in img:
        for j in i:
            sum = 0
            for w in range(3):
                sum += j[w]
            for w in range(3):
                j[w] = int(sum/3)
    img_printer(img)


if operation == 4:
    img, max_color_val = read_ppm_file(filename)
    # filter listesi yapıyorum
    filter_name = input()
    stride = int(input())
    fp = open(filter_name)
    lst_of_filter = []
    nlst_of_filter = []
    for line in fp:
        lst_of_filter.append(line.strip())
    for el in lst_of_filter:
        ls = el.split()
        for i in range(len(ls)):
            ls[i] = float(ls[i])
        nlst_of_filter.append(ls)
    fil_num = len(nlst_of_filter)


    nimg = []
    # bu döngülerin sonunda 9 çarpımın toplamını subrowun içine yazıyorum
    #sonra da subrow row nimg şeklinde iç içe liste yapıyorum
    for k in range(0, len(img)-(fil_num-1), stride):
        base=0
        row = []
        while base <= len(img)-fil_num:


            subrow = []
            for linx in range(3):
                sum = 0
                for incx in range(base,fil_num+base):
                    for inc in range(fil_num):


                        sum += (img[k + inc][incx][linx] * nlst_of_filter[inc][incx - base])

                if sum < 0:
                    subrow.append(0)
                if sum > 255:
                    subrow.append(255)
                if 0 <= sum <= 255:
                    subrow.append(int(sum))
            row.append(subrow)

            base += stride
        nimg.append(row)



    img_printer(nimg)

if operation == 5:
    img, max_color_val = read_ppm_file(filename)

    # filter listesi yapıyorum
    filter_name = input()
    stride = int(input())
    fp = open(filter_name)
    lst_of_filter = []
    nlst_of_filter = []
    for line in fp:
        lst_of_filter.append(line.strip())
    for el in lst_of_filter:
        ls = el.split()
        for i in range(len(ls)):
            ls[i] = float(ls[i])
        nlst_of_filter.append(ls)
    fil_num = len(nlst_of_filter)


    mimg = [[[0] * 3] * (len(img) + (fil_num - 1))]
    for i in range(((fil_num - 1) // 2) - 1):
        mimg.append([[0] * 3] * (len(img) + (fil_num - 1)))

    for el in img:
        nel = [[0] * 3] * ((fil_num - 1) // 2) + el + [[0] * 3] * ((fil_num - 1) // 2)

        mimg.append(nel)
    for i in range((fil_num - 1) // 2):
        mimg.append([[0] * 3] * (len(img) + (fil_num - 1)))

    nimg = []

    # operation 4'ün aynısını yeni liste ile yapıyorum
    for k in range(0, len(mimg) - (fil_num - 1), stride):
        base = 0
        row = []
        while base <= len(mimg) - fil_num:

            subrow = []
            for linx in range(3):
                sum = 0
                for incx in range(base, fil_num + base):
                    for inc in range(fil_num):

                        sum += (mimg[k + inc][incx][linx] * nlst_of_filter[inc][incx - base])

                if sum < 0:
                    subrow.append(0)
                if sum > 255:
                    subrow.append(255)
                if 0 <= sum <= 255:
                    subrow.append(int(sum))
            row.append(subrow)

            base += stride
        nimg.append(row)

    img_printer(nimg)

if operation == 6:
    img, max_color_val = read_ppm_file(filename)

    len_img = len(img)
    dif_range = int(input())

    #recursion ile verilen düzendeki arka arkaya gelen pixelleri kontrol edyorum
    def recuropsix(lst, set_val=[0,0,0], x=0, y=0):

        #base condition
        if abs(lst[x][y][0] - set_val[0]) < dif_range and abs(lst[x][y][1] - set_val[1]) < dif_range and abs(lst[x][y][2] - set_val[2]) < dif_range:
            lst[x][y] = set_val

        else:
            set_val = lst[x][y]



        if len_img%2 == 0 and x == 0 and y == len_img-1:
            return lst
        if len_img%2 == 1 and x == len_img-1 and y == len_img-1:
            return lst


        if y%2==0 and x == len_img-1:
            return recuropsix(lst, set_val, x, y+1)
        if y%2==1 and x == 0:
            return recuropsix(lst, set_val, x, y+1)
        if y%2 == 0:
            return recuropsix(lst, set_val, x+1, y)
        if y%2 == 1:
            return recuropsix(lst, set_val, x-1, y)


    new_img = recuropsix(img)
    img_printer(new_img)


if operation == 7:
    img, max_color_val = read_ppm_file(filename)

    len_img = len(img)
    dif_range = int(input())
    # operation6'yı 3d'ye uygun olması için genelleştirdim
    def recuropseven(lst, set_val=0, x=0, y=0, z=0):

        #base condition
        if abs(lst[x][y][z]-set_val) < dif_range:
            lst[x][y][z] = set_val
        else:
            set_val = lst[x][y][z]

        if len_img%2 == 0 and z == 2 and x == 0 and y == len_img-1:
            return lst
        if len_img%2 == 1 and z == 2 and x == len_img-1 and y == len_img-1:
            return lst

        if len_img%2==0:
            if x == 0 and y == len_img-1 and z == 0:
                return recuropseven(lst,set_val,x, y, z+1)
            if x == 0 and y == 0 and z == 1:
                return recuropseven(lst,set_val,x,y,z+1)
        if len_img%2==1:
            if x == len_img-1 and y == len_img-1 and z == 0:
                return recuropseven(lst,set_val, x,y,z+1)
            if x == 0 and y == 0 and z == 1:
                return recuropseven(lst,set_val,x,y,z+1)




        if x == len_img-1 and y%2 == 0 and z == 0:
            return recuropseven(lst,set_val,x,y+1,z)
        if x == 0 and y%2 == 1 and z == 0:
            return recuropseven(lst,set_val,x,y+1,z)

        if x == 0 and y%2==0 and z == 1:
            return  recuropseven(lst,set_val,x,y-1,z)
        if x == len_img-1 and y % 2 == 1 and z == 1:
            return recuropseven(lst,set_val,x,y-1,z)

        if x == len_img-1 and y%2==0 and z==2:
            return recuropseven(lst,set_val,x,y+1,z)
        if x == 0 and y%2 == 1 and z == 2:
            return recuropseven(lst,set_val,x,y+1,z)


        if z == 0:
            if y%2==0:
                return recuropseven(lst,set_val,x+1,y,z)
            if y%2==1:
                return recuropseven(lst,set_val,x-1,y,z)
        if z == 1:
            if y%2==0:
                return recuropseven(lst,set_val,x-1,y,z)
            if y%2==1:
                return recuropseven(lst,set_val,x+1,y,z)
        if z == 2:
            if y%2==0:
                return recuropseven(lst,set_val,x+1,y,z)
            if y%2==1:
                return recuropseven(lst,set_val,x-1,y,z)


    new_img = recuropseven(img)
    img_printer(new_img)




# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

