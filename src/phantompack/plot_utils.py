import cv2
import numpy as np

def display_image(img, name='image', waitkey=0):
    cimg = np.uint8(cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX))
    cimg = cv2.cvtColor(cimg, cv2.COLOR_GRAY2BGR)
    cv2.imshow(name, cimg)
    cv2.waitKey(waitkey)
    cv2.destroyAllWindows()

def display_image_with_circles(img, circles, name='image', waitkey=0):
    cimg = np.uint8(cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX))
    cimg = cv2.cvtColor(cimg, cv2.COLOR_GRAY2BGR)
    np_circles = np.uint16(np.around(circles))
    for c in np_circles:
        cv2.circle(cimg,(c[0],c[1]),c[2],(0,255,0),2)
    cv2.imshow(name, cimg)
    cv2.waitKey(waitkey)
    cv2.destroyAllWindows()

    
def plot_circles(circles, title="Circles Visualization"):
    fig, ax = plt.subplots()
    for idx, (x, y, r) in enumerate(circles):
        circle = plt.Circle((x, y), r, fill=False, edgecolor='b')
        ax.add_patch(circle)
        ax.text(x, y, str(idx), fontsize=12, ha='center', va='center', color='r')
    min_dim = 0
    max_dim = 256
    # for idx, (x, y, r) in enumerate(circles):
    #     min_dim = min(min_dim, x - r)
    #     min_dim = min(min_dim, y - r)
    #     max_dim = max(max_dim, x + r)
    #     max_dim = max(max_dim, y + r)
    ax.set_aspect('equal', 'box')
    ax.set_xlim(min_dim, max_dim)
    ax.set_ylim(min_dim, max_dim)
    plt.title(title)
    plt.grid(True)
    plt.show()
