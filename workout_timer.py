import time
import tkinter as tk
import plan_constructor


def main():
    ## PLAN
    plan_chooser = 1
    plan = plan_constructor.constructor(plan_chooser)

    ## FUNCTIONS
    def rep_counter(max_ind, single_rep_secs):
        counter = 1
        while counter < max_ind:
            lower_label.config(text=str(counter) + "\n")
            time.sleep(single_rep_secs)
            root.update()
            counter += 1

    def rest_timer(tot_time, name, chilos):
        while tot_time > -1:
            mins = int(tot_time / 60)
            secs = tot_time % 60
            upper_label.config(text=f"{mins:02}:{secs:02}\n")
            lower_label.config(
                text="Next exercise is\n" + name + "\nand use " + str(chilos) + " Kg"
            )
            root.update()
            time.sleep(1)
            tot_time -= 1

    def plan_timer(plan):
        block_ind = 0
        while block_ind < len(plan):
            block = plan[block_ind]
            for set_ind in range(len(block.sets_plan)):
                upper_label.config(text="\n" + block.name + ":\t")
                lower_label.config(text="Start 0\n")
                root.update()

                # reps count
                max_ind = block.sets_plan[set_ind][0] + 1
                rep_counter(max_ind, block.single_rep_secs)
                time.sleep(1)

                # rest count
                mins, secs = block.sets_plan[set_ind][2].split(":")
                tot_time = int(secs) + 60 * int(mins)
                ### improve nested exception
                try:
                    name = block.name
                    chilos = block.sets_plan[set_ind + 1][1]
                except:
                    try:
                        name = plan[block_ing + 1].name
                        chilos = plan[block_ind + 1].sets_plan[0][1]
                    except:
                        break
                rest_timer(tot_time, name, chilos)
            block_ind += 1

        upper_label.config(text="\t")
        lower_label.config(text="End\n")

    ## TIMER
    root = tk.Tk()
    root.geometry("700x500")
    upper_label = tk.Label(root, font=("Arial", 65))
    upper_label.pack()
    lower_label = tk.Label(root, font=("Arial", 65))
    lower_label.pack()

    plan_timer(plan)

    root.mainloop()


if __name__ == "__main__":
    main()
