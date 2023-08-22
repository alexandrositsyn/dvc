# DVC Demo

This repository contains a simple guide on how to set up DVC (Data Version Control) with S3 for versioning and storing data files.

## Prerequisites
Before you begin, make sure you have the following:

- Git installed: [Download Git](https://git-scm.com/downloads)
- DVC installed: [DVC Installation Guide](https://dvc.org/doc/install)
- AWS S3 account and credentials

## Getting Started

1. Initialize a Git repository:
    ```bash
    git init
    ```

2. Initialize DVC in your project directory:
    ```bash
    dvc init
    ```

3. Add an S3 remote storage location named 'bikes':
    ```bash
    dvc remote add -d bikes s3://dvc-s3-onto
    ```

4. Configure your S3 access credentials for the 'bikes' remote:
    ```bash
    dvc remote modify --local bikes access_key_id 'your_access_key_id'
    dvc remote modify --local bikes secret_access_key 'your_secret_access_key'
    ```

    Replace `'your_access_key_id'` and `'your_secret_access_key'` with your AWS S3 credentials.

5. Add data files to DVC tracking (replace 'path_to_your_file' with the actual file path):
    ```bash
    dvc add path_to_your_file
    ```

6. Push the data to the remote 'bikes' storage on S3:
    ```bash
    dvc push
    ```

## Usage
You can now version and manage your data using DVC, and it will be stored securely on your S3 remote storage.

For more information on DVC commands and usage, please refer to the [DVC documentation](https://dvc.org/doc).

## Using Google Drive

1. Initialize a Git repository:
    ```bash
    git init
    ```

2. Initialize a DVC repository:
    ```bash
    dvc init
    ```

3. Add a Google Drive remote storage:
    ```bash
    dvc remote add myremote gdrive://your_dir_id
    ```

4. Add a Google Drive remote storage:
    ```bash
    dvc add data/path_to_your_file
    ```

5. Push the data to the remote storage
    ```bash
    dvc push
    ```