# reddit-scan-datasets
Simple datasets pulled from reddit to do nlp on. Related to the Enki project.

Current datasets:

Titles from various subreddits pulled via pushift api
    - Conservative submission titles ~96k examples
    - Conspiracy submission titles ~134k examples
    - Politics submission titles ~120k examples
    - Guitar submission titles ~40k examples

Largest dataset are titles scrapped from the conpsiracy subreddit with over 480k examples.
They are split up by data pull session but will also contain a single merged file of all previous pulls. lm model trained on all the data perplexity = 12.097483902976112

Included is a utility script to merge these text datasets together to form new datasets from base files. Below is an example command to run the script which will take the path, get all files found via the path and then merge to a new file.

```
python MergeDataSets.py --directory 'data_sets/submission_titles_guitar_*.txt' --output 'data_sets/submission_titles_guitar_merged.txt'
```
