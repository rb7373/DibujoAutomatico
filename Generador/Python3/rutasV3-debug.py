

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
factorCambio = 0.4

def getPunto(p0, p1, p2, p3, p4, p5, t):
        x = (pow(1-t,5))*p0[0]+(5*pow(1-t,4)*t)*p1[0]+(10*pow(1-t,3)*pow(t,2))*p2[0]+(10*pow(1-t,2)*pow(t,3))*p3[0]+(5*(1-t)*pow(t,4))*p4[0]+(pow(t,5))*p5[0]
        y = (pow(1-t,5))*p0[1]+(5*pow(1-t,4)*t)*p1[1]+(10*pow(1-t,3)*pow(t,2))*p2[1]+(10*pow(1-t,2)*pow(t,3))*p3[1]+(5*(1-t)*pow(t,4))*p4[1]+(pow(t,5))*p5[1]
        return [x,y]

def getCasteljau(pListaPuntos):
        print('lista puntos: ');
        t = 0.0
        listaResultante = []
        while t <= 1:
                t += factorCambio
                ##print ("t: ", t)
                puntoTemporal = getCasteljauPofloat(len(pListaPuntos)-1, 0, t,pListaPuntos)
                listaResultante.append(puntoTemporal)
                ##print('lista actual', listaResultante)
                ##print ("Punto generado: ", puntoTemporal)

        return listaResultante

def getCasteljauPofloat(r, i,t,pListaPuntos):
        
        if r == 0:
                return pListaPuntos[i]

        punto1 = getCasteljauPofloat(r - 1, i, t,pListaPuntos)
        punto2 = getCasteljauPofloat(r - 1, i + 1, t,pListaPuntos)

        x = ((1 - t) * punto1[0] + t * punto2[0])
        y = ((1 - t) * punto1[1] + t * punto2[1])

        return [factorEscala*x,factorEscala*y]

###print (getCasteljau([[14.270481,282.29694],[3.9297998,274.69121],[0.74775866,260.1491],[0.068879591,247.89146]]))
##0.06887959099999863, 247.89146],[0.69958944,215.59828],[7.7223231,183.84996],[10.674051,151.73844]]))

###print (getCasteljau([[0,0],[286.08295,0]]))
###print (getCasteljau([[286.08295000000015, 0.0],[286.08295,292.53186]]))

##Ruta secuencia de pasos

