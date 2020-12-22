import json

import pytest

from hyp3lib import DemError
from hyp3lib.dem import get_best_dem, utm_from_lat_lon, get_coverage_geometry


def test_get_best_dem():
    # assert get_best_dem(y_min=38.2, y_max=38.8, x_min=-110.8, x_max=-110.2) == 'NED13'
    assert get_best_dem(y_min=-6.8, y_max=-6.2, x_min=27.2, x_max=27.8) == 'SRTMGL1'
    # assert get_best_dem(y_min=67.9, y_max=68.1, x_min=-155.6, x_max=-155.4) == 'NED2'
    assert get_best_dem(y_min=59.975, y_max=60.1, x_min=99.5, x_max=100.5) == 'COP30'
    assert get_best_dem(y_min=59.976, y_max=60.1, x_min=99.5, x_max=100.5) == 'COP30'

    with pytest.raises(DemError):
        get_best_dem(y_min=0, y_max=1, x_min=0, x_max=1)


def test_utm_from_lat_lon():
    assert utm_from_lat_lon(0, 0) == 32631
    assert utm_from_lat_lon(-1, -179) == 32701
    assert utm_from_lat_lon(1, 179) == 32660
    assert utm_from_lat_lon(89, 27) == 32635
    assert utm_from_lat_lon(1, 182) == 32601
    assert utm_from_lat_lon(1, -182) == 32660
    assert utm_from_lat_lon(-1, -360) == 32731


def test_get_coverage_geometry(tmp_path):
    coverage_file = tmp_path / 'coverage.geojson'
    geojson = {
        "type": "FeatureCollection",
        'features': [
            {
                'type': 'Feature',
                'geometry': {
                  'type': 'Point',
                  'coordinates': [125.6, 10.1],
                },
            },
        ],
    }
    with open(coverage_file, 'w') as f:
        json.dump(geojson, f)

    geom = get_coverage_geometry(str(coverage_file))
    assert geom.ExportToWkt() == 'POINT (125.6 10.1)'


# def test_get_best_dem_antimeridian():
#     # aleutian islands
#     name, projection, tile_list, wkt_list = get_best_dem(y_min=51.3, y_max=51.7, x_min=-179.5, x_max=179.5)
#     assert name == 'SRTMGL1'
#     assert projection == 4326
#     assert len(tile_list) == 241
#     for tile in tile_list:
#         assert tile.startswith('N51')
#     assert len(wkt_list) == 241
#
#
# def test_get_best_dem_antimeridian_shifted():
#     # aleutian islands
#     name, projection, tile_list, wkt_list = get_best_dem(y_min=51.3, y_max=51.7, x_min=179.5, x_max=180.5)
#     assert name == 'SRTMGL1'
#     assert projection == 4326
#     assert tile_list == ['N51E179', 'N51W180']
#     assert wkt_list == [
#         'POLYGON ((178.999861 52.000139,180.000138777786 52.000139,180.000138777786 50.9998612222142,'
#         '178.999861 50.9998612222142,178.999861 52.000139))',
#         'POLYGON ((179.999861 52.000139,181.000138777786 52.000139,181.000138777786 50.9998612222142,'
#         '179.999861 50.9998612222142,179.999861 52.000139))',
#     ]
