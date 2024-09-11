import streamlit as st

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
