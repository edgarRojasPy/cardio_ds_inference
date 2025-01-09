---
title: Deployment Model Inference
description: Repo para realizar inferencia de problemas cardiacos..
---

# Deployment Model Inference cardio_ds_inference

This project demonstrates a Dockerized inference pipeline for deploying a machine learning model. The pipeline loads a trained model, preprocesses input data, and makes predictions using the model.

## Table of Contents
- [Project Overview](#project-overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

---

## Project Overview

The project consists of the following components:
- **`src/inference.py`**: The main script that loads the model, preprocesses input data, and makes predictions.
- **`src/model_loader.py`**: A utility script to load the trained model.
- **`src/data_preprocessor.py`**: A utility script to preprocess input data.
- **`models/trained_model_2025-01-02.joblib`**: A trained model saved in the `models/` directory.
- **`pyproject.toml`**: A Poetry configuration file for dependency management.

---

## Prerequisites

Before running the project, ensure you have the following installed:
- **Poetry**: [Install Poetry](https://python-poetry.org/docs/#installation)

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/edgarRojasPy/cardio_ds_inference.git
   cd cardio_ds_inference
   ```

2. Install dependencies using Poetry:
   ```
   1.1. Abrir una terminal de powershell y ejecutar el comando:
   (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
   1.2. Agregar el path en variables de entorno, en mi caso es C:\Users\<tuUsuario>\AppData\Roaming\Python\Scripts.
   1.3. Abrir una nueva ventana de cmd y probar:
      poetry --version
      El retorno es Poetry (version 2.0.0)  
  2. Configurar poetry
    Ingresar al directorio de nuestro repo. Iniciar la configuracion.
    poetry init
    2.1 Ingresar el nombre del paquete: pima-diabetes-trainer
    2.2 Version, enter por defecto.
    2.3 Ingresar la descripción:"Pipeline de entrenamiento para Pima diabetes dataset"
    2.4 Ingresar el Autor: Ingresar el dato del autor.
    2.5 Definir el tipo de Licencia: "APACHE 2.0"
    2.6 Versión del Python a utilizar: Enter, pues muestra que debe ser igual o mayor al que usamos.
    2.7 Definir dependencias PRINCIPALES de forma interactiva: Yes, enter 
    2.8 Paquete a agregar o buscar por: Enter
    2.9 Definir dependencias del DESARROLLO de forma interactiva: Yes, enter
    2.10 Paquete a agregar o buscar por: Enter 
    2.11 Confirmar la generacion: Enter.

   ```

---

## Usage

### Running Locally
Run the inference script:
   ```bash
   poetry run python src/inference.py
   ```

### Input Data
The script expects input data in the following format:
```python
input_data = {
    "id": 9999,
    "age": 45,
    "sex": "Female",
    "dataset": "Heart",
    "cp": "non-anginal",
    "trestbps": 130,
    "chol": 250,
    "fbs": False,
    "restecg": "normal",
    "thalch": 170,
    "exang": True,
    "oldpeak": 1.5,
    "slope": "flat",
    "ca": 1,
    "thal": "normal",
    "num": 1
}
```

## Testing

To test the inference pipeline, ensure the model file (`models/trained_model_2025-01-09.joblib`) exists and is correctly loaded. You can also test with different input data to verify the pipeline's robustness.

## License

This project is licensed under the **Apache 2.0 License**. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- Thanks to the open-source community for providing tools and libraries that made this project possible.
- Special thanks to [Poetry](https://python-poetry.org/) and [Docker](https://www.docker.com/) for simplifying dependency management and deployment.

---

## Contact

For questions or feedback, feel free to reach out:
- **Author**: Edgar Rojas
- **Email**: efrojaspy@gmail.com
- **GitHub**: [edgarRojasPy](https://github.com/edgarRojasPy)


---

### **How to Use**
1. Open your project in Visual Studio Code.
2. Open the `README.md` file (or create one if it doesn’t exist).
3. Copy and paste the above content into the file.
4. Save the file (`Ctrl + S` or `Cmd + S`).

---
