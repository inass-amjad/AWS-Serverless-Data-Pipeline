# ☁️ AWS Serverless Data Pipeline

An event-driven, 100% serverless data pipeline built on AWS. This project automates the process of ingesting, processing, cataloging, and analyzing e-commerce sales data without provisioning or managing any servers.

## 📖 Project Overview

In traditional cloud architectures, servers (like Amazon EC2) must run 24/7 to process incoming data, which is expensive and requires manual maintenance. This project solves that by using a **Serverless Architecture**. The system remains completely idle (costing $0) until a new file is uploaded, at which point it automatically processes the data within milliseconds.

## 🏗️ Architecture & Workflow

1. **Amazon S3 (Data Lake):** Raw CSV files are uploaded to the `raw/` folder. S3 is configured to send an event notification upon file creation.
2. **AWS Lambda (Compute):** The S3 event automatically triggers a Python Lambda function. The code reads the file, performs basic validation, and copies the processed file to the `processed/` folder in S3.
3. **AWS Glue (Data Catalog):** A Glue Crawler scans the `processed/` folder, infers the schema (column names and data types), and updates the Glue Data Catalog.
4. **Amazon Athena (Analytics):** Standard SQL queries are run directly against the data in S3 using Athena. No database servers (like MySQL or Redshift) are required to analyze the data.

## 💻 Tech Stack

*   **Cloud Provider:** Amazon Web Services (AWS)
*   **Storage:** Amazon S3
*   **Compute:** AWS Lambda (Python 3.x)
*   **Data Catalog:** AWS Glue
*   **Query Engine:** Amazon Athena
*   **Monitoring:** Amazon CloudWatch

## 📂 Repository Structure

*   `lambda_function.py` - The Python code used in AWS Lambda to process and move the files.
*   `screenshots/` - Images showing the successful execution of the pipeline (S3, Lambda Logs, Glue Crawler, Athena Results).
*   `sample_data/` - Sample CSV files used for testing the pipeline.

## 🚀 How to Replicate This Project

If you want to build this yourself, follow these high-level steps:

1.  Create an S3 Bucket with `raw/` and `processed/` folders.
2.  Create an IAM Role with S3 read/write permissions.
3.  Create an AWS Lambda function (Python) and attach the IAM role.
4.  Add an S3 Trigger to the Lambda function (Event: `PUT`, Prefix: `raw/`).
5.  Create an AWS Glue Database and a Crawler pointing to the `processed/` folder.
6.  Set up Amazon Athena, configure the query result location, and run SQL queries on the cataloged data.

## 💡 Key Learnings

*   **Cost Efficiency:** Pay-as-you-go model. Zero cost when idle.
*   **Event-Driven Design:** No manual intervention or cron jobs required.
*   **Serverless Compute:** Deepened understanding of IAM roles, Lambda triggers, and CloudWatch logs.
