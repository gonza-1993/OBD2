import obd

def main():
    try:
        # Especifica el puerto serial en el que está conectado el adaptador
        port = "/dev/ttyUSB0"  # Cambia este valor si el adaptador está en otro puerto

        # Conectar al adaptador OBD-II usando el puerto serial especificado
        connection = obd.OBD(port)

        if connection.is_connected():
            print("Conexión OBD-II exitosa.")
            
            # Comando para leer códigos de error
            cmd = obd.commands.GET_DTC

            # Enviar el comando
            response = connection.query(cmd)

            # Obtener los códigos de error
            if response.value:
                dtc_codes = response.value
                print("Códigos de error:")
                for code in dtc_codes:
                    print(code)

                # Visualizar los códigos de error usando matplotlib
                import matplotlib.pyplot as plt
                plt.figure(figsize=(10, 6))
                plt.bar(range(len(dtc_codes)), [1] * len(dtc_codes), tick_label=[str(code) for code in dtc_codes])
                plt.xlabel('Códigos de error')
                plt.ylabel('Ocurrencias')
                plt.title('Códigos de error OBD-II')
                plt.xticks(rotation=45)  # Rotar las etiquetas para mejor visualización
                plt.tight_layout()  # Ajustar el diseño para que no se corten las etiquetas
                plt.show()

            else:
                print("No se encontraron códigos de error")
        
        else:
            print("No se pudo conectar al adaptador OBD-II.")
        
    except PermissionError:
        print("Permiso denegado para acceder al puerto serial. Asegúrate de que tu usuario tenga permisos adecuados.")
    except Exception as e:
        print(f"Se produjo un error: {e}")

    finally:
        try:
            connection.close()  # Asegúrate de cerrar la conexión
        except:
            pass

if __name__ == "__main__":
    main()
