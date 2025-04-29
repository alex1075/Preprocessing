

chan_diam_pix = 1450
chan_diam_um = 200
margin_error_pix = 18

pixel_size = round(chan_diam_um / chan_diam_pix, 4)
margin_error_um = round(margin_error_pix * pixel_size, 4)

pixel_area_um = round((pixel_size) ** 2, 4)

print("Pixel size: ", pixel_size)
print("Margin error: ", margin_error_um)
print("Area: ", pixel_area_um)

# print dimentsions for a 416x416 image in um
image_width = 3840
image_height = 2160
print("Image width:", image_width * pixel_size, "um")
print("Image height:", image_height * pixel_size, 'um')
