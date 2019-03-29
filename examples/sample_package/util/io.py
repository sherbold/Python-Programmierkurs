def print_with_linenumbers(*args, numberwidth=3):
    """Prints every argument in a new line and adds line numbers"""
    for i,arg in enumerate(args):
        print(f"{i:0{numberwidth}d}: {arg}")
