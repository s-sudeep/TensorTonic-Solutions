def color_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminance weights.
    """
    # Write code here
    final_res = []
    for i in image:
        per_filter = []
        for r,g,b in i:
            per_filter.append(0.299*r + 0.587*g + 0.114*b)
        final_res.append(per_filter)
    return final_res
        