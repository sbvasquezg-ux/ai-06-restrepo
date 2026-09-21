# Reproducción, exposición y límites de la entrega

## Estado comprobado

- Python del sistema: 3.9.6. No se utilizó para el workflow. Se activó Python **3.12.14** antes de ejecutar AppliedModelingLib.
- Entorno científico probado: NumPy 2.5.3, SciPy 1.18.1, SymPy 1.14.0, Matplotlib 3.11.2. `requirements.txt` fija mínimos compatibles; no promete reproducibilidad bit a bit con futuras versiones.
- Compilador: **LuaHBTeX 1.24.0 / TeX Live 2026**. `presentation.pdf` contiene **16 páginas**, un único deck, sin animaciones. Compilación final sin errores ni advertencias de cajas desbordadas.
- `sim.py`: verificaciones simbólicas, residuos de equilibrio y diferencias finitas aprobadas. Las figuras usan únicamente elaboración propia.
- Foto manuscrita: **recibida el 21 de septiembre de 2026**, copiada sin retoques e incluida en la diapositiva 16. Su caso fija trabajo; `hand/README.md` y el deck explican sus condiciones y matizan dos frases demasiado generales.
- Integridad de la foto: SHA-256 `245e8683c22d18b88a88be085e62707b4168669be776fd8304f3ba4419b57a5c`, idéntico al adjunto de la estudiante.
- No hay una estimación causal ni calibración empírica. Las cifras pertenecen a una especialización ilustrativa.

## Salida de la simulación

