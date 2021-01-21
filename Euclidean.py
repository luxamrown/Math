print('Teorema Euclidean')
m = int(input('Angka :'))
n = int(input('Pembagi: '))

def euclidean(m,n):
    q= int(m/n)
    r=m%n
    print(str(m) + ' dibagi dengan ' + str(n)  + ' memberikan hasil bagi ' + str(q) + ' dan sisa '+ str(r))
    print(str(m) + ' = ' + str(n)+' * ' + str(q)+' + '+str(r))

if n == 0:
    print('Syarat n(pembagi) tidak sama dengan nol ')
else:
    euclidean(m,n)