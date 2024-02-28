# uk-boundaries

A number of projects need boundary files as input into a pipeline. Those projects automate setup with scripts, but when some input files are not hosted statically somewhere in the correct form, making the scripts reproducible is challenging. <https://github.com/martinjc/UK-GeoJSON/> is a previous repo that worked around this by hosting the input files. The current ONS site does not offer static URLs to some files, and in fact some URLs to manually download a file have broken in the last year, so we are restarting this effort.

## To add a new file

Fork the repo, start a new branch, update the README following the examples below, and send a PR.

## 2021 Output Areas

Download: <https://github.com/dabreegster/uk-boundaries/raw/main/2021_output_areas.geojson.gz>
  - Note GitHub raw URLs use HTTP 302 to redirect. Use `curl -L <URL>` to follow.

- Format: GeoJSON file in WGS84, trimmed to 6 decimal places of precision, with only an `OA21CD` property
  - 23MB gzipped, 121MB uncompressed
- Source: Output Areas (December 2021) Boundaries EW BGC V2
  - Downloaded on 28 February 2024. The data was last updated 13 July 2023.
  - BGC means "Generalised (20m) - clipped to the coastline (Mean High Water mark)".
  - [License](https://www.ons.gov.uk/methodology/geography/licences)
    - Source: Office for National Statistics licensed under the Open Government Licence v.3.0
    - Contains OS data © Crown copyright and database right 2024

Steps to reproduce this:

1.  Go to <https://geoportal.statistics.gov.uk/datasets/6beafcfd9b9c4c9993a06b6b199d7e6d_0/explore>
2.  Download the GeoJSON file
3.  `ogr2ogr -f GeoJSON raw_2021_output_areas.geojson -t_srs EPSG:4326 ~/Downloads/Output_Areas_2021_EW_BGC_V2_-3080813486471056666.geojson`
4.  `python3 clean_gj.py raw_2021_output_areas.geojson 2021_output_areas.geojson`
5.  `gzip 2021_output_areas.geojson`

## License

Depends on the input file. Each section documents it. The (minimal) code for this repo is Apache 2.0.
