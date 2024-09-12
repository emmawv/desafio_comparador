import streamlit as st
import pandas as pd
import os

# Seteo de rutas
file_path = (r'../Datos/datos_tarifas.csv')  # Ruta del archivo
directory = os.path.dirname(file_path)  # Carpeta de los datos



#PARTE PANDAS


tarifas = pd.read_csv('../Datos/tarifas.csv',sep = ';')
calculo = tarifas.copy()
calculo['margen_euros/kWh/dia'] = calculo['margen_euros/kWh/dia'].fillna(0)
datos_formulario = pd.read_csv(r'../Datos/datos_tarifas.csv') 
formulario = datos_formulario.tail(1).to_dict(orient = 'records')[0]

formulario['periodo'] = 30

calculo['consumo_valle'] = formulario['Consumo en valle (kWh)']
calculo['consumo_llano'] = formulario['Consumo en llano (kWh)']
calculo['consumo_punta'] = formulario['Consumo en punta (kWh)']
calculo['total_actual'] = formulario['Total factura']

# calculoS DE TARIFA, DEFINIMOS FUNCIONES

#PVPC

def pvpc(fila,formulario):

  calculo = fila.to_dict()  
  #POTENCIA

  #transporte y distribucion
  punta_tp = formulario['Termino de potencia en punta']*formulario['periodo']*calculo['peaje_tran_dist_pot_punta']
  valle_tp = formulario['Termino de potencia en valle']*formulario['periodo']*calculo['peaje_tran_dist_pot_valle']

  #cargos
  punta_cp = formulario['Termino de potencia en punta']*formulario['periodo']*calculo['tp_punta_euros/kwh/dia']
  valle_cp = formulario['Termino de potencia en valle']*formulario['periodo']*calculo['tp_valle_euros/kwh/dia']

  #margen. Se cobra solo sobre potencia punta en el caso de tener dos potencias contratadas
  margen = formulario['Termino de potencia en punta']*formulario['periodo']*calculo['margen_euros/kWh/dia']

  potencia = punta_tp + punta_cp + valle_tp + valle_cp + margen

  # ENERGIA

  #transporte, distribucion y cargos
  valle_te = formulario['Consumo en valle (kWh)']*calculo['peaje_ener_valle_tdc']
  llano_te = formulario['Consumo en llano (kWh)']*calculo['peaje_ener_llano_tdc']
  punta_te = formulario['Consumo en punta (kWh)']*calculo['peaje_ener_punta_tdc']

  #coste de la energia 
  valle_ce = formulario['Consumo en valle (kWh)']*calculo['tc_valle_euros/kwh/hora']
  llano_ce = formulario['Consumo en llano (kWh)']*calculo['tc_llano_euros/kwh/hora']
  punta_ce = formulario['Consumo en punta (kWh)']*calculo['tc_punta_euros/kwh/hora']

  consumo = valle_ce + llano_ce + punta_ce #solo energia consumida
 
  energia = valle_te + llano_te + punta_te + potencia + consumo #energia consumida mas peajes

  #BONO SOCIAL

  bono = formulario['periodo']*calculo['bono_social_euro/dia']

  if formulario['Bono social'] == 'Si':

    base = (potencia + consumo)*0.6 
    subtotal = (potencia + energia) - base

  else:
    subtotal = potencia + energia + bono
    
  imp_elec = subtotal * (calculo['impuesto_actual']/100)

  contador = formulario['periodo'] * calculo['alquiler_equipo_euros/dia']

  total = subtotal + imp_elec + contador

  total_factura = total * 1.10

  return total_factura

#falta el bono y el descuento de familia numerosa

#FIJA

def fija(fila,formulario):

  calculo = fila.to_dict() 

  pot_v = formulario['Termino de potencia en valle'] *formulario['periodo']*calculo['tp_valle_euros/kwh/dia']
  pot_p = formulario['Termino de potencia en punta'] *formulario['periodo']*calculo['tp_punta_euros/kwh/dia']

  energia = formulario['Consumo total (kWh)']*calculo['termino_consumo_euros/kwh/hora']

  subtotal = pot_v + pot_p + energia

  impuesto = subtotal * (calculo['impuesto_actual']/100)

  contador = formulario['periodo']*calculo['alquiler_equipo_euros/dia']

  total = subtotal + impuesto + contador

  total_factura = total * 1.10

  return total_factura


