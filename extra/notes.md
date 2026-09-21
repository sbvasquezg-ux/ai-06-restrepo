# Reproducción, exposición y límites de la entrega

## Estado comprobado

- Python del sistema: 3.9.6. No se utilizó para el workflow. Se activó Python **3.12.14** antes de ejecutar AppliedModelingLib.
- Entorno científico probado: NumPy 2.5.3, SciPy 1.18.1, SymPy 1.14.0, Matplotlib 3.11.2. `requirements.txt` fija mínimos compatibles; no promete reproducibilidad bit a bit con futuras versiones.
- Compilador: **LuaHBTeX 1.24.0 / TeX Live 2026**. `presentation.pdf` contiene **16 páginas**, un único deck, sin animaciones. Compilación final sin errores ni advertencias de cajas desbordadas.
- `sim.py`: verificaciones simbólicas, residuos de equilibrio y diferencias finitas aprobadas. Las figuras usan únicamente elaboración propia.
- Foto manuscrita: **pendiente**. El deck muestra el estado pendiente y la incluye automáticamente si aparece `hand/manual-verification.png` al recompilar.
- No hay una estimación causal ni calibración empírica. Las cifras pertenecen a una especialización ilustrativa.

## Salida de la simulación

```text
SymPy: PASS (B9-B10, reinstatement, sigma=1 limit, exact K threshold, household supply)
Domains: W,R,B,gamma>0; 0<sL<1; s,epsilon>0; 0<I<1 in the closed form.
s=1.5, K=1, I=0.1: W=3.50487439, sL=0.86164426, P=1.58645924, D=0.93903921, dlnW/dI=0.64742003
s=1.5, K=1, I=0.3: W=3.58584865, sL=0.72264399, P=0.42335908, D=0.72131793, dlnW/dI=-0.29795885
s=1, K=0.5, I=0.1: W=3.14456563, sL=0.90000000, P=1.35675765, D=1.05555556, dlnW/dI=0.30120210
s=0.7, K=0.5, I=0.12: W=3.08378260, sL=0.89190367, P=1.34577591, D=1.39857122, dlnW/dI=-0.05279531
Numerical residual/finite-difference checks: PASS; maximum checked error=3.837e-10
Default: B=1, eta=0, sigma=1.5, A=2, N=1, K=1, theta=1, nu=L^2/2
Wage turning point I=0.22116206; adoption threshold I*=0.42013628
Figures regenerated: extra/figures/displacement-productivity.pdf and .png
```

## Lean: alcance real y error de traducción

Clone fuente del workflow: <https://github.com/nikhgarg/AppliedModelingLib>, commit `2db7d108cd3a2cb10148974bb2a77856e7d87428`. Se usó la skill `skills/econcs-formalizer/SKILL.md`, con el prompt de la usuaria y contexto técnico de rutas/runtime. Modelo del subagente: **GPT-5.6 Sol (`gpt-5.6-sol`), xhigh**. Toolchain: **Lean 4.30.0-rc2**. Se reutilizaron dependencias y cachés de compilación ya instaladas; no se copió una formalización de otro trabajo.

El agente produjo su propio scaffold y dos endpoints. Se interrumpió por límite de uso antes de concluir el registro de estado, el mapa de fuente y las revisiones independientes. Por eso el README generado todavía dice `Not started`, hay texto de plantilla en `status.json`, no hay informe final ni DAG certificado y no se ha realizado cierre v11. **No se editaron esos archivos para que parecieran completos.**

La compilación estrecha real del módulo completo produjo:

```text
Build completed successfully (8316 jobs).
```

El check pedido terminó con **exit code 0**. La salida literal, sin convertirla en una certificación más amplia, está en `lean/CHECK_OUTPUT.txt`. Para este scaffold incompleto, el comando ejecutó únicamente `lake build +AR18RaceManMachine.PaperInterface` y `git diff --check`. No revisó correspondencia económica ni cerró el inventario. Un primer intento local de check no encontró `lake` en PATH; se corrigió activando `.elan/bin` y se guardó la salida del intento final. No fue un fallo de Python 3.12.

### Qué encontró la inspección posterior

Al contrastar el código generado con **NBER rev. 2017, Prop. 2, p. 11**, aparecen estas diferencias:

| Objeto | PDF verificado | Código literal generado |
|---|---|---|
| Efecto relativo de automatizar | $-\Lambda_I/(\widehat\sigma+\varepsilon_L)$ | `-1 / (sigmaHat + epsilonL * lambdaI)` |
| Efecto relativo de nuevas tareas | $\Lambda_N/(\widehat\sigma+\varepsilon_L)$ | `1 / (sigmaHat + epsilonL * lambdaN)` |
| Elasticidad libre | $\widehat\sigma+\Lambda_I/\varepsilon_\gamma$ | `sigmaHat + 1 / (epsilonGamma * lambdaI)` |

Aunque los signos compilados coinciden para parámetros positivos, **las funciones son diferentes**. El compilador prueba las funciones escritas, no las fórmulas del PDF. Por tanto, `proposition2ComparativeStaticsCore` no recibe crédito de correspondencia con Prop. 2. Es un error de traducción del agente, no del paper.

