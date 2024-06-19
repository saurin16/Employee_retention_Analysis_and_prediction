from wsgiref import simple_server
from flask import Flask, request, render_template
from flask import Response
from apps.prediction.predict_model import PredictModel
from apps.core.config import Config
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route('/training', methods=['POST'])
@cross_origin()
def training_route_client():
    try:
        config = Config()
        #get run id
        run_id = config.get_run_id()
        data_path = config.prediction_data_path
        #prediction object initialization
        predictModel=PredictModel(run_id, data_path)
        #prediction the model
        predictModel.batch_predict_from_model()
        return Response("Prediction successfull! and its RunID is : "+str(run_id))
    except ValueError:
        return Response("Error Occurred! %s" % ValueError)
    except KeyError:
         return Response("Error Occurred! %s" % KeyError)
    except Exception as e:
        return Response("Error Occurred! %s" % e)


if __name__ == "__main__":

        host = '0.0.0.0'
        port = 5000
        httpd = simple_server.make_server(host, port, app)
        httpd.serve_forever()
