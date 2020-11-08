# Spark

<code>start-master.sh</code></br>
<code>http://127.0.0.1:80880</code></br>
<code>start-slave.sh spark://hadoop-master:7077</code></br>
Example of python script execution (executed while being located in ```spark/python folder```): </p>

```mkdir /tmp/spark-events```</br>
<code>spark-submit --master spark://hadoop-master:7077 ~/Downloads/spark-3.0.1-bin-hadoop2.7/python/ratings-counter.py</code> 


Very valuable ressources:
https://phoenixnap.com/kb/install-spark-on-ubuntu
https://blog.insightdatascience.com/simply-install-spark-cluster-mode-341843a52b88