`proposition3WageRentalDecomposition` toma reales `laborShare`, `productivityI`, `productivityN`, `relativeI`, `relativeN` y presupone sus signos. Comprueba consecuencias algebraicas de `wageChange = productivity + (1-laborShare)*relativePriceChange`, incluyendo la implicación salarial mostrada en la diapositiva. **No** representa derivadas de funciones de equilibrio ni prueba que Assumptions 1–3 generen los coeficientes. El bloque de Prop. 3 no llama al bloque erróneo de Prop. 2 para construir sus variables: esos números entran como parámetros.

Esta inspección es una observación externa a la copia y **no sustituye** los juicios independientes ni los recibos del protocolo. No se ha fabricado una auditoría en `lean/audit/`. No hay prueba completa de Props. 1–6, dinámica, equilibrio de esquina ni umbral de capital.

### Integridad de la copia y archivos ignorados

Se copió el directorio entero `papers/AR18RaceManMachine/` a `lean/` después de guardar la salida del check. Se compararon nombres y SHA-256 de **23 archivos**: coincidencia exacta. El manifiesto técnico se conserva localmente fuera del repositorio. Se ejecutó `git add lean/` sin `-f`. La revisión global de espacios señala una línea vacía final en `lean/PAPER_NOTES.md:29`; se conserva para respetar la copia literal. El check del workflow no la detectó porque ese archivo aún no estaba incorporado a su índice Git.

Archivos presentes en la copia local y excluidos por su propio `.gitignore`:

```text
lean/source/paper.pdf
lean/source/source.txt
```

`repository_visibility: private_only` es el valor por defecto del scaffold conservado. La publicación de esta copia de curso fue expresamente solicitada por la usuaria; no significa que AppliedModelingLib haya aprobado un release o un cambio de estado. El paper y sus textos fuente no se publican.

El directorio copiado no es un proyecto Lean autónomo: importa Mathlib y requiere el clone de AppliedModelingLib, su archivo raíz `papers/AR18RaceManMachine.lean` y la entrada de `lakefile.toml` generados por el workflow. Para reproducir ese run, partir del commit indicado, activar Python >=3.11 y el toolchain Lean, ejecutar el mismo prompt/workflow y conservar el scaffold generado. El comando `check` del README se ejecuta en ese clone; no basta entrar en `lean/`.

### Bloqueos para continuar

1. Reanudar el workflow con el modelo requerido cuando vuelva a estar disponible.
2. Corregir **dentro del workflow**, no sobre la copia entregada, las tres fórmulas de `PaperInterface.lean` de Prop. 2 y reconstruir sus pruebas.
3. Conectar los parámetros algebraicos de Prop. 3 con derivadas de equilibrio y todas sus condiciones, o mantener explícitamente el alcance parcial.
4. Actualizar inventario/estado y ejecutar revisiones independientes y cierre del protocolo. Repetir el check, copiar nuevamente la carpeta completa y actualizar el deck.

## Guion para 20 minutos

| Diapositiva | Minutos | Trabajo que debe explicar la estudiante |
|---|---:|---|
| 1 | 0.50 | Fuente fijada y pregunta |
| 2 | 0.75 | Salario, participación y empleo son objetos distintos |
| 3 | 1.00 | Factibilidad frente a adopción |
| 4 | 1.00 | Qué supuesto firma cada paso |
| 5 | 1.00 | Tabla de signos con regímenes |
| 6 | 1.50 | Diferenciar demanda relativa y participación |
| 7 | 1.50 | Resolver (B9)–(B10) |
| 8 | 1.50 | Explicar $P_I>D_I$ |
| 9 | 1.00 | Diferenciar reinstalación de productividad |
| 10 | 1.25 | Leer la figura y el cambio de régimen |
| 11 | 1.25 | Frontera, dominio y comprobación numérica |
| 12 | 1.25 | Capital fijo frente a ajuste de largo plazo |
| 13 | 1.25 | Esquina y límites de la clasificación |
| 14 | 1.50 | Condiciones de autocorrección |
| 15 | 2.00 | Lean, error de traducción y frontera de verificación |
| 16 | 1.75 | Derivación manuscrita y veredicto |
| **Total** | **20.00** | |

## Fragilidades que deben revisarse antes del merge

- **Lean:** check 0 y build 0 no acreditan el modelo. Hay un error de traducción confirmado y el run está incompleto.
- **Esquina y crecimiento:** distinguir el crecimiento de la senda tecnológica candidata del crecimiento AK y no leer $\rho_c(g)$ como umbral numérico independiente de $g$. Revisar NBER pp. 16–18 y prueba p. 43.
- **Versiones:** las cláusulas sobre el umbral $K$ cambian entre NBER p. 13 y AER p. 1502. La condición central aquí es $P_I>D_I$; el umbral cerrado de `extensions.md` corresponde solo a nuestra especialización.
- **Representatividad:** preferencias específicas, tareas ordenadas e innovación con científicos escasos no son evidencia de autocorrección universal en economías reales.
- **Foto:** realizar la derivación de `hand/README.md`, fotografiarla, añadirla y recompilar. El deck actual no satisface todavía el requisito de una foto auténtica en pantalla.

## Git y entrega

`main` conserva el commit inicial. El trabajo se propone en `feat/repo-6` mediante PR. El merge y el comentario en el issue quedan a cargo de la estudiante. La carpeta de trabajo contiene el PDF local del paper, pero ese archivo no forma parte del commit.
