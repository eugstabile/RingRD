import iallreduce
import iallcomp
import utils


def main():

    newdata = 0
    iall = 0
    iallcomparative = 1
    con  = 1 #contiguo

    if newdata == 1:
        utils.filing()
        exit()

    ini = 10
    msj_size = utils.create_size(ini, 31)

    if iall == 1:
        mbs = 1
        chunks =[1,2,3]
        for j in range(3, 4, 1):
            for i in range(3, 4, 1):
                for k in range(len(chunks)):
                    p = 2**i
                    n = 2**j
                    c = chunks[k]
                    iallreduce.main(p, n, c, msj_size, ini, mbs)
                    print("Finalizado nº nodos {} con nº procesos {} y chunk {}".format(n, p, c))

    if iallcomparative == 1:
        for i in range(3, 4, 1): #8
            for j in range(4, 6, 1): #8, 16, 32
                n = 2**i
                p = 2**j
                for opt in range(2, 3, 1):
                    iallcomp.main(p, n, msj_size, ini, opt, con)
                    print("Finalizado nº nodos {} con nº procesos {} con config {}".format(n, p, opt))


main()
