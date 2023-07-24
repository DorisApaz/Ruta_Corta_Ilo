self.tabla.delete(*self.tabla.get_children())
        i = -1
        for dato in nombre_buscado:
            i= i+1                       
            self.tabla.insert('',i, text = nombre_buscado[i][1:2], values=nombre_buscado[i][2:6])
    def mostrar_todo(self):
        self.tabla.delete(*self.tabla.get_children())
        registro = self.base_datos.mostrar_producto()
        for dato in registro:
            codigo = dato[0]
            nombre = dato[1]
            modelo = dato[2]
            precio = dato[3]
            cantidad = dato[4]
            self.tabla.insert('', 'end', text=codigo, values=(nombre, modelo, precio, cantidad))
    def eliminar_fila(self):
        val=messagebox.askyesno("Eliminar fila","Â¿Desea eliminar la fila seleccionada?")
        if val==True:
            fila = self.tabla.selection()
            if len(fila) !=0:        
                self.tabla.delete(fila)
                nombre = ("'"+ str(self.nombre_borar) + "'")       
                self.base_datos.elimina_producto(nombre)
            else:
                messagebox.askretrycancel("Error","Seleccione la fila a eliminar")
    def obtener_fila(self, event):
        current_item = self.tabla.focus()
        if not current_item:
            return
        data = self.tabla.item(current_item)
        self.nombre_borar = data['values'][0]
#root--------------------------------------------------------------------------------------
root = Tk()
root.wm_title("Registro de Datos en MySQL")
root.config(bg='gray22')
root.geometry('900x500')
et = tk.Label(root, text="R E G I S T R O \t D E \t D A T O S", bg="grey22", fg="white", font=('Orbitron',15,'bold'))
et.place(y=8,x=270)
root.resizable(0,0)
app = Ventana(root)
app.mainloop()