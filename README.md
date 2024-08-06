# Image Compression with K-Means and Django

## Overview

This project demonstrates how to use the K-Means clustering algorithm to compress images and then display the results on a web application using the Django framework. The primary goal of this project is to reduce the color palette of an image while preserving its overall appearance, and then provide a web interface where users can upload images, compress them, and view the results.
**Fun Fact**: It look some one has handrawn the pitcure after compressing

## Project Structure

- **`image_compression/`**: Contains the image compression logic and related files.
  - `compressor/`
    - `views.py`: Contains the logic for handling image uploads, compression, and displaying the results.
    - `forms.py`: Defines the form for image upload.
    - `compress_image.py`: Contains the K-Means algorithm implementation for image compression.
    - `templates/`
      - `compressor/upload.html`: HTML form for uploading images.
      - `compressor/compressed_image.html`: HTML template for displaying the compressed image.



- **`manage.py`**: Django’s command-line utility for administrative tasks.

- **`settings.py`**: Configuration settings for the Django project.
- **`dbsqlite`**: Database for django project not used

## Installation

### Prerequisites

Ensure you have Python installed on your machine. You will also need to have `pip` (Python package installer) installed.



### Clone the Repository

```bash



git clone https://github.com/your-username/image_compression_project.git
cd image_compression_project

```

### Example
![image](https://github.com/user-attachments/assets/a5b7ac65-4ba9-4b5e-9374-15f81640bb58)   ![image](https://github.com/user-attachments/assets/5281a14d-4a99-4344-a1ad-177173fef3e0)
