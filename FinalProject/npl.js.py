from pyspark.ml.feature import Tokenizer
from pyspark.sql.functions import col, udf
from pyspark.sql.types import IntegerType
from pyspark.sql import SparkSession 
spark = SparkSession.builder.getOrCreate()
import pandas as pd
sc =spark.sparkContext
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark import SparkFiles
from pyspark.sql.functions import length
from pyspark.ml.feature import Tokenizer, StopWordsRemover, HashingTF, IDF, StringIndexer
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.linalg import Vector
from pyspark.ml import Pipeline
from pyspark.ml.classification import NaiveBayes


def file_reading(path,name) : 
    print("control entered file_reading ")
    url =path
    spark.sparkContext.addFile(url)
    start_data = spark.read.csv(SparkFiles.get(name), sep=",", header=True)
    return start_data


def clean_file(file):
    print("control entered clean_file ")
    df=file.filter(file.Body != '').filter(file.Sentiment != '')
    data_df = df.withColumn('length', length(df['Body']))
    return data_df


def data_operations(file):
    print("control entered data_operations ")
    stop_list = ["The", "I", "fuck",'cook','This','is','was','there','when','care','agent','card']
    pos_neg_to_num = StringIndexer(inputCol='Sentiment',outputCol='label')
    tokenizer = Tokenizer(inputCol="Body", outputCol="token_text")
    # stopremove = StopWordsRemover(inputCol='token_text',outputCol='stop_tokens')
    stopremove = StopWordsRemover(inputCol="token_text", outputCol="stop_tokens", stopWords=stop_list)
    hashingTF = HashingTF(inputCol="token_text", outputCol='hash_token')
    idf = IDF(inputCol='hash_token', outputCol='idf_token')
    clean_up = VectorAssembler(inputCols=['idf_token', 'length'], outputCol='features')
    data_prep_pipeline = Pipeline(stages=[pos_neg_to_num, tokenizer, stopremove, hashingTF, idf, clean_up])
    return data_prep_pipeline


def pipeline_bayes(file,name):
    print("control entered pipeline_bayes ")
    cleaner = file.fit(name)
    cleaned = cleaner.transform(name)
    training, testing = cleaned.randomSplit([0.7, 0.3])

# Create a Naive Bayes model and fit training data
    nb = NaiveBayes()
    predictor = nb.fit(training)
    test_results = predictor.transform(testing)
    return test_results


def model_accuracy(test_results):
    print("control entered model_accuracy ")
    print(test_results. select('Sentiment','length','stop_tokens','hash_token','idf_token','probability','prediction').show(20))
    acc_eval = MulticlassClassificationEvaluator()
    acc = acc_eval.evaluate(test_results)
    return acc




a=file_reading("https://smubootcamprohith.s3.us-east-2.amazonaws.com/ios_app_ratings.csv","ios_app_ratings.csv")
b=clean_file(a)
c=data_operations(b)
d=pipeline_bayes(c,b)
x=model_accuracy(d)


print("Convert pyspark to pandas....")
pdf=d.toPandas()
print("Convert DF to HTML....")
pdf.to_html('myrockytable.html')
