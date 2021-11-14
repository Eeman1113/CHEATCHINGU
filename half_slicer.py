from scipy import misc
import imageio

def half_slicer():
        # Read the image
        img = imageio.imread("screenshot.png")
        height, width = img.shape(1080, 1920)
        
        # Cut the image in half
        width_cutoff = width // 2
        s1 = img[:, :width_cutoff]
        s2 = img[:, width_cutoff:]
        
        # Save each half
        misc.imsave("face1.png", s1)
        misc.imsave("face2.png", s2)
half_slicer()
