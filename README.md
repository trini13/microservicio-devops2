# Microservicio DevOps - EP1

Repositorio creado para la Evaluación Parcial 1 de Ingeniería DevOps (DOY0101).

## Descripción

API REST desarrollada en Python/Flask como base para implementar prácticas DevOps con Git, GitHub y GitHub Actions.

---

## Modelo de Ramificación: GitFlow

Se eligió **GitFlow** porque:
- Separa claramente el código en producción (`main`) del código en desarrollo (`develop`)
- Las ramas `feature/` permiten trabajar en funcionalidades sin afectar al resto del equipo
- Las ramas `hotfix/` permiten corregir errores urgentes en producción sin detener el desarrollo
- Es compatible con pipelines CI/CD automatizados por rama

### Comparación de modelos

| Modelo | Ramas principales | Ideal para |
|--------|-------------------|------------|
| **GitFlow** | main, develop, feature, hotfix | Proyectos con versiones planificadas |
| **GitHub Flow** | main + feature | Entrega continua, equipos pequeños |
| **Trunk-Based** | main | Equipos maduros con CI/CD completo |

---

## Convenciones del Repositorio

### Naming de Ramas

| Tipo | Formato | Ejemplo |
|------|---------|---------|
| Funcionalidad nueva | `feature/<descripcion>` | `feature/agregar-login` |
| Corrección urgente | `hotfix/<descripcion>` | `hotfix/corregir-error-404` |
| Producción | `main` | — |
| Desarrollo | `develop` | — |

### Mensajes de Commit

Se usa la convención **Conventional Commits**:



| Tipo | Cuándo usarlo |
|------|--------------|
| `feat` | Nueva funcionalidad |
| `fix` | Corrección de bug |
| `docs` | Cambios en documentación |
| `ci` | Cambios en configuración CI/CD |
| `hotfix` | Corrección urgente en producción |

### Estructura de Carpetas
microservicio-devops2/
├── .github/
│ └── workflows/
│ └── ci.yml
├── app.py
├── requirements.txt
├── .gitignore
└── README.md


### Flujo de Merge

1. Crear rama `feature/` desde `develop`
2. Desarrollar y hacer commits
3. Abrir Pull Request hacia `develop`
4. Revisión y merge
5. Los `hotfix/` se crean desde `main` y se mergean a `main` y `develop`

---

## GitHub Actions - Pipeline CI/CD

El archivo `.github/workflows/ci.yml` se ejecuta automáticamente:
- En cada `push` a `develop`
- En cada `pull request` hacia `main`

**¿Qué hace el pipeline?**
1. Clona el repositorio
2. Instala Python 3.11
3. Instala las dependencias
4. Verifica que la app funciona correctamente
5. Muestra mensaje de éxito

**Rol en CI/CD:**
- **CI (Integración Continua):** Detecta errores automáticamente con cada push
- **CD (Despliegue Continuo):** Base para automatizar despliegues a entornos cloud

---

## Trazabilidad de Commits

| Commit | Rama | Descripción |
|--------|------|-------------|
| `feat: agregar microservicio base Flask` | develop | Código inicial |
| `feat: agregar endpoint de informacion del servicio` | feature/agregar-endpoint-saludo | Ruta `/info` |
| `feat: agregar endpoint de estado del servicio` | feature/agregar-version | Ruta `/estado` |
| `hotfix: agregar manejo de error 500` | hotfix/corregir-error-404 | Manejo de errores |
| `ci: configurar pipeline GitHub Actions` | develop | Automatización CI/CD |

---

## Declaración de uso de IA

Se utilizó Perplexity AI como apoyo para revisar estructura de archivos YAML y formato Markdown.
Todas las decisiones técnicas fueron revisadas y validadas por el equipo.
Referencia: https://bibliotecas.duoc.cl/ia
