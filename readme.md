
## Projekt Inżynieria Oprogramowania ISI2 - Desktopowa aplikacja z informacjami pogodowymi

* Witold Nowogórski
* Adam Pliszka
* Kaja Dzielnicka
* Bartłomiej Stępniewski
  
============================================================================================================

├ src     #folder źródłowy
   └── location     
          ├── location_request.py   # łączenie z google geolocation api -> zapisywanie odpowiedzi do loc.json
          └── loc.json              # plik json przechowujący informacje o lokalizacji użytkownika 
          

 ### Struktura aplikacji 
 
 Aplikacja określa lokalizacje poprzez zewnętrzne api, następnie dla tej lub podanej przez użytkownika miejscowości z pomocą kolejnego api pobiera informacje pogodowe, które zostają odpowiednio przetworzone i wyświetlone w oknie aplikacji
 
 ![app structure diagram](https://github.com/witek3100/Weather-app-IO/blob/master/app_structure_diagram.png)
 
 ### Główne interfejsy