canvasHTML2 ='''
ctx.save();
ctx.translate(0,0);
ctx.beginPath();
ctx.moveTo(0,0);
ctx.lineTo(500,0);
ctx.lineTo(500,300);
ctx.lineTo(0,300);
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
ctx.save();
ctx.fillStyle = "#ffffff";
ctx.strokeStyle = "#000000";
ctx.miterLimit = 10;
ctx.beginPath();
ctx.moveTo(132.679,103.462);
ctx.bezierCurveTo(132.679,116.206,127.087,126.802,115.90700000000001,135.249);
ctx.bezierCurveTo(106.629,142.231,95.64300000000001,145.72299999999998,82.94800000000001,145.72299999999998);
ctx.bezierCurveTo(76.649,145.72299999999998,69.44600000000001,144.575,61.342000000000006,142.28099999999998);
ctx.bezierCurveTo(60.46300000000001,147.016,58.04600000000001,149.385,54.09100000000001,149.385);
ctx.bezierCurveTo(51.11200000000001,149.385,49.037000000000006,148.14,47.86500000000001,145.64999999999998);
ctx.bezierCurveTo(46.74100000000001,143.30599999999998,46.18000000000001,139.39899999999997,46.18000000000001,133.93099999999998);
ctx.bezierCurveTo(46.18000000000001,122.50499999999998,47.718,96.94399999999999,50.794000000000004,57.24599999999998);
ctx.lineTo(51.38,48.969999999999985);
ctx.bezierCurveTo(52.112,40.033999999999985,52.918,34.27399999999999,53.797000000000004,31.684999999999985);
ctx.bezierCurveTo(55.066,28.022999999999985,57.459,26.191999999999986,60.975,26.191999999999986);
ctx.bezierCurveTo(65.417,26.191999999999986,67.64,29.148999999999987,67.64,35.060999999999986);
ctx.bezierCurveTo(67.64,33.350999999999985,66.785,42.121999999999986,65.077,61.37399999999998);
ctx.bezierCurveTo(63.221,81.99499999999998,62.025,104.00799999999998,61.488,127.41299999999998);
ctx.bezierCurveTo(69.885,130.00199999999998,77.382,131.295,83.973,131.295);
ctx.bezierCurveTo(93.787,131.295,101.819,128.582,108.07,123.15399999999998);
ctx.bezierCurveTo(114.076,117.87299999999998,117.079,111.32099999999998,117.079,103.49599999999998);
ctx.bezierCurveTo(117.079,88.19099999999997,106.532,80.53799999999998,85.43799999999999,80.53799999999998);
ctx.bezierCurveTo(84.70599999999999,80.53799999999998,83.594,80.56299999999999,82.10499999999999,80.61099999999998);
ctx.bezierCurveTo(80.615,80.65999999999998,79.47999999999999,80.68399999999997,78.69899999999998,80.68399999999997);
ctx.bezierCurveTo(74.20599999999999,80.68399999999997,71.96099999999998,78.63299999999997,71.96099999999998,74.53199999999997);
ctx.bezierCurveTo(71.96099999999998,71.55399999999997,73.20599999999999,69.55199999999996,75.69599999999998,68.52599999999997);
ctx.bezierCurveTo(77.16099999999999,67.89199999999997,79.30899999999998,67.45299999999997,82.14099999999999,67.20799999999997);
ctx.bezierCurveTo(85.55799999999999,66.86699999999998,87.92699999999999,66.54899999999996,89.24499999999999,66.25599999999997);
ctx.bezierCurveTo(93.39399999999999,65.23099999999997,96.752,62.84999999999997,99.31599999999999,59.114999999999974);
ctx.bezierCurveTo(101.87999999999998,55.379999999999974,103.16099999999999,50.900999999999975,103.16099999999999,45.674999999999976);
ctx.bezierCurveTo(103.16099999999999,38.44899999999998,100.20599999999999,32.845999999999975,94.29899999999999,28.865999999999975);
ctx.bezierCurveTo(88.38999999999999,24.886999999999976,79.94399999999999,22.896999999999974,68.957,22.896999999999974);
ctx.bezierCurveTo(61.437,22.896999999999974,53.330999999999996,24.703999999999972,44.64099999999999,28.31699999999997);
ctx.bezierCurveTo(42.54099999999999,29.294999999999973,40.41699999999999,30.270999999999972,38.26899999999999,31.24699999999997);
ctx.bezierCurveTo(35.77899999999999,32.27199999999997,33.60699999999999,32.78499999999997,31.749999999999993,32.78499999999997);
ctx.bezierCurveTo(29.845999999999993,32.78499999999997,28.270999999999994,32.17499999999997,27.025999999999993,30.95399999999997);
ctx.bezierCurveTo(25.78099999999999,29.73399999999997,25.157999999999994,28.292999999999967,25.157999999999994,26.632999999999967);
ctx.bezierCurveTo(25.157999999999994,23.94799999999997,27.550999999999995,21.212999999999965,32.33599999999999,18.429999999999968);
ctx.bezierCurveTo(43.468999999999994,11.936999999999967,56.77399999999999,8.688999999999968,72.25299999999999,8.688999999999968);
ctx.bezierCurveTo(86.60799999999999,8.688999999999968,97.98499999999999,11.93699999999997,106.38399999999999,18.429999999999968);
ctx.bezierCurveTo(114.63499999999999,24.874999999999968,118.76199999999999,33.46999999999997,118.76199999999999,44.21099999999997);
ctx.bezierCurveTo(118.76199999999999,54.17199999999997,115.05099999999999,62.57099999999997,107.62899999999999,69.40599999999998);
ctx.bezierCurveTo(115.49,71.84799999999998,121.62899999999999,76.09599999999998,126.04899999999999,82.14999999999998);
ctx.bezierCurveTo(130.469,88.204,132.679,95.308,132.679,103.462);
ctx.closePath();
ctx.fill();
ctx.stroke();
ctx.restore();
ctx.restore();
ctx.restore();
'''



f = open("RUTAS-canvas-svg.txt", "w+")
f.write(str(canvasHTML2))
f.close()

##Se elimininan los canbios de linea
canvasHTML2 = canvasHTML2.replace("\n","")

##Se eliminina el ultimo ";" (queda vacio)
canvasHTML2 = canvasHTML2[:-1]

##Se separa cada instruccion
instrucciones = canvasHTML2.split(";")
###print (instrucciones)

rutas = []
rutaActual = []

firstPoint = [0,0]
lastPoint = [0,0]
originPathPoint = [0,0]
#puntoOrigen = [0,0]




