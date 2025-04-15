from flask import Flask, request, jsonify, render_template

from problems.prob1 import prob1
from problems.prob2 import prob2
from problems.prob3 import prob3
from problems.prob4 import prob4
from problems.prob5 import prob5
from problems.prob6 import prob6
from problems.prob7 import prob7
from problems.prob9 import prob9
from problems.prob10 import prob10
from problems.prob11 import prob11
from problems.prob12 import prob12
from problems.prob13 import prob13
from problems.prob14 import prob14
from problems.prob15 import prob15
from problems.prob16 import prob16
from problems.prob17 import prob17
from problems.prob18 import prob18
from problems.prob19 import prob19
from problems.prob20 import prob20
from problems.prob21 import prob21
from problems.prob22 import prob22
from problems.prob23 import prob23
from problems.prob25 import prob25
from problems.prob26 import prob26
from problems.prob27 import prob27
from problems.prob28 import prob28
from problems.prob29 import prob29
from problems.prob30 import prob30
from problems.prob31 import prob31
from problems.prob32 import prob32
from problems.prob34 import prob34
from problems.prob35 import prob35
from problems.prob36 import prob36
from problems.prob38a import prob38a
from problems.prob38b import prob38b
from problems.prob38c import prob38c
from problems.prob39 import prob39
from problems.prob40 import prob40
from problems.prob41 import prob41
from problems.prob42 import prob42
from problems.prob43 import prob43
from problems.prob44 import prob44
from problems.prob45 import prob45
from problems.prob46 import prob46
from problems.prob47 import prob47
from problems.prob48 import prob48
from problems.prob49 import prob49
from problems.prob50 import prob50
from problems.prob51 import prob51
from problems.prob51a import prob51a
from problems.prob52 import prob52
from problems.prob54 import prob54
from problems.prob55 import prob55
from problems.prob56 import prob56
from problems.prob57 import prob57
from problems.prob58 import prob58
from problems.prob60 import prob60
from problems.prob62 import prob62
from problems.prob66 import prob66
from problems.prob67 import prob67
from problems.prob68 import prob68


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/calculate1', methods=['POST'])
def calculate1():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        r = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob1(r))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate2', methods=['POST'])
def calculate2():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        min_val = next((int(value) for key, value in data.items() if key.startswith("inputMin")), None)
        max_val = next((int(value) for key, value in data.items() if key.startswith("inputMax")), None)

        if min_val >= max_val:
            return jsonify({"error": "Min musi być mniejsze od Max"}), 400

        return jsonify(prob2(min_val, max_val))

    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate3', methods=['POST'])
def calculate3():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        r = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob3(r))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate4', methods=['POST'])
def calculate4():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        r = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob4(r))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate5', methods=['POST'])
def calculate5():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        r = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob5(r))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate6', methods=['POST'])
def calculate6():
    return jsonify(prob6())


@app.route('/calculate7', methods=['POST'])
def calculate7():
    return jsonify(prob7())


@app.route('/calculate9', methods=['POST'])
def calculate9():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        r = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob9(r))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate10', methods=['POST'])
def calculate10():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        r = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob10(r))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate11', methods=['POST'])
def calculate11():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        r = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob11(r))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate12', methods=['POST'])
def calculate12():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        n = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        max_x = next((int(value) for key, value in data.items() if key.startswith("inputNumberMax")), None)
        iterations = next((int(value) for key, value in data.items() if key.startswith("inputNumberIt")), None)

        return jsonify(prob12(n, max_x,iterations))

    except ValueError:
        return jsonify({"error": "Invalid number"}), 400

@app.route('/calculate13', methods=['POST'])
def calculate13():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        x = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        max_n = next((int(value) for key, value in data.items() if key.startswith("inputNumberMax")), None)
        iterations = next((int(value) for key, value in data.items() if key.startswith("inputNumberIt")), None)

        return jsonify(prob13(x, max_n, iterations))

    except ValueError:
        return jsonify({"error": "Invalid number"}), 400

