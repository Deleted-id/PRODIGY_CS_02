# importing required libraries 
from PIL import Image
import numpy as np

# encryption method
def encrypt_image(image_path, key):
    # open the image
    img = Image.open(image_path)
    
    # converting the image to a numpy array
    img_array = np.array(img)
    
    # converting the 3d to 1d array
    flattend_array = img_array.flatten()
    
    # Store the permutation indices for decryption
    permutation_indices = np.random.permutation(len(flattend_array))
    
    # shuffling the array
    shuffeld_array = flattend_array[permutation_indices]
    
     # Store the permutation indices for decryption
    np.save('key.npy', permutation_indices)
    
    print("Encrypting image.....") # encrypting image message
    
    # encrypting the array using xor
    encrypted_array = np.bitwise_xor(shuffeld_array, key % 256)
    
    # reshaping the array to form a shape
    encrypted_array = encrypted_array.reshape(img_array.shape)
    
    # converting the array into an image
    encrypted_img = Image.fromarray(encrypted_array.astype('uint8'))
    
    # saving the image with new name
    encrypted_img.save('encrypted_img.png')

    # #success message 
    print("Image encryption successfull")
    
    
  
# decryption method  
def decrypt_image(image_path, key):
    # open the image
    encrypted_img = Image.open(image_path)
    
    # converting the image to array
    encrypted_array = np.array(encrypted_img)
    
    # converting to flattend array
    flattend_array = encrypted_array.flatten()
    
    print("Decrypting image.....") # decrypting image message
    
    # reversing the xor 
    decrypted_array = np.bitwise_xor(flattend_array, key % 256)
    
    # loading the permutaion indices
    permutaion_indices = np.load("key.npy")
    
    # unshuffle array
    unshuffled_array = decrypted_array[np.argsort(permutaion_indices)]
    
    # reshaping the array to original shape
    decrypted_array = unshuffled_array.reshape(encrypted_array.shape)
    
    # converting the array back to an image
    decrypted_image = Image.fromarray(decrypted_array.astype('uint8'))
    
    # saving the image 
    decrypted_image.save("decrypted_img.png")
    
    # success message
    print("Image Decryption Successfully")