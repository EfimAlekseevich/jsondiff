import argparse


def parse_argv():
    """Command-line parsing arguments"""
    # Initiate the parser
    parser = argparse.ArgumentParser(description='It is program for comparing two json files')

    # Add required arguments
    parser.add_argument("source_filename", help="filename of the source json file", type=str)
    parser.add_argument("compared_filename", help="filename of the compared json file", type=str)

    # Add long and short optional arguments
    parser.add_argument("--source", "-s", help="designation of the source file", type=str)
    parser.add_argument("--compared", "-c", help="designation of the compared file", type=str)
    parser.add_argument("--filenames", "-f", help="use filenames for designation of the files", action="store_true")
    parser.add_argument("--result_filename", "-r", help="name for result file", type =str)
    parser.add_argument("--text", "-t", help="save result to txt", action="store_true")
    parser.add_argument("--json", "-j", help='save result to json !integer keys will replaced strings (1 -> "1")!',
                        action="store_true")

    # Read arguments from the command line
    args = parser.parse_args()
    return args


def define_designations(args=None):
    """Defining designations for source and compared in result"""
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
