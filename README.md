# reddit-scan-datasets
Simple datasets pulled from reddit to do nlp on.

Current datasets:

Titles from various subreddits pulled via pushift api

    - Conservative submission titles ~96k examples
    - Conspiracy submission titles ~134k examples
    - Politics submission titles ~120k examples
    - Guitar submission titles ~40k examples

Included is a utility script to merge these text datasets together to form new datasets from base files. Below is an example command to run the script which will take the path, get all files found via the path and then merge to a new file.

```
python MergeDataSets.py --directory 'data_sets/submission_titles_guitar_*.txt' --output 'data_sets/submission_titles_guitar_merged.txt'
```
