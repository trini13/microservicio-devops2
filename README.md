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

---

## Reflexión Personal

Durante el desarrollo de este encargo aprendímos a crear un repositorio en GitHub con 4 ramas: `main`, que es la rama principal donde se encuentra el producto en producción; `develop`, donde se realizan los cambios e integraciones; `feature/agregar-endpoint`, donde agregamos nuevas funcionalidades al código; y `hotfix`, que se usa para corregir errores urgentes directamente desde `main`.

Tuve un problema de credenciales, ya que mi PC tenía asociada otra cuenta de GitHub. Lo resolví eliminando las credenciales guardadas en el Administrador de credenciales de Windows y volviendo a autenticarme con mi cuenta correcta.

También aprendimos a crear Pull Requests, donde se comparan los cambios entre ramas y se hace el merge para integrarlos. Creamos los archivos base del microservicio: `app.py`, que contiene la aplicación Flask; `requirements.txt`, con las dependencias; y `.gitignore`, para excluir archivos innecesarios. El archivo `README.md` funciona como la portada del repositorio, donde se documenta todo el proyecto para que cualquier persona del equipo pueda entender cómo está organizado y cómo trabajar en él. Además configuramos el pipeline CI/CD creando la carpeta `.github/workflows/` con el archivo `ci.yml`, que se ejecuta automáticamente con cada push a `develop`.

Aprendimos comandos como `git clone`, `git checkout`, `git add`, `git commit` y `git push`. Aunque aún no los manejamos a la perfección, entendimos conceptos que desconociamos y siento que avanzamos bastante en este tema.

Este encargo lo realicé en conjunto con mi compañero Sebastián Antipán. nos coordinamos a través de Discord para organizar el trabajo, resolver dudas y avanzar juntos en cada etapa del repositorio.


---
## 🛠️ Guía de Buenas Prácticas (Contribución de Seba)

Para cumplir con los estándares de calidad del proyecto, definimos:

* **Estrategia de Ramificación:** Usamos **GitFlow** para asegurar trazabilidad.
* **Naming de Ramas:** * `feature/` para nuevas funciones.
    * `hotfix/` para errores en producción.
* **Convención de Commits:** Usamos el formato `tipo: descripción` (ej. `feat: agregar validación`).
* **Revisión de Código:** Todo cambio a `main` debe pasar por un **Pull Request**.

## 📝 Reflexión Personal - Seba
En esta actividad, aprendí a entender cómo trabajar de forma colaborativa sin pisar el código de mi compañero mediante el correcto uso de repositorios GitHub. Al principio me costó entender el flujo de ramas, pero logré crear mi propia rama feature para añadir la documentación técnica y las buenas prácticas. Esto me hizo comprender la importancia de la comunicación y el orden en los commits a la hora de trabajar en equipo, para que todo funcione bien y el pipeline no encuentre errores innecesarios.