i = 0
for instruccionActual in instrucciones:
        ##print ("Inst: ", i)
        ##print ("Inst: ", i, ": ", instruccionActual)
        i+=1

        if instruccionActual.find("translate") != -1:
                
                print ("translate")
                inicio = instruccionActual.find("(")
                final = instruccionActual.find(")")
                subInstruccion = instruccionActual[inicio+1:final]
                ##print ("SubIns :", subInstruccion)
                puntosObtenidos = subInstruccion.split(",")
                print ("Puntos obtenidos :", puntosObtenidos)
                ##print (subInstruccion) 
                #puntoOrigen[0] = float(puntosObtenidos[0]) ## TODO check
                #puntoOrigen[1] = float(puntosObtenidos[1])

        elif instruccionActual.find("beginPath") != -1:
                #reinicia los parametros del trazado, ejemplo strokeStyle="purple"; // Purple path
                print ("beginPath")
                
        elif instruccionActual.find("closePath") != -1:

                print ("closePath")

                puntos = getCasteljau([lastPoint,originPathPoint])

                print('---------')
                print(puntos)
                print('---------')
                
                rutaActual += puntos
                print('---subruta actual---')
                print(rutaActual)
                

                lastPoint[0] = originPathPoint[0]
                lastPoint[1] = originPathPoint[1]

                originPathPoint[0] = lastPoint[0] #Es codigo redundante pero necesario para mantener claro el algoritmo
                originPathPoint[1] = lastPoint[1] #Es codigo redundante pero necesario para mantener claro el algoritmo
                

        elif instruccionActual.find("moveTo") != -1:

                print ("moveTo")

                if len(rutaActual) != 0:
                        #Se agrega la ruta formada hasta el momento
                        rutas.append(rutaActual)                                

                #ReiniciaInicia la sub ruta actual                
                rutaActual = []
                
                #print ("-------reubicando coordenada de trazado-------")
                
                inicio = instruccionActual.find("(")
                final = instruccionActual.find(")")
                subInstruccion = instruccionActual[inicio+1:final]
                
                puntosObtenidos = subInstruccion.split(",")
                #print ("Puntos obtenidos :", puntosObtenidos)
                
                firstPoint[0] = float(puntosObtenidos[0])
                firstPoint[1] = float(puntosObtenidos[1])
                lastPoint[0] = float(puntosObtenidos[0])
                lastPoint[1] = float(puntosObtenidos[1])

                originPathPoint[0] = firstPoint[0]
                originPathPoint[1] = firstPoint[1]

                #Se agrega el primer punto de la subruta
                rutaActual.append( [firstPoint[0],firstPoint[1]] )

        elif instruccionActual.find("lineTo") != -1:
                
                print ("lineTo")
                inicio = instruccionActual.find("(")
                final = instruccionActual.find(")")
                subInstruccion = instruccionActual[inicio+1:final]
                ##print ("SubIns :", subInstruccion)
                puntosObtenidos = subInstruccion.split(",")
                #print ("Puntos obtenidos :", puntosObtenidos)
                #Se actualizan los puntos de referencia

                firstPoint[0] = lastPoint[0];
                firstPoint[1] = lastPoint[1];

                lastPoint[0] = float(puntosObtenidos[0])
                lastPoint[1] = float(puntosObtenidos[1])

                
                rutaActual += getCasteljau([firstPoint,lastPoint])

##                #print ("Ruta actual:", rutaActual)



                


        elif instruccionActual.find("scale") != -1:
                print ("scale")

        elif instruccionActual.find("strokeStyle") != -1:
                print ("strokeStyle")

        elif instruccionActual.find("lineCap") != -1:
                print ("lineCap")

        elif instruccionActual.find("lineJoin") != -1:
                print ("lineJoin")

        elif instruccionActual.find("miterLimit") != -1:
                print ('''"miterLimit"''')

        elif instruccionActual.find("fillStyle") != -1:
                print ('''fillStyle''')

        elif instruccionActual.find("bezierCurveTo") != -1:
                print ('''bezierCurveTo''')

                inicio = instruccionActual.find("(")
                final = instruccionActual.find(")")
                subInstruccion = instruccionActual[inicio+1:final]
                ##print ("SubIns :", subInstruccion)
                puntosObtenidos = subInstruccion.split(",")
                #print ("Puntos obtenidos :", puntosObtenidos)

