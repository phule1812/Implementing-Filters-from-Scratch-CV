# Computer Vision Lab 1: Implementing Filters from Scratch 
## Introduction: 
This lab focuses on building fundamental image processing filters from scratch using only NumPy for calculations and Matplotlib for visualization. The goal is to gain a deep understanding of how filters work at a pixel level, rather than relying on high-level libraries like OpenCV.
In this lab, it was nessessary to implement the following filters:
1. Erosion
2. Dilation
3. Median
4. Gaussian
5. Light correction
6. Gamma correction
7. Binarization

## RGB Channel Filtering
Each filter is applied independently to the Red (R), Green (G), and Blue (B) channels of the image. The workflow is as follows:
1. Split the RGB image into its three channels: R, G, B.
2. Apply the filter to each channel separately.
3. Merge the processed channels back together to form the final filtered RGB image.

This method ensures that the effect of the filters is reflected in the composite image while preserving the color relationships between channels.

## Implemented filters:
### 1. Erosion Filter
Erosion reduces the boundaries of the foreground object by applying a minimum filter. It is useful for removing small white noise and separating two connected objects. 

**Mathematical Formula**:

$$\
E(x,y) = \min_{(i,j) \in K} I(x+i, y+j)
\$$

Where:
- $\ E(x,y)\$: the eroded pixel value at position \$(x,y)\$
- $\ I(x+i, y+j) \$: pixel values in the neighborhood defined by the kernel $\ K \$
- $\ K \$: the structuring element (kernel) used to probe the image

**Code implementation**: The kernel slides over the image, and at each position, the minimum pixel value within the kernel's area is taken as the output. This shrinks bright regions and enlarges dark regions. 
See `erode()` function in `lab1.py`.

**Results**: After Erosion, bright areaes are shunk, especially noticeable in the R channel (due to the orange color of the cat's fur). Fine details and white noise are also removed or reduced.
Dark areas become more prominent due to the shrinkage of the highlights.

![](images/erode.png)
