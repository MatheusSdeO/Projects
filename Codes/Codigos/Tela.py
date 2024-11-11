import tkinter as tk
import pyautogui
import time
import threading

# Variável de controle para o rastreamento da posição do cursor
tracking = False
identified_window = None  # Variável global para armazenar a janela identificada

# Listas para armazenar as posições do cursor e as teclas identificadas
cursor_positions = []
identified_keys = []

# Variável para armazenar a posição anterior do cursor
previous_position = None

# Função para capturar e exibir a posição do cursor na nova janela
def show_mouse_position(label):
    global tracking, previous_position
    tracking = True
    previous_position = pyautogui.position()  # Posição inicial do cursor
    last_movement_time = time.time()  # Tempo do último movimento

    try:
        while tracking:
            curser_pos = pyautogui.position()
            label.config(text=f'Posição do cursor: {curser_pos}')
            if curser_pos != previous_position:  # Verifica se a posição mudou
                last_movement_time = time.time()  # Atualiza o tempo do último movimento
                previous_position = curser_pos  # Atualiza a posição anterior

            # Verifica se o cursor não se moveu por 2.5 segundos
            if time.time() - last_movement_time > 2.5:
                tracking = False  # Para o rastreamento
                cursor_positions.append(curser_pos)  # Armazena a posição
                show_message("Valor salvo")  # Exibe a mensagem "Valor salvo"
            time.sleep(0.1)  # Pequeno delay para evitar muitas atualizações
    except KeyboardInterrupt:
        print('Interrupção pelo usuário')

# Função para mostrar mensagens na tela
def show_message(message):
    message_window = tk.Toplevel(root)
    message_window.title("Mensagem")
    message_window.geometry("200x100")  # Tamanho ajustado da janela de mensagem
    message_window.configure(bg="#f0f0f0")  # Cor de fundo

    label = tk.Label(message_window, text=message, font=("Arial", 12), bg="#f0f0f0")
    label.pack(expand=True)

    # Fechar automaticamente após 2 segundos
    message_window.after(2000, message_window.destroy)

# Função para iniciar a captura de posição do cursor e abrir nova janela para exibir coordenadas
def start_cursor_position_tracking():
    # Criar uma nova janela para exibir as coordenadas
    position_window = tk.Toplevel(root)
    position_window.title("Rastreamento do Cursor")
    position_window.geometry("400x200")  # Tamanho ajustado da nova janela
    position_window.configure(bg="#f0f0f0")  # Cor de fundo

    # Rótulo para mostrar a posição do cursor
    position_label = tk.Label(position_window, text="Posição do cursor:", font=("Arial", 14), bg="#f0f0f0")
    position_label.pack(pady=20)

    # Iniciar em uma nova thread para evitar congelamento
    tracking_thread = threading.Thread(target=show_mouse_position, args=(position_label,), daemon=True)
    tracking_thread.start()

    # Adiciona um botão para fechar a janela
    close_button = tk.Button(position_window, text="Fechar", command=position_window.destroy, bg="#007bff", fg="white", font=("Arial", 12), relief="raised")
    close_button.pack(pady=10, padx=20)

# Função para levar o mouse à última posição armazenada
def move_mouse_to_last_position():
    if cursor_positions:
        last_position = cursor_positions[-1]  # Pega a última posição armazenada
        pyautogui.moveTo(last_position)  # Move o mouse para a última posição armazenada
        show_message(f"Mouse movido para: {last_position}")  # Mostra a mensagem

# Função para abrir a tela "Sobre"
def show_about():
    about_window = tk.Toplevel(root)
    about_window.title("Sobre")
    about_window.geometry("300x150")  # Tamanho ajustado da janela "Sobre"
    about_window.configure(bg="#f0f0f0")  # Cor de fundo

    about_text = "Powered by Matheus Stocco\nMade in Brasil"
    label = tk.Label(about_window, text=about_text, font=("Arial", 12), bg="#f0f0f0")
    label.pack(expand=True)

