from form_test import app
import sys

try:
    port = int(sys.argv[1])
except:
    port = 5000

app.run(host='0.0.0.0', port=port, debug=True, threaded=True)
