# Derivación, condiciones y veredicto

**Versión de trabajo:** NBER WP 22252, revisada en junio de 2017, 87 páginas PDF. Las referencias `p.` son las páginas **impresas**, no el contador del visor. El apéndice B conserva su paginación `B-…`. El mapa a AER está en `paper/README.md`. Las igualdades marcadas «derivación propia» se obtienen de las ecuaciones citadas, no se presentan como numeración original.

## 1. Qué representa el modelo y qué se mantiene fijo

El continuo activo es $[N-1,N]$, de medida **uno**. Aumentar $N$ reemplaza la tarea inferior, no aumenta la masa total de tareas. $I$ es factibilidad técnica, mientras $I^*=\min\{I,\widetilde I\}$ es adopción efectiva, con $\gamma(\widetilde I)=W/R$. Por tanto, el trabajo realiza una masa $N-I^*$, que solo coincide con $N-I$ en el régimen restringido por tecnología. Fuente: NBER rev. 2017, §2.1–2.2, ecs. (1), (3), (6), pp. 6–9.

El agregador y las tecnologías son

$$Y=\widetilde B\left[\int_{N-1}^{N}y(i)^{(\sigma-1)/\sigma}\,di\right]^{\sigma/(\sigma-1)},$$
$$y(i)=\overline B(\zeta)\left[\eta^{1/\zeta}q(i)^{(\zeta-1)/\zeta}+(1-\eta)^{1/\zeta}x(i)^{(\zeta-1)/\zeta}\right]^{\zeta/(\zeta-1)},$$
$$x(i)=\begin{cases}k(i)+\gamma(i)l(i),&i\le I,\\\gamma(i)l(i),&i>I.\end{cases}$$

Competencia, minimización de costos y vaciado de mercados determinan conjuntamente $W,R,L,Y,I^*$. Los intermedios cuestan $\psi$ unidades de bien final. $\overline B(1)=\psi^\eta(1-\eta)^{\eta-1}\eta^{-\eta}$ y $\overline B(\zeta)=1$ si $\zeta\ne1$. Fuente: NBER rev. 2017, ecs. (1)–(3), pp. 6–7. Las potencias CES en elasticidad uno se interpretan mediante el límite apropiado, no por sustitución en una fracción cero sobre cero.

### Supuestos y dominios usados

