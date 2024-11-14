def heartRate(fc):
    
    if fc >= 50 and fc <=80:
        return "Treino aeróbico"
    elif fc > 80 and fc <=100:
        return "Treino Cardiovascular"
    elif fc >100 and fc <=120:
        return "Treino Aeróbico Ideal"
    elif fc > 120 and fc <=140:
        return "Treino Anaeróbico"
    else: 
        return "Womp Womp"
    
fc = int(input("Introduza a Frquência Cardíaca: "))
print(heartRate(fc))