# Fuentes y mapa de versiones

**Fuente fijada:** Acemoglu y Restrepo, *The Race Between Machine and Man*, NBER WP 22252, mayo de 2016, **revisada en junio de 2017**, 87 páginas del archivo. Página de descarga: <https://www.nber.org/papers/w22252>. PDF: <https://www.nber.org/system/files/working_papers/w22252/w22252.pdf>.

```bash
curl -L --fail https://www.nber.org/system/files/working_papers/w22252/w22252.pdf -o paper/w22252.pdf
```

Verificar portada, fecha, páginas y SHA-256 antes de reutilizar una referencia. Una URL puede cambiar de contenido.

**SHA-256 del PDF NBER leído:** `441d01202afd56ef8002fc24ffc2beb51191741c0b5accb11d2534620dd616b7`.

`paper/w22252.pdf` es exclusivamente local y está en `.gitignore`. La licencia MIT del repositorio se aplica al trabajo original, no al artículo. La copia de trabajo de AppliedModelingLib también ignora sus bytes fuente mediante su propio `.gitignore`.

**Contraste publicado:** *The Race between Man and Machine*, AER **108(6)** (2018), 1488–1542, DOI <https://doi.org/10.1257/aer.20160696>. Se abrió además el PDF público del autor: <https://economics.mit.edu/sites/default/files/publications/The%20Race%20Between%20Man%20and%20Machine%20-%20Implications%20of.pdf> (56 páginas del archivo descargado, incluyendo material final). No se versiona esa copia.

## Correspondencias comprobadas

Los números de las **proposiciones centrales 1–6 se conservan** en estos dos PDF. Lo que no coincide es la paginación, la organización por secciones y algunos pasajes. No inventamos una renumeración de proposiciones para satisfacer una advertencia general del curso.

| Contenido usado | NBER rev. junio 2017: página impresa | AER 2018: página impresa |
|---|---|---|
| CES y tecnología, ecs. (1)–(3) | 6–7, §2.1 | 1494–1495, §I.A |
| Preferencias (4), Assumptions 1–2 | 7 | 1495–1496 |
| Umbral (6), Assumption 3 | 8 | 1497 |
| Equilibrio (8)–(11), Prop. 1, ec. (12) | 9–10 | 1498 |
| Ec. (13), demanda relativa | 10 | 1499 |
| Corollary 1 | 11 | 1500 |
| Prop. 2, estática comparativa | 11–12 | 1500–1501 |
| Prop. 3, productividad y salarios | 12–14 | 1501–1503 |
| Assumption 1′, ec. (15) | 15 | 1504 |
| Euler (18), umbral (21) | 16 | 1505–1506 |
| Prop. 4, crecimiento exógeno | 17–18 | 1507–1508 |
| Prop. 5, largo plazo | 19–21 | 1508–1511 |
| Assumption 4 | 24 | 1513 |
| Prop. 6, innovación endógena | 25–26 | 1515–1516 |
| Prueba salarial, (B9)–(B10) | B-13 (página 65 del PDF) | Apéndice online B, no incluido en el PDF AER aquí leído: correspondencia de sus números no verificada |

Para NBER: páginas impresas 1–50 corresponden a posiciones PDF 3–52; B-1–B-35 corresponden a posiciones 53–87. Por ejemplo, Prop. 3 p. 13 está en la página 15 del visor. No se confunden estos números.

## Diferencias materiales que no se corrigen en silencio

1. **Umbral de capital:** el NBER, Prop. 3 p. 13, imprime un umbral con barra, salarios crecientes para $K<\overline K$ y decrecientes para $K>\overline K$. La AER, Prop. 3 p. 1502, imprime $\widetilde K$ y salarios crecientes para $K>\widetilde K$, decrecientes para $K<\widetilde K$. Se comprobó el pasaje en los PDF. Los glifos de barras/subrayados son especialmente frágiles al extraer texto. No se trasplanta el enunciado AER al NBER ni se proclama aquí una corrección del artículo: el veredicto usa la descomposición común y el umbral propio de la especialización.
2. **Prop. 5 NBER p. 19:** el inciso final habla de un aumento de $n$ causado por aumento de $I$, aunque $n=N-I$. El desarrollo pp. 20–21 describe la caída de $n$ por automatización; la presentación se apoya en ese experimento explícito. Esta discrepancia de redacción no se convierte en un resultado nuevo ni se codifica como hipótesis oculta.
3. La foto de una página del paper no sustituye una ecuación tipeada ni la derivación de la estudiante. Las imágenes de lectura permanecen fuera del repositorio.

## Alcance de las atribuciones

Cada referencia del análisis y deck indica NBER rev. 2017 o AER 2018. La prueba manual usa NBER (B9)–(B10). Las expresiones con $P_I,D_I,H,a$ y $K_{\rm crit}$ son abreviaturas o derivaciones propias, no números de ecuaciones inventados del artículo.
