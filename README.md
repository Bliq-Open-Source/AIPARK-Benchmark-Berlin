<img src="/images/aipark-berlin-benchmark.gif"  width="500">

# AIPARK-Benchmark-Berlin

This repository contains the code and data required to reproduce the results from the article on Medium on the Benchmark of AIPARK Predictive Parking Data in Berlin. You can find the article here [LINK].

# Requirements
In order to be able to run the project, you need to have Python 3.6 installed.
You will need to have these libraries installed:
* numpy
* requests
* urllib3

You can install new Python libraries using the pip command (https://pypi.org/project/pip/).
To install them all at once, do:
```
pip3 install numpy requests urllib3
```

# Setup
1. To run this project, clone or download the repository and cd into the directory "AIPARK-Benchmark-Berlin".

2. Next, go to https://studio.aipark.io/sign-up to obtain your API key. It's free and done in a minute.

3. Open compare_predictions.py with a text editor of your choice and put in your API key at the bottom of the file. Then you are all set.
```
if __name__ == "__main__":
    api = AIPARK_API(apikey="insert-your-api-key-here")
    run_comparison()
```

4. Now, run compare_predictions.py on your terminal
```
python3 compare_predictions.py
```
5. The script now parses the ground truth data from ground_truth.csv and fetches predictive parking data from AIPARK. Finally, the prediction metric as defined on Medium gets applied and the results are printed out on the command line.
