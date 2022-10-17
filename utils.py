import matplotlib.pyplot as plt
import numpy as np
import glob

def filing():
    total_files = []
    name_files = []
    #subfiles = ["chunks_ringrd", "segments_ringrd", "sincrona", "sinsegmentar_ringrd"]
    subfiles = ["sinsegmentar_ringrd"]
    for i in range(len(subfiles)):
        for f in glob.iglob(root_dir="./", pathname="times_comparative/contiguo/{}/**.dat".format(subfiles[i]), recursive=True):
            total_files.append(f)
            name_files.append("normalized_comparative/contiguo/{}/".format(subfiles[i]) + f.rstrip('\n').rpartition('/')[-1])
        parser(total_files, name_files)

def parser(file, outputfile):
    # traducir los ficheros de obtención de la ejecución
    for i in range(len(file)):
        with open('{}'.format(file[i])) as file_in, open('{}'.format(outputfile[i]), 'w') as file_out:
            [file_out.write(line.rpartition(',')[-1]) for line in file_in.readlines() if '#' != line[0]]

def get_file(path, ini):
    f = open(path, "r")
    data = [line.rstrip('\n') for line in f]
    plot = 31 - ini
    data = data[-plot:]
    f.close()
    return data


def create_size(ini, end):
    """Creación de la tabla de tamaños de mensaje"""
    table_size = []
    for i in range(ini, end):
        table_size.append(2 ** i)
    return table_size


def tombs(msj_size, time):
    type_size = 4
    res_time = []
    for t in range(len(time)):
        aux_time = time[t]
        res = [((msj_size[i] / aux_time[i]) / 1000000) for i in range(len(msj_size))]
        res_time.append(res)
    return res_time


def plotting(p, nodes, c, alg, times, x_tam, ini, mbs):
    fig = plt.figure()
    fig.set_size_inches(18, 10)
    plt.title("Iallreduce algorithms with {} nodes ({} process) and {} B chunk size".format(str(nodes), str(p), str(c)), fontsize=16)
    # eje y normal
    #plt.subplot(1, 2, 1)
    plt.plot(x_tam, times[0], "k.--", linewidth=2, markersize=4, label=str(times[0]))
    plt.plot(x_tam, times[1], "bo-", linewidth=2, markersize=4, label=str(times[1]))
    plt.plot(x_tam, times[2], "rd-", linewidth=2, markersize=4, label=str(times[2]))
    plt.plot(x_tam, times[3], "gs-", linewidth=2, markersize=4, label=str(times[3]))
    plt.plot(x_tam, times[4], "mv-", linewidth=2, markersize=4, label=str(times[4]))
    plt.plot(x_tam, times[5], "cp-", linewidth=2, markersize=4, label=str(times[5]))
    plt.plot(x_tam, times[6], "yh-", linewidth=2, markersize=4, label=str(times[6]))
    plt.plot(x_tam, times[7], color="#30DADA", marker="D", linestyle="solid", linewidth=2, markersize=4, label=str(times[7]))

    if mbs == 1:
        plt.xlabel("Message size (Bytes)")
        plt.ylabel("MB/s")
        plt.xscale("log", base=2)
        plt.grid(color='gray', linestyle='--', linewidth=1)
        plt.xticks(2 ** np.arange(ini, 31, step=1))
        plt.legend(alg)
        plt.tight_layout()
        plt.savefig("Plots/iallreduce_mbs_p{}_n{}.png".format(str(p), str(nodes)), format="png", dpi=600)
    else:
        plt.xlabel("Message size (Bytes)")
        #plt.ylabel("Time (s)")
        plt.ylabel("MB/s")
        plt.xscale("log", base=2)
        plt.grid(color='gray', linestyle='--', linewidth=1)
        plt.xticks(2 ** np.arange(ini, 31, step=1))
        plt.legend(alg)
        plt.tight_layout()
        plt.savefig("Plots/chunks/iallreduce_p{}_n{}_c{}.png".format(str(p), str(nodes), str(c)), format="png", dpi=600)



def plotring(p, nodes, alg, times, x_tam, ini, opt, con):
    fig = plt.figure()
    fig.set_size_inches(16, 9)

    if opt == 0: #chunks
        plt.title(
            "Comparative Iallreduce Ring-RD vs chunks Ring-RD with {} nodes ({} process)".format(str(nodes), str(p)),
            fontsize=18)
    if opt == 1: #segmentado
        plt.title(
            "Comparative Iallreduce Ring-RD vs segmented Ring-RD with {} nodes ({} process)".format(str(nodes), str(p)),
            fontsize=18)
    if opt == 2: #sin segmentar
        if con == 0:
            plt.title(
                "Iallreduce algorithms with {} nodes ({} process)".format(str(nodes), str(p)),
                fontsize=18)
        if con == 1:
            plt.title(
                "Iallreduce algorithms with {} nodes ({} process) Deep-first".format(str(nodes), str(p)),
                fontsize=18)
    if opt == 3: #sincrona
        plt.title(
            "Iallreduce Ring-RD vs Allreduce algorithms with {} nodes ({} process)".format(str(nodes), str(p)),
            fontsize=18)

    # eje y normal
    #plt.subplot(1, 2, 1)
    plt.plot(x_tam, times[0], "k.--", linewidth=2, markersize=8, label=str(times[0]))
    plt.plot(x_tam, times[1], "bo-", linewidth=2, markersize=4, label=str(times[1]))
    plt.plot(x_tam, times[2], "rd-", linewidth=2, markersize=4, label=str(times[2]))
    plt.plot(x_tam, times[3], "gs-", linewidth=2, markersize=4, label=str(times[3]))
    plt.plot(x_tam, times[4], "mv-", linewidth=2, markersize=4, label=str(times[4]))
    if opt != 1:
        plt.plot(x_tam, times[5], "cp-", linewidth=2, markersize=4, label=str(times[5]))
    if opt == 3:
        plt.plot(x_tam, times[6], "y2-", linewidth=2, markersize=4, label=str(times[6]))
        plt.plot(x_tam, times[7], color="#FFBF00", marker="D", linestyle="solid", linewidth=2, markersize=4, label=str(times[7]))


    plt.xlabel("Message size (Bytes)", fontsize=14)
    #plt.ylabel("Time (s)")
    plt.ylabel("MB/s", fontsize=14)
    plt.xscale("log", base=2)
    plt.grid(color='gray', linestyle='--', linewidth=1)
    plt.xticks(2 ** np.arange(ini, 31, step=1))
    plt.legend(alg)
    plt.tight_layout()
    if opt == 0:  # chunks
        plt.savefig("Plots/normalized_comparative/iallreduce_p{}_n{}_chunks.png".format(str(p), str(nodes)),
                    format="png", dpi=600)
    if opt == 1: #segmentado
        plt.savefig("Plots/normalized_comparative/iallreduce_p{}_n{}_segmented.png".format(str(p), str(nodes)),
                    format="png", dpi=600)
    if opt == 2: #sin segmentar
        if con == 0:
            plt.savefig("Plots/normalized_comparative/iallreduce_p{}_n{}_sinsegmentar.png".format(str(p), str(nodes)),
                        format="png", dpi=600)
        if con == 1:
            plt.savefig("Plots/normalized_comparative/contiguo/iallreduce_p{}_n{}_sinsegmentar.png".format(str(p), str(nodes)),
                        format="png", dpi=600)
    if opt == 3: #sincrona
        plt.savefig("Plots/normalized_comparative/iallreduce_p{}_n{}_sincrona.png".format(str(p), str(nodes)),
                    format="png", dpi=600)