from flask import Flask, request, render_template, jsonify, session, redirect, url_for
import requests
from converter import Converter

app = Flask(__name__)
app.config["SECRET_KEY"] = "fdfgkjtjkkg45yfdb"


converter = Converter()

@app.route('/')
def show_home():
    return render_template('index.html')

@app.route('/convert', methods = ['POST'])
def convert_forex():
    
    base  = request.form.get('base')
    other  = request.form.get('final')

    amount  = request.form.get('amount')


    output = converter.process_conversion(base = base, other = other, amount = amount)

    if 'ok' in output:
        result = output[1]
        if result == -1:
            message = 'oops something is wrong'
            return render_template('index.html', message = message)
        else: 
            return render_template('index.html', converted = True, converted_amount = result, base = base.upper(), other = other.upper(), amount = amount)


    else: 
        message = output[1]
        return render_template('index.html', message = message)





    # if (not base or not other or not amount):
    #     message = 'Please enter all inputs'
    #     return render_template('index.html', message = message)
    
    # if ((not converter.check_valid_currency(base)) or not converter.check_valid_currency(other)):
    #     message = 'One of your requested currencies are not supported'
    #     return render_template('index.html', message = message)


        
    # try:
    #     float(amount)
    #     amount = float(amount)
    #     if amount < 0:
    #         message = 'The amount is not valid'
    #         return render_template('index.html', message = message)
    # except ValueError:
    #     message = 'The amount is not valid'
    #     return render_template('index.html', message = message)


    

 
    





    # converted = True
    # converted_amount = amount

    # # f'your base: {base}, your final: {final}, your amount: {amount}'

    # # return redirect('/', code = 302)
    # # return redirect(url_for('show_home', converted=converted, converted_amount = converted_amount))
    # return render_template('index.html', converted=converted, converted_amount = converted_amount)



# # Set API endpoint and required parameters
# endpoint = 'convert'
# access_key = '5eb1d7778541779ef8eef603af8eb38a'  # Replace with your actual access key
# params = {
#     'access_key': access_key,
#     'from': 'USD',
#     'to': 'EUR',
#     'amount': 10
# }

# # Initialize and send GET request
# response = requests.get(f'http://api.exchangerate.host/{endpoint}', params=params)

# # If the response was successful, decode the JSON data
# if response.ok:
#     conversion_result = response.json()
# else:
#     conversion_result = None

# # conversion_result now contains the API response

# print(conversion_result)
