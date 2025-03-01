#!/bin/bash

while IFS= read -r line; do
  file_path=$(echo "$line" | cut -d' ' -f1)
  description=$(echo "$line" | cut -d' ' -f2-)

  python3 ./analysis.py "$file_path" "$description"
done < "for_analysis.txt"
