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

## Justificación
La separación en capas permite aislar responsabilidades: la capa de 
presentación gestiona la interacción con el usuario, la lógica de negocio 
concentra las reglas del marketplace (catálogo, carrito, pedidos, sellers), 
y la capa de datos centraliza el almacenamiento. Esta organización responde 
directamente a los drivers de **mantenibilidad** (DA-relacionados) y facilita 
la integración con sistemas externos sin afectar el núcleo del sistema.