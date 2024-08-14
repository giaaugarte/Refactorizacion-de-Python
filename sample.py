while True:
    print( 'Seleccione el proceso que desea aplicar' )
    print( '1: Introduzca los puntos de valoración y los comentarios.' )
    print( '2: Comprueba los resultados obtenidos hasta ahora.' )
    print( '3: Terminación.' )
    num = input()
    if num.isdecimal():
        num = int(num)
        if  1 <= num <= 3:
            print('Procesando...')
        else:
            print('Por favor, introduzca de 1 al 3')
    

        if num == 1:
            def obtener_puntuacion():
                while True:
                    print('Por favor, introduzca una puntuación en una escala de 1 a 5')
                    point = input()
                    if point.isdecimal():
                        point = int(point)
                        if 1 <= point <= 5: # Expresión condicional que es menor que 0 o mayor que 5
                            return point
                        else:
                            print( 'Indíquelo en una escala de 1 a 5' )

            def obtener_comentario():
                print('Introduzca sus comentarios.') 
                comment = input()
                return comment 
                

            def obtener_post(point, comment): 
                post = f'punto: {point} comentario: {comment}'
                file_pc = open("data.txt", 'a')
                file_pc.write( f'{ post } \n' )
                file_pc.close()    
        
            point = obtener_puntuacion()
            comment = obtener_comentario()
            obtener_post(point, comment)
        
        elif num == 2:
            
            print( 'Resultados hasta la fecha.' )
            read_file = open("data.txt", "r")
            print( read_file.read() )
            read_file.close()
        elif num == 3:
            print( 'Terminación.' )
            break  # Sintaxis para terminar un proceso iterativo.
        
    



  