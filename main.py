import matplotlib.pyplot as plt

mu_array = [1, 2, 3, 4, 4, 3, 2, 1, 3, 4, 5, 5, 4, 3, 0, 1, 3, 3, 1, 1, 0]
mu_array_initial = mu_array

max_mu = max(mu_array)

mode_ind = []
ind = 0

for i in mu_array:
    if i == max_mu:
        mode_ind.append(ind)
    ind += 1

step = 1  # set parameters
addstep = 1
noise = 0

IH = []  # IH = interval hull
max_mu_array = []

plt.plot(mu_array)
y = [max_mu for i in range(len(mode_ind))]  # переделать
plt.plot(mode_ind, y)
plt.show()


# def ROImode(mode_ind):
#     inowL = min(mode_ind)
#     inowR = max(mode_ind)
#     out = [i for i in range(inowL, inowR + 1)]


def ROI_mode(mode_ind):
    global ROInow

    inowL = min(mode_ind)
    inowR = max(mode_ind)
    # ROInow = ROImode(mode_ind)  #?

    ROInow = [i for i in range(inowL, inowR + 1)]
    print(ROInow)

    mu_arraynow = mu_array

    if len(ROInow) > 0:  # vanish the peak
        for i in ROInow:
            mu_arraynow[i] = 0

    Lebesgue_lev = max(mu_arraynow)

    plt.plot(mu_arraynow)  # plot without peak
    y = [0 for i in range(len(mode_ind))]
    plt.plot(mode_ind, y)
    plt.show()

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

    Lebesgue_lev = max(mu_arraynow[inowL], mu_arraynow[inowR])

    # [aa, aa_ind] = find(mu_arraynow(ROInow) == 0);  ????????
    # ROInow(aa_ind) = [];

    GOFW = 0  # flag

    if Lebesgue_lev > 0:
        GOFW = 1  # move forward

    while GOFW:  # infinite cycle, correct
        GOFW = ((Lebesgue_lev + add_noise) > max(mu_arraynow))  # check if   max(Left, Rigth) > max remain array

    if mu_arraynow[inowL - 1] < mu_arraynow[inowL] & mu_arraynow[inowR + 1] < mu_arraynow[inowR]:
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

        print(ROInow)

    Lebesgue_lev = max(mu_arraynow[inowL], mu_arraynow[inowR])

    return ROInow


ROI_mode(ROI_mode(ROI_mode(mode_ind)))

max_mu_array.append(max_mu)

IH.append(min(ROInow))
IH.append(max(ROInow))


