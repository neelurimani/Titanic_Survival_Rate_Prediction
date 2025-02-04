from flask import Flask, render_template, request
from pyspark.ml.classification import LogisticRegressionModel
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.ml.feature import VectorAssembler

# Initialize Flask app
app = Flask(__name__)

# Initialize Spark session
spark = SparkSession.builder.appName("TitanicModelApp").getOrCreate()

# Load the trained model
model_path = "titanic_model"
model = LogisticRegressionModel.load(model_path)

# Define feature columns
feature_cols = ["Pclass", "Sex_Index", "Age", "SibSp", "Parch", "Fare"]

# Function to preprocess input
def preprocess_input(data):
    # Convert categorical 'Sex' input to numeric (Male=1, Female=0)
    sex_index = 1 if data["Sex"].lower() == "male" else 0

    # Create a DataFrame for prediction
    input_data = spark.createDataFrame([(data["Pclass"], sex_index, data["Age"], data["SibSp"], data["Parch"], data["Fare"])],
                                       ["Pclass", "Sex_Index", "Age", "SibSp", "Parch", "Fare"])
    
    # Vectorize input
    vector_assembler = VectorAssembler(inputCols=feature_cols, outputCol="features")
    input_vector = vector_assembler.transform(input_data).select("features")

    return input_vector

# Home route
@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    input_values = {}

    if request.method == "POST":
        # Retrieve form data
        input_values = {
            "Pclass": int(request.form["Pclass"]),
            "Sex": request.form["Sex"],
            "Age": float(request.form["Age"]),
            "SibSp": int(request.form["SibSp"]),
            "Parch": int(request.form["Parch"]),
            "Fare": float(request.form["Fare"])
        }

        # Preprocess input
        input_vector = preprocess_input(input_values)

        # Make prediction
        prediction = model.transform(input_vector).select("prediction").collect()[0]["prediction"]
        prediction = "Survived" if prediction == 1 else "Not Survived"

    return render_template("index.html", prediction=prediction, input_values=input_values)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
