from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os

app = Flask(__name__)

@app.route('/static/images/<filename>')
def serve_image(filename):
    return send_from_directory('static/images', filename)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/yamaha')
def yamaha():
    return render_template('yamaha.html')

@app.route('/honda')
def honda():
    return render_template('honda.html')

@app.route('/suzuki')
def suzuki():
    return render_template('suzuki.html')

@app.route('/kuba')
def kuba():
    return render_template('kuba.html')

@app.route('/karsilastirma')
def karsilastirma():
    return render_template('karsilastirma.html')

@app.route('/arama', methods=['GET', 'POST'])
def arama():
    if request.method == 'POST':
        arama_terimi = request.form.get('arama_terimi').lower().strip()
        
        # Marka adı kontrolü - direkt o markanın sayfasına yönlendir
        if 'yamaha' in arama_terimi:
            return redirect(url_for('yamaha'))
        elif 'honda' in arama_terimi:
            return redirect(url_for('honda'))
        elif 'suzuki' in arama_terimi:
            return redirect(url_for('suzuki'))
        elif 'kuba' in arama_terimi:
            return redirect(url_for('kuba'))
        elif 'karşılaştır' in arama_terimi or 'karsilastir' in arama_terimi or 'compare' in arama_terimi:
            return redirect(url_for('karsilastirma'))
        else:
            # Normal arama sonuçları
            return render_template('arama_sonuclari.html', arama_terimi=arama_terimi)
    return render_template('arama.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000) 