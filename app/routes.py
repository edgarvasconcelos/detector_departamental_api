from flask import request, jsonify
from model.model_loader import load_model
from model.prediction import predict
import gc

def configure_routes(app):
    """
    Configures the routes for the Flask application.

    Args:
        app: The Flask application instance.
    """
    # Load the model and tokenizer
    model, tokenizer = load_model()
    class_names = [
        'CIÊNCIAS AGRÁRIAS', 'Ciências Contábeis', 'FILOSOFIA', 'GEOCIÊNCIAS',
        'Estágios e Práticas Escolares', 'Clínica Médica', 'EDUCAÇÃO FÍSICA E DO DESPORTO',
        'CIÊNCIAS DA ADMINISTRAÇÃO', 'Saúde Mental e Saúde Coletiva', 'Artes', 
        'Educação', 'COMUNICAÇÃO E LETRAS', 'Política e Ciências Sociais', 'Enfermagem',
        'Ciências da Computação', 'Ciências Econômicas', 'CIÊNCIAS EXATAS', 'Odontologia',
        'Métodos e Técnicas Educacionais', 'Fisiopatologia', 'Direito Privado',
        'Direito Público Adjetivo', 'Direito Público Substantivo'
    ]
    max_len = 728  # This should ideally come from the model

    @app.route('/')
    def home():
        """
        Home route that returns a welcome message.

        Returns:
            str: Welcome message.
        """
        return "Welcome to the Flask API for Keras Model Predictions!"

    @app.route('/predict', methods=['POST'])
    def predict_route():
        """
        Prediction route that handles POST requests to make predictions using the loaded model.

        Returns:
            JSON: JSON object containing the predictions.
        """
        try:

            data = request.get_json(force=True)
            if 'input' not in data:
                return jsonify({'error': 'No input data provided'}), 400
            
            # Generate predictions using the provided input
            predictions = predict(model, tokenizer, data['input'], class_names, max_len)

            # Convert float32 values to float for JSON serialization
            predictions = [(dept, float(score)) for dept, score in predictions]

            del data
            gc.collect() 

            return jsonify({'predictions': predictions})
        
        except Exception as e:
            # Return an error message with a 500 status code if something goes wrong
            return jsonify({'error': str(e)}), 500
