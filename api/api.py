from fastapi import FastAPI, APIRouter, File, UploadFile
import sys
import io
import pandas as pd
sys.path.append(r"../")
from auslesen import readFromFile
from diagram import calculate

path = APIRouter(prefix="/api")


@path.get("/data/")
async def get_data():
    calculation = calculate()
    if calculation is not None:
        t, s, v, a, ps, pv, aa = calculation
        return dict(t=t, s=s, v=v, a=a, ps=ps, pv=pv, aa=aa)
    return None


@path.post("/data/")
async def get_data_from_file(file: UploadFile = File(...)):
    bytesOfFile = io.BytesIO(await file.read())
    if file.content_type.__contains__("openxmlformats"):
        file = pd.read_excel(bytesOfFile)
    else:
        file = pd.read_csv(bytesOfFile)
    times = readFromFile(file=file)
    calculation = calculate(times)
    if calculation is not None:
        t, s, v, a, ps, pv, aa = calculation
        return dict(t=t, s=s, v=v, a=a, ps=ps, pv=pv, aa=aa)
    else:
        return None
