#!/usr/bin/env python

"""Trim a BVH file by excepting a subset of its frames

Arguments:
in_file -- the input BVH file
out_file -- the BVH file to write the result to
start_time -- time (in seconds) where to start the except
end_time -- time (in seconds) where to end the except
"""

__author__ = "Gustav Eje Henter"
__email__ = "ghe@kth.se"
__copyright__ = "Copyright 2022, Gustav Eje Henter"
__license__ = "CC BY 4.0 International"

# Imports
import sys
import math
import warnings

def trim_bvh(in_file, out_file, start_time, end_time):
  assert start_time < end_time
  
  # Constants
  headerword = 'MOTION'
  framestr1 = 'Frames:'
  framestr2 = 'Frame Time:'
  
  with open(in_file, 'r') as fin, open(out_file, 'w') as fout:
    # Copy every line from the header to the new file
    line = fin.readline()
    while line:
      fout.write(line)
      if line[0:len(headerword)] == headerword:
        break
      line = fin.readline()
    
    # We now know that we have just read (and written)
    # the line with the header word
    
    line = fin.readline()
    assert line[0:len(framestr1)] == framestr1
    numframes = int(line[len(framestr1):])
    
    line = fin.readline()
    assert line[0:len(framestr2)] == framestr2
    frametime = float(line[len(framestr2):])
    
    # Cuts are based on the midpoints of each frame
    # The midpoint of the frame 0 is at frametime/2
    
    startframe = int(math.ceil((start_time/frametime) - (1/2)))
    assert startframe < numframes
    if startframe < 0:
      warnings.warn('Invalid first frame: ' + int(startframe) +
                    ' . Export will start from frame 0 instead.')
      startframe = 0
    
    endframe = int(math.floor((end_time/frametime) - (1/2)))
    assert endframe >= 0
    if endframe > numframes:
      warnings.warn('Invalid end frame: ' + int(endframe) +
                    ' . Export will end at frame ' + int(numframes-1) +
                    ' (the last frame) instead.')
      endframe = numframes - 1
    
    numframes = endframe - startframe + 1
    assert numframes > 0
    
    # Write the number of frames
    fout.write(framestr1 + ' ' + str(numframes) + '\n')
    
    fout.write(line) # Write the Frame Time line
    
    # Note: The code assumes that the number of lines
    # matches the given number of frames
    
    # Frames before the cut; discard
    for n in range(0, startframe):
      line = fin.readline()
    
    # Write the frames that we are keeping to file
    for n in range(startframe, endframe):
      line = fin.readline()
      fout.write(line)
    
    # Write the last line without a newline
    line = fin.readline()
    fout.write(line.rstrip('\n').rstrip('\r'))
    
    # Remaining frames are after the cut; we don't need to consider those

if __name__ == '__main__':
  assert len(sys. argv) == 5
  args = sys.argv[1:]
  sys.exit(trim_bvh(args[0], args[1], args[2], args[3]))