@app.route('/calculate14', methods=['POST'])
def calculate14():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        r = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob14(r))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate15', methods=['POST'])
def calculate15():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        r = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob15(r))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate16', methods=['POST'])
def calculate16():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        r = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob16(r))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate17', methods=['POST'])
def calculate17():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        a = next((int(value) for key, value in data.items() if key.startswith("inputNumberA")), None)
        r = next((int(value) for key, value in data.items() if key.startswith("inputNumberRange")), None)
        return jsonify(prob17(a, r))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400

@app.route('/calculate18', methods=['POST'])
def calculate18():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        r = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob18(r))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate19', methods=['POST'])
def calculate19():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        r = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob19(r))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate20', methods=['POST'])
def calculate20():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        r = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob20(r))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate21', methods=['POST'])
def calculate21():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        r = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob21(r))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate22', methods=['POST'])
def calculate22():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        r = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob22(r))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate23', methods=['POST'])
def calculate23():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        p_range = next((int(value) for key, value in data.items() if key.startswith("inputNumberPRange")), None)
        n_range = next((int(value) for key, value in data.items() if key.startswith("inputNumberNRange")), None)
        return jsonify(prob23(p_range,n_range))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate25', methods=['POST'])
def calculate25():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        r = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob25(r))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate26', methods=['POST'])
def calculate26():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        r = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob26(r))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate27', methods=['POST'])
def calculate27():
    return jsonify(prob27())


@app.route('/calculate28', methods=['POST'])
def calculate28():
    return jsonify(prob28())


@app.route('/calculate29', methods=['POST'])
def calculate29():
    return jsonify(prob29())


@app.route('/calculate30', methods=['POST'])
def calculate30():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        r = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob30(r))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate31', methods=['POST'])
def calculate31():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        a = next((int(value) for key, value in data.items() if key.startswith("inputNumberA")), None)
        b = next((int(value) for key, value in data.items() if key.startswith("inputNumberB")), None)
        c = next((int(value) for key, value in data.items() if key.startswith("inputNumberC")), None)

        return jsonify(prob31(a,b,c))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400



@app.route('/calculate32', methods=['POST'])
def calculate32():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        r = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob32(r))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate34', methods=['POST'])
def calculate34():
    return jsonify(prob34())


@app.route('/calculate35', methods=['POST'])
def calculate35():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        r = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob35(r))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate36', methods=['POST'])
def calculate36():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        r = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob36(r))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate381', methods=['POST'])
def calculate381():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        n = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob38a(n))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate382', methods=['POST'])
def calculate382():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        n = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob38b(n))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate383', methods=['POST'])
def calculate383():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        n = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob38c(n))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate39', methods=['POST'])
def calculate39():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        a = next((int(value) for key, value in data.items() if key.startswith("inputNumberA")), None)
        b = next((int(value) for key, value in data.items() if key.startswith("inputNumberB")), None)
        c = next((int(value) for key, value in data.items() if key.startswith("inputNumberC")), None)
        n = next((int(value) for key, value in data.items() if key.startswith("inputNumberN")), None)

        return jsonify(prob39(a,b,c,n))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate40', methods=['POST'])
def calculate40():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        n = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob40(n))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate41', methods=['POST'])
def calculate41():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        r = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob41(r))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate42', methods=['POST'])
def calculate42():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        r = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob42(r))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate43', methods=['POST'])
def calculate43():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        r = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob43(r))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400

@app.route('/calculate44', methods=['POST'])
def calculate44():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        a = next((int(value) for key, value in data.items() if key.startswith("inputNumberA")), None)
        b = next((int(value) for key, value in data.items() if key.startswith("inputNumberB")), None)
        limit = next((int(value) for key, value in data.items() if key.startswith("inputNumberLimit")), None)

        return jsonify(prob44(a,b,limit))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate45', methods=['POST'])
