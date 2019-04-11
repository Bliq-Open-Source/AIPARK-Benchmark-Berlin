<p align="center"> <img src="/images/aipark-berlin-benchmark.gif"  width="600"> </p>

# AIPARK-Benchmark-Berlin

This repository contains the code and data required to reproduce the results from the article <i>Automating quality tests for map data to solve urban parking </i> on the Benchmark of AIPARK Predictive Parking Data in Berlin. You can find the full article <a href="https://medium.com/aipark/quality-at-scale-automating-quality-tests-for-map-data-to-solve-urban-parking-4e6194cbfef2">here</a>: .

# Requirements
In order to run the project, you need to have Python 3.6 installed.
You will need to have these libraries installed:
* numpy
* requests
* urllib3

You can install new Python libraries using the pip command (https://pypi.org/project/pip/).
To install them all at once, run:
```
pip3 install numpy requests urllib3
```

# Setup
1. To run this project, clone or download the repository and cd into the directory "AIPARK-Benchmark-Berlin".

2. Next, go to https://studio.aipark.io/sign-up to obtain your personal API key. It's free and done in a minute.

3. Open compare_predictions.py with a text editor of your choice and put in your API key at the bottom of the file. Then you are all set.
```
if __name__ == "__main__":
    api = AIPARK_API(apikey="insert-your-api-key-here")
    run_comparison()
```

4. Now, run compare_predictions.py on your terminal.
```
python3 compare_predictions.py
```
5. The script now imports the ground truth data from ground_truth.csv and fetches predictive parking data from the AIPARK API. Finally, the prediction metric as defined in <a href="https://medium.com/aipark/quality-at-scale-automating-quality-tests-for-map-data-to-solve-urban-parking-4e6194cbfef2">the article</a> gets applied and the results are printed out on the command line.
