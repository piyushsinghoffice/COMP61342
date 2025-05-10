import torchvision.datasets as datasets
from torchvision import transforms
import os
import zipfile
import tarfile
import urllib.request
import argparse
import shutil

def download_and_extract_caltech101(destination='./data'):
    url = "https://data.caltech.edu/records/mzrjq-6wc02/files/caltech-101.zip?download=1"
    zip_path = os.path.join(destination, "caltech-101.zip")
    temp_extract_path = os.path.join(destination, "caltech-101")
    final_data_path = os.path.join(destination, "101_ObjectCategories")

    if os.path.exists(final_data_path):
        print("✅ Caltech-101 dataset already exists. Skipping download.")
        return

    os.makedirs(destination, exist_ok=True)

    print("🔽 Downloading caltech-101.zip...")
    urllib.request.urlretrieve(url, zip_path)

    print("📦 Extracting ZIP file...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(destination)

    tar_gz_path = os.path.join(temp_extract_path, "101_ObjectCategories.tar.gz")
    print("📦 Extracting 101_ObjectCategories.tar.gz...")
    with tarfile.open(tar_gz_path, 'r:gz') as tar:
        tar.extractall(path=destination)

    print("🧹 Cleaning up...")
    os.remove(zip_path)
    os.remove(tar_gz_path)
    
    # Delete __MACOSX and caltech-101 folders
    macosx_path = os.path.join(destination, "__MACOSX")

    if os.path.exists(macosx_path):
        shutil.rmtree(macosx_path)
    if os.path.exists(temp_extract_path):
        shutil.rmtree(temp_extract_path)
    
    print("✅ Caltech-101 dataset is ready at:", final_data_path)

def download_cifar10(destination='./data'):
    transform = transforms.Compose([
        transforms.ToTensor()
    ])

    print("🔽 Downloading CIFAR-10 dataset...")
    datasets.CIFAR10(root=destination, train=True, download=True, transform=transform)
    datasets.CIFAR10(root=destination, train=False, download=True, transform=transform)
    print("✅ CIFAR-10 downloaded and extracted successfully.")

    print("Cleaning up...")
    zip_path = f"{destination}/cifar-10-python.tar.gz"
    os.remove(zip_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download datasets for coursework")
    parser.add_argument('--dataset', type=str, choices=['cifar10', 'caltech101', 'all'], default='all',
                        help="Which dataset to download: cifar10, caltech101, or all")
    args = parser.parse_args()

    if args.dataset in ['cifar10', 'all']:
        print("=== CIFAR-10 ===")
        download_cifar10()

    if args.dataset in ['caltech101', 'all']:
        print("\n=== Caltech-101 ===")
        download_and_extract_caltech101()