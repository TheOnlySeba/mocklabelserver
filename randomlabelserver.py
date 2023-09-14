import random

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/test", methods=['POST'])
def test():
    data = request.get_json()
    guid = data[0]['guid']
    
    # Define possible values
    levels = ["first", "second"]
    departments = ["basis", "contract", "application"]
    products = [
        "ERPsim", "SAP S/4HANA TS410", "SAP S/4HANA (GBI/GBS/Kundensonderwünsche)", 
        "SAP BW", "SAP BusinessObjects", "SAP HANA", "SAP Entwicklungssysteme", 
        "ERP4Schools / SAP4Schools", "SAP ME/Mii (nur Installation Guides)", 
        "ERP GBI/ ECC", "ERP IDES", "Move to S/4HANA / Sunset ECC", 
        "S/4HANA Mandant (GBI)", "GBS / Digital Transformation Curriculum (+Website)", 
        "SAP BW & BW+BusinessObiects (Lumira)", "HANA", "Business by Design", 
        "Entwicklungssystem bzw. Mandant", "BIP (Development)", 
        "(BTP = Business Technology Platform)", "ME. MII. Pco (Industrie 4.0)", 
        "TS410", "SAP4Schools IUS", "ERPAs~bool", "Signavio", "Business One"
    ]
    
    # Randomly sample values
    level = random.choice(levels)
    
    # If level is 'second', choose a department, else it's None
    department = random.choice(departments) if level == "second" else None
    
    # If department is 'basis' or 'application', choose a product, else it's None
    product = random.choice(products) if department in ["basis", "application"] else None
    
    # Build response
    response = {"guid": guid, "level": level}
    if department:
        response["department"] = department
    if product:
        response["product"] = product
    
    return jsonify(response)



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
