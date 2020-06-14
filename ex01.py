from url_image import (
    download_image,
    save_image,
    apply_filter_blur,  
    get_image_name, 
    open_image,  
    download_image2,
    show_img
)

download_image('http://site.meishij.net/r/58/25/3568808/a3568808_142682562777944.jpg')
img = open_image('a3568808_142682562777944.jpg')
img_with_blur = apply_filter_blur(img)
save_image("image_antiga.jpg", img)
save_image("image_com_filtro.jpg", img_with_blur)

show_img(img_with_blur)
show_img(img)
