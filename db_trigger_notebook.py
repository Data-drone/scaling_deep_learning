# Databricks notebook source
# MAGIC %md
# MAGIC # Testing Running notebooks

# COMMAND ----------

#dbutils.fs.mkdirs('/dbfs/user/brian.law/lightning_fashion_mnist/checkpoints')

# COMMAND ----------

# MAGIC %sh 
# MAGIC 
# MAGIC python fashion_mnist_main.py

# COMMAND ----------

# MAGIC %sh
# MAGIC 
# MAGIC $DB_DRIVER_IP

# COMMAND ----------

from sparkdl import HorovodRunner
import horovod.torch as hvd
from fashion_mnist_main import main_hvd

hr = HorovodRunner(np=1, driver_log_verbosity='all')

model = hr.run(main_hvd)

# COMMAND ----------