##              Start point moveTo(20,20)
##              Control point 1 bezierCurveTo(20,100,200,100,200,20)
##              Control point 2 bezierCurveTo(20,100,200,100,200,20)
##              End point bezierCurveTo(20,100,200,100,200,20)

##              context.bezierCurveTo(cp1x,cp1y,cp2x,cp2y,x,y);

                cp1x =  float(puntosObtenidos[0])
                cp1y =  float(puntosObtenidos[1])
                cp2x =  float(puntosObtenidos[2])
                cp2y =  float(puntosObtenidos[3])
                endPointX =  float(puntosObtenidos[4])
                endPointY =  float(puntosObtenidos[5])

                #Se acualizan los puntos

                firstPoint[0] = lastPoint[0];
                firstPoint[1] = lastPoint[1];

                #Se actualizan los puntos de referencia

                puntosCasteljau = [[firstPoint[0],firstPoint[1]],
                                   [cp1x,cp1y],
                                   [cp2x,cp2y],
                                   [endPointX,endPointY]]

                rutaActual += getCasteljau(puntosCasteljau)

                lastPoint[0] = float(puntosObtenidos[4])
                lastPoint[1] = float(puntosObtenidos[5])

        else:
               print('Undefined instruction: ', instruccionActual)


if len(rutaActual) != 0:
        #Se agrega la ruta foramda hasta el momento
        rutas.append(rutaActual)                                

#ReiniciaInicia la sub ruta actual                
rutaActual = []

#print (rutas[1:])

#rutas = rutas[1:]
print('%%%%%%%%%%%%%%%%%%%%')
print('Total subrutas: ', len(rutas))
for ruta in rutas:
        print('Ruta: ', len(ruta))
        print(ruta)
        print('******************')

f = open("RUTAS.txt", "w+")
f.write(str(rutas))
f.close()

##
##archivo = open("rutas.txt", "w+")
##archivo.write();
##
### Close opend file
##archivo.close()
        
                
####print ("Rutas actuales: ",rutas)
##
###print ("Cantidad de rutas actuales: ",len(rutas))
###print ("RUTAS:")
###print (rutas[1:])
###print ("---------------")

