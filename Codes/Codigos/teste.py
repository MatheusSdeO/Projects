import http.server
import socketserver
import os

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def list_directory(self, path):
        try:
            file_list = os.listdir(path)
            file_list.sort(key=lambda a: a.lower())
            
            # Adicione o link externo na parte superior da página HTML
            html = f"""
                <html>
                    <head>
                        <title>Servidor de Arquivos</title>
                        <style>
                            body {{
                                font-family: Arial, sans-serif;
                                background-color: #f4f4f9;
                                color: #333;
                                margin: 0;
                                padding: 0;
                                display: flex;
                                justify-content: center;
                                align-items: center;
                                min-height: 100vh;
                            }}
                            h2 {{
                                color: #444;
                                text-align: center;
                            }}
                            .container {{
                                width: 80%;
                                max-width: 800px;
                                background: #fff;
                                padding: 20px;
                                box-shadow: 0px 0px 15px rgba(0,0,0,0.1);
                                border-radius: 10px;
                            }}
                            .external-link {{
                                text-align: center;
                                margin-bottom: 15px;
                            }}
                            .external-link a {{
                                color: #007bff;
                                text-decoration: none;
                                font-weight: bold;
                            }}
                            .external-link a:hover {{
                                text-decoration: underline;
                            }}
                            ul {{
                                list-style-type: none;
                                padding: 0;
                                margin: 0;
                            }}
                            li {{
                                margin: 10px 0;
                                display: flex;
                                align-items: center;
                                padding: 10px;
                                border-radius: 5px;
                                transition: background 0.2s;
                            }}
                            li:hover {{
                                background-color: #f0f0f5;
                            }}
                            a {{
                                text-decoration: none;
                                color: #007bff;
                                font-weight: 500;
                                display: flex;
                                align-items: center;
                                width: 100%;
                            }}
                            a:hover {{
                                text-decoration: underline;
                            }}
                            .icon {{
                                margin-right: 15px;
                                font-size: 1.2em;
                            }}
                            .icon.folder {{
                                color: #ffbf00;
                            }}
                            .icon.file {{
                                color: #007bff;
                            }}
                        </style>
                    </head>
                    <body>
                        <div class="container">
                            <div class="external-link">
                                <a href="https://www.seulinkexterno.com" target="_blank">Acessar Link Externo</a>
                            </div>
                            <h2>Arquivos no diretório: {os.path.basename(path)}</h2>
                            <ul>
            """
            
            for name in file_list:
                fullname = os.path.join(path, name)
                display_name = name + "/" if os.path.isdir(fullname) else name
                icon_class = "folder" if os.path.isdir(fullname) else "file"
                
                html += f"""
                    <li>
                        <a href="{name}">
                            <span class="icon {icon_class}">{'📁' if os.path.isdir(fullname) else '📄'}</span>
                            {display_name}
                        </a>
                    </li>
                """
            
            html += """
                            </ul>
                        </div>
                    </body>
                </html>
            """

            # Enviar resposta HTTP com HTML
            encoded = html.encode("utf-8", "surrogateescape")
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(encoded)))
            self.end_headers()
            self.wfile.write(encoded)  # Envia o HTML para o navegador
            return None  # Corrige o erro retornando None
        except Exception as e:
            self.send_error(404, "No permission to list directory")
            return None

    def do_GET(self):
        if self.path == '/':
            self.list_directory(self.translate_path(self.path))  # Chama o list_directory sem retornar valor
        else:
            super().do_GET()

# Configuração do servidor
PORT = 8000
with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
    print(f"Servidor rodando na porta {PORT}")
    httpd.serve_forever()
