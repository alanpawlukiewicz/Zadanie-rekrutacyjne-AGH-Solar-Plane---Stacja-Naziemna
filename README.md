# Program stacji naziemnej

## Opis
Program ma na celu odbieranie obrazów oraz danych z systemu wizyjnego oraz wyświetlanie ich w przeglądarce pod adresem http://192.168.0.100:5000/.
Został on napisany w framework-u o nazwie [Flask](https://flask.palletsprojects.com/en/stable/).


## Założenia

Aby program zadziałał muszą zostać spełnione następujące warunki:

- zarazem samolot jak i stacja naziemna muszą być podłączone do tej samej sieci lokalnej za pomocą modemu lub routera
- stacja naziemna musi mieć ustawione lokalne ip na ```192.168.0.100```
- port ```5000``` nie może być zajęty przez inny program
- w trakcie przesyłania obrazów program stacji naziemnej musi być włączony

**UWAGA**: Jeżeli chcemy sprawdzić działanie programów na jednym komputerze należy w obydwóch zmienić wartość ```SERVER_IP``` na ```127.0.0.1```.<br>
Jeżeli chcemy, aby programy działały na innym porcie niż ```5000```, to należy zmienić w obydwóch zmienić wartość ```SERVER_PORT```.

## Instalacja

1. Sklonowanie repozytorium

- ```git clone https://github.com/alanpawlukiewicz/Zadanie-rekrutacyjne-AGH-Solar-Plane---Stacja-Naziemna.git``` 

2. Przejście do folderu projektu

- ```cd Zadanie-rekrutacyjne-AGH-Solar-Plane---Stacja-Naziemna```

3. Stworzenie środkowiska wirtualnego

- ```python -m venv venv```

4. Aktywacja środowiska

- ```venv\Scripts\activate```

5. Instalacja zależności

- ```pip install -r requirements.txt```

6. Uruchomienie projektu

- ```python app.py```

