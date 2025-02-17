from PIL import Image
import io

def stitch_images(images, max_height=3000):
    """
    Stitch multiple images vertically into a single image
    with consideration for maximum dimensions
    """
    if not images:
        return None
        
    # Calculate dimensions
    total_height = sum(img.size[1] for img in images)
    max_width = max(img.size[0] for img in images)
    
    # Create new image
    stitched = Image.new('RGB', (max_width, total_height), (255, 255, 255))
    
    # Paste images
    y_offset = 0
    for img in images:
        stitched.paste(img, (0, y_offset))
        y_offset += img.size[1]
    
    # Resize if needed
    if total_height > max_height:
        ratio = max_height / total_height
        new_width = int(max_width * ratio)
        stitched = stitched.resize((new_width, max_height), Image.Resampling.LANCZOS)
    
    return stitched

def image_to_bytes(image):
    """Convert PIL Image to bytes"""
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    return img_byte_arr.getvalue()