##numeroRuta = 0
##
##for rutaTemporal in rutas:
##        #print ("Ruta: ", numeroRuta, " elementos: ",len(rutaTemporal))
##        #print ("---")
##        #print (rutaTemporal)
##        #print ("---")
##        numeroRuta+=1

        
##ctx.save();
##ctx.translate(0,0);
##ctx.beginPath();
##ctx.moveTo(0,0);
##ctx.lineTo(500,0);
##ctx.lineTo(500,300);
##ctx.lineTo(0,300);
##ctx.closePath();
##ctx.clip();
##ctx.translate(0,0);
##ctx.translate(0,0);
##ctx.scale(1,1);
##ctx.translate(0,0);
##ctx.strokeStyle = 'rgba(0,0,0,0)';
##ctx.lineCap = 'butt';
##ctx.lineJoin = 'miter';
##ctx.miterLimit = 4;
##ctx.save();
##ctx.save();
##ctx.fillStyle = "#ffffff";
##ctx.strokeStyle = "#000000";
##ctx.miterLimit = 10;
##ctx.beginPath();
##ctx.moveTo(132.679,103.462);
##ctx.bezierCurveTo(132.679,116.206,127.087,126.802,115.90700000000001,135.249);
##ctx.bezierCurveTo(106.629,142.231,95.64300000000001,145.72299999999998,82.94800000000001,145.72299999999998);
##ctx.bezierCurveTo(76.649,145.72299999999998,69.44600000000001,144.575,61.342000000000006,142.28099999999998);
##ctx.bezierCurveTo(60.46300000000001,147.016,58.04600000000001,149.385,54.09100000000001,149.385);
##ctx.bezierCurveTo(51.11200000000001,149.385,49.037000000000006,148.14,47.86500000000001,145.64999999999998);
##ctx.bezierCurveTo(46.74100000000001,143.30599999999998,46.18000000000001,139.39899999999997,46.18000000000001,133.93099999999998);
##ctx.bezierCurveTo(46.18000000000001,122.50499999999998,47.718,96.94399999999999,50.794000000000004,57.24599999999998);
##ctx.lineTo(51.38,48.969999999999985);
##ctx.bezierCurveTo(52.112,40.033999999999985,52.918,34.27399999999999,53.797000000000004,31.684999999999985);
##ctx.bezierCurveTo(55.066,28.022999999999985,57.459,26.191999999999986,60.975,26.191999999999986);
##ctx.bezierCurveTo(65.417,26.191999999999986,67.64,29.148999999999987,67.64,35.060999999999986);
##ctx.bezierCurveTo(67.64,33.350999999999985,66.785,42.121999999999986,65.077,61.37399999999998);
##ctx.bezierCurveTo(63.221,81.99499999999998,62.025,104.00799999999998,61.488,127.41299999999998);
##ctx.bezierCurveTo(69.885,130.00199999999998,77.382,131.295,83.973,131.295);
##ctx.bezierCurveTo(93.787,131.295,101.819,128.582,108.07,123.15399999999998);
##ctx.bezierCurveTo(114.076,117.87299999999998,117.079,111.32099999999998,117.079,103.49599999999998);
##ctx.bezierCurveTo(117.079,88.19099999999997,106.532,80.53799999999998,85.43799999999999,80.53799999999998);
##ctx.bezierCurveTo(84.70599999999999,80.53799999999998,83.594,80.56299999999999,82.10499999999999,80.61099999999998);
##ctx.bezierCurveTo(80.615,80.65999999999998,79.47999999999999,80.68399999999997,78.69899999999998,80.68399999999997);
##ctx.bezierCurveTo(74.20599999999999,80.68399999999997,71.96099999999998,78.63299999999997,71.96099999999998,74.53199999999997);
##ctx.bezierCurveTo(71.96099999999998,71.55399999999997,73.20599999999999,69.55199999999996,75.69599999999998,68.52599999999997);
##ctx.bezierCurveTo(77.16099999999999,67.89199999999997,79.30899999999998,67.45299999999997,82.14099999999999,67.20799999999997);
##ctx.bezierCurveTo(85.55799999999999,66.86699999999998,87.92699999999999,66.54899999999996,89.24499999999999,66.25599999999997);
##ctx.bezierCurveTo(93.39399999999999,65.23099999999997,96.752,62.84999999999997,99.31599999999999,59.114999999999974);
##ctx.bezierCurveTo(101.87999999999998,55.379999999999974,103.16099999999999,50.900999999999975,103.16099999999999,45.674999999999976);
##ctx.bezierCurveTo(103.16099999999999,38.44899999999998,100.20599999999999,32.845999999999975,94.29899999999999,28.865999999999975);
##ctx.bezierCurveTo(88.38999999999999,24.886999999999976,79.94399999999999,22.896999999999974,68.957,22.896999999999974);
##ctx.bezierCurveTo(61.437,22.896999999999974,53.330999999999996,24.703999999999972,44.64099999999999,28.31699999999997);
##ctx.bezierCurveTo(42.54099999999999,29.294999999999973,40.41699999999999,30.270999999999972,38.26899999999999,31.24699999999997);
##ctx.bezierCurveTo(35.77899999999999,32.27199999999997,33.60699999999999,32.78499999999997,31.749999999999993,32.78499999999997);
##ctx.bezierCurveTo(29.845999999999993,32.78499999999997,28.270999999999994,32.17499999999997,27.025999999999993,30.95399999999997);
##ctx.bezierCurveTo(25.78099999999999,29.73399999999997,25.157999999999994,28.292999999999967,25.157999999999994,26.632999999999967);
##ctx.bezierCurveTo(25.157999999999994,23.94799999999997,27.550999999999995,21.212999999999965,32.33599999999999,18.429999999999968);
##ctx.bezierCurveTo(43.468999999999994,11.936999999999967,56.77399999999999,8.688999999999968,72.25299999999999,8.688999999999968);
##ctx.bezierCurveTo(86.60799999999999,8.688999999999968,97.98499999999999,11.93699999999997,106.38399999999999,18.429999999999968);
##ctx.bezierCurveTo(114.63499999999999,24.874999999999968,118.76199999999999,33.46999999999997,118.76199999999999,44.21099999999997);
##ctx.bezierCurveTo(118.76199999999999,54.17199999999997,115.05099999999999,62.57099999999997,107.62899999999999,69.40599999999998);
##ctx.bezierCurveTo(115.49,71.84799999999998,121.62899999999999,76.09599999999998,126.04899999999999,82.14999999999998);
##ctx.bezierCurveTo(130.469,88.204,132.679,95.308,132.679,103.462);
##ctx.closePath();
##ctx.fill();
##ctx.stroke();
##ctx.restore();
##ctx.restore();
##ctx.restore();





        
                
        
