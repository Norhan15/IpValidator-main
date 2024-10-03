import tkinter as tk
from tkinter import filedialog, messagebox
import csv

class IPValidator:
    FINAL_STATES = {'q33', 'q36', 'q38', 'q34', 'q37', 'q39', 'q13', 'q40', 'q49', 'q53'}

    def __init__(self):
        self.current_state = 'q0'

    def is_letter_or_digit(self, char):
        return char.isalnum()

    def transition(self, char):
        # Aquí implementa la lógica de transición de estados
        if self.current_state == 'q0':
            if char.isdigit():
                self.current_state = 'q1'  # Asumiendo que q1 es un estado válido después de un dígito
                return True
            else:
                return False
        # Agrega más lógica para otros estados y caracteres
        # Ejemplo simple
        elif self.current_state == 'q1':
            if char == '.':
                self.current_state = 'q2'
                return True
            elif char.isdigit():
                self.current_state = 'q1'  # Permitir dígitos consecutivos
                return True
        # Continuar definiendo la lógica para todos los estados...
        # Recuerda volver a 'q0' para el inicio de una nueva sección de IP
        return False

    def is_valid_ip(self):
        return self.current_state in self.FINAL_STATES

    def reset(self):
        self.current_state = 'q0'

    def validate_ip(self, ip_string):
        self.reset()
        for char in ip_string:
            if not self.transition(char):
                return False, f"Error: La IP '{ip_string}' falló en el estado '{self.current_state}' con el carácter '{char}'"
        if self.is_valid_ip():
            return True, f"La IP '{ip_string}' es válida"
        else:
            return False, f"La IP '{ip_string}' no alcanzó un estado final válido"


class IpApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Validador de IPs")
        self.validator = IPValidator()
        self.valid_ips = []
        self.invalid_ips = []

        # Botón para cargar archivo
        self.load_button = tk.Button(root, text="Cargar archivo de IPs", command=self.load_file)
        self.load_button.pack(pady=10)

        # Área de texto para mostrar resultados
        self.text_area = tk.Text(root, width=50, height=20)
        self.text_area.pack(pady=10)

        # Botón para generar el reporte
        self.report_button = tk.Button(root, text="Generar reporte CSV", command=self.generate_report)
        self.report_button.pack(pady=10)

    def load_file(self):
        file_path = filedialog.askopenfilename(title="Selecciona un archivo", filetypes=[("Text files", "*.txt")])
        if file_path:
            self.valid_ips.clear()
            self.invalid_ips.clear()
            self.text_area.delete(1.0, tk.END)  # Limpiar el área de texto

            with open(file_path, 'r') as file:
                for line in file:
                    ip = line.strip()
                    if ip:  # Asegurarse de que no sea una línea vacía
                        valid, message = self.validator.validate_ip(ip)
                        if valid:
                            self.valid_ips.append(ip)
                        else:
                            self.invalid_ips.append(ip)
                        self.text_area.insert(tk.END, message + "\n")

    def generate_report(self):
        report_path = filedialog.asksaveasfilename(defaultextension=".csv", title="Guardar reporte", filetypes=[("CSV files", "*.csv")])
        if report_path:
            with open(report_path, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["IP", "Estado"])
                for ip in self.valid_ips:
                    writer.writerow([ip, "Válida"])
                for ip in self.invalid_ips:
                    writer.writerow([ip, "No válida"])
            messagebox.showinfo("Reporte generado", "El reporte se ha generado correctamente.")

if __name__ == "__main__":
    root = tk.Tk()
    app = IpApp(root)
    root.mainloop()
