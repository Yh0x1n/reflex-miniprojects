# Reflex Mini-Projects

5 miniproyectos progresivos para aprender
los componentes básicos de Reflex.

Cada proyecto es un esqueleto completo de Reflex listo para ejecutar. El
archivo principal de la app contiene **solamente un docstring** con el
enunciado del ejercicio y la lista de componentes a utilizar — los
estudiantes escriben el código.

## Proyectos

| # | Proyecto | Conceptos |
|---|----------|-----------|
| 01 | **Counter** — Contador básico | `rx.State`, eventos increment/decrement/reset, `rx.button`, `rx.text`, `rx.heading`, layout con `rx.hstack` / `rx.vstack` / `rx.center` |
| 02 | **Todo** — Lista de tareas | `rx.State`, `rx.input`, `rx.checkbox`, `rx.foreach`, `rx.cond`, add/toggle/delete items, `rx.Base` |
| 03 | **Calculator** — Calculadora | `rx.State`, eventos con argumentos, operaciones aritméticas, display dinámico con `rx.text` |
| 04 | **Form Validation** — Validación de formularios | `rx.form`, validación de campos, `rx.cond` para errores, estados de carga |
| 05 | **Dashboard** — Tablero con gráficos | `ChartState`, `rx.foreach`, módulo `components/` reutilizable, visualización de datos |

## Requisitos

- Python 3.10 o superior
- Reflex ≥ 0.6.0
- Pip o UV para manejo de dependencias y entorno virtual

## Uso

```bash
# 1. Clonar el repositorio
git clone https://github.com/Yh0x1n/reflex-miniprojects
cd reflex-miniprojects

# 2. Entrar a un proyecto e instalar dependencias
cd 01-counter
pip install -r requirements.txt

# 3. Ejecutar la app
reflex run
```

Cada proyecto es independiente — no es necesario instalar dependencias
a nivel del repositorio raíz.

## Estructura

```
reflex-miniprojects/
├── .gitignore
├── README.md
├── requirements.txt
├── 01-counter/
│   ├── rxconfig.py
│   ├── requirements.txt
│   ├── counter/
│   │   ├── __init__.py
│   │   └── counter.py      ← ¡completar!
│   └── assets/
├── 02-todo/
│   ├── rxconfig.py
│   ├── requirements.txt
│   ├── todo/
│   │   ├── __init__.py
│   │   └── todo.py         ← ¡completar!
│   └── assets/
├── 03-calculator/
├── 04-form-validation/
└── 05-dashboard/
```

## Licencia

Educativa — uso libre para fines de aprendizaje.
