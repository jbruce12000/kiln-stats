#!/usr/bin/perl -w
use strict;

# This script splits a log up by adding a number
# at the start of each line.

my $x=0;
my $record=0;

while(<>) {

  if($_=~/schedule ended, shutting down/) {
    print "$x $_";
    $record=0;
    }

  if($_=~/Running schedule/) {
    $x++;
    $record=1;
    }

  if($record) {
    print "$x $_";
    }
  }
