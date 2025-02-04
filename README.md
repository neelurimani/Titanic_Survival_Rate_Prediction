# Titanic Survival Prediction 🚢

A machine learning-based web application to predict whether a passenger would have survived the Titanic disaster based on user input data.

---

## Table of Contents 📚
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Live Demo](#live-demo)
- [Contributing](#contributing)
- [License](#license)

---

## Introduction 🚀
This project is a web application that uses a trained Logistic Regression model to predict the survival of Titanic passengers. Users can input details like passenger class, age, sex, number of siblings/spouses, number of parents/children, and fare to get a prediction.

The application is built using Flask for the backend and PySpark for the machine learning model.

---

## Features ✨
- **User-friendly Interface**: Simple and intuitive form for inputting passenger details.
- **Real-time Prediction**: Instantly predicts whether a passenger would have survived.
- **Responsive Design**: Works seamlessly on both desktop and mobile devices.
- **Error Handling**: Provides clear error messages for invalid inputs.

---

## Technologies Used 🛠️
- **Frontend**: HTML, CSS
- **Backend**: Flask (Python)
- **Machine Learning**: PySpark (Logistic Regression)
- **Deployment**: (Add deployment platform if applicable, e.g., Render, AWS, etc.)

---

## Installation 🛠️
To run this project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```
2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requriement.txt
   ```
4. **Run the Flask application**:
   ```bash
   python app.py
   ```
5. **Open your browser and navigate to** `http://127.0.0.1:5000/`

---

## Usage 🖥️
1. Enter the required passenger details:
   - **Pclass**: Passenger class (1, 2, or 3).
   - **Sex**: Male or Female.
   - **Age**: Age of the passenger.
   - **SibSp**: Number of siblings/spouses aboard.
   - **Parch**: Number of parents/children aboard.
   - **Fare**: Fare paid for the ticket.
2. Click the **Predict** button to see the result.

---

## Live Demo 🌐
[Live Demo](ADD_LIVE_LINK_HERE)

---

## Contributing 🤝
Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a pull request.

---

## License 📄
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments 🙏
- Titanic Dataset: Kaggle
- Flask Documentation: [Flask](https://flask.palletsprojects.com/)
- PySpark Documentation: [PySpark](https://spark.apache.org/docs/latest/api/python/)
