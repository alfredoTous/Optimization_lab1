#!/usr/bin/env python3
import customtkinter as ctk
import matplotlib
matplotlib.use('Agg')
from PIL import Image
from problem3 import *
from problem1 import *
from problem2 import *
from problem4 import *


def create_input_pair(parent, label_text, default_value):
    frame = ctk.CTkFrame(parent)
    frame.pack(side="left", padx=10, pady=5, fill="x", expand=True)
    
    label = ctk.CTkLabel(frame, text=label_text)
    label.pack(side="top", anchor="w")
    
    entry = ctk.CTkEntry(frame)
    entry.insert(0, str(default_value))
    entry.pack(side="top", fill="x", expand=True)
    
    return entry

def problem1_frame():
    clean_content_frame()
    root.geometry("800x800")
    center_window(root)
    text = """
    Determine the area of the largest rectangle that can be inscribed in
a circle of radius 5 cm. Formulate this as an optimization problem
by writing down the objective function and the constraint. Solve the
problem using the graphical method\n\n -Our design variables are x = width, y = height\n-Objective Function: Area = xy\n-Constraint: (x/2)^2 + (y/2)^2 ≤ r^2\n-Optimal Solution: x = y = r × √2"""
    label_title = ctk.CTkLabel(content_frame,text="Selected OPT Problem",font=("Times New Roman",19,"bold"))
    label_title.pack()
    label_instructions = ctk.CTkLabel(content_frame, text=text, font=("Times New Roman", 16,"italic"))
    label_instructions.pack()

    input_frame = ctk.CTkFrame(content_frame)
    input_frame.pack(anchor="n",pady=(0,10),fill="x", expand=True)

    entry_r = create_input_pair(input_frame, "Radius (r):", 5)
    entry_x = create_input_pair(input_frame, "Width (x):", 7.07)
    entry_y = create_input_pair(input_frame, "Height (y):", 7.07) 

    global img_label
    graph_frame = ctk.CTkFrame(content_frame)
    graph_frame.pack(pady=10, fill="both")
    img_label = None
    
    def calculate_graph_problem1():
        root.geometry("800x1000")
        center_window(root)
        global img_label
        try:
            r,x,y = int(entry_r.get()),float(entry_x.get()),float(entry_y.get())
            image_path = problem1_graphic_solution(r,x,y)
            
            if img_label:
                img_label.destroy()

            img = Image.open(image_path)
            ctk_img = ctk.CTkImage(light_image=img, size=(500,400))

            img_label = ctk.CTkLabel(graph_frame,text="",image=ctk_img)
            img_label.pack()

        except Exception as e:
            label_result.configure(text=f"Error: {str(e)}")
    
    btn_calculate = ctk.CTkButton(content_frame, text="Calculate", command=calculate_graph_problem1)
    btn_calculate.pack(pady=5)


