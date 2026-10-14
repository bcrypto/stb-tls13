#!/bin/bash
# *****************************************************************************
# \file build.sh
# \brief Build RFC draft
# \project stb-tls13
# \created 2026.09.02
# \version 2026.10.14
# *****************************************************************************

scripts_dir=`pwd`
src_dir=$scripts_dir/../src
build_dir=$scripts_dir/..
draft_name=draft-stb-tls13.md

build(){
  mkdir -p $build_dir
  awk 'FNR==1 && NR!=1 {printf "\n"} 1' $src_dir/*.md > $build_dir/$draft_name
  cp -f $scripts_dir/makefile $build_dir
  cd $build_dir && make
}

build