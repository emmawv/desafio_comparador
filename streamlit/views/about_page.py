
import streamlit as st

st.title('Compara tu Luz')

st.subheader('Proyecto final Data Science The Bridge.')

st.markdown("""
## ¡Bienvenido al comparador de tarifas de luz de The Bridge!            

Esta aplicación está diseñada para comparar tu factura de la luz y obtener la mejor oferta del mercado.
Su funcionamiento es muy sencillo: Carga tu factura de tres formas distintas y nuestro comparador te dará la mejor tarifa del mercado.
""")


st.markdown("""
## Cómo Descifrar la Factura de la Luz            

Entender una factura de la luz puede parecer complicado, pero con un poco de orientación, puedes aprender a desglosar los diferentes elementos y asegurarte de que estás pagando lo que realmente debes. En esta primera página te proporcionamos una guía completa para ayudarte a comprender todos los detalles de tu factura de electricidad.
""")


st.markdown("""
## Datos Básicos de la Factura
            
Cuando recibes una factura de electricidad, lo primero que encontrarás son los datos básicos. Estos son importantes para identificar tu cuenta y el periodo de facturación. El **número de cliente** es un identificador único asociado a tu cuenta de electricidad. Este número es esencial para cualquier gestión o consulta que realices con tu proveedor de electricidad. El **periodo de facturación** indica las fechas exactas que abarcan el consumo de electricidad que se está cobrando en esa factura. Por ejemplo, podría cubrir desde el 1 de julio hasta el 31 de julio. Además, cada factura tiene un **número de factura** que sirve como referencia única para esa emisión específica.
""")

st.image('Imagenes/encabezado_factura.jpg', width=600)


st.markdown("""
## Componentes de la Factura            
           
La factura de electricidad se divide en varios componentes que reflejan diferentes aspectos del servicio que te proporcionan:

### Consumo de Energía

Uno de los principales conceptos en tu factura es el **consumo de energía**. Este es el total de electricidad que has utilizado durante el periodo de facturación, y se mide en kilovatios hora (kWh). En tu factura, verás un desglose del consumo total. Es importante revisar este dato para asegurarte de que coincide con tus expectativas y hábitos de uso. A menudo, las facturas también muestran el **precio por kWh**, que es el coste de cada unidad de electricidad consumida. Este precio puede variar dependiendo de la tarifa que tengas contratada y de las condiciones del mercado.

### Potencia Contratada

Otro componente clave es la **potencia contratada**. Esta se refiere a la capacidad máxima que puedes utilizar simultáneamente en tu hogar o negocio, y se mide en kilovatios (kW). En la factura, encontrarás el coste asociado a esta potencia, que suele ser un importe fijo mensual. La potencia contratada es importante porque determina cuántos electrodomésticos y dispositivos puedes utilizar al mismo tiempo sin que se produzcan cortes o bajones en el suministro.

### Impuestos y Otros Cargos

Además del consumo y la potencia, tu factura incluirá varios **impuestos** y **cargos adicionales**. Entre estos, el **Impuesto sobre la Electricidad** es un porcentaje que se añade al importe total de la factura. Este impuesto puede variar según la legislación vigente. También se aplica el **IVA** (Impuesto sobre el Valor Añadido) sobre el total de la factura, que es un porcentaje estándar añadido al importe final.
""")

st.image('Imagenes/detalles_factura.jpg', width=600)


st.markdown("""
## Tipos de Tarifas
            
Las tarifas de electricidad pueden variar y se reflejan en la factura de diferentes maneras:

### Tarifa de Precio Fijo

Una **tarifa de precio fijo** significa que el precio del kWh de electricidad es constante durante todo el periodo de facturación, sin importar cuánto consumas ni en qué hora del día. Esto proporciona estabilidad en el coste de la electricidad, ya que el precio no cambia.

### Tarifa de Precio Variable

En contraste, una **tarifa de precio variable** hace que el precio de la electricidad cambie según el consumo y la hora del día. Esto puede llevar a que pagues más si consumes electricidad en horas punta o menos si utilizas electricidad en horas de menor demanda. Pueden llegar a estar divididas en **tres periodos** de tiempo, llamados punta (el más caro), llano y valle (el más barato). También puede estar dividido en **dos tramos**, el más caro abarcaría 8 horas y el más barato abarcaría 16 horas. Este tipo de tarifas divididas en tramos puede ser más económica si puedes ajustar tu consumo a las horas más baratas.
""")

st.image('Imagenes/consumo_factura.jpg', width=600)

st.markdown("""
### Tarifas Reguladas y el Bono Social en la Factura de la Luz

Las **tarifas reguladas** de electricidad, conocidas como **PVPC** (Precio Voluntario para el Pequeño Consumidor), son fijadas por el gobierno y varían según la hora del día. Este tipo de tarifa está disponible para usuarios con menos de 10 kW de potencia contratada y es considerada una opción económica y transparente, ya que refleja los precios del mercado mayorista de energía en tiempo real.

El **bono social** es un descuento disponible solo para quienes tienen la tarifa regulada PVPC y están en situación de vulnerabilidad económica. Este bono ofrece un descuento del 25% para consumidores vulnerables y del 40% para vulnerables severos, y aquellos en riesgo de exclusión social pueden estar exentos de pagar la factura. El descuento aparece en la factura en la sección de "Descuentos", y se puede solicitar cumpliendo con ciertos requisitos económicos a través de las comercializadoras de referencia.
""")


st.markdown("""
## Cómo Leer Tu Factura            

Para interpretar correctamente tu factura, sigue estos pasos:

Primero, **revisa el periodo de facturación** para asegurarte de que las fechas coinciden con el periodo en el que realmente has consumido electricidad. Luego, **comprueba el consumo total** en kWh para asegurarte de que es acorde con tu uso y con lo que esperabas. Es útil comparar este dato con el consumo de meses anteriores para identificar posibles discrepancias.

Después, **verifica los precios** del kWh y la potencia contratada. Asegúrate de que estos precios coinciden con los que tienes en tu contrato y que no haya errores en los cálculos. Finalmente, **chequea los impuestos aplicados** y confirma que están calculados correctamente según la normativa.
""")


st.markdown("""
## Consejos para Reducir la Factura
            
El artículo también ofrece algunos consejos para reducir tu factura de electricidad:

- **Revisa tu tarifa**: Asegúrate de estar en la tarifa más adecuada para tu perfil de consumo. Si descubres que una tarifa diferente podría ser más económica, considera cambiarte.

- **Controla tu consumo**: Utiliza dispositivos para medir tu consumo real y ajustar tus hábitos en consecuencia. Esto puede ayudarte a identificar qué electrodomésticos consumen más y cómo reducir el uso de los mismos.

- **Optimiza el uso de energía**: Apaga los electrodomésticos cuando no los uses, y considera invertir en dispositivos más eficientes que consuman menos electricidad. Pequeños cambios en tus hábitos diarios pueden llevar a un ahorro significativo en tu factura.
""")

st.image('Imagenes/grafico_factura.jpg', width=600)


st.markdown("""
## Conclusión
Entender tu factura de la luz es crucial para gestionar tu consumo y evitar sorpresas en el importe a pagar. Conociendo cada componente y cómo se calcula, puedes tomar decisiones informadas sobre tu consumo de electricidad y asegurarte de que estás pagando un precio justo por el servicio.
""")

