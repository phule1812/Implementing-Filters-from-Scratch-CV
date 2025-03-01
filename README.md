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

**Results**: After Erosion, bright areaes are shunk, especially noticeable in the R channel (due to the orange color of the cat's fur). Fine details and white noise are also removed or reduced. Dark areas become more prominent due to the shrinkage of the highlights.

![](images/erode.png)

### 2. Dilation Filter
Dilation adds pixels to the boundaries of objects by applying a maximum filter. It helps to connect broken parts of an object.

**Mathematical Formula**:

$$\
D(x,y) = \max_{(i,j) \in K} I(x+i, y+j)
\$$

Where:
- $\ D(x,y)\$: the dilated pixel value at position \$(x,y)\$
- $\ I(x+i, y+j) \$: pixel values in the neighborhood defined by the kernel $\ K \$
- $\ K \$: the structuring element (kernel) used to probe the image

**Code implementation**: The kernel moves across the image, and at each position, the maximum pixel value within the kernel is taken as the output. This enlarges bright regions and shrinks dark ones.
See `dilate()` function in `lab1.py`

**Results**: Dilation has the opposite effect of erosion; it expands bright regions and shrinks dark areas:
- Edges and small bright details have become more pronounced compared to the original image.
- Thin lines and bright regions appear thicker, making features like whiskers or fur more prominent.
- Dark areas have been reduced, and bright areas have expanded, improving visibility in certain regions.

![](images/dilate.png)

### 3. Median Filter
The median filter replaces each pixel with the median value of its neighbors. This is particularly effective in removing salt-and-pepper noise.

**Mathematical Formula**:

$$\
M(x,y) = \text{median}\{I(x+i, y+j) | (i,j) \in K\}
\$$

**Code implementation**: For each pixel, the values in its neighborhood are sorted, and the median value is assigned to the central pixel.
See `median()` function in `lab1.py`

**Results**: The median filter effectively removes salt-and-pepper noise by replacing extreme pixel values with more representative values from their neighborhood. The filtered result shows:
- Reduced noise in all RGB channels.
- Smoother color transitions without blurring sharp edges.

![](images/median.png)