| Objeto | Restricción y función en la prueba | Fuente NBER rev. 2017 |
|---|---|---|
| Tecnología básica | $\sigma,\zeta\in(0,\infty)$, $\widetilde B>0$, $\eta\in(0,1)$; $I\in[N-1,N]$. La definición del equilibrio estático usa $I\in(N-1,N]$. $K>0$ para las razones de precios empleadas. | §2, pp. 6–9 |
| Assumption 1 | $\gamma(i)$ estrictamente creciente. Productividad positiva; para las derivadas de Prop. 2 se usa $\varepsilon_\gamma=d\ln\gamma(I)/dI>0$. Ordena la asignación. | p. 7; Prop. 2, p. 11 |
| Preferencias (4) | $u(C,L)=((Ce^{-\nu(L)})^{1-\theta}-1)/(1-\theta)$; $\nu$ creciente, convexa y diferenciable, con $\nu''+(\theta-1)(\nu')^2/\theta>0$. $C>0$, $L\ge0$. El texto trata $\theta>0$ y separa el caso límite $\theta=0$ en Prop. 6. $\theta=1$ tiene límite logarítmico. No se atribuye a (4) un dominio adicional no declarado. | p. 7; Prop. 6, p. 26 |
| Assumption 2 | $\eta\to0$ **o** $\zeta=1$. Permite demanda homotética, forma CES agregada y descomposición cerrada. El límite $\eta=0$ usado en `sim.py` se declara como especialización. | p. 7; Prop. 1, p. 10 |
| Assumption 3 | $K<\overline K$, donde $R=W/\gamma(N)$ define el umbral. Equivale a trabajar con $R>W/\gamma(N)$: las nuevas tareas se adoptan inmediatamente. | p. 8 |
| Oferta laboral | $L=L^s(\omega)$ creciente, $\omega=W/(RK)$, elasticidad $\varepsilon_L>0$. Hace que empleo y participación se muevan con $\omega$. | ec. (11), p. 10; Prop. 2, pp. 11–12 |
| Assumption 1′ | $\gamma(i)=e^{Ai}$, $A>0$. Necesaria en el análisis de crecimiento aquí citado. | ec. (15), p. 15 |
| Dinámica | $\rho>0$, depreciación $\delta$; $g=A\Delta$ en la senda interior, $\rho+(\theta-1)g>0$ para transversalidad. No se extrapola a tasas arbitrarias. | ecs. (14), (18)–(20), pp. 14–16; Prop. 4, pp. 17–18 |
| Assumption 4 | $\widehat\sigma>\zeta$ para los incentivos de innovación. Con $\widehat\sigma=(1-\eta)\sigma+\eta\zeta$, equivale a $\sigma>\zeta$. | p. 24 |
| Innovación endógena | Científicos $S$ suficientemente pequeño, $\kappa_I,\kappa_N>0$, distribución suave de costos $G$ y normalización $G(0)=\kappa_N/(\kappa_I+\kappa_N)$. Derechos de patente con compensación al incumbente. | §4.1, pp. 21–22; Prop. 6, pp. 25–26 |

No se demuestra aquí todo el paper ni se usa una lista de hipótesis del resultado estático para reclamar el resultado dinámico. Los supuestos auxiliares de innovación importan para el alcance del mecanismo autocorrectivo.

## 2. Reconstrucción de la prueba: dónde está la bisagra

Escribamos $s=\widehat\sigma>0$, $a=I-N+1>0$, $H=\int_I^N\gamma(i)^{s-1}di>0$ **solo en el régimen $N-1<I^*=I<\widetilde I$**. Son abreviaturas propias. Se fija $N,K$ al variar $I$.

Dividir las demandas de capital y trabajo (8)–(9) da

$$\omega^s L^s(\omega)=\frac{H}{a}K^{1-s}.$$

Aquí $L^s(\cdot)$ designa la función de oferta, no una potencia. Para evitar esa ambigüedad en la prueba se toma logaritmos:

$$s\ln\omega+\ln L=s\ln\omega+\ln L^s(\omega)=\ln H-\ln a+(1-s)\ln K.$$

La regla de Leibniz da $H_I=-\gamma(I)^{s-1}$ y $a_I=1$. Por tanto,

$$\frac{\partial\ln\omega}{\partial I}=-\frac{\Lambda_I}{s+\varepsilon_L},\qquad
\Lambda_I=\frac{\gamma(I)^{s-1}}{H}+\frac1a>0.$$

Es la ec. (13) diferenciada, NBER rev. 2017 p. 10, y Prop. 2, pp. 11–12. Assumption 2 da la forma cerrada; la oferta creciente hace positivo el denominador. Assumption 1 sostiene el régimen por umbral. La positividad de $H,a$ exige interioridad.

La participación en **producto neto de intermedios** es

$$s_L=\frac{WL}{RK+WL}=\frac{\omega L}{1+\omega L},\qquad RK+WL=(1-\eta)Y.$$

Derivación propia de la identidad de participación (NBER rev. 2017, p. 10, nota 14; ec. (B9), p. B-13):

$$\frac{\partial s_L}{\partial I}=-s_L(1-s_L)(1+\varepsilon_L)\frac{\Lambda_I}{s+\varepsilon_L}<0,
\quad \frac{\partial L}{\partial I}=-L\varepsilon_L\frac{\Lambda_I}{s+\varepsilon_L}<0.$$

Hasta aquí conocemos la **distribución relativa**, no el salario real. La bisagra es combinarla con la identidad de productividad:

$$s_L\,d\ln W+(1-s_L)\,d\ln R=d\ln Y\big|_{K,L},\tag{B9}$$
$$d\ln W-d\ln R=\frac{\Lambda_NdN-\Lambda_IdI}{s+\varepsilon_L}.\tag{B10}$$

Fuente: NBER rev. 2017, prueba de Prop. 3, p. B-13. La primera es una identidad de envolvente: el efecto directo de tecnología sobre producción a factores fijos. **No** es el cambio total de $Y$ cuando $L$ responde, ni se obtiene suponiendo $dL=0$ en el equilibrio.

## 3. Salario: productividad menos desplazamiento

Resolver el sistema (B9)–(B10), sin añadir supuestos sobre el signo salarial, produce

$$\boxed{\frac{\partial W}{\partial I}=W\left[P_I-D_I\right]},$$
$$P_I=\frac{B^{s-1}}{1-s}\left[\left(\frac{W}{\gamma(I)}\right)^{1-s}-R^{1-s}\right],
\qquad D_I=(1-s_L)\frac{\Lambda_I}{s+\varepsilon_L}.$$

$P_I>0$ porque $W/\gamma(I)>R$ y $x^{1-s}/(1-s)$ es creciente para todo $s>0$, $s\ne1$. $D_I>0$ por interioridad. La fórmula de productividad y la solución del sistema coinciden con NBER rev. 2017, Prop. 3, pp. 12–14 y B-12–B-13.

$$\boxed{\frac{\partial W}{\partial I}>0\quad\Longleftrightarrow\quad
\frac{B^{s-1}\{(W/\gamma(I))^{1-s}-R^{1-s}\}}{1-s}
>(1-s_L)\frac{\gamma(I)^{s-1}/H+1/a}{s+\varepsilon_L}.}$$

Esta es una condición local explícita en los precios y participaciones del equilibrio. La frontera en parámetros primitivos se obtiene resolviendo el equilibrio, no tratando esos precios como constantes al mover $K$ o $I$. En $s=1$, $P_I=\ln[W/(R\gamma(I))]$ por límite y la misma desigualdad se conserva.

**Veredicto:** «la automatización necesariamente baja los salarios» es falso como afirmación universal. «Puede bajarlos» es correcto y condicional. «Reduce la participación laboral» requiere el régimen de adopción vinculante, capital fijo y los supuestos de Prop. 2. Si $I^*=\widetilde I<I$, un pequeño aumento de $I$ no cambia ninguno de los objetos; en $I=\widetilde I$ corresponden derivadas laterales, no una derivada ordinaria única (NBER rev. 2017, Prop. 2, p. 11, nota 15; Prop. 3, p. 13).

## 4. Reinstalación y la carrera conjunta

A $I,K$ fijos, $H_N=\gamma(N)^{s-1}$ y $a_N=-1$. De las mismas identidades:

$$\Lambda_N=\frac{\gamma(N)^{s-1}}H+\frac1a,\quad
P_N=\frac{B^{s-1}}{1-s}\left[R^{1-s}-\left(\frac W{\gamma(N)}\right)^{1-s}\right]>0,$$
$$\boxed{\frac{\partial W}{\partial N}=W\left[P_N+(1-s_L)\frac{\Lambda_N}{s+\varepsilon_L}\right]>0.}$$

Assumption 3 firma $P_N$; la reinstalación firma el segundo término. En $s=1$, $P_N=\ln[R\gamma(N)/W]$. Fuente: NBER rev. 2017, Prop. 3, p. 13; prueba, B-12–B-13. Productividad generada por $dI$ **no es** reinstalación: esta última exige $dN$.

Derivación propia para cambios conjuntos infinitesimales en el mismo régimen:

$$d\ln W=(P_I-D_I)dI+\left[P_N+(1-s_L)\frac{\Lambda_N}{s+\varepsilon_L}\right]dN.$$

La participación sube si $\Lambda_NdN>\Lambda_IdI$. Si $P_I<D_I$ y $dI>0$, el salario sube cuando

$$\frac{dN}{dI}>\frac{D_I-P_I}{P_N+(1-s_L)\Lambda_N/(s+\varepsilon_L)}.$$

Las dos fronteras son diferentes. No basta decir que «nuevas tareas compensan»: hay que indicar qué variable se busca compensar.

## 5. Especialización transparente y frontera reproducible

`sim.py` fija $\eta=0$ (límite de Assumption 2), $B=1$, $\gamma(i)=e^{2i}$, $N=1$, $\theta=1$ y $\nu(L)=L^2/2$. Esta es una **elección propia**, no una calibración del paper. La utilidad límite es $\ln C-L^2/2$, cóncava. De $L=W/C$ y $C=RK+WL$ se obtiene

$$\omega=\frac L{1-L^2},\qquad s_L=L^2,\qquad
\varepsilon_L=\frac{1-L^2}{1+L^2}>0,\quad 0<L<1.$$

Con $s=1.5$ y $K=1$, se resuelve la ecuación de mercados, se comprueba $\gamma(I)<W/R<\gamma(N)$ y se calculan $P_I,D_I$. Tras alcanzar $\widetilde I$, el algoritmo mantiene $I^*=\widetilde I$ y dibuja la meseta. No fuerza toda la tecnología disponible a ser adoptada. El mapa $(I,K)$ deja sin color los puntos fuera del régimen de Prop. 3.

Además hay un caso exactamente soluble: $s=1$, $n=1-I$, $a=I$, con la misma oferta y $\gamma(i)=e^{Ai}$, $A>0$. De los mercados,

$$L=\sqrt n,\quad q=\frac WR=\frac{K\sqrt n}{a},\quad
\ln W=\ln B+a\ln q+\frac A2(1-I^2).$$

Derivación propia:

$$P_I=\ln q-AI,\quad D_I=\frac{1+n}{2n},\quad
\boxed{K_{\rm crit}(I)=\frac{I}{\sqrt{1-I}}
\exp\left[AI+\frac{2-I}{2(1-I)}\right].}$$

El salario sube si $K>K_{\rm crit}(I)$, **dentro** de

$$\frac{I e^{AI}}{\sqrt{1-I}}<K<\frac{I e^A}{\sqrt{1-I}}.$$

La región de subida existe solo si $A(1-I)>(2-I)/(2(1-I))$. SymPy comprueba la derivada, el umbral y esta reducción. Es un resultado propio para una especialización, no un teorema general en $K$ atribuido al NBER.

## 6. Capital endógeno: cambia el experimento

Para sendas interiores de crecimiento con Assumptions 1′ y 2, $g$ constante y las condiciones de existencia/transversalidad de Prop. 4, Euler fija $R=\rho+\delta+\theta g$. Comparar desplazamientos permanentes del nivel de $I$ manteniendo el crecimiento de la frontera no es comparar impactos a capital fijo. Si $n>\overline n(\rho)$ y las nuevas tareas siguen siendo rentables, $d\ln R=0$ en el nuevo largo plazo. La identidad de precios implica

$$\boxed{d\ln W=\frac{d\ln Y|_{K,L}}{s_L}>0.}$$

Fuente: NBER rev. 2017, Prop. 5, pp. 19–21, nota 22 p. 20. La identidad es local, exige $s_L>0$ y no describe la esquina. En ese experimento, empleo y participación todavía caen. Cuando $n<\overline n(\rho)$, pequeñas variaciones tecnológicas son inactivas. Con $s<1$, la acumulación amortigua la caída de participación; con $s>1$, la amplifica. A $s=1$, el efecto de $K$ sobre participación es cero: resultado propio de $\partial\ln\omega/\partial\ln K=(1-s)/(s+\varepsilon_L)$, usando Prop. 2 p. 11.

## 7. Esquina: una condición, no un pronóstico

La frontera se define en la clasificación de sendas candidatas por

$$\rho_c(g)=B-\delta-\theta g,\qquad
\rho<\rho_c(g)\ \Longleftrightarrow\ \rho+\delta+\theta g<B.$$

Usamos $\rho_c$ como alias propio del umbral subrayado del paper. Sale del índice de precios a $n^*=0$: bajo Assumption 2, $R=B$. Fuente: NBER rev. 2017, ec. (21), p. 16; Lemma A2, pp. 40–42. La comparación económicamente relevante es con el salario **por unidad eficiente** $W/\gamma(N)$, no con un número universal para $R/W$. Si $R<W/\gamma(N)$, ni la tarea de mayor ventaja laboral resulta más barata con trabajo. En la región izquierda de la clasificación, $n<\widetilde n(\rho)$ impide adopción rentable de nuevas tareas (Lemma A2, pp. 40–42).

Prop. 4(1), NBER rev. 2017 p. 17, exige además $N(t)=I(t)$ y

$$B>\delta+\rho>\frac{1-\theta}{\theta}(B-\delta-\rho)+\delta.$$

Para $\theta>0$, la última condición es exactamente la transversalidad $B-\delta>g_{AK}$, con $g_{AK}=(B-\delta-\rho)/\theta>0$. Derivación propia por reordenamiento; prueba de Prop. 4, NBER p. 43. **No se sustituye $g_{AK}$ en $\rho_c(g)$ para convertir una igualdad de Euler en una desigualdad estricta**: el $g$ de la clasificación de sendas tecnológicas y el crecimiento de la solución AK deben distinguirse al cambiar de régimen. El texto no ofrece un umbral numérico calibrado.

En la esquina, la prueba usa $F=BK$, $F_L=0$, $L=0$, participación laboral cero (NBER rev. 2017, p. 43). El salario marginal de la representación reducida es cero. Un «salario observado de trabajadores empleados» no existe si no hay trabajadores empleados. No se infiere esta esquina haciendo $s_L\to0$ en la fórmula interior $P_I/s_L$.

Prop. 6(1), NBER rev. 2017 pp. 25–26, conserva la posibilidad de esa esquina con innovación endógena, bajo Assumptions 1′, 2, 4 y científicos suficientemente escasos. La proposición afirma **existencia de una BGP**, no convergencia universal desde todo estado inicial. La evaluación crítica es que el titular omite restricciones de factibilidad, adopción y régimen, no que el teorema sea aritméticamente erróneo.

## 8. Autocorrección condicional y elasticidades

Con $n=N-I$, la reducción de $n$ reduce $w_I=W/\gamma(I)$, aunque puede aumentar $W$ y $w_N=W/\gamma(N)$ al mantener fija la trayectoria de $N$. Esa es la precisión que falta en «la automatización abarata el trabajo». El incentivo **relativo** a automatizar se debilita frente a crear tareas; no significa que todos los beneficios absolutos de innovación suban. Fuente: NBER rev. 2017, Prop. 5 pp. 19–21; Prop. 6 pp. 25–28.

La senda interior exige $\kappa_Iv_I(n)=\kappa_Nv_N(n)$. Prop. 6 requiere $S<\overline S$ y, para unicidad interior, $\rho>\rho_c$ y $\kappa_I/\kappa_N>\overline\kappa$. La estabilidad es global de tipo saddle path si $\theta=0$, local/asintótica de tipo saddle path si $\theta>0$. Entre los umbrales de $\kappa_I/\kappa_N$ hay multiplicidad; por debajo, una esquina sin automatización. No se afirma autocorrección incondicional. Fuente: NBER rev. 2017, Prop. 6 pp. 25–26 y prueba pp. 46–49.

La crítica sustantiva es que los incentivos dependen de patentes con compensación, una oferta pequeña de científicos, ventaja exponencial y especialización de tareas. La estabilidad de una senda dentro del modelo no demuestra que una economía real retorne rápidamente a su participación laboral anterior. Un cambio permanente de oportunidades de innovación puede cambiar esa participación de largo plazo (NBER rev. 2017, discusión tras Prop. 6, pp. 28–29).

| Pregunta | Papel de la elasticidad |
|---|---|
| Signo de participación y empleo a $K$ fijo | No cambia al cruzar $s=1$: $s+\varepsilon_L>0$ y $\Lambda_I>0$. Prop. 2, NBER pp. 11–12. |
| Signo salarial a $K$ fijo | Ambiguo para cualquier $s$ admisible. $s$ altera ambas magnitudes, no da por sí solo un signo. Prop. 3, NBER pp. 12–14. |
| Efecto de acumular capital sobre participación | Lo firma $1-s$, derivando Prop. 2. Discusión NBER p. 21. |
| Innovación endógena | Exige $s>\zeta$, Assumption 4, NBER p. 24. Con $\zeta=1$, exige $\sigma>1$. La simulación estática con $\sigma=1$ no prueba Prop. 6. |

## 9. Endpoints y dominios

- **$I\to N$:** factibilidad total no implica uso total: puede aparecer $I^*=\widetilde I<N$. Assumption 3 del estático preserva tareas laborales. Si se impone además $I^*\to N$, $H\to0$ y las fórmulas interiores son singulares. La esquina dinámica necesita sus propias condiciones. Fuentes: NBER Prop. 2 p. 11, Prop. 4 pp. 17–18.
- **$I\to N-1$:** $a\to0$ y $1/a$ diverge. El punto exacto está fuera de la definición estática con capital empleado. Puede perderse Assumption 3 antes del límite. Las derivadas no se evalúan sustituyendo $a=0$. NBER definición p. 9, Prop. 1 y prueba pp. 38–40.
- **$\sigma\to1$:** bajo Assumption 2, $s\to1$ si $\zeta=1$ o $\eta\to0$. El límite logarítmico de $P_I$ existe. La participación sigue cayendo en el régimen vinculante; no se usa el corolario de $\gamma\equiv1$ como si cumpliera ventaja estricta. NBER Corollary 1 p. 11; derivación propia §5 conserva $\gamma=e^{Ai}$.
- **$\sigma\to\infty$:** infinito no pertenece a $(0,\infty)$. La CES límite permite sustitución perfecta y concentración de producción, y pueden fallar interioridad y unicidad. No se deduce un efecto cero observando únicamente $1/(s+\varepsilon_L)$: $\Lambda_I$, precios y régimen también cambian. El teorema asegura signos para cada elasticidad finita admisible, no un teorema uniforme en el límite. Fuente del dominio: NBER p. 6; advertencia y evaluación del límite propias.

## 10. Lo que esta auditoría demuestra y lo que no

SymPy comprueba el álgebra condicional y una frontera de una especialización. El cálculo numérico resuelve equilibrio, comprueba residuos, contrasta derivadas con diferencias finitas y descarta puntos que violan el régimen. No comprueba empíricamente efectos de IA ni reemplaza la prueba general de existencia o la dinámica de Prop. 6.

El pasaje del umbral de capital en NBER p. 13 y AER p. 1502 difiere incluso en la dirección de sus desigualdades. El apéndice NBER B-12–B-13 verifica el sistema salarial, pero no desarrolla una prueba explícita del inciso de umbral en $K$. Se preserva esa diferencia en el mapa de fuentes, sin fabricar una reconciliación. Nuestro umbral propio de §5 no depende de adoptar ese inciso.

Antes del merge: comprobar a mano (B9)–(B10), las definiciones de producto neto y elasticidad, y la condición salarial; revisar el cambio de régimen en la figura; revisar por separado la lectura de la esquina y el estado real de Lean. La evidencia manuscrita ya está en `hand/manual-verification.png`; su especialización de trabajo fijo y las precisiones a sus conclusiones se explican en `hand/README.md`.
