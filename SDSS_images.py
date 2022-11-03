import argparse
import urllib.request
options_help = """
List of Drawing Options:
G	Grid	\tDraw a N-S E-W grid through the center
L	Label	\tDraw the name, scale, ra, and dec on image
P	PhotoObj	Draw a small circle around each primary photoObj
S	SpecObj	\tDraw a small square around each specObj
O	Outline	\tDraw the outline of each photoObj
B	Bounding Box	Draw the bounding box of each photoObj
F	Fields	\tDraw the outline of each field
M	Masks	\tDraw the outline of each mask considered to be important
Q	Plates	\tDraw the outline of each plate
I	Invert	\tInvert the image (B on W)
"""
parser = argparse.ArgumentParser(epilog=options_help, formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument("ra", action="store", help="center point right ascension in J2000 decimal degrees or hh:mm:ss.s")
parser.add_argument("dec", action="store", help="center point declination in J2000 decimal degrees or dd:mm:ss.s")
parser.add_argument("--scale", action="store", default="0.396127", help="arcsec/pixel (default value is 0.396127)")
parser.add_argument("-s", "--size", action="store", nargs=2, default=["400", "400"], help="image size in pixels")
parser.add_argument("-o", "--output", action="store", default="output.jpg", help="output file name")
parser.add_argument("--options", action="store", default="", help="options string, a set of upper-case characters")
args = parser.parse_args()
url = "http://skyserver.sdss.org/dr16/SkyServerWS/ImgCutout/getjpeg?ra=" + args.ra + "&dec=" + args.dec + "&scale=" + args.scale + "&width=" + args.size[0] + "&height=" + args.size[1] + "&opt=" + args.options
urllib.request.urlretrieve(url, args.output)
