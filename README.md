# DVC Demo

This repository serves as a guide on setting up DVC (Data Version Control) with AWS S3 or Google Drive for efficient data versioning and storage.

## Prerequisites

Before diving into the setup, ensure you have the following prerequisites in place:

- **Git:** If you haven't already, install Git by following the instructions [here](https://git-scm.com/downloads).
- **DVC:** Install DVC by referring to the [DVC Installation Guide](https://dvc.org/doc/install).
- **AWS S3 Account:** You need an AWS S3 account and appropriate credentials.

## Setting Up AWS S3

To utilize AWS S3 for data storage, follow these steps:

1. **Create an S3 Bucket:** Start by creating an S3 bucket in your AWS account.

2. **IAM User:** Create an IAM user with read and write permissions for S3 buckets.

3. **User Credentials:** Generate access key and secret access key for the IAM user, and keep them handy.

## Using AWS S3 with DVC

Follow these steps to integrate DVC with AWS S3:

1. **Initialize a Git Repository:**

   ```bash
   git init
   ```

2. **Initialize DVC in your Project:**

   ```bash
   dvc init
   ```

3. **Add an S3 Remote Storage (named 'bikes'):**

   ```bash
   dvc remote add -d bikes s3://dvc-s3-onto
   ```

4. **Configure S3 Access Credentials for 'bikes' Remote:**

   Replace `'your_access_key_id'` and `'your_secret_access_key'` with your AWS S3 credentials.

   ```bash
   dvc remote modify --local bikes access_key_id 'your_access_key_id'
   dvc remote modify --local bikes secret_access_key 'your_secret_access_key'
   ```

5. **Add Data Files for DVC Tracking:**

   Replace `'path_to_your_file'` with the actual file path.

   ```bash
   dvc add path_to_your_file
   ```

6. **Push Data to the Remote 'bikes' Storage on S3:**

   ```bash
   dvc push
   ```

You are now equipped to version and manage your data efficiently using DVC while ensuring secure storage on your AWS S3 remote storage.

For further details on DVC commands and usage, consult the [DVC documentation](https://dvc.org/doc).

## Using Google Drive with DVC

If you prefer to use Google Drive as your storage option, follow these steps:

1. **Initialize a Git Repository:**

   ```bash
   git init
   ```

2. **Initialize a DVC Repository:**

   ```bash
   dvc init
   ```

3. **Add a Google Drive Remote Storage:**

   ```bash
   dvc remote add myremote gdrive://your_dir_id
   ```

4. **Add Data to Your Google Drive Remote Storage:**

   ```bash
   dvc add data/path_to_your_file
   ```

5. **Push Data to the Google Drive Remote Storage:**

   ```bash
   dvc push
   ```
