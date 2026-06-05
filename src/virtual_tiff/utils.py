from __future__ import annotations


def check_no_partial_strips(image_height: int, rows_per_strip: int):
    """Check that there are no partial chunks based on the image height and rows per strip"""
    if image_height % rows_per_strip > 0:
        raise ValueError(
            "Zarr's default chunk grid expects all chunks to be equal size, but this TIFF has an image height of "
            f"{image_height} which isn't evenly divisible by its rows per strip {rows_per_strip}. "
            "See https://github.com/developmentseed/virtual-tiff/issues/24 for more details."
        )
