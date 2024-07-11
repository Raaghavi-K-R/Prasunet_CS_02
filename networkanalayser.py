from PIL import Image
import os

def encrypt_image(image_path, key):
    try:
        # Open the image file
        img = Image.open(image_path)
        width, height = img.size
        pixels = img.load()

        # Encrypt each pixel value using XOR with key
        for i in range(width):
            for j in range(height):
                r, g, b = pixels[i, j]
                r ^= key
                g ^= key
                b ^= key
                pixels[i, j] = (r, g, b)

        # Save the encrypted image
        encrypted_image_path = os.path.join(os.path.dirname(image_path), "images_encrypted.png")
        img.save(encrypted_image_path)
        print(f"Image encrypted and saved as: {encrypted_image_path}")

    except Exception as e:
        print(f"Error encrypting image: {e}")

def decrypt_image(encrypted_image_path, key):
    try:
        # Open the encrypted image file
        img = Image.open(encrypted_image_path)
        width, height = img.size
        pixels = img.load()

        # Decrypt each pixel value using XOR with key
        for i in range(width):
            for j in range(height):
                r, g, b = pixels[i, j]
                r ^= key
                g ^= key
                b ^= key
                pixels[i, j] = (r, g, b)

        # Save the decrypted image
        decrypted_image_path = os.path.join(os.path.dirname(encrypted_image_path), "images_decrypted.png")
        img.save(decrypted_image_path)
        print(f"Image decrypted and saved as: {decrypted_image_path}")

    except Exception as e:
        print(f"Error decrypting image: {e}")

# Example usage
if __name__ == "__main__":
    # Replace with the full path of the image in the Downloads folder
    image_path = os.path.expanduser("~/Downloads/images.jpeg")

    # Check if the image path is valid
    if not os.path.isfile(image_path):
        print("Invalid image path. Please provide a valid path to an image file.")
    else:
        # Replace with your encryption key (must be the same for encryption and decryption)
        encryption_key = int(input("Enter the encryption key (integer): ").strip())

        # Encrypt the image
        encrypt_image(image_path, encryption_key)

        # Decrypt the encrypted image
        encrypted_image_path = os.path.join(os.path.dirname(image_path), "images_encrypted.png")
        decrypt_image(encrypted_image_path, encryption_key)
