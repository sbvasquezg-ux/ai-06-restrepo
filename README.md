<p align="center"><img src="assets/header.svg" alt="The Race between Man and Machine" width="100%"></p>
<p align="center">
<a href="https://doi.org/10.1257/aer.20160696"><img alt="AER 108(6)" src="https://img.shields.io/badge/AER-108(6)-6D28D9?style=for-the-badge"></a>
<a href="https://doi.org/10.1257/aer.20160696"><img alt="DOI" src="https://img.shields.io/badge/DOI-10.1257%2Faer.20160696-0E7490?style=for-the-badge"></a>
<a href="https://www.nber.org/papers/w22252"><img alt="NBER w22252" src="https://img.shields.io/badge/NBER-w22252-F59E0B?style=for-the-badge"></a>
<a href="presentation.pdf"><img alt="Beamer 20 min" src="https://img.shields.io/badge/Beamer-20_min-E11D48?style=for-the-badge"></a>
</p>
<p align="center">
<a href="presentation.tex"><img alt="Fuente LaTeX" src="https://img.shields.io/badge/fuente-LaTeX-0E7490?style=flat-square"></a>
<a href="lean/"><img alt="Lean parcial" src="https://img.shields.io/badge/Lean-parcial-E11D48?style=flat-square"></a>
<a href="sim.py"><img alt="Auditoría SymPy" src="https://img.shields.io/badge/auditor%C3%ADa-SymPy-6D28D9?style=flat-square"></a>
<a href="LICENSE"><img alt="Licencia MIT" src="https://img.shields.io/badge/licencia-MIT-0E7490?style=flat-square"></a>
</p>
<p align="center">
<img alt="LaTeX" src="https://img.shields.io/badge/LaTeX-6D28D9?style=flat-square&logo=latex">
<img alt="Beamer" src="https://img.shields.io/badge/Beamer-0E7490?style=flat-square">
<img alt="Python" src="https://img.shields.io/badge/Python-6D28D9?style=flat-square&logo=python&logoColor=white">
<img alt="SymPy" src="https://img.shields.io/badge/SymPy-0E7490?style=flat-square&logo=sympy&logoColor=white">
<img alt="Lean 4" src="https://img.shields.io/badge/Lean-4-6D28D9?style=flat-square">
<img alt="GitHub" src="https://img.shields.io/badge/GitHub-14121F?style=flat-square&logo=github">
</p>

# Repository 6 — Acemoglu & Restrepo (2018)

> **Daron Acemoglu y Pascual Restrepo.** *The Race between Man and Machine: Implications of Technology for Growth, Factor Shares, and Employment*. **American Economic Review 108(6), 1488–1542.** DOI: <https://doi.org/10.1257/aer.20160696>. Se trabaja con **NBER WP 22252, rev. junio de 2017**, 87 páginas. Paginación y algunos pasajes difieren de AER; las proposiciones centrales conservan sus números. Véase el [mapa verificado](paper/README.md).

## Pregunta y mecanismo

**¿La automatización reduce necesariamente los salarios y la participación laboral?** La economía combina tareas asignables a trabajo o capital, y distingue:

- **Desplazamiento:** $I$ aumenta y el trabajo pierde tareas cuando la tecnología restringe la adopción.
- **Productividad:** sustituir trabajo por capital más barato eleva producción y demanda en tareas restantes.
- **Reinstalación:** $N$ aumenta e introduce tareas con ventaja laboral, reemplazando las inferiores.

