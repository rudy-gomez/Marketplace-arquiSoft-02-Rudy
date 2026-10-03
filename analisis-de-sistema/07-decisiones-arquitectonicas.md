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
| **ADR-003** | Estrategia de caché (Redis) | DA02 – Rendimiento | Reducir consultas repetitivas a la base de datos en la verificación de stock durante picos de concurrencia (mostrador y sitio web). | Respuestas de stock en menos de 2 segundos bajo carga pico. |
| **ADR-004** | Integración de pagos mediante interfaces y adaptadores | DA04 – Pasarela de pago | Desacoplar los casos de uso del proveedor de pagos externo, facilitando cambiarlo sin afectar el núcleo del sistema. | Contrato de pagos y adaptador para la pasarela externa. |
| **ADR-005** | Integración con ERP mediante adaptador | DA06 – Integración ERP | Desacoplar la sincronización de stock del proveedor ERP externo, evitando dependencia directa del dominio hacia ese sistema. | Adaptador de sincronización de stock con el ERP. |
| **ADR-006** | Autenticación y autorización por rol (JWT) | DA03 – Seguridad | Proteger los datos de usuarios y operaciones mediante autenticación cifrada y permisos diferenciados por rol. | Control de acceso diferenciado (Superadmin, Admin de Cadena, Admin de Pastelería, Empleado). |