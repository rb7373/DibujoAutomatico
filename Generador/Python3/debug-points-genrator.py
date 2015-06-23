

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
##factorCambioOriginal = 0.001
factorCambio = 0.4
condition = False;

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
                print('lista actual', listaResultante)
                print ("Punto generado: ", puntoTemporal)

        return listaResultante

def getCasteljauPofloat(r, i,t,pListaPuntos):
        
        if r == 0:
                return pListaPuntos[i]

        punto1 = getCasteljauPofloat(r - 1, i, t,pListaPuntos)
        punto2 = getCasteljauPofloat(r - 1, i + 1, t,pListaPuntos)

        x = ((1 - t) * punto1[0] + t * punto2[0])
        y = ((1 - t) * punto1[1] + t * punto2[1])

        return [factorEscala*x,factorEscala*y]

print ('getCasteljau: ', getCasteljau([[14.270481,282.29694],[3.9297998,274.69121],[0.74775866,260.1491],[0.068879591,247.89146]]))
#[[4.999860197504001, 270.430736], [0.8138303048319997, 255.44641360000003], [-0.07531222579199992, 240.88477920000003]]

###print (getCasteljau([[0,0],[286.08295,0]]))
###print (getCasteljau([[286.08295000000015, 0.0],[286.08295,292.53186]]))
