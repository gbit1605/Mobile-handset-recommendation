<------------------     Mobile Handset Recommendation     ------------------>

This project comprises of 4 parts:

    Data acquisition and cleaning
    Data pre-processing
    Knn algorithm for recommendation and accuracy calculations
    A UI for choosing among different handsets to obtain recommendations

The project can be run by the following process:
1. Run app_runner.py file
2. Goto http://127.0.0.1:5000/ in the browser
3. Click on the model names to yield their descriptions and 5 related recommendations

Accuracy measure used: Precision

Precision = (recommended ∩ relevant) / recommended 

Here, recommended is the number of recommedations given for each product and relevant are the number of recommendations that have a value lower than that of a dynamic threshold. The dynamic threshold, in this case hase been defined as, (avg of the five recommedation distances + distance value of recommendation 5 / 5) where recommedation 1 is the closest match and recommedation 5 is the farthest. 
