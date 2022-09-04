import logging
from flask import Flask
from income_census.exception import IC_Exception
from income_census.logger import logging
from income_census.exception import IC_Exception
import sys




app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    
    try:
        raise Exception(" WE are testing custom exception")
    except Exception as e:
        incomcensuserror = IC_Exception(e,sys)
        logging.info(incomcensuserror.error_message)
        logging.info("We are Testing logging module")
    return "Starting Machine Learning Project: Adult Censes Dataset"



if __name__=="__main__":
    app.run(debug=True)

