Height to Weight Predictor
A web application that predicts a person's weight (in kilograms) from their height (in meters) using a trained Simple Linear Regression model.

The application uses Flask for the backend and HTML/CSS for the user interface.
Features
- Accepts height in meters as input.
- Predicts weight in kilograms using a saved machine-learning model.
- Displays the prediction on the web page.
- Includes browser-side input validation for heights between 1.00 m and 2.50 m.
- Uses a responsive HTML/CSS interface.
Technology Stack
- Python
- Flask
- NumPy
- Scikit-learn
- HTML
- CSS
- Gunicorn (for deployment)
Project Structure
Arrange the files in this structure before running the application:
height-to-weight-predictor/
│
├── app.py
├── SLR_MODEL.pkl
├── requirements.txt
├── Procfile
├── test.py
│
└── templates/
    └── index.html
Important: Flask's render_template("index.html") looks for the HTML file inside a folder named templates. If your index.html is currently in the project root, create the templates folder and move index.html into it.
How It Works
1. The user enters their height in meters on the web page.
2. The form sends the value to the Flask /predict route using a POST request.
3. The backend converts the input to a numeric value and passes it to the saved model.
4. The model predicts the weight.
5. Flask sends the prediction back to the page, where it is displayed in kilograms.
The HTML file documents the model's reference equation as:
Weight = (63.1317191283293 × Height) - 42.178608958837785
The application uses the saved SLR_MODEL.pkl model for predictions; the equation is documentation in the HTML file.
Installation and Setup
1. Clone the repository
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY
Replace the URL with your GitHub repository URL.
2. Create and activate a virtual environment (recommended)
macOS / Linux
python3 -m venv venv
source venv/bin/activate
Windows
python -m venv venv
venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
4. Run the application
python app.py
Open this address in your browser:
http://127.0.0.1:5000/
Enter a height (in meters) and select Predict Weight.
Deployment
The included Procfile contains:
web: gunicorn app:app
This tells a compatible hosting platform to start the Flask application with Gunicorn. Make sure app.py, requirements.txt, Procfile, and SLR_MODEL.pkl are in the repository root, and that index.html is inside templates/.
Important Notes
- SLR_MODEL.pkl is required by app.py when the application starts.
- Only commit the model file if you are comfortable making that trained model publicly available. If you do not want to publish it, keep it out of the public repository and arrange secure model delivery for deployment.
- Security: Pickle files can execute code when loaded. Load only pickle files that you created yourself or obtained from a trusted source. Do not load an untrusted .pkl file.
- For reliable loading, use a compatible Python and scikit-learn environment with the versions used when the model was trained.
- test.py currently contains only print("hello world"); it is a placeholder, not a prediction test suite.
Author
Singireddy Nagaraju
