# dws2017sydney
Code, Examples, Templates and Scripts for DataWorksSummit 2017 Sydney Talk

https://dataworkssummit.com/sydney-2017/sessions/real-time-ingesting-and-transforming-sensor-data-and-social-data-with-nifi-and-tensorflow/

In this talk I will show data engineers and architects how to run real-time TensorFlow Inception Image Recognition on images captured by remote sensors and images in tweets. 


In the same flow I will also demonstrate how to apply real-time sentiment analysis and intelligent routing of data to Phoenix, Email and Slack. I will elaborate on a number of different sentiment analysis frameworks available for use within Apache NiFi including Python NLTK, Stanford CoreNLP, Python SpaCy and Python TextBlob. This talk will be a deep dive into how to manage complex dataflow pipelines ingesting from multiple streaming sources including social, public open data feeds, logs, drones, RDBMS and IoT with transformations, deep learning, machine learning and business rules. 


Data engineers will be shown the power of Apache NiFi for loading diverse sources of data, applying transformations in-stream, routing based on attributes, adding sentiment data to workflows, running deep learning algorithms in stream and storing data into Apache Phoenix on HBase. In this talk, I will walk through each step in the process from ingest of each source, applying filters, performing transformations, converting types, picking and converting fields and finally storing data to Apache Phoenix on HBase. A quick data analysis to show streaming updates to data will be done in Apache Zeppelin running on HDP 2.x. 


This talk will be based on several HCC articles I have written:  

References:  
https://community.hortonworks.com/articles/76935/using-sentiment-analysis-and-nlp-tools-with-hdp-25.html https://community.hortonworks.com/articles/52415/processing-social-media-feeds-in-stream-with-apach.htmlhttps://community.hortonworks.com/content/kbentry/77988/ingest-remote-camera-images-from-raspberry-pi-via.html https://community.hortonworks.com/articles/58265/analyzing-images-in-hdf-20-using-tensorflow.html https://community.hortonworks.com/articles/59349/hdf-20-flow-for-ingesting-real-time-tweets-from-st.html https://community.hortonworks.com/articles/64122/incrementally-streaming-rdbms-data-to-your-hadoop.html https://community.hortonworks.com/articles/72420/ingesting-remote-sensor-feeds-into-apache-phoenix.html https://community.hortonworks.com/content/kbentry/55839/reading-sensor-data-from-remote-sensors-on-raspber.html https://community.hortonworks.com/content/kbentry/67309/routing-logs-through-apache-nifi-to-phoenix-hdfs-a.html  

Twitter:  @PaasDev
