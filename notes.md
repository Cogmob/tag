## example

# traditional filesystem

page 1
	page.html
	logo_red.jpg
page 2
	page.html
	logo_blue.jpg
shared
	header.jpg

# page oriented perspective

header_image
pages_tag_group
page_1
	html
	logo_image
    \_bin
        logo_image
page_2
	html
	logo_image
    \_bin
        logo_image

# type oriented perspective

types_tag_group
html
    page_1
    page_2
images
    page_1_logo
    page_2_logo
    header_image
    \_bin
        page_1_logo
        page_2_logo
        header_image
