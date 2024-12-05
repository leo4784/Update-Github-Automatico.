import os
from github import Github
import tkinter as tk
from tkinter import filedialog, messagebox
import json

class GitHubUploader:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("GitHub Project Uploader")
        self.window.geometry("500x400")
        self.window.configure(bg='#f0f0f0')
        
        # Carregar token salvo se existir
        self.token = self.load_token()
        
        self.create_widgets()
        
    def load_token(self):
        try:
            with open('github_token.json', 'r') as f:
                data = json.load(f)
                return data.get('token', '')
        except FileNotFoundError:
            return ''
            
    def save_token(self, token):
        with open('github_token.json', 'w') as f:
            json.dump({'token': token}, f)
            
    def create_widgets(self):
        # Token Frame
        token_frame = tk.Frame(self.window, bg='#f0f0f0')
        token_frame.pack(pady=20, padx=20, fill='x')
        
        tk.Label(token_frame, text="GitHub Token:", bg='#f0f0f0').pack(anchor='w')
        self.token_entry = tk.Entry(token_frame, width=50)
        self.token_entry.insert(0, self.token)
        self.token_entry.pack(fill='x', pady=5)
        
        # Project Frame
        project_frame = tk.Frame(self.window, bg='#f0f0f0')
        project_frame.pack(pady=20, padx=20, fill='x')
        
        tk.Label(project_frame, text="Project Details:", bg='#f0f0f0').pack(anchor='w')
        
        # Nome do repositório
        tk.Label(project_frame, text="Repository Name:", bg='#f0f0f0').pack(anchor='w')
        self.repo_name = tk.Entry(project_frame, width=50)
        self.repo_name.pack(fill='x', pady=5)
        
        # Descrição
        tk.Label(project_frame, text="Description:", bg='#f0f0f0').pack(anchor='w')
        self.description = tk.Entry(project_frame, width=50)
        self.description.pack(fill='x', pady=5)
        
        # Pasta do projeto
        tk.Label(project_frame, text="Project Folder:", bg='#f0f0f0').pack(anchor='w')
        folder_frame = tk.Frame(project_frame, bg='#f0f0f0')
        folder_frame.pack(fill='x', pady=5)
        
        self.folder_path = tk.Entry(folder_frame, width=40)
        self.folder_path.pack(side='left', fill='x', expand=True)
        
        browse_button = tk.Button(folder_frame, text="Browse", command=self.browse_folder)
        browse_button.pack(side='right', padx=5)
        
        # Botão de upload
        upload_button = tk.Button(
            self.window,
            text="Upload to GitHub",
            command=self.upload_to_github,
            bg='#4CAF50',
            fg='white',
            pady=10
        )
        upload_button.pack(pady=20)
        
    def browse_folder(self):
        folder_selected = filedialog.askdirectory()
        self.folder_path.delete(0, tk.END)
        self.folder_path.insert(0, folder_selected)
        
    def upload_to_github(self):
        token = self.token_entry.get().strip()
        repo_name = self.repo_name.get().strip()
        description = self.description.get().strip()
        folder_path = self.folder_path.get().strip()
        
        if not all([token, repo_name, folder_path]):
            messagebox.showerror("Error", "Please fill in all required fields!")
            return
            
        try:
            # Salvar token para uso futuro
            self.save_token(token)
            
            # Criar conexão com GitHub
            g = Github(token)
            user = g.get_user()
            
            # Criar novo repositório
            repo = user.create_repo(
                repo_name,
                description=description,
                private=False
            )
            
            # Preparar comandos git
            git_commands = [
                f'git init',
                f'git add .',
                f'git commit -m "Initial commit"',
                f'git branch -M main',
                f'git remote add origin {repo.clone_url}',
                f'git push -u origin main'
            ]
            
            # Executar comandos git
            os.chdir(folder_path)
            for cmd in git_commands:
                os.system(cmd)
                
            messagebox.showinfo("Success", f"Project uploaded successfully!\nURL: {repo.html_url}")
            
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = GitHubUploader()
    app.run()
