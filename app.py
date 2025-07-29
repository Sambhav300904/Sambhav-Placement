from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# Your personal details for the API response
USER_ID_FULL_NAME = "sambhav_singh"  # [cite: 24, 26]
USER_ID_DOB = "30092004"  # [cite: 24]
USER_EMAIL = "sambhavsingh10@gmail.com"  # [cite: 9]
COLLEGE_ROLL_NUMBER = "2210993840"  # [cite: 10]

@app.route('/bfhl', methods=['POST'])
def process_data():
    try:
        print("Request received!")
        print(f"Request Headers: {request.headers}")
        print(f"Request JSON Data: {request.json}") # This will show the parsed JSON
        data = request.json.get('data', [])
        print(f"Extracted 'data' array: {data}")
 # [cite: 48, 66, 84]

        # Initialize lists for categorization
        numbers = []
        odd_numbers = []  # [cite: 12]
        even_numbers = []  # [cite: 11]
        alphabets = []  # [cite: 13]
        special_characters = []  # [cite: 14]
        total_sum = 0  # [cite: 15]
        alphabet_chars_for_concat = [] # To store individual alphabetical characters for concatenation

        for item in data:
            # Check if it's a number
            if isinstance(item, str) and item.isdigit():
                num = int(item)
                numbers.append(item) # Numbers must be returned as strings [cite: 42, 43]
                total_sum += num # [cite: 15]
                if num % 2 == 0:
                    even_numbers.append(item) # [cite: 11]
                else:
                    odd_numbers.append(item) # [cite: 12]
            # Check if it's an alphabet (single character or multiple, as per Example C)
            elif isinstance(item, str) and re.fullmatch(r'[a-zA-Z]+', item):
                alphabets.append(item.upper()) # Convert to uppercase [cite: 13]
                for char in item: # Extract individual characters for concatenation [cite: 16]
                    if char.isalpha():
                        alphabet_chars_for_concat.append(char)
            # Otherwise, consider it a special character
            elif isinstance(item, str):
                special_characters.append(item) # [cite: 14]

        # Generate concat_string in reverse order with alternating caps [cite: 16]
        concat_string = ""
        for i, char in enumerate(reversed(alphabet_chars_for_concat)): # [cite: 16]
            if i % 2 == 0:
                concat_string += char.upper() # Alternating caps [cite: 16]
            else:
                concat_string += char.lower() # Alternating caps [cite: 16]

        response = {
            "is_success": True,  # [cite: 7, 27]
            "user_id": f"{USER_ID_FULL_NAME}_{USER_ID_DOB}",  # [cite: 8, 23, 24, 25, 26]
            "email": USER_EMAIL,  # [cite: 9]
            "roll_number": COLLEGE_ROLL_NUMBER,  # [cite: 10]
            "odd_numbers": odd_numbers,  # [cite: 12]
            "even_numbers": even_numbers,  # [cite: 11]
            "alphabets": alphabets,  # [cite: 13]
            "special_characters": special_characters,  # [cite: 14]
            "sum": str(total_sum),  # Return sum as a string [cite: 15, 60]
            "concat_string": concat_string  # [cite: 16]
        }
        return jsonify(response), 200  # [cite: 32]

    except Exception as e:
        # Handle exceptions gracefully [cite: 28]
        return jsonify({
            "is_success": False,  # [cite: 27]
            "user_id": f"{USER_ID_FULL_NAME}_{USER_ID_DOB}",
            "email": USER_EMAIL,
            "roll_number": COLLEGE_ROLL_NUMBER,
            "error": str(e)
        }), 400

if __name__ == '__main__':
    app.run(debug=True)