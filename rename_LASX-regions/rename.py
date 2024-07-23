import xml.etree.ElementTree as ET
import sys

def rename_regions(in_fn, out_fn=None):
    if out_fn is None:
        out_fn = in_fn

    tree = ET.parse(in_fn)
    root = tree.getroot()

    for r in root.find('Regions/ShapeList/Items'):
        row = r.find('Name').text
        for c in r.find('Children/Items'):
            col = c.find('Name').text
            for s in c.find('Children/Items'):
                name = s.find('Name')
                name.text = f"{row}{int(col):02d}_{name.text}"

    tree.write(out_fn)

if __name__ == "__main__":
    # Check if the script received the correct number of arguments
    if len(sys.argv) < 2:
        print("Usage: python script.py <input_file> [<output_file>]")
        sys.exit(1)

    in_fn = sys.argv[1]
    out_fn = sys.argv[2] if len(sys.argv) > 2 else None

    if len(sys.argv) > 3:
        print("Too many arguments, only the first two will be used")

    rename_regions(in_fn, out_fn)