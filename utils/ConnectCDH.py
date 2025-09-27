from pyspark.sql import SparkSession

if __name__ == '__main__':
    spark = SparkSession.builder \
        .appName("ClusterApp") \
        .master("spark://hadoop100:7077") \
        .config("spark.executor.memory", "4g") \
        .getOrCreate()

    # df.createOrReplaceTempView("temp_table")
    result = spark.sql("SELECT * FROM temp_table WHERE age > 30")
    result.show()

    spark.stop()
