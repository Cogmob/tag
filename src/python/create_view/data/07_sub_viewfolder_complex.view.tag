viewfiles:
-   tags: [root]
    files: [file]
    folders:
        four_legs: [four_legs]
        less_than_four_legs: [two_legs no_legs]
    foreach:
        files: [files]
        folders:
            green: [green]
            brown: [brown]
-   tags: [four_legs]
    files: [file]
    folders:
        red_eyes: [red_eyes]
    foreach:
        files: []
        folders:
            fast: [fast]