```text
Handwritten fixed-L audit: PASS (wage, labor share, general-form equivalence, sigma=1 limit)
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

El primer run quedó interrumpido por límite de uso. El 21 de septiembre se reanudó el mismo workflow con el modelo requerido: se corrigieron las fórmulas, se reconstruyeron las pruebas y se actualizaron el estado y la documentación. El estado canónico de la copia final es **`partially formalized`**. El informe generado se conserva en [`lean/PARTIAL_FORMALIZATION_REPORT.md`](../lean/PARTIAL_FORMALIZATION_REPORT.md).

La compilación del módulo completo produjo `Build completed successfully (8316 jobs).` con **exit code 0**. El check pedido también terminó con **exit code 0**; su salida literal está en `lean/CHECK_OUTPUT.txt`. La salida del check rápido enumera `lake build +AR18RaceManMachine.PaperInterface` y `git diff --check`; entre ambos, el script también comprueba aislamiento de dependencias mediante el grafo de módulos Lean. Ese control no certifica correspondencia económica con el PDF. Un primer intento histórico no encontró `lake` en PATH; se corrigió activando `.elan/bin`. No fue un fallo de Python 3.12.

### Qué se corrigió dentro del workflow

La inspección inicial contra **NBER rev. 2017, Prop. 2, p. 11** encontró tres traducciones incorrectas. Se repararon en AppliedModelingLib, no sobre la copia de entrega:

| Objeto | Fórmula corregida y verificada en el PDF | Lean final |
|---|---|---|
| Efecto relativo de automatizar | $-\Lambda_I/(\widehat\sigma+\varepsilon_L)$ | `-lambdaI / (sigmaHat + epsilonL)` |
| Efecto relativo de nuevas tareas | $\Lambda_N/(\widehat\sigma+\varepsilon_L)$ | `lambdaN / (sigmaHat + epsilonL)` |
| Elasticidad libre | $\widehat\sigma+\Lambda_I/\varepsilon_\gamma$ | `sigmaHat + lambdaI / epsilonGamma` |

La primera copia compilaba fórmulas distintas. Ese fue un error de traducción del agente, no del paper; la compilación sola no lo detectaba. La copia final reemplaza aquella versión con el directorio entero regenerado.

### Resultado de la revisión independiente

Un revisor aislado examinó el inventario de la fuente completa y volvió a inspeccionar visualmente la página 11; corrigió también una lectura inicial equivocada de los paréntesis en su propio diagnóstico. Otro revisor, sin contexto de autoría, contrastó los pasajes pertinentes y los tres módulos completos. Su revisión acotada produjo:

- **2** juicios `matches_selected_algebraic_atom`: las dos pruebas coinciden con sus fragmentos algebraicos seleccionados.
- **2** juicios `not_covered`: ninguna prueba equivale a la proposición completa correspondiente.
- **0** discrepancias en los fragmentos revisados.

Son diagnósticos independientes, **no recibos aceptados del protocolo global**. El informe generado distingue expresamente esas categorías. No hay un grafo de obligaciones aceptado, panel adversarial final ni certificado de cierre; el planner además solicita registrar la transición local de `lakefile.toml`. Resolver ese paso mecánico no probaría los resultados económicos aún ausentes.

`proposition2ComparativeStaticsCore` prueba signos de expresiones cuyos argumentos positivos se suministran como números reales. No define las integrales que generan $\Lambda_I,\Lambda_N$, ni conecta las expresiones con derivadas del equilibrio, regímenes de adopción, empleo o participación.

`proposition3WageRentalDecomposition` toma reales `laborShare`, `productivityI`, `productivityN`, `relativeI`, `relativeN` y presupone sus signos. Comprueba consecuencias de `wageChange = productivity + (1-laborShare)*relativePriceChange`, incluida la implicación salarial del deck. **No** representa derivadas de funciones de equilibrio ni demuestra que Assumptions 1–3 generen los coeficientes. Tampoco prueba el umbral de capital ni la existencia de una economía que realice cada rama de signo. Las otras proposiciones del paper permanecen fuera de esta formalización parcial.

### Integridad de la copia y archivos ignorados

Se copia íntegramente `papers/AR18RaceManMachine/` a `lean/` después del último check, verificando nombres y SHA-256 de los **25 archivos**: coincidencia exacta. De ellos, 23 quedan versionados y 2 fuentes permanecen ignoradas. El manifiesto técnico se conserva localmente fuera del repositorio. Se ejecuta `git add lean/` sin `-f`. Los archivos presentes localmente y excluidos por el `.gitignore` del workflow son:

```text
lean/source/paper.pdf
lean/source/source.txt
```

El valor de visibilidad del scaffold se preserva como lo dejó el workflow. La publicación de esta copia fue expresamente solicitada por la usuaria; no se presenta como una aprobación de release por AppliedModelingLib. El paper y su texto fuente no se publican.

La carpeta copiada requiere el clone de AppliedModelingLib, Mathlib, el archivo raíz generado `papers/AR18RaceManMachine.lean` y su entrada en `lakefile.toml`. Para reproducir el run, partir del commit indicado, activar Python >=3.11 y el toolchain Lean, ejecutar el prompt/workflow registrado y conservar el scaffold. El comando `check` se ejecuta en ese clone; no basta entrar en `lean/`.

### Deuda de formalización, no errores ocultos

La reparación y revisión acotadas están terminadas. El agente volvió a alcanzar su límite de uso después de guardar el informe parcial; el coordinador repitió build/check y realizó la copia literal final. Quedan restos documentales del scaffold: `review_entrypoint` apunta a un `FINAL_VALIDATION_REPORT.md` inexistente y una tabla de `docs/FORMALIZATION_NOTES.md` conserva texto de plantilla. Se preservan por integridad; el informe vigente es `PARTIAL_FORMALIZATION_REPORT.md`, no un reporte de cierre. Sigue pendiente una formalización completa: derivar los coeficientes desde el equilibrio, cubrir todas las cláusulas y resultados, y completar las revisiones y el cierre global. Este alcance parcial debe mantenerse visible al presentar el trabajo. No se atribuye un teorema económico completo a dos pruebas algebraicas correctas.

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

- **Lean:** las tres traducciones se corrigieron y los dos fragmentos fueron revisados, pero check 0 y build 0 no acreditan el modelo completo. Distinguir prueba algebraica de derivación de equilibrio y de cierre global.
- **Esquina y crecimiento:** distinguir el crecimiento de la senda tecnológica candidata del crecimiento AK y no leer $\rho_c(g)$ como umbral numérico independiente de $g$. Revisar NBER pp. 16–18 y prueba p. 43.
- **Versiones:** las cláusulas sobre el umbral $K$ cambian entre NBER p. 13 y AER p. 1502. La condición central aquí es $P_I>D_I$; el umbral cerrado de `extensions.md` corresponde solo a nuestra especialización.
- **Representatividad:** preferencias específicas, tareas ordenadas e innovación con científicos escasos no son evidencia de autocorrección universal en economías reales.
- **Foto:** verificar la distinción entre trabajo fijo en la hoja y oferta creciente en el modelo principal. Leer las dos precisiones junto a la imagen: ahorro de costos nulo y supuestos del resultado de participación.

## Git y entrega

`main` conserva el commit inicial. El trabajo se propone en `feat/repo-6` mediante PR. El merge y el comentario en el issue quedan a cargo de la estudiante. La carpeta de trabajo contiene el PDF local del paper, pero ese archivo no forma parte del commit.
