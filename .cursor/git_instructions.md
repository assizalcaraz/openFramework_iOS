# Git Instructions for Cursor IDE

## ⚙️ Configuración Git

Cursor IDE tiene integración nativa de Git. Para gestionar el repositorio:

### Estado Actual

**Directorio**: `/Users/joseassizalcarazbaxter/Developer/iphone/app`
**Repositorio**: Necesita inicialización
**Remote**: `git@github.com:assizalcaraz/openFramework_iOS.git`

## 📋 Pasos en Cursor IDE

### 1. Abrir Source Control Panel
- Presiona `Cmd+Shift+G` (macOS) para abrir Source Control
- O haz clic en el icono de Git en la barra lateral izquierda

### 2. Inicializar Repositorio (si no existe)

En la terminal integrada de Cursor (`Cmd+` ~ ``):
```bash
cd /Users/joseassizalcarazbaxter/Developer/iphone/app
git init
git branch -M main
```

### 3. Agregar Archivos

En Source Control Panel:
- Haz clic en el botón "+" para stage changes
- O usa `git add .` en terminal

### 4. Crear Commit

En Source Control Panel:
- Escribe mensaje de commit: `WIP: Initial commit - Project structure`
- Presiona `Cmd+Enter` o clic en "✓"

### 5. Configurar Remote

En terminal:
```bash
git remote add origin git@github.com:assizalcaraz/openFramework_iOS.git
```

### 6. Push

En Source Control Panel:
- Presiona "..." (tres puntos)
- Selecciona "Push" o "Push to"
- Selecciona "origin" y rama "main"

## 🎯 Comandos Rápidos en Terminal de Cursor

Abre terminal en Cursor (`Cmd+` ~ ``) y ejecuta:

```bash
cd /Users/joseassizalcarazbaxter/Developer/iphone/app
git status
git add .
git commit -m "WIP: Initial commit - Project structure with sensors, communication, 47 tests"
git remote add origin git@github.com:assizalcaraz/openFramework_iOS.git
git push -u origin main
```

## ✅ Verificar

En Cursor IDE, abre Source Control (`Cmd+Shift+G`) y verás:
- Estado de archivos modificados
- Branches disponibles
- Remote configurado

## 📝 Workflow Futuro

Para commits futuros en Cursor:
1. Modifica archivos
2. Presiona `Cmd+Shift+G` (Source Control)
3. Agrega archivos (botón "+")
4. Escribe mensaje de commit
5. Presiona `Cmd+Enter` para commit
6. Push desde menú "..."

