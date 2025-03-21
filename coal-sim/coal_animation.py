import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

def coalescent_simulation(N, num_lineages):
    time = 0
    events = []
    active_lineages = {i: i for i in range(num_lineages)}
    lineage_colors = {i: (random.random(), random.random(), random.random()) for i in range(num_lineages)}

    while len(active_lineages) > 1:
        rate = len(active_lineages) * (len(active_lineages) - 1) / (2 * N)
        wait_time = np.random.exponential(1 / rate)
        time += wait_time
        parent, child = np.random.choice(list(active_lineages.keys()), size=2, replace=False) # pick two random lineages to merge
        new_x = (active_lineages[parent] + active_lineages[child]) / 2
        events.append((time, active_lineages[parent], active_lineages[child], new_x, lineage_colors[parent]))
        active_lineages[parent] = new_x  #update
        del active_lineages[child]  

    return events

def animate_coalescence(N, num_lineages):
    events = coalescent_simulation(N, num_lineages)

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_xlim(-1, num_lineages)
    ax.set_ylim(max(t for t, _, _, _, _ in events) + 1, -50) 
    ax.set_xlabel("Lineage Index")
    ax.set_ylabel("Time (Generations Ago)")
    ax.set_title("Coalescent Tree Animation with Explanations")

    lines = []
    text_labels = []
    label_positions = set() 

    def update(frame):
        t, x1, x2, new_x, color = events[frame]

        line1, = ax.plot([x1, x1], [t, 0], color=color, lw=2)
        line2, = ax.plot([x2, x2], [t, 0], color=color, lw=2)
        line3, = ax.plot([x1, x2], [t, t], color=color, lw=2)

        y_offset = 15
        while any(abs(t - existing_t) < y_offset for existing_t in label_positions):
            t += y_offset #label issues
        label_positions.add(t)
        
        label_x = new_x + 1 if new_x < num_lineages / 2 else new_x - 1 
        txt = ax.text(label_x, t, f"Coalesced at {int(t)} gens", fontsize=9, ha="right" if new_x < num_lineages / 2 else "left", bbox=dict(facecolor="white", alpha=0.6))
        
        lines.append((line1, line2, line3))
        text_labels.append(txt)

    ani = animation.FuncAnimation(fig, update, frames=len(events), repeat=False, interval=600)
    plt.show()

# run with these parameters
N = 500  # pop
num_lineages = 20  # sample
animate_coalescence(N, num_lineages)