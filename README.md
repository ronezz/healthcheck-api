#  HealthCheck API 

HealthCheck API es una aplicación sencilla en Flask que expone el estado del sistema (CPU, RAM, disco, uptime y servicios simulados) mediante una API REST. 

Este proyecto tiene como objetivo demostrar el uso de herramientas DevOps esenciales como Docker, Terraform y AWS EC2, automatizando el despliegue de una API y exponiéndola públicamente mediante el mapeo de puertos
---

## Tecnologías utilizadas

- **Python 3.12 + Flask**
- **Docker**
- **Terraform**
- **AWS EC2**
- **Shell**
- **Git**

---

## Estructura del proyecto

```
healthcheck-api/
├── app/
│   ├── main.py
│   ├── utils.py
│   └── requirements.txt
├── Dockerfile
├── terraform/
│   ├── main.tf
│   ├── outputs.tf
│   └── init.sh
└── README.md
```

---

##  Docker

### Construcción manual:
```bash
docker build -t healthcheck-api .
```

### Ejecución:
```bash
docker run -d -p 80:5000 --name healthcheck_api healthcheck-api
```

> La API estará disponible en: http://localhost/health

---

## ☁️ Despliegue en AWS EC2 con Terraform

### Requisitos previos:
- Cuenta en AWS
- AWS CLI configurado (`aws configure`)
- Clave SSH generada (`ssh-keygen -t rsa -f ~/.ssh/healthcheck-key`)

### Pasos:

1. Entra en la carpeta `terraform/`
2. Sustituye la clave pública por la tuya en el bloque `aws_key_pair` de `main.tf`:
   ```hcl
   public_key = file("~/.ssh/tu-clave-publica.pem")
   ```
3. Ejecuta:

```bash
terraform init
terraform apply
```

4. Copia la IP pública mostrada al que devuelve Terraform y accede a:

```
http://<IP_PUBLICA>/health
```

---

##  Endpoint

```http
GET /health – Devuelve un JSON con:
- Porcentaje de CPU utilizado
- Porcentaje de memoria RAM
- Porcentaje de uso del disco
- Tiempo de actividad del sistema (uptime)
- Estado simulado de servicios (`nginx`, `mysql`)
```
