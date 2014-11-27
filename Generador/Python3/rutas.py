

#getPunto ([0,0],[0.2,1],[1,1],[1,0.2],[2,0.2],[2,1],0.17)
#[0.287,0.576]

##Start point moveTo(20,20)
##Control point 1 bezierCurveTo(20,100,200,100,200,20)
##Control point 2 bezierCurveTo(20,100,200,100,200,20)
##End point bezierCurveTo(20,100,200,100,200,20) 
##getCasteljau ([[20,20],[20,100],[200,100],[200,20]])
##[[Start point], [Control point 1], [Control point 2], [End point]]


listaPuntosTemp = [[0,0],[0.2,1],[1,1],[1,0.2],[2,0.2],[2,1]]

factorEscala = 1
factorCambioOriginal = 0.001
factorCambio = 0.05

def getPunto(p0, p1, p2, p3, p4, p5, t):
        x = (pow(1-t,5))*p0[0]+(5*pow(1-t,4)*t)*p1[0]+(10*pow(1-t,3)*pow(t,2))*p2[0]+(10*pow(1-t,2)*pow(t,3))*p3[0]+(5*(1-t)*pow(t,4))*p4[0]+(pow(t,5))*p5[0]
        y = (pow(1-t,5))*p0[1]+(5*pow(1-t,4)*t)*p1[1]+(10*pow(1-t,3)*pow(t,2))*p2[1]+(10*pow(1-t,2)*pow(t,3))*p3[1]+(5*(1-t)*pow(t,4))*p4[1]+(pow(t,5))*p5[1]
        return [x,y]

def getCasteljau(pListaPuntos):
        t = 0.0
        listaResultante = []
        while t <= 1:
                t += factorCambio
                #print ("t: ", t)
                puntoTemporal = getCasteljauPofloat(len(pListaPuntos)-1, 0, t,pListaPuntos)
                listaResultante.append(puntoTemporal)
                #print ("Punto generado: ", puntoTemporal)

        return listaResultante

def getCasteljauPofloat(r, i,t,pListaPuntos):
        
        if r == 0:
                return pListaPuntos[i]

        punto1 = getCasteljauPofloat(r - 1, i, t,pListaPuntos)
        punto2 = getCasteljauPofloat(r - 1, i + 1, t,pListaPuntos)

        x = ((1 - t) * punto1[0] + t * punto2[0])
        y = ((1 - t) * punto1[1] + t * punto2[1])

        return [factorEscala*x,factorEscala*y]

##print (getCasteljau([[14.270481,282.29694],[3.9297998,274.69121],[0.74775866,260.1491],[0.068879591,247.89146]]))
##0.06887959099999863, 247.89146],[0.69958944,215.59828],[7.7223231,183.84996],[10.674051,151.73844]]))

##print (getCasteljau([[0,0],[286.08295,0]]))
##print (getCasteljau([[286.08295000000015, 0.0],[286.08295,292.53186]]))

##Ruta secuencia de pasos

canvasHTML = '''ctx.save();
ctx.translate(0,0);
ctx.beginPath();
ctx.moveTo(0,0);
ctx.lineTo(300,0);
ctx.lineTo(300,200);
ctx.lineTo(0,200);
ctx.closePath();
ctx.clip();
ctx.translate(0,0);
ctx.translate(0,0);
ctx.scale(1,1);
ctx.translate(0,0);
ctx.strokeStyle = 'rgba(0,0,0,0)';
ctx.lineCap = 'butt';
ctx.lineJoin = 'miter';
ctx.miterLimit = 4;
ctx.save();
ctx.fillStyle = "#ffffff";
ctx.strokeStyle = "#000000";
ctx.miterLimit = 10;
ctx.beginPath();
ctx.moveTo(18.62,7.271);
ctx.bezierCurveTo(18.748,7.655,18.692,7.983,18.452,8.254999999999999);
ctx.bezierCurveTo(18.213,8.527,17.901000000000003,8.662999999999998,17.516000000000002,8.662999999999998);
ctx.bezierCurveTo(16.971,8.662999999999998,16.62,8.383,16.46,7.822999999999999);
ctx.bezierCurveTo(16.299,7.262999999999998,15.963000000000001,6.822999999999999,15.451,6.502999999999998);
ctx.bezierCurveTo(14.939,6.183999999999998,14.379000000000001,6.022999999999998,13.771,6.022999999999998);
ctx.bezierCurveTo(13.035,6.022999999999998,12.411000000000001,6.262999999999998,11.9,6.741999999999998);
ctx.bezierCurveTo(11.387,7.220999999999998,11.131,7.907999999999998,11.131,8.802999999999997);
ctx.lineTo(11.131,15.033999999999997);
ctx.lineTo(17.419,13.366999999999997);
ctx.bezierCurveTo(17.803,13.239999999999997,18.122,13.296999999999997,18.379,13.537999999999997);
ctx.bezierCurveTo(18.634,13.778999999999996,18.763,14.093999999999998,18.763,14.480999999999996);
ctx.bezierCurveTo(18.763,14.997999999999996,18.509,15.352999999999996,18,15.545999999999996);
ctx.lineTo(11.131,17.372999999999998);
ctx.lineTo(11.131,35.111);
ctx.bezierCurveTo(11.131,35.464,11.018,35.733999999999995,10.795,35.927);
ctx.bezierCurveTo(10.57,36.117,10.315,36.214,10.027,36.214);
ctx.bezierCurveTo(9.258999999999999,36.214,8.875,35.845,8.875,35.11);
ctx.lineTo(8.875,18.07);
ctx.lineTo(4.411,19.222);
ctx.bezierCurveTo(3.9949999999999997,19.35,3.659,19.294,3.4029999999999996,19.054000000000002);
ctx.bezierCurveTo(3.1469999999999994,18.814000000000004,3.0189999999999997,18.502000000000002,3.0189999999999997,18.118000000000002);
ctx.bezierCurveTo(3.0189999999999997,17.607000000000003,3.3069999999999995,17.254,3.8829999999999996,17.062);
ctx.lineTo(8.876,15.7);
ctx.lineTo(8.876,8.799);
ctx.bezierCurveTo(8.876,7.201,9.347999999999999,5.9639999999999995,10.292,5.084999999999999);
ctx.bezierCurveTo(11.236,4.206999999999999,12.364,3.767999999999999,13.676,3.767999999999999);
ctx.bezierCurveTo(14.764,3.767999999999999,15.780000000000001,4.079999999999999,16.724,4.703999999999999);
ctx.bezierCurveTo(17.667,5.327,18.299,6.184,18.62,7.271);
ctx.closePath();
ctx.fill();
ctx.stroke();
ctx.restore();
ctx.restore();'''

