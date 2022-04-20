import pandas as pd
from flask import Flask
from flask_restful import Api, Resource, reqparse, request
import pandas as pd
import joblib
loaded_st = joblib.load("stacking.joblib")


app = Flask(__name__)
api = Api(app)


@app.route('/is_loyality', methods=['GET'])
def get_user():
    try:
        parser = reqparse.RequestParser()
        parser.add_argument("id")
        parser.add_argument("login")
        parser.add_argument("NlogonAll")
        parser.add_argument("calendbinary")
        parser.add_argument("filterbinary")
        parser.add_argument("Nexport")
        parser.add_argument("diffdate")
        parser.add_argument("diffbill")
        parser.add_argument("fastbill")
        parser.add_argument("msignal")
        parser.add_argument("avgSectionbinary")
        parser.add_argument("avgNullSearchW")
        parser.add_argument("avgNullSearchM")
        parser.add_argument("avgEmptyStupid")
        parser.add_argument("Nlongfilter")
        parser.add_argument("NcontractAll")
        parser.add_argument("NcontractAllAuction")
        parser.add_argument("NcontractAllReq")
        parser.add_argument("NprotNotAll")
        parser.add_argument("NprotNotAllAuction")
        parser.add_argument("NprotNotAllReq")
        parser.add_argument("protContractRatio")
        params = parser.parse_args()

        # Оставление столбцов, которые были использованны при обучении

        new_user = {
            "login": params["login"],
            "NlogonAll": params["NlogonAll"],
            "calendbinary": params["calendbinary"],
            "filterbinary": params["filterbinary"],
            "Nexport": params["Nexport"],
            "diffdate": params["diffdate"],
            "diffbill": params["diffbill"],
            "fastbill": params["fastbill"],
            "msignal": params["msignal"],
            "avgSectionbinary": params["avgSectionbinary"],
            "avgNullSearchW": params["avgNullSearchW"],
            "avgEmptyStupid": params["avgEmptyStupid"],
            "Nlongfilter": params["Nlongfilter"],
            "NcontractAllAuction": params["NcontractAllAuction"],
            "protContractRatio": params["protContractRatio"]
        }


        user = pd.DataFrame([new_user])
        answer = loaded_st.predict(user)

        a = dict()
        a['is_loyality'] = int(answer[0])
        return a, 200
    except:
        return f'Bad requests', 400


if __name__ == '__main__':
    app.run(debug=True)