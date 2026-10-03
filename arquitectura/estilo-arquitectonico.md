# 🏛️ Estilo Arquitectónico

## Objetivo
Definir la forma global de organización y despliegue del sistema, 
respondiendo a los drivers arquitectónicos identificados en la Guía 02.

---

## Estilo seleccionado: Monolito Modular con Escalamiento Horizontal

| Aspecto | Descripción |
|---|---|
| **Unidad de despliegue** | Una sola aplicación backend, un solo proceso Node.js/Express |
| **Organización interna** | Módulos independientes por responsabilidad (Usuarios, Sellers, Catálogo, Carrito, Pedidos) |
| **Escalamiento** | Horizontal — se agregan instancias adicionales del mismo monolito |
| **Comunicación entre módulos** | Interna, mediante llamadas directas a servicios (no hay red entre módulos) |
| **Base de datos** | PostgreSQL compartida, con acceso centralizado mediante ORM (Sequelize) |

---

## Diagrama de arquitectura

![Estilo arquitectónico del Marketplace — Monolito modular en capas](estilo-arquitectonico.png)

---

## Reglas de la arquitectura
1. Cada capa solo invoca a la capa inmediatamente inferior.
2. Un módulo no accede al repositorio ni a las tablas de otro módulo.
3. La comunicación entre módulos se hace llamando a su service.
4. Todo se ejecuta en un único proceso Node.js con una única base de datos.