#TRAMOS

def tramos(fila,formulario):

  calculo = fila.to_dict() 

  pot_v = formulario['Termino de potencia en valle'] *formulario['periodo']*calculo['tp_valle_euros/kwh/dia']
  pot_p = formulario['Termino de potencia en punta'] *formulario['periodo']*calculo['tp_punta_euros/kwh/dia']

  potencia = pot_v + pot_p

  valle_c = formulario['Consumo en valle (kWh)']*calculo['tc_valle_euros/kwh/hora']
  llano_c = formulario['Consumo en llano (kWh)']*calculo['tc_llano_euros/kwh/hora']
  punta_c = formulario['Consumo en punta (kWh)']*calculo['tc_punta_euros/kwh/hora']

  energia = valle_c + llano_c + punta_c

  subtotal = potencia + energia

  impuesto = subtotal * (calculo['impuesto_actual']/100)

  contador = formulario['periodo']*calculo['alquiler_equipo_euros/dia']

  total = subtotal + impuesto + contador

  total_factura = total * 1.10

  return total_factura

#DISCRIMINACION HORARIA

def dh(fila,formulario):

  calculo = fila.to_dict() 

  periodo_bon = formulario['Consumo en valle (kWh)'] 
  periodo_nbon = formulario['Consumo en llano (kWh)'] + formulario['Consumo en punta (kWh)']

  pot_v = formulario['Termino de potencia en valle'] *formulario['periodo']*calculo['tp_valle_euros/kwh/dia']
  pot_p = formulario['Termino de potencia en punta'] *formulario['periodo']*calculo['tp_punta_euros/kwh/dia']

  energia_bon = periodo_bon * calculo['tc_8h_euros/kwh/hora']
  energia_nbon = periodo_nbon * calculo['tc_16h_euros/kwh/hora']

  subtotal = pot_v + pot_p + energia_bon + energia_nbon

  impuesto = subtotal * (calculo['impuesto_actual']/100)

  contador = formulario['periodo']*calculo['alquiler_equipo_euros/dia']

  total = subtotal + impuesto + contador

  total_factura = total * 1.10

  return total_factura

def tramo_fija(fila):

    datos = fila.to_dict()

    energia_valle = datos['consumo_valle'] * datos['termino_consumo_euros/kwh/hora']
    energia_llano = datos['consumo_llano'] * datos['termino_consumo_euros/kwh/hora']
    energia_punta = datos['consumo_punta'] * datos['termino_consumo_euros/kwh/hora']

    return {'coste_valle': energia_valle,
        'coste_llano': energia_llano,
        'coste_punta': energia_punta}

def tramo_pvpc(fila):

    datos = fila.to_dict() 

    energia_valle = datos['consumo_valle'] * datos['tc_valle_euros/kwh/hora']
    energia_llano = datos['consumo_llano'] * datos['tc_llano_euros/kwh/hora']
    energia_punta = datos['consumo_punta'] * datos['tc_punta_euros/kwh/hora']

    return {'coste_valle': energia_valle,
        'coste_llano': energia_llano,
        'coste_punta': energia_punta}

def tramo_libre(fila):

    datos = fila.to_dict() 

    energia_valle = datos['consumo_valle'] * datos['tc_valle_euros/kwh/hora']
    energia_llano = datos['consumo_llano'] * datos['tc_llano_euros/kwh/hora']
    energia_punta = datos['consumo_punta'] * datos['tc_punta_euros/kwh/hora']

    return {'coste_valle': energia_valle,
        'coste_llano': energia_llano,
        'coste_punta': energia_punta}


def tramo_dh(fila):

    datos = fila.to_dict() 

    energia_valle = datos['consumo_valle'] * datos['tc_8h_euros/kwh/hora']
    energia_llano = datos['consumo_llano'] * datos['tc_16h_euros/kwh/hora']
    energia_punta = datos['consumo_punta'] * datos['tc_16h_euros/kwh/hora']

    return {'coste_valle': energia_valle,
        'coste_llano': energia_llano,
        'coste_punta': energia_punta}


def calcular_total(fila):
    if fila['tipo'] == 'PVPC':
        return pvpc(fila, formulario)
    elif fila['tipo'] == 'TRAMOS':
        return tramos(fila, formulario)
    elif fila['tipo'] == 'DH':
        return dh(fila, formulario)
    else:
        return fija(fila, formulario)

