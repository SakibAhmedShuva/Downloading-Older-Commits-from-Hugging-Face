# This code gets the files exactly as they were at the specified commit hash.
# While the initial clone downloads history, the checkout command ensures
# your working directory contains *only* the files from that specific version.

# Define the specific commit hash and repository details
TARGET_COMMIT = "7622487216c98c3f3c860f2d0ddbf8289d3109b8"
REPO_URL = "https://huggingface.co/unsloth/Qwen2.5-VL-7B-Instruct-unsloth-bnb-4bit"
REPO_DIR = "Qwen2.5-VL-7B-Instruct-unsloth-bnb-4bit" # Default directory name from clone

# 1. Clone the repository
# This downloads the necessary history, including the target commit.
print(f"Cloning the repository {REPO_URL} (downloads history including your target commit)...")
!git clone {REPO_URL}
print("Cloning complete.")

# 2. Change into the cloned directory and checkout the specific commit
# This is the crucial step that makes your working files reflect *only* the state of the TARGET_COMMIT.
print(f"\nChanging directory to {REPO_DIR} and checking out commit {TARGET_COMMIT}...")
# Use '&&' to ensure the checkout command runs only after the cd command succeeds in the same shell
!cd {REPO_DIR} && git checkout {TARGET_COMMIT}
print(f"Successfully checked out commit {TARGET_COMMIT}.")
print("Your working directory now contains the files *exactly* as they were at this version.")

# 3. Pull Git LFS files for the checked-out commit
# This is crucial for downloading the actual large files (like model weights)
# that are tracked by LFS *for the specified commit version*.
# Addresses the 'may not have been copied correctly' warning.
print("\nPulling Git LFS files for the checked-out commit...")
!cd {REPO_DIR} && git lfs pull
print("Git LFS pull complete.")

print(f"\nSetup complete. The directory '{REPO_DIR}' now contains the files from commit {TARGET_COMMIT}.")