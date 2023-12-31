# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from PIL import Image, ImageDraw, ImageFont
from typing import Tuple, List

"""
`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,
`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,
`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,
`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,**:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,
`:,:***:`:,:`:,:`:,:`:,:`:,*********`:,:`:,:`:,:`:,:`:,:`***`:,:`:,:`:,
`:,:***:`:,:`:,:`:,:`:,:`:************,:`:,:`:,:`:,:`:,:`***`:,:`:,:`:,
`:,:***:`:,:`:,:`:,:`:,:`*************,:`:,:`:,:`:,:`:,:`***`:,:`:,:`:,
`:,:`:,:`:,:`:,:`:,:`:,:`**************:`:,:`:,:`:,:`:,:`***`:,:`:,:`:,
`:,:`:,:`:,:`:,:`:,:`:,:*****:,**:*****:`:,:`:,:`:,:`:,:`***`:,:`:,:`:,
`:,:`:,:`:,:`:,:`:,:`:,:****`:,**:,****:`:,:`:,:`:,:`:,:`***`:,:`:,:`:,
`:,:***:`:,:`:,:`:,:`:,:****`:,**:,:`:,:`:,:`:,:`:,:`:,:`***`********:,
`:,:***:`:,:`:,:`:,:`:,:*****:,**:,:`:,:`:,:`:,:`:,:`:,:`*************,
`:,:***:`:,:`:,:`:,:`:,:`********:,:`:,:`:,:`:,:`:,:`:,:`**************
`:,:***:`:,:`:,:`:,:`:,:`*********,:`:,:`:,:`:,:`:,:`:,:`**************
`:,:***:`:,:`:,:`:,:`:,:`:**********`:,:`:,:`:,:`:,:`:,:`*****,:`:,****
`:,:***:`:,:`:,:`:,:`:,:`:,***********,:`:,:`:,:`:,:`:,:`****:,:`:,****
`:,:***:`:,:`:,:`:,:`:,:`:,:`**********:`:,:`:,:`:,:`:,:`****:,:`:,****
`:,:***:`:,:`:,:`:,:`:,:`:,:`:,********:`:,:`:,:`:,:`:,:`****:,:`:,****
`:,:***:`:,:`:,:`:,:`:,:`:,:`:,**:,*****`:,:`:,:`:,:`:,:`***`:,:`:,****
`:,:***:`:,:`:,:`:,:`:,:`:,:`:,**:,:****`:,:`:,:`:,:`:,:`***`:,:`:,****
`:,:***:`:,:`:,:`:,:`:,:****`:,**:,:****`:,:`:,:`:,:`:,:`***`:,:`:,****
`:,:***:`:,:`:,:`:,:`:,:****`:,**:,:****`:,:`:,:`:,:`:,:`***`:,:`:,****
`:,:***:`:,:`:,:`:,:`:,:*****:,**:,*****`:,:`:,:`:,:`:,:`***`:,:`:,****
`:,:***:`:,:`:,:`:,:`:,:***************:`:,:`:,:`:,:`:,:`***`:,:`:,****
`:,:***:`:,:`:,:`:,:`:,:`**************:`:,:`:,:`:,:`:,:`***`:,:`:,****
`:,:***:`:,:`:,:`:,:`:,:`:************,:`:,:`:,:`:,:`:,:`***`:,:`:,****
`:,:***:`:,:`:,:`:,:`:,:`:,**********:,:`:,:`:,:`:,:`:,:`***`:,:`:,****
`:,:***:`:,:`:,:`:,:`:,:`:,:`:,**:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,
`:,****:`:,:`:,:`:,:`:,:`:,:`:,**:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,
`:*****:`:,:`:,:`:,:`:,:`:,:`:,**:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,
*******:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,
*******:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,
******,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,
`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,
`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,
`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,'
"""
from pri import nt

print = nt


def get_prominent_colors(image_path: str, colors: int) -> List[Tuple[int, int, int]]:
    px = []
    print("open")
    i = Image.open(image_path).convert("RGB")
    w, h = i.size
    print("pythonize")
    for y in range(h):
        for x in range(w):
            r, g, b = i.getpixel((x, y,))
            px.append((r, g, b,))
    print("init kmeans")
    kmeans = KMeans(n_clusters=colors)
    print("fit")
    kmeans.fit(np.array(px))
    freeq = {}
    label_to_color = {}
    print("iter8 labels")
    for label, color in zip(kmeans.labels_, px):
        if not label_to_color.get(label):
            label_to_color.update({label: color})
        freeq.update({label: freeq.get(label, 0) + 1})
    print("freq updated. return")
    # Create list of tuples, sorted by the frequency of the color
    sorted_tup_list: List[Tuple[int, int, int]] = []
    for k_v in sorted(freeq.items(), key=lambda _kv: _kv[1]):
        print(k_v)
        color = map(int, label_to_color[k_v[0]])
        print(color)
        sorted_tup_list.append(tuple(color))
    # print(sorted_tup_list)
    return sorted_tup_list
