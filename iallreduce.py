import utils

def main(p, n, c, msj_size, ini, mbs):
    # Other parameters
    contiguo = 0
    iallred_algs = ["Default", "Ring", "binomial", "rabenseifner", "recursive_doubling", "knomial", "rd_knomial", "ring_rd"]
    #iallred_algs = ["Ring", "binomial", "rabenseifner", "recursive_doubling", "ring_rd"]

    # Get real result
    if contiguo == 0:
        time_default = [float(i) for i in utils.get_file("times_chunk/Default/time_default_{}_n{}_c_{}.txt".format(p, n, c), ini)]
        time_ring = [float(i) for i in utils.get_file("times_chunk/Ring/time_ring_{}_n{}_c_{}.txt".format(p, n, c), ini)]
        time_binomial = [float(i) for i in utils.get_file("times_chunk/Binomial/time_binomial_{}_n{}_c_{}.txt".format(p, n, c), ini)]
        time_rabenseifner = [float(i) for i in utils.get_file("times_chunk/Rabenseifner/time_rabenseifner_{}_n{}_c_{}.txt".format(p, n, c), ini)]
        time_rd = [float(i) for i in utils.get_file("times_chunk/RD/time_rd_{}_n{}_c_{}.txt".format(p, n, c), ini)]
        time_knomial = [float(i) for i in utils.get_file("times_chunk/RD/time_rd_{}_n{}_c_{}.txt".format(p, n, c), ini)]
        time_rd_knomial = [float(i) for i in utils.get_file("times_chunk/RD/time_rd_{}_n{}_c_{}.txt".format(p, n, c), ini)]
        time_ring_rd = [float(i) for i in utils.get_file("times_chunk/Ring_RD/time_ringrd_{}_n{}_c_{}.txt".format(p, n, c), ini)]
    else:
        time_default = [float(i) for i in utils.get_file("contiguo_times/Default/time_default_{}_n{}.txt".format(p, n), ini)]
        time_ring = [float(i) for i in utils.get_file("contiguo_times/Ring/time_ring_{}_n{}.txt".format(p, n), ini)]
        time_binomial = [float(i) for i in utils.get_file("contiguo_times/Binomial/time_binomial_{}_n{}.txt".format(p, n), ini)]
        time_rabenseifner = [float(i) for i in utils.get_file("contiguo_times/Rabenseifner/time_rabenseifner_{}_n{}.txt".format(p, n), ini)]
        time_rd = [float(i) for i in utils.get_file("contiguo_times/RD/time_rd_{}_n{}.txt".format(p, n), ini)]
        time_ring_rd = [float(i) for i in utils.get_file("contiguo_times/Ring_RD/time_ringrd_{}_n{}.txt".format(p, n), ini)]

    time_algs = [time_default, time_ring, time_binomial, time_rabenseifner, time_rd, time_knomial, time_rd_knomial, time_ring_rd]
    #time_algs = [time_ring, time_binomial, time_rabenseifner, time_rd, time_ring_rd]
    # Save result in file
    #for i in range(len(iallred_algs)):
    #    utils.write_file(iallred_algs[i], "result/iallred/{}_{}.txt".format(str(iallred_algs[i]), p))

    # Plot the result
    if mbs == 1:
        res_time_algs = utils.tombs(msj_size, time_algs)
        utils.plotting(p, n, iallred_algs, res_time_algs, msj_size, ini, mbs)
    else:
        utils.plotting(p, n, c, iallred_algs, time_algs, msj_size, ini, mbs)
