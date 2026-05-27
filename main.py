from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import pandas as pd

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

# carrello
df = pd.DataFrame(columns=["prodotto", "prezzo", "quantita"])


@app.get("/")
def home():
    return FileResponse("static/index.html")


# =========================
# 🔵 AGGIUNGI PRODOTTO
# =========================

@app.get("/add")
def add_get(prodotto: str, prezzo: float, quantita: int):

    global df

    df = pd.concat([
        df,
        pd.DataFrame([[prodotto, prezzo, quantita]],
                     columns=["prodotto", "prezzo", "quantita"])
    ], ignore_index=True)

    return {"messaggio": "aggiunto GET"}


@app.post("/add")
def add_post(prodotto: str = Form(...), prezzo: float = Form(...), quantita: int = Form(...)):

    global df

    df = pd.concat([
        df,
        pd.DataFrame([[prodotto, prezzo, quantita]],
                     columns=["prodotto", "prezzo", "quantita"])
    ], ignore_index=True)

    return {"messaggio": "aggiunto POST"}


# =========================
# 🔵 LISTA PRODOTTI
# =========================

@app.get("/lista")
def lista_get():
    return df.to_dict(orient="records")


@app.post("/lista")
def lista_post():
    return df.to_dict(orient="records")


# =========================
# 🔵 TOTALE CARRELLO
# =========================

@app.get("/totale")
def totale_get():

    if len(df) == 0:
        return {"totale": 0}

    totale = (df["prezzo"] * df["quantita"]).sum()

    return {"totale": round(totale, 2)}


@app.post("/totale")
def totale_post():

    if len(df) == 0:
        return {"totale": 0}

    totale = (df["prezzo"] * df["quantita"]).sum()

    return {"totale": round(totale, 2)}


# =========================
# 🔵 PRODOTTI COSTOSI (>50€)
# =========================

@app.get("/costosi")
def costosi_get():

    df["tot"] = df["prezzo"] * df["quantita"]

    return df[df["tot"] > 50].to_dict(orient="records")


@app.post("/costosi")
def costosi_post():

    df["tot"] = df["prezzo"] * df["quantita"]

    return df[df["tot"] > 50].to_dict(orient="records")