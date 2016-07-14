# Create sub direcotry mobi inside all the subdirectories of current directory
for dir in */; do mkdir -- "$dir/mobi"; done
# Move all the files with extension mobi inside subdirectory of subdirectory
for dir in */; do mv "$dir"/*.mobi "$dir/mobi/"; done
