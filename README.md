# rolling-median-venmo

A solution for the insight data science coding challenge, hosted on: https://github.com/InsightDataScience/coding-challenge

# Objective

To calculate the median degree of a venmo payment transaction graph within a 60 second window.

# Implementation
Venmo payments are provided in a file with the below JSON data format:
<pre>
{"created_time": "2014-03-27T04:28:20Z", "target": "Jamie-Korn", "actor": "Jordan-Gruber"}
</pre>

Payments are processed using a python generator. A graph is built with undirected edges between payment targets and actors. A min-max heap is used to keep track of the newest and oldest payments. Each time a payment is added the heap is pruned until the time difference between the newest and oldest payment is <= 60seconds. When a payment is added or removed from the heap a corresponding edge is either inserted or removed from the payment graph.
