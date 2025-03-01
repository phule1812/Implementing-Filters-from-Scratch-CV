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

### 4. Gaussian filter
Gaussian filtering applies a convolution with a Gaussian kernel, smoothing the image and reducing high-frequency noise.

**Mathematical Formula**:

$$\
G(x,y) = \sum_{i,j} I(x+i, y+j) \cdot K(i,j)
\$$

The Gaussian kernel  is calculated as:

$$\
K(i,j) = \frac{1}{2\pi\sigma^2} e^{-\frac{i^2 + j^2}{2\sigma^2}}
\$$

where:
- $\ G(x,y)\$: the output pixel value after Gaussian filtering at position 
- $\ I(x+i, y+j)\$: the pixel value at position  in the input image
- $\ K(i,j)\$: the Gaussian kernel value at position 
- $\sigma$ : the standard deviation of the Gaussian distribution, controlling the amount of blur

**Effect of $\sigma$**:
- A **small $\sigma$**results in a narrow Gaussian kernel, causing minimal blurring and preserving more details.
- A **large $\sigma$** produces a wider kernel, leading to stronger blurring and smoother results, but at the cost of losing fine details.

**Code implementation**: The kernel is a 2D bell-shaped curve that gives more weight to central pixels and less to distant ones, resulting in a soft blurring effect.
See `gaussian()` function in `lab1.py`

**Results**: After Gaussian filter:
Based on the image processed with the Gaussian filter:
- The filtered image appears smoother, with fine details like the cat's fur and eye edges slightly blurred.
- The major outlines and shapes of the cat remain clear, indicating that the Gaussian filter blurs softly without completely erasing important details.
- When comparing each color channel, small noise is reduced, but the contrast between different regions of color is reasonably preserved.

![](images/guassian.png)

