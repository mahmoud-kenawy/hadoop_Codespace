# MapReduce Stock Example
Create a MapReduce program that processes a CSV file of stock prices and finds the maximum 'Volume' for each stock symbol (quote).

* `stocks.csv`
```
Date,Open,High,Low,Close,Volume,Name
2025-04-18,175.35,177.85,174.03,177.56,57346000,AAPL
2025-04-18,2855.00,2899.44,2842.00,2886.00,1800000,GOOG
2025-04-18,175.00,178.00,174.00,177.00,65000000,AAPL
2025-04-18,2850.00,2890.00,2830.00,2880.00,2000000,GOOG
```
Output:
```
AAPL   65000000
GOOG   2000000
```

## Solution
* `mapper.py`
```
#!/usr/bin/env python
import sys
import csv

reader = csv.reader(sys.stdin)
header = next(reader, None)  # skip header

for row in reader:
    try:
        name = row[6]
        volume = int(row[5])
        print(f"{name}\t{volume}")
    except:
        continue  # skip malformed rows

```

* `reducer.py`
```
#!/usr/bin/env python
import sys

current_name = None
max_volume = 0

for line in sys.stdin:
    name, volume = line.strip().split('\t')
    volume = int(volume)

    if name == current_name:
        if volume > max_volume:
            max_volume = volume
    else:
        if current_name is not None:
            print(f"{current_name}\t{max_volume}")
        current_name = name
        max_volume = volume

if current_name is not None:
    print(f"{current_name}\t{max_volume}")
```


* Running the MapReduce Tasks
1. Create `stocks.csv`:

```bash
nano stocks.csv
```

Paste the sample data.

2. Upload to HDFS:

```bash
hdfs dfs -mkdir -p /user/cloudera/stocks_input
hdfs dfs -put stocks.csv /user/cloudera/stocks_input/
```

3. Run MapReduce:

```bash
hdfs dfs -rm -r /user/cloudera/stocks_output

hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
  -file mapper.py -mapper mapper.py \
  -file reducer.py -reducer reducer.py \
  -input /usr/cloudera/stocks_input \
  -output /usr/cloudera/stocks_output
```

4. View result:

```bash
hdfs dfs -cat /user/cloudera/stocks_output/part-00000
```