Fuente: NBER rev. 2017, §2 pp. 6–10, Props. 2–3 pp. 11–14. Es el único paper de este bloque del curso que analiza la **economía agregada**: precios, oferta laboral, inversión e innovación se determinan conjuntamente, en vez de estudiar solo la decisión de un agente o firma ([issue 5](https://github.com/alexanderquispe/AI-Econ-Modeling/issues/5)).

## El problema del agente

Empresas competitivas minimizan costos y el hogar elige consumo y trabajo. En el límite $\eta\to0$ de Assumption 2, la tecnología se escribe

$$Y=\widetilde B\left[\int_{N-1}^N y(i)^{(\sigma-1)/\sigma}di\right]^{\sigma/(\sigma-1)},\qquad
 y(i)=\begin{cases}k(i)+\gamma(i)l(i),&i\le I,\\\gamma(i)l(i),&i>I.\end{cases}$$

$\gamma$ es positiva y estrictamente creciente, $\sigma\in(0,\infty)$, $I\in[N-1,N]$. El umbral efectivo es $I^*=\min\{I,\widetilde I\}$, con $\gamma(\widetilde I)=W/R$: factibilidad no equivale a adopción. El CES completo incluye intermedios; $\widehat\sigma=(1-\eta)\sigma+\eta\zeta$. Fuente: NBER rev. 2017, ecs. (1)–(6), pp. 6–9; tecnología completa y preferencias en [extensions.md](extensions.md#1-qué-representa-el-modelo-y-qué-se-mantiene-fijo).

## El resultado principal

**Estática local:** bajo Assumptions 1–3 (ventaja estricta; $\eta\to0$ o $\zeta=1$; $K<\overline K$, equivalente al régimen $R>W/\gamma(N)$), preferencias (4), oferta $L^s(W/(RK))$ con $\varepsilon_L>0$, capital fijo y $N-1<I^*=I<\widetilde I$, automatizar reduce **empleo y participación** $s_L=WL/(RK+WL)$, pero el **salario real $W$ es ambiguo**. Nuevas tareas aumentan los tres. Si $I^*=\widetilde I<I$, ampliar $I$ no tiene efecto local; en el punto de cambio se usan derivadas laterales. Fuente: NBER rev. 2017, Props. 2–3 pp. 11–14, nota 15 p. 11.

**Dinámica:** con Assumptions 1′ y 2, BGP interior admisible, $n=N-I>\overline n(\rho)$, $g$ fijo y transversalidad $\rho+(\theta-1)g>0$, el capital ajusta y $R=\rho+\delta+\theta g$: un aumento permanente de $I$ eleva el salario de largo plazo y reduce participación y empleo. La innovación endógena requiere además Assumption 4, $S$ pequeño y restricciones de rentabilidad para la senda estable; también admite esquinas y multiplicidad. Fuente: NBER rev. 2017, Props. 4–6 pp. 17–26. Condiciones completas de cada régimen, sin extrapolar la interioridad: [extensions.md, §§6–9](extensions.md#6-capital-endógeno-cambia-el-experimento).

## El titular, revisado

«La automatización baja los salarios» omite la condición decisiva. A partir de (B9)–(B10), con $s=\widehat\sigma$, $H=\int_I^N\gamma(i)^{s-1}di$ y $\Lambda_I=\gamma(I)^{s-1}/H+1/(I-N+1)$:

$$\frac{\partial W}{\partial I}=W\left[\underbrace{P_I}_{\text{productividad}}-\underbrace{(1-s_L)\frac{\Lambda_I}{s+\varepsilon_L}}_{\text{desplazamiento}}\right],\qquad
P_I=\frac{B^{s-1}[(W/\gamma(I))^{1-s}-R^{1-s}]}{1-s}.$$

$$\boxed{\partial_I W>0\iff P_I>(1-s_L)\Lambda_I/(s+\varepsilon_L).}$$

Para $s=1$, $P_I=\ln[W/(R\gamma(I))]$. Fuente: NBER rev. 2017, Prop. 3 p. 13 y prueba p. B-13; reordenamiento y límite propios. **Veredicto:** falso como necesidad, correcto como posibilidad. `sim.py` demuestra un ejemplo admisible donde $W$ sube mientras $s_L$ cae. No se reclama un error del teorema.

## Formalización en Lean

**Run propio parcial, reparado y revisado.** Agente `gpt-5.6-sol`, esfuerzo `xhigh`; Python 3.12.14. `lake build +AR18RaceManMachine` y el **check --fast terminaron con código 0**. El check rápido compila `PaperInterface` y comprueba aislamiento de módulos y diferencias; su [salida íntegra](lean/CHECK_OUTPUT.txt) no certifica equivalencia con el modelo.

Se corrigieron dentro de AppliedModelingLib tres fórmulas de Prop. 2 (NBER rev. 2017, p. 11) antes de volver a copiar la carpeta entera. La revisión independiente encuentra **dos fragmentos algebraicos coincidentes y ninguna proposición completa cubierta**: Prop. 2 aporta signos de expresiones dadas; Prop. 3, consecuencias de una descomposición suministrada. Falta derivar esas expresiones desde el equilibrio y formalizar los demás resultados. El estado conservado es `partially formalized`; no existe cierre global certificado. Véase [alcance y revisión](extra/notes.md#lean-alcance-real-y-error-de-traducción).

## Reproducción

Python **3.11 o superior**; ejecución realizada con **3.12.14**. Para el PDF se requiere TeX Live con LuaLaTeX y los paquetes de `assets/restrepo-beamer.sty`.

```bash
pip install -r requirements.txt
python sim.py
lualatex presentation.tex
lualatex presentation.tex
# En la raíz del clone de AppliedModelingLib usado por el workflow:
python3 scripts/paper_contribution.py check AR18RaceManMachine --fast
```

Las figuras se regeneran sin argumentos. El check pertenece al clone de la biblioteca, no a este repositorio independiente. Véanse versiones, resultados reales y limitaciones en [extra/notes.md](extra/notes.md).

## Estructura

```text
.
├── assets/
│   ├── header.svg
│   └── restrepo-beamer.sty
├── extra/
│   ├── figures/
│   │   ├── displacement-productivity.pdf
│   │   └── displacement-productivity.png
│   └── notes.md
├── hand/
│   ├── README.md
│   └── manual-verification.png
├── lean/                      # carpeta íntegra del run, con sus subcarpetas
├── paper/
│   ├── README.md
│   └── w22252.pdf             # solo local; ignorado
├── presentation.pdf
├── presentation.tex
├── README.md
├── extensions.md
├── prompts.md
├── sim.py
├── requirements.txt
├── LICENSE
└── .gitignore
```

La estudiante aportó su [foto original](hand/manual-verification.png), incluida en el deck. [hand/README.md](hand/README.md) distingue su caso de trabajo fijo y precisa el alcance de sus conclusiones; este repositorio no inventa esa evidencia.

## Referencia

Acemoglu, D., & Restrepo, P. (2018). *The Race between Man and Machine: Implications of Technology for Growth, Factor Shares, and Employment*. American Economic Review, 108(6), 1488–1542. <https://doi.org/10.1257/aer.20160696>
