import os
import numpy as np
import cv2

def compute(pic_path, filter_mat):
    im = cv2.imread(pic_path)
    im_s, fil_s = list(im.shape), list(filter_mat.shape)
    res = np.zeros((im_s[0]-fil_s[0]+1, im_s[1]-fil_s[1]+1, im_s[2]), dtype=np.uint8)

    for i in range(res.shape[0]):
        for j in range(res.shape[1]):
            for k in range(res.shape[2]):
                tmp = im[i: (i+fil_s[0]), j:(j+fil_s[1]), k] * filter_mat
                res[i][j][k] = max(min(255, int(round(np.sum(tmp)))), 0)

    cache_dir = os.path.abspath(os.path.join(__file__, "..", "cache"))
    if not os.path.isdir(cache_dir):
        os.makedirs(cache_dir)
    new_path = os.path.join(cache_dir, "tmp.jpg")

    cv2.imwrite(new_path, res)
    return new_path
