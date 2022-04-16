import numpy as np


def calculate(target_list):
    # check the length of the list
    if len(target_list) != 9:
        raise ValueError("List must contain nine numbers.")
    # transform the list to numpy array
    num_arr = np.array(target_list)
    num_arr = num_arr.reshape(3, 3)

    # create a list containing numpy arrays of all calculations
    all_list = []
    for i in range(2):
        all_list.append(num_arr.mean(axis=i))
        all_list.append(num_arr.var(axis=i))
        all_list.append(num_arr.std(axis=i))
        all_list.append(num_arr.max(axis=i))
        all_list.append(num_arr.min(axis=i))
        all_list.append(num_arr.sum(axis=i))
    # transform the list of numpy arrays into list of python elements
    for i in range(len(all_list)):
        all_list[i] = all_list[i].tolist()
    all_list.append(num_arr.mean())
    all_list.append(num_arr.var())
    all_list.append(num_arr.std())
    all_list.append(num_arr.max())
    all_list.append(num_arr.min())
    all_list.append(num_arr.sum())

    # create the required dictionary
    calculations = dict()
    calculations["mean"] = all_list[0::6]
    calculations["variance"] = all_list[1::6]
    calculations["standard deviation"] = all_list[2::6]
    calculations["max"] = all_list[3::6]
    calculations["min"] = all_list[4::6]
    calculations["sum"] = all_list[5::6]

    return calculations

# if __name__ == "__main__":
#     nlist = list(range(9))
#     ntest = calculate(nlist)
#     narr = np.array(nlist)
#     print(narr)
#     narr_3d = narr.reshape(3, 3)
#     print(narr_3d)
#     print(ntest)