canvasHTML2 ='''var draw = function(ctx) {
ctx.save();
ctx.translate(0,0);
ctx.beginPath();
ctx.moveTo(0,0);
ctx.lineTo(300,0);
ctx.lineTo(300,200);
ctx.lineTo(0,200);
ctx.closePath();
ctx.clip();
ctx.translate(0,0);
ctx.translate(0,0);
ctx.scale(1,1);
ctx.translate(0,0);
ctx.strokeStyle = 'rgba(0,0,0,0)';
ctx.lineCap = 'butt';
ctx.lineJoin = 'miter';
ctx.miterLimit = 4;
ctx.save();
ctx.fillStyle = "#ffffff";
ctx.strokeStyle = "#000000";
ctx.miterLimit = 10;
ctx.beginPath();
ctx.moveTo(18.62,7.271);
ctx.bezierCurveTo(18.748,7.655,18.692,7.983,18.452,8.254999999999999);
ctx.bezierCurveTo(18.213,8.527,17.901000000000003,8.662999999999998,17.516000000000002,8.662999999999998);
ctx.bezierCurveTo(16.971,8.662999999999998,16.62,8.383,16.46,7.822999999999999);
ctx.bezierCurveTo(16.299,7.262999999999998,15.963000000000001,6.822999999999999,15.451,6.502999999999998);
ctx.bezierCurveTo(14.939,6.183999999999998,14.379000000000001,6.022999999999998,13.771,6.022999999999998);
ctx.bezierCurveTo(13.035,6.022999999999998,12.411000000000001,6.262999999999998,11.9,6.741999999999998);
ctx.bezierCurveTo(11.387,7.220999999999998,11.131,7.907999999999998,11.131,8.802999999999997);
ctx.lineTo(11.131,15.033999999999997);
ctx.lineTo(17.419,13.366999999999997);
ctx.bezierCurveTo(17.803,13.239999999999997,18.122,13.296999999999997,18.379,13.537999999999997);
ctx.bezierCurveTo(18.634,13.778999999999996,18.763,14.093999999999998,18.763,14.480999999999996);
ctx.bezierCurveTo(18.763,14.997999999999996,18.509,15.352999999999996,18,15.545999999999996);
ctx.lineTo(11.131,17.372999999999998);
ctx.lineTo(11.131,35.111);
ctx.bezierCurveTo(11.131,35.464,11.018,35.733999999999995,10.795,35.927);
ctx.bezierCurveTo(10.57,36.117,10.315,36.214,10.027,36.214);
ctx.bezierCurveTo(9.258999999999999,36.214,8.875,35.845,8.875,35.11);
ctx.lineTo(8.875,18.07);
ctx.lineTo(4.411,19.222);
ctx.bezierCurveTo(3.9949999999999997,19.35,3.659,19.294,3.4029999999999996,19.054000000000002);
ctx.bezierCurveTo(3.1469999999999994,18.814000000000004,3.0189999999999997,18.502000000000002,3.0189999999999997,18.118000000000002);
ctx.bezierCurveTo(3.0189999999999997,17.607000000000003,3.3069999999999995,17.254,3.8829999999999996,17.062);
ctx.lineTo(8.876,15.7);
ctx.lineTo(8.876,8.799);
ctx.bezierCurveTo(8.876,7.201,9.347999999999999,5.9639999999999995,10.292,5.084999999999999);
ctx.bezierCurveTo(11.236,4.206999999999999,12.364,3.767999999999999,13.676,3.767999999999999);
ctx.bezierCurveTo(14.764,3.767999999999999,15.780000000000001,4.079999999999999,16.724,4.703999999999999);
ctx.bezierCurveTo(17.667,5.327,18.299,6.184,18.62,7.271);
ctx.closePath();
ctx.fill();
ctx.stroke();
ctx.restore();
ctx.restore();
};
'''

