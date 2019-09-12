'Funciona apenas na multiplicação de DUAS matrizes quadradas, obviamente de mesmo grau (Vou melhorar isso ainda) :(  '

def multiplica(la, ca, a, lb, cb, b):
    if ca == lb:
        c = [[0 for i in range(cb)]for j in range(la)]
        lc = 0
        cc = 0
        acum = 0
        ia = 0
        ja = 0
        ib = 0
        jb = 0
        cont = 1
        while cont <= la:
            for i in range(la):
                for j in range(cb):
                    acum += a[ia][ja] * b[ib][jb]
                    ib += 1
                    ja += 1
                c[lc][cc] = acum
                acum = 0
                if cc < cb-1: cc += 1
                else:
                    if cc == cb-1 and lc < la-1: lc += 1
                ib = 0
                jb += 1
                ja = 0
            cont += 1
            ia += 1
            jb = 0
            cc = 0
        print(c)
       

la = 4
ca = 4
a = [[4,5,6,7], [4,5,6,7], [4,5,6,7], [4,5,6,7]]
print(a)

lb = 4
cb = 4
b = [[1,2,3,4], [8,8,8,8], [9,9,9,9], [10,10,10,88]]
print(b)
multiplica(la, ca, a, lb, cb, b)
