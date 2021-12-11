import argparse


def parse_argv():
    # Initiate the parser
    parser = argparse.ArgumentParser(description='It is program for comparing two json files')

    # Add required arguments
    parser.add_argument("source_filename", help="filename of the source json file", type=str)
    parser.add_argument("compared_filename", help="filename of the compared json file", type=str)

    # Add long and short optional arguments
    parser.add_argument("--source", "-s", help="designation of the source file", type=str)
    parser.add_argument("--compared", "-c", help="designation of the compared file", type=str)
    parser.add_argument("--filenames", "-f", help="use filenames for designation of the files", action="store_true")

    # Read arguments from the command line
    args = parser.parse_args()
    return args


def define_designations(args=None):
    if not args:
        args = parse_argv()

    s, c = 'src', 'cmp'
    if args.source:
        s = args.source
    if args.compared:
        c = args.compared
    if args.filenames:
        s, c = args.source_filename, args.compared_filename

    return s, c
