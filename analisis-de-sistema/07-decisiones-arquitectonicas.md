# 📋 Decisiones Arquitectónicas (ADR)

## Objetivo
Documentar las decisiones arquitectónicas importantes tomadas para responder 
a los drivers identificados, junto con su justificación. 

**ADR (Architecture Decision Record)** = Registro de Decisión Arquitectónica.

---

| ID | Decisión arquitectónica | Driver relacionado | Justificación | Resultado |
|---|---|---|---|---|
| **ADR-001** | Monolito modular con escalamiento horizontal | DA01 – Escalabilidad, DA07 – Mantenibilidad | Organizar las funcionalidades en módulos independientes dentro de una misma aplicación desplegable, permitiendo agregar instancias detrás de un balanceador de carga a medida que crece la cadena. | Módulos de Cuentas, Catálogo, Traslados, Turnos/Caja, Ventas y Reportes. |
| **ADR-002** | Clean Architecture | DA07 – Mantenibilidad | Separar las reglas del negocio (ej. control de stock, cierre de caja) de los detalles tecnológicos (BD, framework), evitando que cambios externos afecten el núcleo del sistema. | Capas de Dominio, Aplicación, Infraestructura y Presentación. |
| **ADR-003** | Caché (Redis) + Pool de conexiones (PgBouncer) | DA02 – Rendimiento | Reducir consultas repetitivas a PostgreSQL en la verificación de stock, y evitar el agotamiento de conexiones bajo picos de venta simultánea (mostrador + web). | Respuestas de stock en menos de 2 segundos bajo carga pico. |
| **ADR-004** | Bloqueo transaccional con reserva temporal (TTL) | DA-Concurrencia (control de stock) | Garantizar que un mismo producto no se comprometa en dos ventas/pedidos simultáneos, usando `SELECT ... FOR UPDATE` y liberación automática de reservas abandonadas. | Consistencia del stock entre canal mostrador y canal web. |
| **ADR-005** | Aislamiento multi-tenant por `tenant_id` | DA04 – Seguridad multi-tenant | Mantener los datos de cada pastelería/cadena lógicamente aislados dentro de la misma base de datos, sin duplicar infraestructura por cliente. | Separación de datos entre cuentas sin visibilidad cruzada. |
| **ADR-006** | Réplica de lectura para reportes | Rendimiento / separación de cargas | Aislar las consultas pesadas de reportes de la carga transaccional principal (ventas, caja), evitando que afecten el rendimiento de la operación diaria. | Reportes consolidados sin impactar las transacciones de venta. |