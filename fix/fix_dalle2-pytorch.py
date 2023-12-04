import os


import dalle2_pytorch_code
dir_path = dalle2_pytorch_code.__path__[0]
file_path = os.path.join(dir_path, 'dalle2_pytorch.py')

# with open(file_path, 'r') as file:
#     content = file.readlines()

# modified_content = [
#     line.replace('self.decoder.sample(image_embed', 'images = self.decoder.sample(image_embed = image_embed') 
#     for line in content
# ]

# with open(file_path, 'w') as file:
#     file.writelines(modified_content)
