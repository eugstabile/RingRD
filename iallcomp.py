import utils

def main(p, n, msj_size, ini, opt, con):
    # Get real result
    if opt == 0: #chunks
        time_ring_rd_sseg = [float(i) for i in utils.get_file(
            "normalized_comparative/sinsegmentar_ringrd/iallreduce_N{}_alg_7_procs_{}.dat".format(n, p), ini)]
        time_ring_rd_c512 = [float(i) for i in utils.get_file(
            "normalized_comparative/chunks_ringrd/iallreduce_N{}_alg_7_procs_{}_C524288.dat".format(n, p), ini)]
        time_ring_rd_c1 = [float(i) for i in utils.get_file(
            "normalized_comparative/chunks_ringrd/iallreduce_N{}_alg_7_procs_{}_C1048576.dat".format(n, p), ini)]
        time_ring_rd_c2 = [float(i) for i in utils.get_file(
            "normalized_comparative/chunks_ringrd/iallreduce_N{}_alg_7_procs_{}_C2097152.dat".format(n, p), ini)]
        time_ring_rd_c4= [float(i) for i in utils.get_file(
            "normalized_comparative/chunks_ringrd/iallreduce_N{}_alg_7_procs_{}_C4194304.dat".format(n, p), ini)]
        time_ring_rd_c8 = [float(i) for i in utils.get_file(
            "normalized_comparative/chunks_ringrd/iallreduce_N{}_alg_7_procs_{}_C8388608.dat".format(n, p), ini)]

        iallred_algs = ["Ring_RD", "Ring_RD 512KB", "Ring_RD 1MB", "Ring_RD 2MB", "Ring_RD 4MB", "Ring_RD 8MB"]
        time_algs = [time_ring_rd_sseg, time_ring_rd_c512, time_ring_rd_c1, time_ring_rd_c2, time_ring_rd_c4,
                     time_ring_rd_c8]
        utils.plotring(p, n, iallred_algs, time_algs, msj_size, ini, opt)

    elif opt == 1: #segmentado
        time_ring_rd_sseg = [float(i) for i in utils.get_file(
            "normalized_comparative/sinsegmentar_ringrd/iallreduce_N{}_alg_7_procs_{}.dat".format(n, p), ini)]
        time_ring_rd_p2 = [float(i) for i in utils.get_file(
            "normalized_comparative/segments_ringrd/iallreduce_N{}_alg_7_procs_{}_P2.dat".format(n, p), ini)]
        time_ring_rd_p4 = [float(i) for i in utils.get_file(
            "normalized_comparative/segments_ringrd/iallreduce_N{}_alg_7_procs_{}_P4.dat".format(n, p), ini)]
        time_ring_rd_p8 = [float(i) for i in utils.get_file(
            "normalized_comparative/segments_ringrd/iallreduce_N{}_alg_7_procs_{}_P8.dat".format(n, p), ini)]
        time_ring_rd_p16 = [float(i) for i in utils.get_file(
            "normalized_comparative/segments_ringrd/iallreduce_N{}_alg_7_procs_{}_P16.dat".format(n, p), ini)]

        iallred_algs = ["Ring_RD", "Ring_RD 2 parts", "Ring_RD 4 parts", "Ring_RD 8 parts", "Ring_RD 16 parts"]
        time_algs = [time_ring_rd_sseg, time_ring_rd_p2, time_ring_rd_p4, time_ring_rd_p8, time_ring_rd_p16]
        utils.plotring(p, n, iallred_algs, time_algs, msj_size, ini, opt)

    elif opt == 2: #sin segmentar
        if con == 0:
            time_ring_rd = [float(i) for i in utils.get_file(
                "normalized_comparative/sinsegmentar_ringrd/iallreduce_N{}_alg_7_procs_{}.dat".format(n, p), ini)]
            time_default = [float(i) for i in utils.get_file(
                "normalized_comparative/sinsegmentar_ringrd/iallreduce_N{}_alg_0_procs_{}.dat".format(n, p), ini)]
            time_ring = [float(i) for i in utils.get_file(
                "normalized_comparative/sinsegmentar_ringrd/iallreduce_N{}_alg_1_procs_{}.dat".format(n, p), ini)]
            time_binomial = [float(i) for i in utils.get_file(
                "normalized_comparative/sinsegmentar_ringrd/iallreduce_N{}_alg_2_procs_{}.dat".format(n, p), ini)]
            time_rabenseifner = [float(i) for i in utils.get_file(
                "normalized_comparative/sinsegmentar_ringrd/iallreduce_N{}_alg_3_procs_{}.dat".format(n, p), ini)]
            time_rd = [float(i) for i in utils.get_file(
                "normalized_comparative/sinsegmentar_ringrd/iallreduce_N{}_alg_4_procs_{}.dat".format(n, p), ini)]
        if con == 1:
            time_ring_rd = [float(i) for i in utils.get_file(
                "normalized_comparative/contiguo/sinsegmentar_ringrd/iallreduce_N{}_alg_7_procs_{}_C.dat".format(n, p), ini)]
            time_default = [float(i) for i in utils.get_file(
                "normalized_comparative/contiguo/sinsegmentar_ringrd/iallreduce_N{}_alg_0_procs_{}_C.dat".format(n, p), ini)]
            time_ring = [float(i) for i in utils.get_file(
                "normalized_comparative/contiguo/sinsegmentar_ringrd/iallreduce_N{}_alg_1_procs_{}_C.dat".format(n, p), ini)]
            time_binomial = [float(i) for i in utils.get_file(
                "normalized_comparative/contiguo/sinsegmentar_ringrd/iallreduce_N{}_alg_2_procs_{}_C.dat".format(n, p), ini)]
            time_rabenseifner = [float(i) for i in utils.get_file(
                "normalized_comparative/contiguo/sinsegmentar_ringrd/iallreduce_N{}_alg_3_procs_{}_C.dat".format(n, p), ini)]
            time_rd = [float(i) for i in utils.get_file(
                "normalized_comparative/contiguo/sinsegmentar_ringrd/iallreduce_N{}_alg_4_procs_{}_C.dat".format(n, p), ini)]

        iallred_algs = ["Ring_RD", "Default", "Ring", "Binomial", "Rabenseifner", "Recursive_Doubling"]
        time_algs = [ time_ring_rd, time_default, time_ring, time_binomial, time_rabenseifner, time_rd]
        utils.plotring(p, n, iallred_algs, time_algs, msj_size, ini, opt, con)

    elif opt == 3: #version sincrona
        time_ring_rd = [float(i) for i in utils.get_file(
            "normalized_comparative/sinsegmentar_ringrd/iallreduce_N{}_alg_7_procs_{}.dat".format(n, p), ini)]
        time_default = [float(i) for i in utils.get_file(
            "normalized_comparative/sincrona/allreduce_alg_0_procs_{}.dat".format(p), ini)]
        time_linear = [float(i) for i in utils.get_file(
            "normalized_comparative/sincrona/allreduce_alg_1_procs_{}.dat".format(p), ini)]
        time_nonoverlapping = [float(i) for i in utils.get_file(
            "normalized_comparative/sincrona/allreduce_alg_2_procs_{}.dat".format(p), ini)]
        time_rd = [float(i) for i in utils.get_file(
            "normalized_comparative/sincrona/allreduce_alg_3_procs_{}.dat".format(p), ini)]
        time_ring = [float(i) for i in utils.get_file(
            "normalized_comparative/sincrona/allreduce_alg_4_procs_{}.dat".format(p), ini)]
        time_segring = [float(i) for i in utils.get_file(
            "normalized_comparative/sincrona/allreduce_alg_5_procs_{}.dat".format(p), ini)]
        time_rabenseifner = [float(i) for i in utils.get_file(
            "normalized_comparative/sincrona/allreduce_alg_6_procs_{}.dat".format(p), ini)]

        iallred_algs = ["Ring_RD", "Default", "Linear", "Nonoverlapping", "Recursive_Doubling", "Ring", "Segmented_Ring", "Rabenseifner"]
        time_algs = [time_ring_rd, time_default, time_linear, time_nonoverlapping, time_rd, time_ring, time_segring, time_rabenseifner]
        utils.plotring(p, n, iallred_algs, time_algs, msj_size, ini, opt)

    else:
        print("No se escogió una configuración correcta")
        exit()

