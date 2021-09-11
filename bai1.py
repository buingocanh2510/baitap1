print("Nhap vao 1 so: ")
n = int(input())
print(n)

if n<2:
    print("khong phai la so nguyen to!");
else:
    laSoNt = True
    for i in range(2, int(n/2)+1):
        if n%i == 0:
            laSoNt = False
            
    if laSoNt==True:
        print("la so nguyen to!")
    else:
        print("khong phai la so nguyen to!")