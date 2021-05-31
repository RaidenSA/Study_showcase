from tkinter import *
from tkinter import ttk
from L_graph_system import LGraph,load_graph,save_graph
graphs ={}
graph_control_ind_to_key=[]
graph =LGraph()

def load_click():
    file_name = name_txt.get()
    global graph
    graph = load_graph(file_name)
    text = str(graph)
    note_text.delete(1.0, END)
    note_text.insert(1.0, text)

def save_click():
    file_name = name_txt.get()
    global graph
    save_graph(graph, file_name)

def check_click():
    res_text.delete(1.0,END)
    in_s = string_txt.get()
    satus = graph.solve(in_s)
    res_text.delete(1.0, END)
    res_text.insert(1.0, str(satus))
    if satus:
        text= graph.solve(in_s, vertex_trace=True)
        res_text.insert(1.0,text)





window = Tk()
window.title("L-graph-system showcase app")
window.geometry('800x400')

name_lbl = Label(window, text="Имя файла")
name_lbl.grid(column=0, row=0)
name_txt = Entry(window,width=20)
name_txt.grid(column=1, row=0)
string_txt = Entry(window,width=20)
string_txt.grid(column=3, row=0)
status_lbl = Label(window, text="")
status_lbl.grid(column=3, row=2, columnspan =2) #here
load_btn = Button(window, text="Загрузить", command=load_click)
load_btn.grid(column=2, row=0)
save_btn = Button(window, text="Сохранить", command=save_click)
save_btn.grid(column=2, row=1)
arc_btn = Button(window, text="Проверить", command=check_click)
arc_btn.grid(column=3, row=1)
note_space = ttk.Frame(window,borderwidth=5, relief="ridge", width=200, height=100)
note_space.grid(column =0, row =3,columnspan=3, sticky=(N, S, E, W))
note_text = Text(note_space)
note_text.grid(sticky = (N,S,E,W))
res_space = ttk.Frame(window,borderwidth=5, relief="ridge")
res_space.grid(column =3, row =3, sticky=(N, S, E, W))
res_text = Text(res_space)
res_text.grid(sticky = (N,S,E,W))
note_space.grid_columnconfigure(0,weight=1)
note_space.grid_rowconfigure(0,weight=1)
res_space.grid_columnconfigure(0,weight=1)
res_space.grid_rowconfigure(0,weight=1)
window.grid_columnconfigure(1,weight=1)
window.grid_columnconfigure(3,weight=1)#grid_remove()
window.grid_rowconfigure(3,weight=1)
window.mainloop()
