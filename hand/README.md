# Derivación manuscrita que debe fotografiarse

Copiar a papel esta derivación (media carilla). Usar $W$ para salario real, no $w=W/\gamma(I)$ normalizado. Fuente: **NBER WP 22252, rev. junio 2017**, Prop. 2 pp. 11–12, Prop. 3 pp. 12–13, prueba p. B-13, ecs. (B9)–(B10).

Bajo Assumptions 1–3, $K,N$ fijos, oferta creciente con $\varepsilon_L>0$ y $N-1<I^*=I<\widetilde I$ y $W/R<\gamma(N)$, escribir

$$s=\widehat\sigma,\quad H=\int_I^N\gamma(i)^{s-1}di,\quad
\Lambda_I=\frac{\gamma(I)^{s-1}}H+\frac1{I-N+1},\quad s_L=\frac{WL}{RK+WL}.$$

Para $s\ne1$, definir

$$P_I=\frac{B^{s-1}}{1-s}\left[\left(\frac W{\gamma(I)}\right)^{1-s}-R^{1-s}\right]>0.$$

Sea $x=\partial_I\ln W$, $z=\partial_I\ln R$. De (B9)–(B10),

$$s_Lx+(1-s_L)z=P_I,\qquad x-z=-\frac{\Lambda_I}{s+\varepsilon_L}.$$

Sustituir $z=x+\Lambda_I/(s+\varepsilon_L)$ en la primera:

$$\boxed{\frac{\partial W}{\partial I}=W\left[\underbrace{P_I}_{\text{productividad}}-\underbrace{(1-s_L)\frac{\Lambda_I}{s+\varepsilon_L}}_{\text{desplazamiento}}\right].}$$

Como $W>0$, terminar exactamente con

$$\boxed{\frac{\partial W}{\partial I}>0\iff
P_I>(1-s_L)\frac{\Lambda_I}{s+\varepsilon_L}.}$$

Para $s=1$, reemplazar solo $P_I$ por $\ln[W/(R\gamma(I))]$ (límite derivado).

Guardar la foto como `hand/manual-verification.png`; la diapositiva la incorporará al recompilar. La foto la añade la estudiante después de hacer y revisar su propia derivación. Este repositorio no inventa esa evidencia.
