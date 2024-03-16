from flask import Flask, jsonify, request
import subprocess
import asyncio

# async def start_ddos_async( target_url):  # Make the function asynchronous
#     # ... (code to extract the target_url) ...

#     with open('start.sh', 'w') as file:  
#         file.write('source myvenv/bin/activate\n')
#         file.write('python3 ddos.py {} 90'.format(target_url))         

#     proc = await asyncio.create_subprocess_shell(
#         './start.sh',
#         stdout=asyncio.subprocess.PIPE,
#         stderr=asyncio.subprocess.PIPE
#     )

#     stdout, stderr = await proc.communicate()  # Wait for the process
#     if proc.returncode == 0:
#         return jsonify("Success, DDoS running!") 
#     else:
#         return jsonify("DDoS start failed: {}".format(stderr.decode())), 500









app = Flask(__name__)

@app.route('/echo/', methods=['POST'])
def echo_body_json():
    # print("Heyyaaa")
    # print(request)
    # if not request.is_json:
    #     return jsonify("Error: Request data must be JSON"), 400

    # request_data = request.get_json()
    # return jsonify(request_data)
    return jsonify("Hey Mom")


@app.route('/use/ddos/start', methods=['POST'])
def start_ddos(request):
    # if not request.is_json:
    #     return jsonify("Error: Request data must be JSON"), 400

    data = request.body()
    target_url = data.get('url')
    # with open('mynewfile.txt', 'w') as file:  # 'w' for write mode (overwrites)  
    # print('File writing complete!')
    # subprocess.run(['./start.sh'], shell=True)  # Assuming start.sh is in the same directory
    # return jsonify("Success, DDoS running!")  # Replace with placeholder action
    # loop = asyncio.get_event_loop()  # Get the event loop
    # return loop.run_forever(start_ddos_async( target_url))  # Run the async function
    return jsonify(target_url)


@app.route('/use/ddos/stop', methods=['POST'])
def stop_ddos():
    return jsonify("Hi Dad")  # Replace with placeholder action



@app.route('/use/ddos/status', methods=['GET'])
def ddos_status():
    return jsonify("Hi Dad")  # Replace with placeholder action



if __name__ == '__main__':
    app.run(debug=True, port=5667) 
