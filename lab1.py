import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image


def merge_channels(r, g, b):
    return np.stack((r, g, b), axis=-1)

def show_all_img(img, type_filter):
    r_img = img[:, :, 0]
    g_img = img[:, :, 1]
    b_img = img[:, :, 2]

    if type_filter == 'erode':
        r_filtered_img = erode(r_img, kernel)
        g_filtered_img = erode(g_img, kernel)
        b_filtered_img = erode(b_img, kernel)
    elif type_filter == 'dilate':
        r_filtered_img = dilate(r_img, kernel)
        g_filtered_img = dilate(g_img, kernel)
        b_filtered_img = dilate(b_img, kernel)
    elif type_filter == 'median':
        r_filtered_img = median(r_img, kernel)
        g_filtered_img = median(g_img, kernel)
        b_filtered_img = median(b_img, kernel)
    elif type_filter == 'gaussian':
        r_filtered_img = gaussian(r_img, kernel)
        g_filtered_img = gaussian(g_img, kernel)
        b_filtered_img = gaussian(b_img, kernel)
    elif type_filter == 'lighting_correction':
        r_filtered_img = lighting_correction(r_img)
        g_filtered_img = lighting_correction(g_img)
        b_filtered_img = lighting_correction(b_img)
    elif type_filter == 'gamma_correction':
        r_filtered_img = gamma_correction(r_img)
        g_filtered_img = gamma_correction(g_img)
        b_filtered_img = gamma_correction(b_img)
    elif type_filter == 'binarization':
        r_filtered_img = binarization(r_img)
        g_filtered_img = binarization(g_img)
        b_filtered_img = binarization(b_img)
        
    filtered_img = merge_channels(r_filtered_img, g_filtered_img, b_filtered_img)
    plt.figure(figsize=(15, 6))

    # Original images
    plt.subplot(2, 4, 1)
    plt.title('Original Image')
    plt.imshow(img)
    plt.axis('off')

    plt.subplot(2, 4, 2)
    plt.title('Original R Channel')
    plt.imshow(r_img, cmap='gray')
    plt.axis('off')

    plt.subplot(2, 4, 3)
    plt.title('Original G Channel')
    plt.imshow(g_img, cmap='gray')
    plt.axis('off')

    plt.subplot(2, 4, 4)
    plt.title('Original B Channel')
    plt.imshow(b_img, cmap='gray')
    plt.axis('off')

    # Filtered images
    plt.subplot(2, 4, 5)
    plt.title("Filtered Image")
    plt.imshow(filtered_img)
    plt.axis('off')

    plt.subplot(2, 4, 6)
    plt.title("Filtered R Channel")
    plt.imshow(r_filtered_img, cmap='gray')
    plt.axis('off')


    plt.subplot(2, 4, 7)
    plt.title("Filtered G Channel")
    plt.imshow(g_filtered_img, cmap='gray')
    plt.axis('off')

    plt.subplot(2, 4, 8)
    plt.title("Filtered B Channel")
    plt.imshow(b_filtered_img, cmap='gray')
    plt.axis('off')

    plt.show()
    return filtered_img

def plot_rgb_histograms(img, filtered_img, title="RGB Histograms Comparison"):
    img = np.array(img)
    filtered_img = np.array(filtered_img)
    colors = ['Red', 'Green', 'Blue']
    
    plt.figure(figsize=(16, 6))
    
    for i, color in enumerate(colors):
        plt.subplot(2, 3, i + 1)
        plt.hist(img[:, :, i].ravel(), bins=256, color=color.lower(), alpha=0.7)
        plt.title(f'{color} Channel - Original')
        plt.xlabel('Pixel Value')
        plt.ylabel('Frequency')

        plt.subplot(2, 3, i + 4)
        plt.hist(filtered_img[:, :, i].ravel(), bins=256, color=color.lower(), alpha=0.7)
        plt.title(f'{color} Channel - Filtered')
        plt.xlabel('Pixel Value')
        plt.ylabel('Frequency')

    plt.tight_layout()
    plt.show()

#Erode filter
def erode(img, kernel):
    img_h, img_w = img.shape
    eroded_img = np.zeros_like(img, dtype=np.uint8)
    
    k_h, k_w = kernel.shape
    pad_h, pad_w = k_h // 2, k_w // 2
    
    # Padding
    padded_img = np.pad(img, ((pad_h, pad_h), (pad_w, pad_w)), mode='edge')

    # Erosion
    for i in range(img_h):
        for j in range(img_w):
            roi = padded_img[i:i + k_h, j:j + k_w]
            eroded_img[i, j] = np.min(roi)
    
    return eroded_img

#Dilate filter
def dilate(img, kernel):
    img_h, img_w = img.shape
    dilated_img = np.zeros_like(img, dtype=np.uint8)
    
    k_h, k_w = kernel.shape
    pad_h, pad_w = k_h // 2, k_w // 2
    padded_img = np.pad(img, ((pad_h, pad_h), (pad_w, pad_w)), mode='edge')

    for i in range(img_h):
        for j in range(img_w):
            roi = padded_img[i:i + k_h, j:j + k_w]
            dilated_img[i, j] = np.max(roi)
    
    return dilated_img

#Median filter
def median(img, kernel):
    img_h, img_w = img.shape
    median_img = np.zeros_like(img, dtype=np.uint8)
    
    kernel_size = kernel.shape[0]
    pad = kernel_size // 2
    
    # Padding
    padded_img = np.pad(img, pad, mode='edge')

    for i in range(img_h):
        for j in range(img_w):
            roi = padded_img[i:i + kernel_size, j:j + kernel_size]
            median_img[i, j] = np.median(roi)
    
    return median_img

#Create kernel for gaussian filter
def create_gaussian_kernel(kernel_size, sigma):
    kernel = np.zeros((kernel_size, kernel_size))
    for i in range(kernel_size):
        for j in range(kernel_size):
            kernel[i, j] = np.exp(-((i - kernel_size // 2) ** 2 + (j - kernel_size // 2) ** 2) / (2 * sigma ** 2)) / (2 * np.pi * sigma ** 2)
    return kernel/np.sum(kernel)

#Gaussian filter
def gaussian(img, kernel, sigma = 2):
    img_h, img_w = img.shape
    gaussian_img = np.zeros_like(img, dtype=np.uint8)
    kernel_size = kernel.shape[0]
    
    pad = kernel_size // 2
    padded_img = np.pad(img, pad, mode='edge')
    kernel = create_gaussian_kernel(kernel_size, sigma)

    for i in range(img_h):
        for j in range(img_w):
            roi = padded_img[i:i + kernel_size, j:j + kernel_size]
            gaussian_img[i, j] = np.sum(roi * kernel)

    return gaussian_img

# Lighting correction
def lighting_correction(img, brightness = 2):
    corrected_img = img.astype(np.float64) * brightness
    corrected_img = np.clip(corrected_img, 0, 255).astype(np.uint8)
    return corrected_img

# Gamma correction
def gamma_correction(img, gamma=0.5):
    gamma_corrected_img = np.power(img / 255.0, gamma) * 255.0
    return gamma_corrected_img.astype(np.uint8)


# Binarization
def binarization(img, threshold=128):
    binary_img = np.where(img >= threshold, 255, 0).astype(np.uint8)
    return binary_img


img = Image.open('images/image-5.png')
# img = Image.open('images/salt_and_pepper.jpeg')
img = np.array(img)
kernel = np.ones((3, 3), dtype=np.uint8)
filtered_img = show_all_img(img, 'binarization')
# plot_rgb_histograms(img, filtered_img)