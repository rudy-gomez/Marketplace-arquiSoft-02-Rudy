# 🏗️ Arquitectura Inicial del Sistema

## Descripción general
La arquitectura inicial se organiza en **tres capas principales**:

| Capa | Pregunta que responde |
|---|---|
| **Presentación** | ¿Cómo interactúa el usuario? |
| **Lógica de negocio** | ¿Qué hace el sistema? |
| **Datos** | ¿Dónde se almacena la información? |

Además, el módulo de **Pedidos** se integra con sistemas externos como la 
**pasarela de pago**, el **ERP** y el **servicio de envío**.
---

## Diagrama de arquitectura

![Arquitectura inicial del Marketplace](arquitectura-inicial.png)

---
---

## Diagrama de arquitectura

```mermaid
flowchart TD

    subgraph ACTORES["👥 ACTORES"]
        Cliente["Cliente"]
        Seller["Seller"]
        Admin["Administrador"]
    end

    subgraph PRESENTACION["🖥️ PRESENTACIÓN"]
        Web["Aplicación Web → API REST"]
    end

    subgraph NEGOCIO["⚙️ LÓGICA DE NEGOCIO"]
        Usuarios["Usuarios"]
        Sellers["Sellers"]
        Catalogo["Catálogo"]
        Carrito["Carrito"]
        Pedidos["Pedidos"]
    end

    subgraph DATOS["🗄️ DATOS"]
        BD["Base de datos"]
    end

    subgraph EXTERNOS["🌐 SISTEMAS EXTERNOS"]
        Pago["Pasarela de pago"]
        ERP["ERP"]
        Envio["Servicio de envío"]
    end

    ACTORES --> PRESENTACION
    PRESENTACION --> NEGOCIO
    NEGOCIO --> DATOS
    Pedidos -->|"integraciones"| EXTERNOS
```

### Vista visual de la arquitectura

<p align="center">
  <a href="marketplace-mascotas-blanco.svg">
    <img src="marketplace-mascotas-blanco.svg" alt="Arquitectura del Marketplace de mascotas: actores, presentación, lógica de negocio, datos e integraciones de Pedidos." width="100%">
  </a>
</p>

<p align="center">
  <em>Arquitectura por capas · Integraciones externas desde Pedidos</em><br>
  <a href="marketplace-mascotas-blanco.svg">Ver imagen completa</a> ·
  <a href="marketplace-mascotas.html">Versión interactiva</a>
</p>

La versión interactiva permite cambiar entre fondo claro y oscuro, ampliar y exportar el diagrama. Para utilizarla, descarga el archivo HTML y ábrelo en tu navegador.

## Justificación
La separación en capas permite aislar responsabilidades: la capa de 
presentación gestiona la interacción con el usuario, la lógica de negocio 
concentra las reglas del marketplace (catálogo, carrito, pedidos, sellers), 
y la capa de datos centraliza el almacenamiento. Esta organización responde 
directamente a los drivers de **mantenibilidad** (DA-relacionados) y facilita 
la integración con sistemas externos sin afectar el núcleo del sistema.
