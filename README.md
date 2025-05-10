# 📚 Comparative Study: Local Features vs CNNs for Object Recognition

This project presents a comparative analysis between traditional computer vision techniques (SIFT + ORB + Bag-of-Visual-Words) and deep learning approaches (CNNs, Improved CNNs, ResNet18) for object recognition on the **Caltech101** and **CIFAR-10** datasets.

## 🔍 Project Summary

The study aims to evaluate the performance, generalization, and applicability of these models, particularly in the context of **robotic vision systems**. Traditional pipelines using SIFT and ORB are paired with classifiers like SVM, Random Forest, and XGBoost. CNN architectures range from basic implementations to pretrained ResNet18 models, incorporating enhancements such as Batch Normalization, SiLU activation, Label Smoothing, and Learning Rate Scheduling.

---

## 📁 Project Structure

```bash
├── download_data.py          # Script to download and extract Caltech101 and CIFAR-10
├── SIFT.ipynb                # SIFT + BoVW + Classifier (SVM, RF, XGB)
├── ORB.ipynb                 # ORB + BoVW + Classifier (SVM, RF, XGB)
├── simple_cnn_v1.ipynb       # Simple CNN for Caltech101 and CIFAR-10
└── resnet.ipynb              # ResNet18 fine-tuning on Caltech101

| Model               | Caltech101 Accuracy | CIFAR-10 Accuracy |
| ------------------- | ------------------- | ----------------- |
| SIFT + SVM          | 16.34%              | 26.50%            |
| ORB + SVM           | 23.70%              | X Failed          |
| Simple CNN          | 56.22%              | 74.85%            |
| Improved CNN        | 69.38%              | —                 |
| ResNet18 (Transfer) | **90.16%**          | —                 |
| ------------------- | ------------------- | ----------------- |
```

# Dependencies
- Python 3.9+

- OpenCV

- NumPy

- PyTorch

- Torchvision

- scikit-learn

- matplotlib

Install all dependencies:

```bash
pip install -r requirements.txt
```

# Dataset Instructions

The download_data.py script automates downloading and extracting:

- Caltech101

- CIFAR-10

To run:
```bash
python download_data.py
```

Application in Robotics

- ORB is used in ORB-SLAM for efficient matching in real-time SLAM.

- CNNs and ResNet18 are used in robotics for grasp planning, navigation, and object detection.

# Author
Piyush Singh

MSc Data Science (Social Analytics)

University of Manchester

🔗 piyushsingh.in