def calcular_tramos(fila):
    if fila['tipo'] == 'PVPC':
        return tramo_pvpc(fila)
    elif fila['tipo'] == 'TRAMOS':
        return tramo_libre(fila)
    elif fila['tipo'] == 'DH':
        return tramo_dh(fila)
    else:
        return tramo_fija(fila)

calculo['total_factura'] = calculo.apply(calcular_total, axis=1)

calculo = calculo.join(calculo.apply(lambda fila: pd.Series(calcular_tramos(fila)), axis=1))

minimo = calculo[calculo['total_factura'] == calculo['total_factura'].min()].iloc[0]

print(f'Hemos encontrado esta tarifa: {minimo["tarifa"]} de {minimo["compania"]}')

dif_tarifa = minimo['total_actual'] - minimo['total_factura']

if dif_tarifa < 0:
    print('No existe una mejor tarifa actualmente.')
else:
    print(f'Mejoraría tu tarifa en {dif_tarifa:.2f}€')








# Crear la carpeta si no existe
if not os.path.exists(directory):
    os.makedirs(directory, exist_ok=True)

# Streamlit
st.title('Introduce tus datos manualmente')

dh = st.selectbox('¿Cuentas con una tarifa de discriminación horaria?', ('SI', 'NO'))
st.write('Tu tarifa', dh, 'cuenta con discriminación por tramos.')


potencia_punta = st.selectbox('¿Cuál es tu término de potencia en período punta?', ('3.3', '4.6', '5.5', '6.9'))
st.write('Potencia, período punta:', potencia_punta)



potencia_valle = st.selectbox('¿Cuál es tu término de potencia en período valle?', ('3.3', '4.6', '5.5', '6.9'))
st.write('Potencia, período valle:', potencia_valle)


total = st.number_input('¿Cuál ha sido el total de la factura? En €')
st.write('Total factura:', total)

consumo_punta = st.number_input('¿Cuál es tu consumo en período punta? En kW/h', min_value=0.0)
consumo_llano = st.number_input('¿Cuál es tu consumo en período llano? En kW/h', min_value=0.0)
consumo_valle = st.number_input('¿Cuál es tu consumo en período valle? En kW/h', min_value=0.0)
consumo_total = consumo_punta + consumo_llano + consumo_valle

st.write("<br>", unsafe_allow_html=True)

calculo_total = st.write(f'Tu consumo total es  {consumo_total} kW/h.')

st.write("<br>", unsafe_allow_html=True)



bono = st.selectbox('¿Su tarifa cuenta con el bono social?', ('SI','NO'))
st.write('Tu tarifa', bono, 'cuenta con bono social.')
st.write("<br>", unsafe_allow_html=True)
st.write("<br>", unsafe_allow_html=True)
# Botón para calcular la mejor tarifa
if st.button('Calcula la mejor tarifa'):

    # Crear DataFrame con discriminación horaria o sin ella
    datos_tarifas = pd.DataFrame({
        'Discriminación horaria': [dh],
        'Termino de potencia en valle': [potencia_valle],
        'Termino de potencia en punta': [potencia_punta],
        'Consumo en punta (kWh)': [consumo_punta],
        'Consumo en llano (kWh)': [consumo_llano],
        'Consumo en valle (kWh)': [consumo_valle],
        'Consumo total (kWh)': [consumo_total],
        'Bono social': [bono],
        'Total factura':[total]
    })


    # Comprobar si el archivo ya existe para actualizar o crear uno nuevo
    if os.path.exists(file_path):
        df_existente = pd.read_csv(file_path)
        df_actualizado = pd.concat([df_existente, datos_tarifas], ignore_index=True)
    else:
        df_actualizado = datos_tarifas

    # Guardar el DataFrame actualizado
    df_actualizado.to_csv(file_path, index=False)
    st.success("Datos guardados correctamente.")


#min dataframe

if dif_tarifa <= 0:
    st.write('No existe una mejor tarifa actualmente.')
else:
    st.write(f'La tarifa {minimo["tarifa"]} de {minimo["compania"]} mejoraría tu tarifa en {dif_tarifa:.2f}€') #min tarifa para datos dados) 
    






