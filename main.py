from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Halo, ini FastAPI pertama kamu!"}

@app.get("/halo/{nama}")
def baca_nama(nama: str):
    return {"pesan": f"Halo {nama}, selamat datang di FastAPI!"}
