# Downloading Specific Older Commits from Hugging Face (and other Git LFS Repos)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) <!-- Replace with your chosen license badge if different -->

## Overview

This repository provides a script and guide demonstrating how to download the exact state of the files within a Git repository, particularly those using Git Large File Storage (LFS) like many Hugging Face models, as they existed at a specific older commit hash.

While a standard `git clone` downloads the repository's history, checking out a specific commit ensures your local working directory precisely mirrors the file structure and content (including large LFS files) from that point in time. This is crucial for reproducibility, debugging, or comparing model versions.

## Motivation

Why would you need to download files from an older commit?

*   **Reproducibility:** Ensure you are using the exact version of code or model weights used in a previous experiment or paper.
*   **Debugging:** Investigate issues that might have been introduced in later commits by reverting to a known working state.
*   **Version Comparison:** Analyze differences in model weights, configurations, or code between specific versions.
*   **Accessing Deprecated Features:** Retrieve older versions if newer ones have removed functionality you rely on.

## Prerequisites

Before running the example script, ensure you have the following installed on your system:

1.  **Git:** [https://git-scm.com/downloads](https://git-scm.com/downloads)
2.  **Git Large File Storage (LFS):** [https://git-lfs.github.com/](https://git-lfs.github.com/)
    *   After installing Git LFS, you often need to run `git lfs install --system` once to integrate it with your Git setup globally.

## How to Use

1.  **Clone this Repository:**
    ```bash
    git clone https://github.com/SakibAhmedShuva/Downloading-Older-Commits-from-Hugging-Face.git # Or your actual repo URL
    cd Downloading-Older-Commits-from-Hugging-Face
    ```

2.  **Configure the Script:**
    Open the provided Python script (e.g., `download_commit.py` or the notebook `example.ipynb`). Modify the following configuration variables at the top of the script:

    *   `TARGET_COMMIT`: Set this to the full commit hash you want to check out.
    *   `REPO_URL`: The `https://` URL of the target Git repository (e.g., a Hugging Face model repo).
    *   `REPO_DIR`: The desired local directory name for the cloned repository. Git usually defaults to the repository name from the URL.

    ```python
    # Example configuration in the script:
    TARGET_COMMIT = "7622487216c98c3f3c860f2d0ddbf8289d3109b8" # <-- CHANGE THIS
    REPO_URL = "https://huggingface.co/unsloth/Qwen2.5-VL-7B-Instruct-unsloth-bnb-4bit" # <-- CHANGE THIS
    REPO_DIR = "Qwen2.5-VL-7B-Instruct-unsloth-bnb-4bit" # <-- CHANGE THIS (Optional, usually based on REPO_URL)
    ```

3.  **Run the Script:**
    Execute the script from your terminal (or run the cells in the notebook):

    *   **For a `.py` script:**
        ```bash
        python download_commit.py
        ```
    *   **For a `.ipynb` notebook:**
        Open it with Jupyter Lab/Notebook and run the code cells sequentially.

4.  **Result:**
    The script will:
    *   Clone the specified repository (`REPO_URL`). This downloads the history.
    *   Navigate into the cloned directory (`REPO_DIR`).
    *   Checkout the specific commit (`TARGET_COMMIT`), updating the working directory files.
    *   Run `git lfs pull` to download the actual large file content corresponding to the checked-out commit.

    Upon completion, the directory specified by `REPO_DIR` will contain the exact file structure and content of the repository as it was at `TARGET_COMMIT`.

## How the Code Works

The script executes the following core Git commands:

1.  **`git clone <REPO_URL>`:** Downloads the entire repository history, including metadata about all commits and LFS pointers, but usually only the *latest* LFS files initially.
2.  **`cd <REPO_DIR> && git checkout <TARGET_COMMIT>`:**
    *   `cd <REPO_DIR>`: Changes the current directory to the cloned repository.
    *   `git checkout <TARGET_COMMIT>`: This is the crucial step. It modifies the files in your working directory to match *exactly* how they were recorded in that specific commit. LFS pointer files will be updated to reference the correct LFS objects for that commit.
    *   Using `&&` ensures the `checkout` command runs only if the `cd` command is successful and within the same (sub)shell context, which is important when running via `!` in notebooks or simple scripts.
3.  **`cd <REPO_DIR> && git lfs pull`:**
    *   After checking out the desired commit, the LFS pointer files reflect that specific version.
    *   `git lfs pull` reads these pointer files and downloads the corresponding large files from the LFS storage, ensuring you have the actual model weights or other large assets for that *specific commit*. This step is essential because the initial `clone` might not have downloaded these specific older LFS objects.

## Important Notes

*   **Disk Space:** Cloning large repositories, especially those with extensive LFS history, can consume significant disk space. Ensure you have enough available.
*   **Network Bandwidth:** `git lfs pull` will download potentially large files, consuming network bandwidth.
*   **Error Handling:** The provided example script has basic print statements but minimal error handling. In a production environment, you would add checks for command success (e.g., using Python's `subprocess` module for `.py` scripts).
*   **Authentication:** For private repositories, you might need to configure Git credentials or use SSH keys.

## Contributing

Contributions are welcome! If you have suggestions for improvements, find a bug, or want to add more examples, please feel free to:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/YourFeature`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add some feature'`).
5.  Push to the branch (`git push origin feature/YourFeature`).
6.  Open a Pull Request.

Alternatively, open an issue to discuss the changes you'd like to propose.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. <!-- Make sure you add a LICENSE file (e.g., MIT) -->
