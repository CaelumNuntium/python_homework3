import textwrap
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("input", action="store", help="Name of the input file")
parser.add_argument("-o", "--output", action="store", default="output.txt", help="Name of the output file")
parser.add_argument("--encoding", action="store", default="utf_8", help="Input file encoding. Default value is 'utf_8'")
args = parser.parse_args()
with open(args.input, "r", encoding=args.encoding) as inp:
    with open(args.output, "w") as out:
        for s in inp:
            if len(s) > 90:
                strings = textwrap.wrap(s, width=70)
                for sw in strings:
                    out.write(sw + "\n")
            else:
                out.write(s + "\n")
