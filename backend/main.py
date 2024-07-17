# import pandas as pd
# import numpy as np
# import json
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from fastapi import FastAPI ,HTTPException
# from pydantic import BaseModel
# from fastapi.middleware.cors import CORSMiddleware

# data = pd.read_csv("FinalDataset.csv")

# app = FastAPI()

# origins = [
#     "http://localhost:3000",
#     "http://localhost:8000"
# ]
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# class Nirf(BaseModel):
#     TLR:float
#     RPC:float
#     GO:float
#     OI:float
#     PERCEPTION:float

# class wholeData(BaseModel):
#     N:int
#     F1:float
#     f2:float
#     EA:float
#     EI:float
#     LI:int
#     EXLI:float
#     EXLIE:float
#     LB:int
#     PA:float
#     PB:float
#     PC:int
#     PC:int=0

# @app.get("/")
# def demoNirf():
#     data = "This is a simple data response."
#     return {"data": data}

# @app.post("/detail/nirf")
# def dataNirf(item:Nirf):
#     try:
    
#         return {"value":item.TLR}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail="Server problem") 
    
# @app.post("/nirf")
# def getScore(item:Nirf):
#     # data = item.model_dump()
#     # TLR= data['TLR']
#     # RPC= data['RPC']
#     # GO= data['GO']
#     # OI= data['OI']
#     # PERCEPTION= data['PERCEPTION']
#     # print(TLR)
#     # finalValue = inputValues([[TLR,RPC,GO,OI,PERCEPTION]])
#     # print(finalValue)
#     # TLR=item.TLR
#     # RPC=item.RPC
#     # GO = item.GO
#     # OI=item.OI
#     # PERCEPTION = item.PERCEPTION
#     # finalValue = predict({"TLR": TLR, "RPC": RPC, "GO": GO, "OI": OI, "PERCEPTION": PERCEPTION})
#     # print(finalValue)
#     # return {"finalValue": finalValue}
#     return {"ans":inputValues(item)}


#     try:
#         return item.dict()
#     except Exception as e:
#         raise HTTPException(status_code=500, detail="Server problem")

# # @app.post("/data/nirf")
# # def wholeData():


# @app.post('/nirf/data')
# def dataCheck(data:wholeData):
#     return data.PC
#     # print(data.json())



# def loadModel(Z):
#     X = data.iloc[:, 6:11]
#     y = data.iloc[:, 4]
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=20)
#     regressor = LinearRegression()
#     regressor.fit(X_train, y_train)
#     y_pred = regressor.predict(Z)
#     return y_pred

# def predict(params):
#     Y = np.array([[params.TLR, params.RPC, params.GO, params.OI, params.PERCEPTION]])
#     score = loadModel(Y)
#     return score[0]

# def inputValues(params):
#     print("params", params)
#     return(predict(params))

# # You can add the following lines to call the inputValues function if needed
# # Example:
# # input_data = '{"TLR": 80, "RPC": 70, "GO": 80, "OI": 90, "PERCEPTION": 78}'
# # inputValues(input_data)

import pandas as pd
import numpy as np
import json
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from fastapi import FastAPI ,HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.read_csv("FinalDataset.csv")
data = pd.read_csv("dataNIRF.csv")

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:8000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Nirf(BaseModel):
    TLR:float
    RPC:float
    GO:float
    OI:float
    PERCEPTION:float

class wholeData(BaseModel):
    NE:float
    NT:float
    NP:float
    F:float
    FRA:float
    F1:int
    F2:float
    F3:float
    BC:int
    BO:float
    FRQ:float
    CC:int
    P:float
    T:float
    OP25:float
    PG:float
    PP:float
    RF:float
    CF:float
    NPP:float
    NHS:float
    NG:float
    MS:float
    NPH:float
    D:float
    Rd:float
    NWS:float
    NESC:float
    PCS:float
    OPT:float
    PR:float


@app.get("/")
def demoNirf():
    data = "This is a simple data response."
    return {"data": data}

@app.post("/detail/nirf")
def dataNirf(item:Nirf):
    try:
    
        return {"value":item.TLR}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Server problem") 
    
@app.post("/nirf")
def getScore(item:Nirf):
    # data = item.model_dump()
    # TLR= data['TLR']
    # RPC= data['RPC']
    # GO= data['GO']
    # OI= data['OI']
    # PERCEPTION= data['PERCEPTION']
    # print(TLR)
    # finalValue = inputValues([[TLR,RPC,GO,OI,PERCEPTION]])
    # print(finalValue)
    TLR=item.TLR
    RPC=item.RPC
    GO = item.GO
    OI=item.OI
    PERCEPTION = item.PERCEPTION
    finalValue = predict({"TLR": TLR, "RPC": RPC, "GO": GO, "OI": OI, "PERCEPTION": PERCEPTION})
    print(finalValue)
    return {"finalValue": finalValue}


    try:
        return item.dict()
    except Exception as e:
        raise HTTPException(status_code=500, detail="Server problem")

# @app.post( =  {"NT": 2773, "NP": 696, "F": 919}

class wholeData(BaseModel):
    NT: float
    NP: float
    F: float
    FSR:float

@app.post("/nirf/data")
def calculate_tlrscore(data: wholeData):
    try:
        fsr_params = {
            "NT": data.NT,
            "NP": data.NP,
            "F": data.F
        }
        N = data.NT+data.NP
        if(data.F/N<1.5):
            data.FSR =0
            return data.FSR
        tlr_score = Models.tlrPredict(fsr_params)
        return {"TLR Score": tlr_score}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Server problem")
# @app.post('/nirf/data')
# def dataCheck(data:wholeData):
#     return data.PC
#     # print(data.json())


class Models:
    def fsrModel(Z):
        X = data.iloc[:, 1:4]
        y = data.iloc[:, 31]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        regressor = LinearRegression()
        regressor.fit(X_train, y_train)
        y_pred = regressor.predict(Z)
        return y_pred

  
    def fsrPredict(params):
        Y = [[params["NT"], params["NP"], params["F"]]] #Yahan value ghus rha hai
        score = Models.fsrModel(Y)
        return score[0]
        

   
    def tlrModel(Z):
        X = data.iloc[:, 31:32]
        print(X)
        y = data.iloc[:, 34]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        regressor = LinearRegression()
        regressor.fit(X_train, y_train)
        y_pred = regressor.predict(Z)
        return y_pred

 
    def tlrPredict(params):
        Y = [[Models.fsrPredict(params)]]
        score = Models.tlrModel(Y)
        return score[0]


def loadModel(Z):
    X = data.iloc[:, 6:11]
    y = data.iloc[:, 4]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=20)
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    y_pred = regressor.predict(Z)
    return y_pred

def predict(params):
    Y = np.array([[params["TLR"], params["RPC"], params["GO"], params["OI"], params["PERCEPTION"]]])
    score = loadModel(Y)
    return score[0]

def inputValues(params):
    values = json.loads(params)
    print(predict(values))

fsr_params = {"NT": 2773, "NP": 696, "F": 919} #Idhar se data model mai jata hai
   
tlr_params = fsr_params  

    #Print karke check kar raha hu
print("TLR Score:", Models.tlrPredict(tlr_params)) #yeh andar ka funciton tera tlr score predeict kar rha hai using the data of fsr {Yeh hai tera tlr score as responcse tereko isiko dena hai anurag ko}

# You can add the following lines to call the inputValues function if needed
# Example:
# input_data = '{"TLR": 80, "RPC": 70, "GO": 80, "OI": 90, "PERCEPTION": 78}'
# inputValues(input_data)