def problem2_frame():
    clean_content_frame()
    center_window(root)
    input_frame = ctk.CTkFrame(content_frame)
    input_frame.pack(anchor="n",pady=(0,5),fill="x", expand=True)
    
    label1_list = ["COO MATRIX"]
    label2_list = ["COO MATRIX", "CSR MATRIX", "CSC MATRIX"]
    label3_list = ["ADDITION", "MULTIPLICATION"]
    label4_list = ["16x16","32x32","128x128"]

    col1_frame = ctk.CTkFrame(input_frame)
    col1_frame.pack(side="left", fill="both", expand=True, padx=5)

    col2_frame = ctk.CTkFrame(input_frame)
    col2_frame.pack(side="left", fill="both", expand=True, padx=5)

    col3_frame = ctk.CTkFrame(input_frame)
    col3_frame.pack(side="left", fill="both", expand=True, padx=5)

    label1 = ctk.CTkLabel(col1_frame, text="Self Implemented")
    label1.pack(side="top", anchor="w")
    comboBox_label1 = ctk.CTkComboBox(col1_frame, values=label1_list)
    comboBox_label1.pack(side="top", fill="x", expand=True)

    label2 = ctk.CTkLabel(col2_frame, text="Spicy.py Implementation")
    label2.pack(side="top", anchor="w")
    comboBox_label2 = ctk.CTkComboBox(col2_frame, values=label2_list)
    comboBox_label2.pack(side="top", fill="x", expand=True)

    label3 = ctk.CTkLabel(col3_frame, text="Operation")
    label3.pack(side="top", anchor="w")
    comboBox_label3 = ctk.CTkComboBox(col3_frame, values=label3_list)  
    comboBox_label3.pack(side="top", fill="x", expand=True)

    label4 = ctk.CTkLabel(input_frame, text="Matrix Size:")
    label4.pack()
    size_combobox = ctk.CTkComboBox(input_frame, values=label4_list)
    size_combobox.pack()
    
    global result_frame
    result_frame = None
    def calculate_sparse_matrix():
        root.geometry("720x600")
        center_window(root)
        
        global result_frame
        if result_frame is not None:
            result_frame.destroy()

        result_frame = ctk.CTkFrame(content_frame)
        result_frame.pack(pady=10, fill="x", expand=True)

        operation = comboBox_label3.get()
        python_implementation = comboBox_label2.get()
        matrix_size = size_combobox.get()
        format_spicy = comboBox_label2.get()
        

        self_matrix_building_time, self_matrix_operation_time = calculate_operation_self_matrix(matrix_size,operation)
        spicy_matrix_building_time, spicy_matrix_operation_time = calculate_operation_spicy_matrix(matrix_size,operation,format_spicy)
        dense_matrix_operation_time = calculate_operation_dense_matrix(matrix_size,operation)


        result_label = ctk.CTkLabel(result_frame, text="Execution Times:", font=("Times New Roman",20,"bold"))
        result_label.pack()

        time_self_label = ctk.CTkLabel(result_frame, text=f"Self Implemented: {self_matrix_operation_time*1000:.5f}ms ----- ({self_matrix_building_time*1000:.5f}ms to build format)",font=("Times New Roman",18,"italic"))
        time_self_label.pack()

        time_python_label = ctk.CTkLabel(result_frame, text=f"Python Libraries: {spicy_matrix_operation_time*1000:.5f}ms ----- ({spicy_matrix_building_time*1000:.5f}ms to build format)",font=("Times New Roman",18,"italic"))
        time_python_label.pack()

        time_dense_label = ctk.CTkLabel(result_frame, text=f"Dense Matrix Time: {dense_matrix_operation_time*1000:.5f}ms",font=("Times New Roman",18,"italic"))
        time_dense_label.pack()

    calculate_button = ctk.CTkButton(content_frame, text="Calculate", command=calculate_sparse_matrix)
    calculate_button.pack(pady=10)

        



def problem3_frame(): 
    clean_content_frame()
    root.geometry("800x720")
    center_window(root) 
    label_instructions = ctk.CTkLabel(content_frame, text="Input the parameters for the Taylor Expansion", font=("Times New Roman",18,"bold"))
    label_instructions.pack(pady=5)

    label_n = ctk.CTkLabel(content_frame, text="Number of Terms: ")
    label_n.pack()
    entry_n = ctk.CTkEntry(content_frame)
    entry_n.pack()

    label_a = ctk.CTkLabel(content_frame, text="Expansion Point: ")
    label_a.pack()
    entry_a = ctk.CTkEntry(content_frame)
    entry_a.pack()

    function_list = ["sin(x)", "cos(x)", "exp(x)", "log(x+1)", "1/x**2"]
    label_func = ctk.CTkLabel(content_frame, text="Select a Function:")
    label_func.pack()
    comboBox_func = ctk.CTkComboBox(content_frame, values=function_list)
    comboBox_func.pack()

    label_result = ctk.CTkLabel(content_frame, text="")
    label_result.pack(pady=10)

    global img_label
    graph_frame = ctk.CTkFrame(content_frame)
    graph_frame.pack(pady=10, fill="both")

    img_label = None  

    def calculate_taylor_expansion():
        global img_label
        root.geometry("800x1000")
        center_window(root)
        try:
            n = int(entry_n.get())
            a = int(entry_a.get())
            function = comboBox_func.get()

            if function == "1/x**2" and a == 0:
                return label_result.configure(text="Math Error")

            function = sp.sympify(function)

            expansion_result = taylor_expansion(function, n, a)
            image_path = graph(function, expansion_result, -10, 10)

            label_result.configure(text=f"Taylor Expansion:\n\n{expansion_result}", font=("Times New Roman",16,"bold"))

            if img_label:
                img_label.destroy()

            img = Image.open(image_path)
            ctk_img = ctk.CTkImage(light_image=img, size=(500,400))

            img_label = ctk.CTkLabel(graph_frame,text="",image=ctk_img)
            img_label.pack()

        except Exception as e:
            label_result.configure(text=f"Error: {str(e)}")

    btn_calculate = ctk.CTkButton(content_frame, text="Calculate", command=calculate_taylor_expansion)
    btn_calculate.pack(pady=5)

