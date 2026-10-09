#pakai_module.py
import math
from random import randint
import datetime as dt

print(math.sqrt(16))
print(math.pi)
print(randint(1, 6))
print(dt.date.today().year)


#utils/hitung.py
def rata_rata(data):
    return sum(data) / len(data)


#main.py
from utils.hitung import rata_rata

nilai = [80, 90, 70]
print(rata_rata(nilai))


###terminal - zsh
## buat & aktifkan virtual environment
#python -m venv venv
#.\venv\Scripts\Activate.ps1

# install paket dari PyPI
##pip install pandas requests

# simpan & pasang ulang dependensi
##pip freeze > requirements.txt
##pip install -r requirements.txt