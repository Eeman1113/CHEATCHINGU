from scipy import misc
import imageio

def half_slicer():
        # Read the image
        img = imageio.imread("screenshot.png")
        height, width,length = img.shape
        
        # Cut the image in half
        width_cutoff = width // 2
        s1 = img[:, :width_cutoff]
        s2 = img[:, width_cutoff:]
        
        # Save each half
        imageio.imsave("face1.png", s1)
        imageio.imsave("face2.png", s2)
half_slicer()
