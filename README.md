# MFT-API

Este repositorio está dedicado a la API necesaria para el proyecto
[MyFencingTrainer](https://myfencingtrainer.herokuapp.com/). Dicho proyecto
es una aplicación destinada al mundo de la esgrima, en la que podrás encontrar un entrenador virtual
el cual podrá ayudarte en las competiciones para ayudarte a tomar decisiones o bien para ayudarte
en tus entrenamientos, haciendo estos mas variados.

Para esta API hay dos endpoints ambos siendo llamadas GET. Uno de ellos destinado a levantar
la máquina puesto que por el alojamiento la primera llamada pasados treinta minutos es mas lenta.
El otro es el realmente útil. Dicho endpoint devolverá una predicción con el porcentaje
que tiene cada tirador de ganar el encuentro. A continuación se muestran ejemplos de la llamada
realizados en Debian 9.11 Stretch

# Wake Up

> curl -x GET https://mftapi.herokuapp.com/wake_up/

# Predict

> curl -X GET https://mftapi.herokuapp.com/predict/ -d "tableu=16&fencer1_age=26&fencer1_ranking=33&fencer1_handness=0&fencer1_weapon=1.0&fencer2_age=44&fencer2_ranking=99999999&fencer2_handness=0&fencer2_weapon=1.0"


Los parámetros se distinguiran por fencer1 como tirador de la derecha y fencer2 como tirador de la izquierda.
Los parámetros son los siguientes:

- tableu
  - tipo: integer
  - valores ejemplo: 16
  - descripción: Tablón en el que se enfrentan los tiradores. Este deberá ser potencia de dos (2, 4, 8, 16, ...)
- fencer1_age
  - tipo: integer
  - valores ejemplo: 26
  - descripción: Edad del tirador 1
- fencer1_ranking
  - tipo: integer
  - valores ejemplo: 33
  - descripción: Ranking del tirador 1
- fencer1_handness
  - tipo: integer
  - valores ejemplo: 0
  - descripción: Mano del tirador 1. La correspondencia de los valores es derecha -> 0 e izquierda -> 1
- fencer1_weapon
  - tipo: integer
  - valores ejemplo: 1.0
  - descripción: Arma principal del tirador 1. La correspondencia de los valores es sable -> 0, florete -> 1 y espada -> 2
- fencer2_age
  - tipo: integer
  - valores ejemplo: 44
  - descripción: Edad del tirador 2
- fencer2_ranking
  - tipo: integer
  - valores ejemplo: 9999999
  - descripción: Ranking del tirador 2
- fencer2_handness
  - tipo: integer
  - valores ejemplo: 0
  - descripción: Mano del tirador 2. La correspondencia de los valores es derecha -> 0, izquierda -> 1
- fencer2_weapon
  - tipo: integer
  - valores ejemplo: 1.0
  - descripción: Arma principal del tirador 2. La correspondencia de los valores es sable -> 0, florete -> 1 y espada -> 2
