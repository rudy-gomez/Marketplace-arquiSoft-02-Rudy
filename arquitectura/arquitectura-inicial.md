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
    DATOS -->|"integraciones"| EXTERNOS
```

## Justificación
La separación en capas permite aislar responsabilidades: la capa de 
presentación gestiona la interacción con el usuario, la lógica de negocio 
concentra las reglas del marketplace (catálogo, carrito, pedidos, sellers), 
y la capa de datos centraliza el almacenamiento. Esta organización responde 
directamente a los drivers de **mantenibilidad** (DA-relacionados) y facilita 
la integración con sistemas externos sin afectar el núcleo del sistema.