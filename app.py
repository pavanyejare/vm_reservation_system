#!/env/bin/python3
from this import d
import cloud

from flask import Flask
app = Flask(__name__)




@app.route('/checkout/<user>')
def vm_request(user):
    data=cloud.vm_allocation(user)
    return "%s" % str(data)

@app.route('/checkin/<user>')
def vm_del(user):
    data=cloud.del_vm(user)
    return "%s" % str(data)
@app.route('/')
def index():
    return """Hit the url with user name you will get vm details \n
              e.g. http://localhost:5000/
    """


if __name__ == "__main__":
    app.run(debug=True)


