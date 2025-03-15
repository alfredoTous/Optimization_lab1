import numpy as np
import matplotlib.pyplot as plt

def problem1_graphic_solution(r, width, height):
    
    feasible = (width/2)**2 + (height/2)**2 <= r**2
    
    plt.figure(figsize=(8, 6))
    
    x = np.linspace(-r, r, 500) 
    y_upper = np.sqrt(r**2 - x**2)
    y_lower = -y_upper

    plt.fill_between(x, y_upper, y_lower, color='lightblue', alpha=0.5, label='Feasible Region')
    
    rect = plt.Rectangle((-width/2, -height/2), width, height, fill=False,color="red",linewidth=1.5, linestyle='--', label=f'Área: {width*height:.1f} cm^2')
    plt.gca().add_patch(rect)
    

    plt.annotate(f'width: {width} cm', (0, -height/2), 
                xytext=(0, -20), textcoords='offset points',
                ha='center', va='top', color="red")
    plt.annotate(f'height: {height} cm', (width/2, 0), 
                xytext=(20, 0), textcoords='offset points',
                ha='left', va='center', color="red")
    
    plt.title(f'Rectangle inscribed in a Circle (r = {r} cm)\nfeasible: {feasible}')
    plt.xlabel('x (cm)')
    plt.ylabel('y (cm)')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.axis('equal')
    plt.legend(bbox_to_anchor=(1.15, 1), loc='upper left')
    plt.tight_layout()
    
    img_path = "actual_plot.png"
    plt.savefig(img_path)
    plt.close()
    
    return img_path
