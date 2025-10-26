# Comandos Git para Ejecutar Manualmente

## ⚠️ IMPORTANTE

Los comandos de shell en el IDE de Cursor no están capturando output. Debes ejecutarlos **manualmente en tu terminal**.

## 📋 Pasos a Seguir

### 1. Abrir Terminal

Abre tu terminal (Terminal.app o iTerm) y ejecuta:

```bash
cd /Users/joseassizalcarazbaxter/Developer/iphone/app
```

### 2. Verificar Estado Actual

```bash
# Ver si .git existe
ls -la .git

# Ver estado de git (si existe)
git status
```

### 3. Si NO existe .git - Inicializar Repositorio

```bash
# Inicializar git
git init

# Configurar rama main
git branch -M main

# Agregar todos los archivos
git add .

# Crear commit inicial
git commit -m "WIP: Initial commit - Project structure with sensors, communication, 47 tests (89% coverage)"

# Configurar remote
git remote add origin git@github.com:assizalcaraz/openFramework_iOS.git

# Push a GitHub
git push -u origin main
```

### 4. Si SÍ existe .git - Actualizar

```bash
# Agregar cambios
git add .

# Crear commit
git commit -m "WIP: Update project structure, documentation, and tests"

# Push
git push origin main
```

### 5. Verificar que Funcionó

```bash
# Ver commits
git log --oneline -5

# Ver remotes
git remote -v

# Ver ramas
git branch -a

# Ver estado
git status
```

## ✅ Después del Push

1. Ir a GitHub: https://github.com/assizalcaraz/openFramework_iOS
2. Verificar que el código está ahí
3. Eliminar archivos temporales: `ESTADO_GIT.md`, `DIAGNOSTICO_SHELL.md`, `COMANDOS_GIT.md`
4. Continuar con desarrollo

## 🎯 Próximos Pasos

Después de tener git configurado:

```bash
# Para futuros commits
git add .
git commit -m "WIP: Descripción del cambio"
git push origin main
```

Siéntete libre de ajustar los mensajes de commit según tus necesidades, pero mantén el prefijo "WIP:" según la METODOLOGIA_DESARROLLO.md.

