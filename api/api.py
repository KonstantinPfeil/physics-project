from fastapi import FastAPI, APIRouter, File, UploadFile
import sys
import io
import pandas as pd
import numpy as np
sys.path.append(r"../")
from auslesen import readFromFile
from diagram import calculate


path = APIRouter(prefix="/api")


@path.get("/data/")
async def get_data():
    calculation = calculate()
    if calculation is not None:
        calculation = [e.tolist() if type(e) == np.ndarray else e for e in calculation]
        t, s, v, a, ps, pv, aa, paras_s, paras_v, paras_a = calculation
        return dict(t=t, s=s, v=v, a=a, ps=ps, pv=pv, aa=aa)
    return None


@path.post("/data/")
async def get_data_from_file(file: UploadFile = File(...)):
    bytesOfFile = io.BytesIO(await file.read())
    if file.content_type.__contains__("openxmlformats"):
        file = pd.read_excel(bytesOfFile)
    else:
        file = pd.read_csv(bytesOfFile, sep=";", header=0)
    times = readFromFile(file=file)
    calculation = calculate(times)
    if calculation is not None:
        calculation = [e.tolist() if type(e) == np.ndarray else e for e in calculation]
        t, s, v, a, ps, pv, aa, paras_s, paras_v, paras_a = calculation
        return dict(t=t, s=s, v=v, a=a, ps=ps, pv=pv, aa=aa)
    return None
