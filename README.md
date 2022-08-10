# trim_bhv

This repository provides a tiny utility function `trim_bvh` for trimming out excerpts from character motion data in the BVH (Biovision hierarchy) format.

## Usage

Invoke the `trim_bvh` method as follows:
```
import trim_bvh
trim_bvh.trim_bvh(in_file, out_file, start_time, end_time)
```

This command reads the file `in_file` and writes an excerpt of its motion to `out_file`, keeping only the frames between `start_time` and `end_time` (which are given in seconds). More specifically, the code retains only those the frames whose midpoints fall between `start_time` and `end_time`, inclusive.

Note: `in_file` is assumed to contain well-formed data in the BVH format. The code contains some basic error checking, but it has not been extensively tested. Pull requests for bug fixes and enhancements are warmly welcome!

## Other resources

The code was originally created for [the GENEA Challenge 2022](https://youngwoo-yoon.github.io/GENEAchallenge2022/), where it was used to crop out training, validation, and test data, and also to extract short motion stimuli for the evaluation from longer motion chunks.

For more information about the BVH format, see the file specification at [https://research.cs.wisc.edu/graphics/Courses/cs-838-1999/Jeff/BVH.html](https://research.cs.wisc.edu/graphics/Courses/cs-838-1999/Jeff/BVH.html).

## Author and license

`trim_bvh` was written by Gustav Eje Henter in 2022. The code is released under a CC BY 4.0 license, as seen in the enclosed LICENSE.txt file.
