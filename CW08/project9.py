import datetime

# =====================================================================
# 1. INPUT (Configuración inicial en variables directas)
# =====================================================================
usuario_nombre = "Carlos"
usuario_puntos = 0
usuario_dinero_digital = 0.0
usuario_personalizaciones = []
usuario_castigos = 0

fuente_calendario = "externo_api"
sonido_configurado = "Efecto_Campanas.wav"
imagen_fondo_configurada = "Playa_Paradisiaca.png"

# Datos de la actividad que el usuario "metió" al sistema
actividad_nombre = "Ir al gimnasio y cardio"
actividad_color = "Verde"
actividad_tipo_regalo = "puntos"  # Puede ser: puntos, dinero_digital, personalizacion
actividad_minutos_antes = 10      # Número natural

# Simulamos que la actividad es en 10 minutos, así que la alarma debe sonar ¡YA!
hora_actual = datetime.datetime.now()
actividad_fecha_hora = hora_actual + datetime.timedelta(minutes=10)

# =====================================================================
# 2. PROCESS (Cálculos y evaluación de condiciones)
# =====================================================================
# Calcular el momento exacto de la alarma
tiempo_alarma = actividad_fecha_hora - datetime.timedelta(minutes=actividad_minutos_antes)
actividad_completada = False

print(f"🚀 Sincronizando con calendario: [{fuente_calendario.upper()}]")
print(f"📅 Actividad registrada: '{actividad_nombre}'")
print(f"⏰ [Reloj Sistema]: {hora_actual.strftime('%H:%M')} | Alarma programada: {tiempo_alarma.strftime('%H:%M')}")

# Verificamos si la hora actual coincide o ya pasó la hora de la alarma
if hora_actual >= tiempo_alarma and not actividad_completada:
    
    # =====================================================================
    # 3. OUTPUT (Interfaz en pantalla y captura de decisión)
    # =====================================================================
    print("\n" + "="*50)
    print(f"📺 [PANTALLA] Mostrando color de actividad: {actividad_color.upper()}")
    print(f"🖼️ [PANTALLA] Fondo de pantalla actual: {imagen_fondo_configurada}")
    print(f"🔊 [AUDIO] 🎵 ¡Sonando: {sonido_configurado}! 🎵")
    print(f"📝 [ACTIVIDAD]: {actividad_nombre}")
    print("="*50)

    print("\n[Botones en pantalla]: 1. Completar | 2. Posponer")
    opcion = input("Elige una opción (1 o 2): ")

    # Consecuencias de la acción del usuario
    if opcion == "1":
        print("\n✅ Acción: Completar")
        actividad_completada = True
        
        # Procesar recompensa según el tipo elegido
        if actividad_tipo_regalo == "puntos":
            usuario_puntos += 100
            print(f"🎉 ¡Ganaste 100 puntos! Total: {usuario_puntos}")
        elif actividad_tipo_regalo == "dinero_digital":
            usuario_dinero_digital += 5.0
            print(f"💰 ¡Dinero digital desbloqueado! Total: ${usuario_dinero_digital}")
        elif actividad_tipo_regalo == "personalizacion":
            usuario_personalizaciones.append("Fondo Especial Animado")
            print(f"✨ ¡Nueva personalización desbloqueada!")

    elif opcion == "2":
        print("\n❌ Acción: Posponer")
        usuario_castigos += 1
        print(f"⚠️ ¡Penalización aplicada por posponer! Total de faltas: {usuario_castigos}")
        
        # Reprogramar sumando 5 minutos al futuro
        tiempo_alarma = tiempo_alarma + datetime.timedelta(minutes=5)
        print(f"🔄 Alarma reprogramada para las: {tiempo_alarma.strftime('%H:%M')}")
        
    else:
        print("\nOpción inválida. No se detectó respuesta correcta.")