# Função para abrir a tela "Ajuda"
def show_help():
    help_window = tk.Toplevel(root)
    help_window.title("Ajuda")
    help_window.geometry("300x150")  # Tamanho ajustado da janela "Ajuda"
    help_window.configure(bg="#f0f0f0")  # Cor de fundo

    help_text = "Contato: Matheus Stocco - 41 988377851"
    label = tk.Label(help_window, text=help_text, font=("Arial", 12), bg="#f0f0f0")
    label.pack(expand=True)

# Função para abrir uma nova janela e mostrar a tecla pressionada
def show_identified_key(key):
    global identified_window
    if identified_window is None or not identified_window.winfo_exists():
        identified_window = tk.Toplevel(root)
        identified_window.title("Teclas Identificadas")
        identified_window.geometry("300x200")  # Tamanho ajustado da janela
        identified_window.configure(bg="#f0f0f0")  # Cor de fundo

        text_frame = tk.Frame(identified_window, bg="#f0f0f0")
        text_frame.pack(expand=True, fill=tk.BOTH)

        key_text = tk.Text(text_frame, wrap=tk.WORD, bg="#ffffff", fg="#000000", font=("Arial", 12))
        key_text.pack(expand=True, fill=tk.BOTH)

        # Armazenar a referência do widget Text na janela identificada
        identified_window.key_text_widget = key_text
    else:
        key_text = identified_window.key_text_widget
        key_text.insert(tk.END, f"Tecla: {key}\n")
        # Armazenar a tecla na lista
        identified_keys.append(key)

# Função para identificar a tecla pressionada e atualizar a janela
def identify_key(event):
    show_identified_key(event.keysym)  # Chama a função para mostrar a tecla

# Função para mostrar todos os valores armazenados em uma nova janela
def show_stored_values():
    values_window = tk.Toplevel(root)
    values_window.title("Valores Armazenados")
    values_window.geometry("400x300")  # Tamanho ajustado da janela
    values_window.configure(bg="#f0f0f0")  # Cor de fundo

    values_text = tk.Text(values_window, wrap=tk.WORD, bg="#ffffff", fg="#000000", font=("Arial", 12))
    values_text.pack(expand=True, fill=tk.BOTH)

    # Adiciona as posições do cursor
    values_text.insert(tk.END, "Posições do Cursor:\n")
    for position in cursor_positions:
        values_text.insert(tk.END, f"{position}\n")

    values_text.insert(tk.END, "\nTeclas Identificadas:\n")
    for key in identified_keys:
        values_text.insert(tk.END, f"{key}\n")

# Criar janela principal
root = tk.Tk()
root.title("Blocos Selecionáveis e Localizar Posição do Cursor")
root.geometry("400x300")  # Tamanho da janela principal
root.configure(bg="#f0f0f0")  # Cor de fundo

# Configurar para identificar teclas pressionadas
root.bind('<Key>', identify_key)

# Criar botão dedicado para a funcionalidade de localização
button_localizar = tk.Button(root, text="Localizar", bg="#007bff", fg="white", width=10, height=2, font=("Arial", 12), relief="raised")
button_localizar.config(command=start_cursor_position_tracking)
button_localizar.grid(row=0, column=0, padx=10, pady=10)

# Criar botão "Executar"
button_executar = tk.Button(root, text="Executar", bg="#28a745", fg="white", width=10, height=2, font=("Arial", 12), relief="raised")
button_executar.config(command=move_mouse_to_last_position)
button_executar.grid(row=0, column=1, padx=10, pady=10)

# Criar botão "Sobre"
button_sobre = tk.Button(root, text="Sobre", bg="#007bff", fg="white", width=10, height=2, font=("Arial", 12), relief="raised")
button_sobre.config(command=show_about)
button_sobre.grid(row=1, column=0, padx=10, pady=10)

# Criar botão "Ajuda"
button_ajuda = tk.Button(root, text="Ajuda", bg="#007bff", fg="white", width=10, height=2, font=("Arial", 12), relief="raised")
button_ajuda.config(command=show_help)
button_ajuda.grid(row=1, column=1, padx=10, pady=10)

# Criar botão para mostrar valores armazenados
button_valores = tk.Button(root, text="Mostrar Valores", bg="#007bff", fg="white", width=10, height=2, font=("Arial", 12), relief="raised")
button_valores.config(command=show_stored_values)
button_valores.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Iniciar o loop da interface gráfica
root.mainloop()
