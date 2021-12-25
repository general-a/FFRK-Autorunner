from PIL import Image

def imageHelper():
    # open method used to open different extension image file
    im = Image.open('etc\images\screenshots\gamestate.png') 
    
    # This method will show image in any image viewer 
    im.show() 