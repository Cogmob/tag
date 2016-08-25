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
tag
page_1
	html
    images
		logo
		header
		\_bin
			logo_image
page_2
	html
    images
        logo
        header
        \_bin
            logo_image

# type oriented perspective

tag
html
    page_1
    page_2
image
    page_1_logo
    page_2_logo
    header_image
    \_bin
        page_1_logo
        page_2_logo
        header_image

# page 1 logo image tag header

page_1 logo image
red
__
bin

# page oriented root tag file

tags = \root
child_tag_groups = \pages

pages = make_tag_group do
    name: \pages
    tags:
        \page_1
        \page_2

pages.init_child = ->
    child_tags = \image

# type oriented perspective root tag file

tags = \root
child_tag_groups = \types

types = make_tag_group do
    name: \types
    tags:
        \html
        \image

types.init_child = ->
    child_tags = \image
