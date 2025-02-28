import numpy as np
import argparse
import cv2

def adjust_gamma(image, gamma=1.0):
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
    return cv2.LUT(image, table)


# original_image = cv2.imread("/home/ilya/FullDataSet/Image_H100_D568_R1136C15336.jpg")

# for gamma in np.arange(0.0, 2.25, 0.25):
#     if gamma == 1:
#         continue
#     gamma = gamma if gamma > 0 else 0.1
#     adjusted = adjust_gamma(original_image, gamma=gamma)

    # cv2.putText(adjusted, "g={}".format(gamma), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
    # cv2.imshow("Images", np.hstack([original_image, adjusted]))
    # cv2.waitKey(0)
