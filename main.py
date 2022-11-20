import matplotlib.pyplot as plt

mu_array = [1, 2, 3, 4, 4, 3, 2, 1, 3, 4, 5, 5, 4, 3, 0, 1, 3, 3, 1, 1, 0]
mu_array_initial = mu_array

mode_ind = []
ind = 0

step = 1  # set parameters
addstep = 1
noise = 0

IH = []  # IH = interval hull
max_mu_array = []

plt.plot(mu_array)
plt.show()

# def ROImode(mode_ind):
#     inowL = min(mode_ind)
#     inowR = max(mode_ind)
#     out = [i for i in range(inowL, inowR + 1)]

i = 1


def ROI_mode(mu_array):
    # global ROInow
    global i
    global ind
    print(f"start_{i}")
    print(mu_array)

    max_mu = max(mu_array)
    max_mu_array.append(max_mu)

    mode_ind = []
    ind = 0

    for i in mu_array:
        if i == max_mu:
            mode_ind.append(ind)
        ind += 1

    inowL = min(mode_ind)
    inowR = max(mode_ind)

    ROInow = [i for i in range(inowL, inowR + 1)]

    if len(ROInow) > 0:  # vanish the peak
        for i in ROInow:
            mu_array[i] = 0

    Lebesgue_lev = max(mu_array)

    add_noise = noise

    stepL = step  # set step
    stepR = step

    try:  # one step forward
        inowL -= stepL
        inowR += stepR
    except inowL < 1:
        inowL = 1
    except inowR > len(mu_array):
        inowR = len(mu_array)

    ROInow = [i for i in range(inowL, inowR + 1)]

    Lebesgue_lev = max(mu_array[inowL], mu_array[inowR])

    # [aa, aa_ind] = find(mu_arraynow(ROInow) == 0);  ????????
    # ROInow(aa_ind) = [];

    GOFW = 0  # flag

    if Lebesgue_lev > 0:
        GOFW = 1  # move forward

    while GOFW:  # infinite cycle, correct
        GOFW = ((Lebesgue_lev + add_noise) > max(mu_array))  # check if   max(Left, Rigth) > max remain array

        if (mu_array[inowL - 1] < mu_array[inowL]) & (mu_array[inowR + 1] < mu_array[inowR]):
            inowL -= stepL

            if inowL < 1:
                inowL = 1
            inowR += stepR

            if inowR > len(mu_array):
                inowR = len(mu_array)

            ROInow = [i for i in range(inowL, inowR + 1)]

        else:
            stepL += addstep
            stepR += addstep
            inowL -= stepL

            if inowL < 1:
                inowL = 1
            inowR += stepR

            if inowR > len(mu_array):
                inowR = len(mu_array)
            ROInow = [i for i in range(inowL, inowR + 1)]

            stepL -= addstep
            stepR -= addstep

            print("no monotone")

        Lebesgue_lev = max(mu_array[inowL], mu_array[inowR])

    if len(ROInow) > 0:  # vanish the peak
        for i in ROInow:
            mu_array[i] = 0

    plt.plot(mu_array)  # plot without peak
    y = [0 for i in range(len(ROInow))]
    plt.plot(ROInow, y)
    plt.show()

    i += 1
    print(mu_array)

    IH.append(min(ROInow))
    IH.append(max(ROInow))

    while max(mu_array) != 0:
        ROI_mode(mu_array)

    return mu_array


ROI_mode(mu_array)
