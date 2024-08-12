from flask import Flask, render_template, request, redirect, url_for
import joblib
import pandas as pd

app = Flask(__name__)

 
def load_model():
     
    return joblib.load(r"C:\NutriScore\notebook\models\modelrandom_forest_gini_4.z")

def load_categories():
    
    df = pd.read_csv(r"C:\NutriScore\Data\categories.csv", header=None)   
    df.columns = ['category']   
    return df['category'].tolist()

 

 
model = load_model()
categories = load_categories()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
    
        energy = float(request.form['energy'])
        saturated_fat = float(request.form['saturated_fat'])
        sugars = float(request.form['sugars'])
        salt = float(request.form['salt'])
        fibers = float(request.form['fibers'])
        category = request.form['category']

      
        product = {
            "energy": round(energy),
            "saturated_fat": round(saturated_fat),
            "sugars": round(sugars),
            "salt": round(salt),
            "fibers": round(fibers),
            "group1_Beverages": 0,
            "group1_Cereals and potatoes": 0,
            "group1_Composite foods": 0,
            "group1_Fat and sauces": 0,
            "group1_Fruits and vegetables": 0,
            "group1_Milk and dairy products": 0,
            "group1_Sugary snacks": 0,
            "group1_unknown": 0,
        }
 
        formatted_category = f"group1_{category}"
        if formatted_category in product:
            product[formatted_category] = 1

        sample = list(product.values())

     
        nutrigrade = model.predict([sample])[0].upper()

         
        return redirect(url_for('result', nutrigrade=nutrigrade))

    return render_template('index.html', categories=categories )

@app.route('/result')
def result():
    nutrigrade = request.args.get('nutrigrade', None)
    return render_template('result.html', nutrigrade=nutrigrade)

if __name__ == '__main__':
    app.run(debug=True)
