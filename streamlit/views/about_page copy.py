import streamlit as st
'''
st.title('Compara tu Luz')

st.subheader('Proyecto final Data Science The Bridge.')


st.markdown("""
¡Bienvenido a Compara tu Luz, el comparador de tarifas de luz de The Bridge!
    
Esta aplicación está diseñada para comparar tu factura de la luz y obtener la mejor oferta del mercado. 
            
Su funcionamiento es muy sencillo: Carga tu factura de tres formas distintas y nuestro comparador te dará la mejor tarifa del mercado.""")

st.image('https://www.ocu.org/-/media/ocu/images/home/vivienda%20y%20energia/gas%20y%20luz/confusion_electricas_1600x900.jpg?rev=daad7dee-5a08-4dce-a46b-934b395bd4bc&mw=480&hash=86D702E41831C25A7D8DB970B913FE25')

st.markdown("""Sabemos que entender una tarea de la luz es algo difícil, por lo que en esta sección desglosaremos los conceptos clave a tener en cuenta.
         

En primer lugar, tenemos el término de **<u>potencia</u>**:

Es el parámetro que indica la cantidad de energía eléctrica máxima admitida por nuestra red doméstica. 

A su vez, este parámetro se descompone a su vez en dos franjas:           
            
             
- **Término de potencia punta**: Va de las 08:00 a las 24:00. 
    
- **Término de potencia valle**: Va de las 24:00 a las 08:00.
            

Podríamos asemejar este concepto al diámetro de una tubería de agua. A mayor diámetro, mayor capacidad de tránsito y mayor capacidad, en general, de la red.


En tu factura, deberías encontrar referencias a estos dos términos así como sus precios asociados.

Te adjuntamos una foto del concepto""", unsafe_allow_html=True)

st.image('images/detalle_potencia.jpg')





st.markdown(""" 

En segundo lugar, debemos observar el término de **<u>consumo o energía</u>**:

Es el parámetro que indica la cantidad de energía consumida a lo largo de un período determinado. Es el término variable de la factura, sobre el que podemos prestar más atención para ahorrar en el día a día. 

Este parámetro se descompone en función de la tarifa que elijamos:

(TERMINAR)

             
- ****: Va de las 08:00 a las 24:00. 
    
- **Término de potencia valle**: Va de las 24:00 a las 08:00

Podríamos asemejar este concepto al diámetro de una tubería de agua. A mayor diámetro, mayor capacidad de tránsito y mayor capacidad, en general, de la red.


Los términos habituales variarán en función del tamaño de tu vivienda, el número de electrodomésticos conectado, 
            
            En tu factura, deberías encontrar referencias a estos dos términos así como sus precios asociados.
            

En segundo lugar, observamos el término de **<u>consumo</u>**:
            
Este parámetro indica la cantidad de energía consumida durante un período determinado de tiempo, habitualmente uno o dos meses. 

Existen dos tipos de tarifas:
            
            
            A su vez, este parámetro se descompone a su vez en dos franjas:           
             
- ** Término de potencia punta **: Va de las 08:00 a las 24:00. 
    
- **Término de potencia valle**: Va de las 24:00 a las 08:00

Podríamos asemejar este concepto al diámetro de una tubería de agua. A mayor diámetro, mayor capacidad de tránsito y mayor capacidad, en general, de la red.


Los términos habituales variarán en función del tamaño de tu vivienda, el número de electrodomésticos conectado, 
            
            En tu factura, deberías encontrar referencias a estos dos términos así como sus precios asociados.           

         

            

            
En esta sección te explicaremos cómo funciona el mercado eléctrico y los conceptos clave para que entiendas cómo se calcula tu factura.

¿Cómo funciona el mercado eléctrico?
El mercado de la luz en España tiene un sistema complejo, pero aquí te lo explicamos de forma sencilla:

Mercado mayorista o "pool": Aquí es donde las empresas productoras de electricidad venden la energía a las comercializadoras. Los precios cambian cada hora dependiendo de la oferta y la demanda. Este precio dinámico influye directamente en tu factura si tienes una tarifa indexada o si estás bajo el Precio Voluntario para el Pequeño Consumidor (PVPC).

Tarifas reguladas y tarifas libres:

Tarifa PVPC: Es la tarifa regulada por el Gobierno. Su precio varía según el mercado mayorista, lo que significa que puedes tener diferentes precios a lo largo del día. Puedes aprovechar si consumes en horas de baja demanda, pero podrías pagar más en momentos de alta demanda.
Tarifa en el mercado libre: Aquí, las comercializadoras ofrecen precios fijos o con descuentos específicos. Te da más estabilidad, ya que conoces el precio que pagarás durante un periodo de tiempo, pero podrías no aprovechar las bajadas de precios del mercado.
Peajes de acceso y cargos: Son los costes que se pagan por el uso de la red de transporte y distribución de electricidad. Estos están incluidos en todas las tarifas, y su precio también puede cambiar en función de la hora del día.

Horas punta, llano y valle: Con la nueva estructura tarifaria, el día se divide en diferentes tramos horarios. El precio es más caro en las horas punta (8h-10h y 18h-22h), intermedio en las horas llano y más barato en las horas valle (medianoche a las 8h). Conocer estos tramos te ayudará a planificar mejor tu consumo.

¿Qué puedes hacer con esta aplicación?
Con Luz Inteligente podrás:

Comparar diferentes tarifas del mercado libre y regulado.
Obtener recomendaciones personalizadas según tu consumo.
Aprovechar las horas valle para reducir tu factura.
Simular tu factura introduciendo tus datos de consumo.
Te invitamos a que explores las opciones de tarifas, visualices gráficos sobre la evolución del precio de la luz y descubras cómo ahorrar. Para más información sobre los detalles del mercado eléctrico, puedes consultar las fuentes oficiales en el siguiente enlace al Ministerio de Transición Ecológica o acceder a la sección de preguntas frecuentes sobre tarifas de luz en la web de la CNMC.

Esperamos que disfrutes de esta experiencia y encuentres lo que estás buscando.
""", unsafe_allow_html=True)



# Texto de introducción con palabra subrayada utilizando HTML
st.markdown("""
    ¡Bienvenido a **Luz Inteligente**, la aplicación creada por **The Bridge** para que puedas comparar tarifas eléctricas de manera sencilla y obtener el mejor precio para tu consumo!
    
    El mercado de la luz en España tiene un sistema complejo, pero aquí te lo explicamos de forma sencilla:
    
    
    
    En el mercado de la luz, debes prestar especial atención a las **horas punta, llano y valle**, que dividen el día según los costes de electricidad.

    Para más detalles, consulta nuestro [enlace al Ministerio de Transición Ecológica](https://www.miteco.gob.es).
    
    """, unsafe_allow_html=True)

# Texto con palabra subrayada""")
            


st.markdown('<p>Presta atención a las <u>horas valle</u> para ahorrar en tu factura de la luz.</p>', unsafe_allow_html=True)

#https://www.ocu.org/vivienda-y-energia/gas-luz/consejos/como-descifrar-la-factura-de-la-luz
'''
import streamlit as st

st.title('Compara tu Luz')

st.subheader('Proyecto final Data Science The Bridge.')

st.markdown("""
## ¡Bienvenido al comparador de tarifas de luz de The Bridge!            

Esta aplicación está diseñada para comparar tu factura de la luz y obtener la mejor oferta del mercado.
Su funcionamiento es muy sencillo: Carga tu factura de tres formas distintas y nuestro comparador te dará la mejor tarifa del mercado.
""")

st.subheader('Cómo Descifrar la Factura de la Luz')

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