def calculate45():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        a = next((int(value) for key, value in data.items() if key.startswith("inputNumberA")), None)
        b = next((int(value) for key, value in data.items() if key.startswith("inputNumberB")), None)
        c = next((int(value) for key, value in data.items() if key.startswith("inputNumberC")), None)
        n = next((int(value) for key, value in data.items() if key.startswith("inputNumberN")), None)

        return jsonify(prob45(a,b,c,n))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate46', methods=['POST'])
def calculate46():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        a = next((int(value) for key, value in data.items() if key.startswith("inputNumberA")), None)
        b = next((int(value) for key, value in data.items() if key.startswith("inputNumberB")), None)
        c = next((int(value) for key, value in data.items() if key.startswith("inputNumberC")), None)
        d = next((int(value) for key, value in data.items() if key.startswith("inputNumberD")), None)
        n = next((int(value) for key, value in data.items() if key.startswith("inputNumberN")), None)

        return jsonify(prob46(a,b,c,d,n))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate47', methods=['POST'])
def calculate47():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        r = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob47(r))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate48', methods=['POST'])
def calculate48():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        n = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob48(n))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate49', methods=['POST'])
def calculate49():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        m = next((int(value) for key, value in data.items() if key.startswith("inputNumberM")), None)
        e = next((int(value) for key, value in data.items() if key.startswith("inputNumberE")), None)
        return jsonify(prob49(m,e))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate50', methods=['POST'])
def calculate50():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        r = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob50(r))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate51', methods=['POST'])
def calculate51():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        n = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob51(n))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate511', methods=['POST'])
def calculate511():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        r = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob51a(r))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate52', methods=['POST'])
def calculate52():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        m = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob52(m))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate54', methods=['POST'])
def calculate54():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        n = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob54(n))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate55', methods=['POST'])
def calculate55():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        limit = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob55(limit))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate56', methods=['POST'])
def calculate56():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        n = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob56(n))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate57', methods=['POST'])
def calculate57():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        a = next((int(value) for key, value in data.items() if key.startswith("inputNumberA")), None)
        b = next((int(value) for key, value in data.items() if key.startswith("inputNumberB")), None)
        return jsonify(prob57(a, b))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate58', methods=['POST'])
def calculate58():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        s = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob58(s))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate60', methods=['POST'])
def calculate60():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        start = next((int(value) for key, value in data.items() if key.startswith("inputNumberStart")), None)
        end = next((int(value) for key, value in data.items() if key.startswith("inputNumberEnd")), None)
        return jsonify(prob60(start, end))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate62', methods=['POST'])
def calculate62():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        a = next((int(value) for key, value in data.items() if key.startswith("inputNumberA")), None)
        b = next((int(value) for key, value in data.items() if key.startswith("inputNumberB")), None)
        m = next((int(value) for key, value in data.items() if key.startswith("inputNumberM")), None)
        n = next((int(value) for key, value in data.items() if key.startswith("inputNumberN")), None)
        return jsonify(prob62(a,b,m,n))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate66', methods=['POST'])
def calculate66():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        n = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob66(n))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400

@app.route('/calculate67', methods=['POST'])
def calculate67():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        a = next((int(value) for key, value in data.items() if key.startswith("inputNumberA")), None)
        b = next((int(value) for key, value in data.items() if key.startswith("inputNumberB")), None)
        n = next((int(value) for key, value in data.items() if key.startswith("inputNumberN")), None)
        return jsonify(prob67(a,b,n))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate68', methods=['POST'])
def calculate68():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        a = next((int(value) for key, value in data.items() if key.startswith("inputNumberA")), None)
        b = next((int(value) for key, value in data.items() if key.startswith("inputNumberB")), None)
        n = next((int(value) for key, value in data.items() if key.startswith("inputNumberN")), None)
        return jsonify(prob68(a,b,n))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400

if __name__ == '__main__':
    app.run(debug=True)
