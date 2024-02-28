import json
import sys


def main():
    if len(sys.argv) < 3:
        print("Usage: python3 clean_gj.py input.geojson output.geojson")
        sys.exit(1)

    if sys.argv[2] == "2021_output_areas.geojson":

        def fixProps(inputProps):
            return {
                "OA21CD": inputProps["OA21CD"],
            }

        cleanUpGeojson(sys.argv[1], sys.argv[2], fixProps)
    else:
        print(
            f"Unknown output file {sys.argv[2]}. Manually edit the script to decide what properties to keep."
        )
        sys.exit(1)


# This method cleans up a GeoJSON file in a few ways:
#
# - Removes redundant top-level attributes set by ogr2ogr
# - Trims coordinate precision
# - Uses the transformProperties callback to transform each feature's
#   properties. The callback takes input properties and should return output
#   properties.
def cleanUpGeojson(inputPath, outputPath, transformProperties):
    print(f"Turning {inputPath} into {outputPath}")
    gj = {}
    with open(inputPath) as f:
        gj = json.load(f)

        # Remove unnecessary attributes present in some files
        for key in ["name", "crs"]:
            if key in gj:
                del gj[key]

        for feature in gj["features"]:
            del feature["id"]

            feature["properties"] = transformProperties(feature["properties"])

            feature["geometry"]["coordinates"] = trimPrecision(
                feature["geometry"]["coordinates"]
            )
    with open(outputPath, "w") as f:
        f.write(json.dumps(gj))


# Round coordinates to 6 decimal places. Takes feature.geometry.coordinates,
# handling any type.
def trimPrecision(data):
    if isinstance(data, list):
        return [trimPrecision(x) for x in data]
    elif isinstance(data, float):
        return round(data, 6)
    else:
        raise Exception(f"Unexpected data within coordinates: {data}")


if __name__ == "__main__":
    main()