puntoActual = [0,0]
puntoOrigen = [0,0]

##Se elimininan los canbios de linea
canvasHTML2 = canvasHTML2.replace("\n","")

##Se eliminina el ultimo ";" (queda vacio)
canvasHTML2 = canvasHTML2[:-1]

##Se separa cada instruccion
instrucciones = canvasHTML2.split(";")
##print (instrucciones)

rutas = []
rutaActual = []

puntoInicial = [0,0]
puntoFinal = [0,0]
puntoActual = [0,0]
puntoSiguiente = [0,0]

puntoOrigenRuta = [0,0]


i = 0
for instruccionActual in instrucciones:
        #print ("Inst: ", i)
        #print ("Inst: ", i, ": ", instruccionActual)
        i+=1

        if instruccionActual.find("translate") != -1:
                
                print ("trasladando coordenadas")
                inicio = instruccionActual.find("(")
                final = instruccionActual.find(")")
                subInstruccion = instruccionActual[inicio+1:final]
                #print ("SubIns :", subInstruccion)
                puntosObtenidos = subInstruccion.split(",")
                print ("Puntos obtenidos :", puntosObtenidos)
                #print (subInstruccion) 
                puntoOrigen[0] = float(puntosObtenidos[0])
                puntoOrigen[1] = float(puntosObtenidos[1])

        elif instruccionActual.find("beginPath") != -1:
                #reinicia los parametros del trazado, ejemplo strokeStyle="purple"; // Purple path
                print ("iniciando nuevo trazo")
                
        elif instruccionActual.find("closePath") != -1:

                print ("cerrando trazo")
                
                rutaActual += getCasteljau([puntoFinal,puntoOrigenRuta])

                puntoFinal[0] = puntoOrigenRuta[0]
                puntoFinal[1] = puntoOrigenRuta[1]
                
                rutas+=rutaActual
                

        elif instruccionActual.find("moveTo") != -1:

                rutas += rutaActual

                rutaActual = []
                
                print ("reubicando coordenada de trazado")
                
                inicio = instruccionActual.find("(")
                final = instruccionActual.find(")")
                subInstruccion = instruccionActual[inicio+1:final]
                
                puntosObtenidos = subInstruccion.split(",")
                print ("Puntos obtenidos :", puntosObtenidos)
                
                puntoInicial[0] = float(puntosObtenidos[0])
                puntoInicial[1] = float(puntosObtenidos[1])
                puntoFinal[0] = float(puntosObtenidos[0])
                puntoFinal[1] = float(puntosObtenidos[1])

                puntoOrigenRuta[0] = puntoInicial[0]
                puntoOrigenRuta[1] = puntoInicial[1]

        elif instruccionActual.find("lineTo") != -1:
                
                print ("trazando linea recta")
                inicio = instruccionActual.find("(")
                final = instruccionActual.find(")")
                subInstruccion = instruccionActual[inicio+1:final]
                #print ("SubIns :", subInstruccion)
                puntosObtenidos = subInstruccion.split(",")
                print ("Puntos obtenidos :", puntosObtenidos)
                #Se actualizan los puntos de referencia

                puntoFinal[0] = float(puntosObtenidos[0])
                puntoFinal[1] = float(puntosObtenidos[1])

                rutaActual.append( [puntoInicial[0],puntoInicial[1]] )
                rutaActual += getCasteljau([puntoInicial,puntoFinal])

##                print ("Ruta actual:", rutaActual)

                puntoInicial[0] = puntoFinal[0];
                puntoInicial[1] = puntoFinal[1];

                


        elif instruccionActual.find("scale") != -1:
                print ("cambio de escala")

        elif instruccionActual.find("strokeStyle") != -1:
                print ("cambio de estilo de borde")

        elif instruccionActual.find("lineCap") != -1:
                print ("cambio de estilo fin de borde")

        elif instruccionActual.find("lineJoin") != -1:
                print ("cambio de estilo de union de linea")

        elif instruccionActual.find("miterLimit") != -1:
                print ('''cambio de estilo "miterLimit"''')

        elif instruccionActual.find("fillStyle") != -1:
                print ('''cambio de estilo de relleno''')


        
                
###print ("Rutas actuales: ",rutas)
##
print ("Cantidad de rutas actuales: ",len(rutas))
numeroRuta = 0
##
for rutaTemporal in rutas:
        print ("Ruta: ", numeroRuta)
        print ("---")
        print (rutaTemporal)
        print ("---")
        numeroRuta+=1
        






        
                
        
