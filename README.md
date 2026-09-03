# Python

## Démarrage d'un projet Python
Gérer la version de Python avec Python Manager (py)
```
py list
py install 3.13
py -3.13
py -3.13 -m venv .venv
py -3.13
```

Gérer la version de Python avec `uv`
```
uv python list
uv python install 3.12
uv python pin 3.12             # fixe/change la version pour ce projet
uv python pin --global 3.12    # version par défaut au global
uv init                        # utilise version défaut ou du fichier .python-version
uv init --python 3.12
uv init --name mon-vrai-nom-de-projet
uv init --name mon-vrai-nom-de-projet --python 3.12
```

## Gestion Projet avec uv
```
uv add <pkg>                     # ajout dépendance
uv add --dev  <pkg>              # ajout dépendance de dev
uv remove <pkg>                  # supprimer dépendance
uv sync                          # installer un projet existant
uv run <cmd>                     # 
uv tool # ex: pytest, mypy, ...
uv build
```

## Résumé des commandes
```
uv init
uv run python coucou.py
uv add jupyterlab
uv add numpy matplotlib
```