def problem4_frame():
    clean_content_frame()
    root.geometry("650x800")
    center_window(root)
    input_frame = ctk.CTkFrame(content_frame)
    input_frame.pack(anchor="n",pady=(0,10),fill="x", expand=True)

    entry_x0 = create_input_pair(input_frame, "Initial Point", 10)
    entry_tol = create_input_pair(input_frame, "Learning Rate", 0.1)

    function_list = ["x**2", "(x - 3)**2 + 2"]
    label_func = ctk.CTkLabel(input_frame, text="Select a Function:")
    label_func.pack()
    comboBox_func = ctk.CTkComboBox(input_frame, values=function_list)
    comboBox_func.pack()
    
    global img_label
    graph_frame = ctk.CTkFrame(content_frame)
    graph_frame.pack(pady=10, fill="both", expand=True)

    img_label = None  

    def calculate_problem4():
        try:
            global img_label
            x0 = int(entry_x0.get())
            tol = float(entry_tol.get())
            f = comboBox_func.get()

            image_path = calculate_optimization_methods(f,tol,x0)

            if img_label:
                img_label.destroy()

            img = Image.open(image_path)
            ctk_img = ctk.CTkImage(light_image=img, size=(500,400))

            img_label = ctk.CTkLabel(graph_frame,text="",image=ctk_img)
            img_label.pack()

        except Exception as e:
            print(f"\nError: {str(e)}")


    btn_calculate = ctk.CTkButton(content_frame, text="Calculate", command=calculate_problem4)
    btn_calculate.pack(pady=5)

def f1(x):
    return x**2

def grad_f1(x):
    return 2*x

def f2(x):
    return (x - 3)**2 + 2

def grad_f2(x):
    return 2*(x - 3)


def clean_content_frame():
    for widget in content_frame.winfo_children():
        widget.destroy()
    root.geometry("650x450")


def center_window(root):
    root.update_idletasks()  
    width = root.winfo_width()
    height = root.winfo_height()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    root.geometry(f"{width}x{height}+{x}+{y}")   

if __name__ == "__main__":
    root = ctk.CTk()
    root.title("Optimization Lab1")
    root.geometry("650x450")

    title = ctk.CTkLabel(root,text="Optimization Problems", font=("Times New Roman",30,"bold"))
    title.pack(pady=30)

    btn_frame = ctk.CTkFrame(root)
    btn_frame.pack(pady=20) 

    content_frame = ctk.CTkFrame(root)
    content_frame.pack(fill="both", expand=True, pady=20)

    
    btn_problem1 = ctk.CTkButton(btn_frame, text="Problem 1", command=problem1_frame)
    btn_problem1.pack(side="left", padx=10)

    btn_problem2 = ctk.CTkButton(btn_frame, text="Problem 2", command=problem2_frame)
    btn_problem2.pack(side="left", padx=10)

    btn_problem3 = ctk.CTkButton(btn_frame, text="Problem 3", command=problem3_frame)
    btn_problem3.pack(side="left", padx=10)

    btn_problem4 = ctk.CTkButton(btn_frame, text="Problem 4", command=problem4_frame)
    btn_problem4.pack(side="left", padx=10)


    root.mainloop()

