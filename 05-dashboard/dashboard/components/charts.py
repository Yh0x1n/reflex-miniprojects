"""Componentes de visualización para el Dashboard interactivo.

Proporciona funciones helper que retornan componentes Reflex
para construir un dashboard de métricas y gráficos.
"""

import reflex as rx


def stat_card(label: str, value: str, color: str) -> rx.Component:
    """Tarjeta de métrica individual.

    Renderiza un rx.card con una etiqueta, un valor destacado
    y un color de acento para la etiqueta.

    Args:
        label: Texto descriptivo de la métrica (ej. "Ventas totales").
        value: Valor a mostrar (ej. "$12,400").
        color: Color de acento para la etiqueta (ej. "blue").

    Returns:
        Un componente rx.card listo para usar en el dashboard.
    """
    return rx.card(
        rx.vstack(
            rx.text(label, font_size="0.875rem", color=color, weight="medium"),
            rx.heading(value, font_size="1.75rem", weight="bold"),
            spacing="0.25em",
            align="center",
        ),
        padding="1.5em",
        width="100%",
        box_shadow="sm",
    )


def bar_chart(
    data: list[dict[str, str | float]], title: str = ""
) -> rx.Component:
    """Gráfico de barras horizontal renderizado con primitivas Reflex.

    Cada ítem en `data` debe tener las claves "label" (str)
    y "value" (float). La barra se escala proporcionalmente
    al valor máximo del conjunto.

    Args:
        data: Lista de diccionarios con "label" y "value".
              Ejemplo: [{"label": "Ene", "value": 4000}, ...]
        title: Título opcional del gráfico.

    Returns:
        Un componente rx.vstack con las barras horizontales.
    """
    if not data:
        return rx.text("No hay datos disponibles.", font_size="0.875rem")

    max_val = max(item["value"] for item in data)

    bars = []
    for item in data:
        label = item["label"]
        value = float(item["value"])
        pct = (value / max_val * 100) if max_val > 0 else 0

        bar = rx.hstack(
            rx.text(str(label), width="6em", font_size="0.875rem"),
            rx.box(
                width=f"{pct:.1f}%",
                height="1.5rem",
                background_color=rx.color("accent", 5),
                border_radius="4px",
                _hover={
                    "background_color": rx.color("accent", 7),
                },
            ),
            rx.text(str(value), font_size="0.875rem", color_scheme="gray"),
            spacing="0.75em",
            align="center",
            width="100%",
        )
        bars.append(bar)

    return rx.vstack(
        rx.heading(title, font_size="1.25rem", weight="semibold")
        if title
        else rx.fragment(),
        rx.vstack(*bars, spacing="0.5em", width="100%"),
        spacing="1em",
        width="100%",
    )
