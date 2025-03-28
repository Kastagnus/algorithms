# import tkinter as tk
# from tkinter import ttk, messagebox
# from algo_manager import AlgorithmManager  # Adjust import based on your structure
# from tasks import TwoNumberSum
#
#
# class ScrollableFrame(ttk.Frame):
#     """A scrollable frame that can hold multiple widgets."""
#     def __init__(self, container, *args, **kwargs):
#         super().__init__(container, *args, **kwargs)
#         canvas = tk.Canvas(self, bg="#f5f5f5", highlightthickness=0)
#         scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
#         self.scrollable_frame = ttk.Frame(canvas)
#
#         self.scrollable_frame.bind(
#             "<Configure>",
#             lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
#         )
#
#         canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
#         canvas.configure(yscrollcommand=scrollbar.set)
#
#         def _on_mouse_wheel(event):
#             canvas.yview_scroll(-1 * (event.delta // 120), "units")
#
#         canvas.bind_all("<MouseWheel>", _on_mouse_wheel)
#
#         canvas.pack(side="left", fill="both", expand=True)
#         scrollbar.pack(side="right", fill="y")
#
#
# class AlgorithmApp:
#     def __init__(self, root, manager):
#         self.root = root
#         self.manager = manager
#         self.root.title("Algorithm Showcase")
#         self.root.geometry("900x700")
#         self.root.configure(bg="#f5f5f5")
#
#         # Apply a modern theme
#         self.style = ttk.Style()
#         self.style.theme_use("clam")  # Try other themes like 'alt', 'default', 'vista'
#
#         # Scrollable Area
#         self.scroll_frame = ScrollableFrame(root)
#         self.scroll_frame.pack(fill="both", expand=True, padx=20, pady=20)
#
#         # Algorithm List
#         self.algo_listbox = tk.Listbox(
#             self.scroll_frame.scrollable_frame, height=10, bg="white", font=("Arial", 12),
#             selectbackground="#4CAF50", selectforeground="white"
#         )
#         self.algo_listbox.pack(pady=10, fill=tk.X, padx=10)
#         for algo in self.manager.get_algorithm_names():
#             self.algo_listbox.insert(tk.END, algo.replace("_", " ").title())
#         self.algo_listbox.bind("<<ListboxSelect>>", self.on_select)
#
#         # Documentation
#         self.doc_text = tk.Text(
#             self.scroll_frame.scrollable_frame, height=5, width=80, bg="white",
#             font=("Arial", 10), wrap=tk.WORD
#         )
#         self.doc_text.pack(pady=10, padx=10)
#         self.doc_text.insert(tk.END, "Select an algorithm to view its documentation.")
#
#         # Test Case Frame
#         self.test_frame = ttk.LabelFrame(self.scroll_frame.scrollable_frame, text="Test Cases", padding=10)
#         self.test_frame.pack(pady=10, fill=tk.X, padx=10)
#         self.run_test_btn = ttk.Button(
#             self.test_frame, text="Run Predefined Tests", command=self.run_test,
#             style="Accent.TButton"
#         )
#         self.run_test_btn.pack(pady=5)
#
#         # Custom Input Frame
#         self.input_frame = ttk.LabelFrame(self.scroll_frame.scrollable_frame, text="Custom Input", padding=10)
#         self.input_frame.pack(pady=10, fill=tk.X, padx=10)
#         self.input_widgets = {}
#         self.run_custom_btn = ttk.Button(
#             self.input_frame, text="Run Custom", command=self.run_custom,
#             style="Accent.TButton"
#         )
#
#         # Output
#         self.output_text = tk.Text(
#             self.scroll_frame.scrollable_frame, height=5, width=80, bg="white",
#             font=("Arial", 10), wrap=tk.WORD
#         )
#         self.output_text.pack(pady=10, padx=10)
#         self.output_text.insert(tk.END, "Output will appear here.")
#
#         # Source Code Frame
#         self.code_frame = ttk.LabelFrame(self.scroll_frame.scrollable_frame, text="Source Code", padding=10)
#         self.code_frame.pack(pady=10, fill=tk.X, padx=10)
#         self.show_code_btn = ttk.Button(
#             self.code_frame, text="Show Solution", command=self.show_code,
#             style="Accent.TButton"
#         )
#         self.show_code_btn.pack(pady=5)
#         self.code_text = tk.Text(
#             self.code_frame, height=10, width=80, bg="white", font=("Courier", 10),
#             wrap=tk.WORD
#         )
#         self.code_text.pack(pady=5)
#         self.code_text.insert(tk.END, "Click 'Show Solution' to view the code.")
#
#         # Custom Styles
#         self.style.configure("Accent.TButton", background="#4CAF50", foreground="white", font=("Arial", 10, "bold"))
#         self.style.map("Accent.TButton", background=[("active", "#45a049")])
#
#     def on_select(self, event):
#         self.show_docs(event)
#         self.update_input_fields()
#
#     def show_docs(self, event):
#         selection = self.algo_listbox.curselection()
#         if selection:
#             algo_name = self.algo_listbox.get(selection[0]).replace(" ", "_").lower()
#             docs = self.manager.get_algorithm_documentation(algo_name)
#             self.doc_text.delete(1.0, tk.END)
#             self.doc_text.insert(tk.END, docs)
#
#     def update_input_fields(self):
#         for param in self.input_widgets:
#             self.input_widgets[param].destroy()
#         for widget in self.input_frame.winfo_children():
#             if widget not in (self.run_custom_btn,):
#                 widget.destroy()
#         self.input_widgets.clear()
#
#         selection = self.algo_listbox.curselection()
#         if not selection:
#             return
#         algo_name = self.algo_listbox.get(selection[0]).replace(" ", "_").lower()
#         test_cases = self.manager.algorithms[algo_name].get_test_cases()
#         if not test_cases:
#             return
#
#         inputs = test_cases[0]["inputs"]
#         for param, value in inputs.items():
#             label = ttk.Label(self.input_frame, text=f"{param}:", font=("Arial", 10, "bold"))
#             label.pack(side=tk.LEFT, padx=5)
#             entry = ttk.Entry(self.input_frame, width=30)
#             entry.pack(side=tk.LEFT, padx=5)
#             if param == "arr":
#                 default_input = str(value)[1:-1]
#             else:
#                 default_input = str(value)
#             entry.insert(0, default_input)
#             self.input_widgets[param] = entry
#
#         if not self.run_custom_btn.winfo_ismapped():
#             self.run_custom_btn.pack(side=tk.LEFT, padx=5)
#
#     def run_test(self):
#         selection = self.algo_listbox.curselection()
#         if not selection:
#             messagebox.showwarning("Warning", "Please select an algorithm.")
#             return
#         algo_name = self.algo_listbox.get(selection[0]).replace(" ", "_").lower()
#         result = self.manager.algorithms[algo_name].run_test()
#         self.output_text.delete(1.0, tk.END)
#         self.output_text.insert(tk.END, result)
#
#     def run_custom(self):
#         selection = self.algo_listbox.curselection()
#         if not selection:
#             messagebox.showwarning("Warning", "Please select an algorithm.")
#             return
#         algo_name = self.algo_listbox.get(selection[0]).replace(" ", "_").lower()
#         try:
#             inputs = {}
#             for param, entry in self.input_widgets.items():
#                 value = entry.get()
#                 if param == "arr":
#                     inputs[param] = [int(x.strip()) for x in value.split(",")]
#                 else:
#                     inputs[param] = int(value)
#             result = self.manager.execute_algorithm(algo_name, **inputs)
#             self.output_text.delete(1.0, tk.END)
#             self.output_text.insert(tk.END, f"Custom Input: {inputs}\nResult: {result}")
#         except ValueError:
#             messagebox.showerror("Error", "Invalid input. Check format (e.g., comma-separated integers for arrays).")
#
#     def show_code(self):
#         selection = self.algo_listbox.curselection()
#         if not selection:
#             messagebox.showwarning("Warning", "Please select an algorithm.")
#             return
#         algo_name = self.algo_listbox.get(selection[0]).replace(" ", "_").lower()
#         code = self.manager.get_algorithm_source_code(algo_name)
#         self.code_text.delete(1.0, tk.END)
#         self.code_text.insert(tk.END, code)
#
#
# if __name__ == "__main__":
#     root = tk.Tk()
#     manager = AlgorithmManager()
#     manager.add_algorithm("Two Number Sum", TwoNumberSum)
#     app = AlgorithmApp(root, manager)
#     root.mainloop()

import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QListWidget,
    QTextEdit, QLabel, QPushButton, QLineEdit, QScrollArea, QFrame, QMessageBox
)
from PyQt5.QtCore import Qt
from algo_manager import AlgorithmManager  # Adjust import based on your structure
from tasks1 import *


class ScrollableFrame(QWidget):
    """A scrollable frame that can hold multiple widgets."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignTop)
        self.setLayout(self.layout)


class AlgorithmApp(QMainWindow):
    def __init__(self, manager):
        super().__init__()
        self.manager = manager
        self.setWindowTitle("Algorithm Showcase")
        self.setGeometry(100, 100, 900, 700)
        self.setStyleSheet("""
            QMainWindow { background-color: #f5f5f5; }
            QListWidget { background-color: white; border: 1px solid #ddd; font-size: 14px; }
            QTextEdit { background-color: white; border: 1px solid #ddd; font-size: 12px; }
            QLabel { font-size: 14px; font-weight: bold; }
            QPushButton {
                background-color: #4CAF50; color: white; font-size: 14px; font-weight: bold;
                padding: 10px; border-radius: 5px;
            }
            QPushButton:hover { background-color: #45a049; }
            QLineEdit { background-color: white; border: 1px solid #ddd; padding: 5px; font-size: 14px; }
            QFrame { background-color: white; border: 1px solid #ddd; border-radius: 5px; }
        """)

        # Central Widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)

        # Scrollable Area
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_frame = ScrollableFrame()
        self.scroll_area.setWidget(self.scroll_frame)
        self.main_layout.addWidget(self.scroll_area)

        # Algorithm List
        self.algo_list = QListWidget()
        self.algo_list.setFixedHeight(150)
        for algo in self.manager.get_algorithm_names():
            self.algo_list.addItem(algo.replace("_", " ").title())
        self.algo_list.itemSelectionChanged.connect(self.on_select)
        self.scroll_frame.layout.addWidget(self.algo_list)

        # Documentation
        self.doc_label = QLabel("Documentation:")
        self.doc_text = QTextEdit()
        self.doc_text.setReadOnly(True)
        self.doc_text.setPlaceholderText("Select an algorithm to view its documentation.")
        self.scroll_frame.layout.addWidget(self.doc_label)
        self.scroll_frame.layout.addWidget(self.doc_text)

        # Test Case Frame
        self.test_frame = QFrame()
        self.test_frame.setLayout(QVBoxLayout())
        self.test_frame.layout().setAlignment(Qt.AlignTop)
        self.test_label = QLabel("Test Cases:")
        self.run_test_btn = QPushButton("Run Predefined Tests")
        self.run_test_btn.clicked.connect(self.run_test)
        self.test_frame.layout().addWidget(self.test_label)
        self.test_frame.layout().addWidget(self.run_test_btn)
        self.scroll_frame.layout.addWidget(self.test_frame)

        # Custom Input Frame
        self.input_frame = QFrame()
        self.input_frame.setLayout(QVBoxLayout())
        self.input_frame.layout().setAlignment(Qt.AlignTop)
        self.input_label = QLabel("Custom Input:")
        self.input_widgets = {}
        self.run_custom_btn = QPushButton("Run Custom")
        self.run_custom_btn.clicked.connect(self.run_custom)
        self.input_frame.layout().addWidget(self.input_label)
        self.scroll_frame.layout.addWidget(self.input_frame)

        # Output
        self.output_label = QLabel("Output:")
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        self.output_text.setPlaceholderText("Output will appear here.")
        self.scroll_frame.layout.addWidget(self.output_label)
        self.scroll_frame.layout.addWidget(self.output_text)

        # Source Code Frame
        self.code_frame = QFrame()
        self.code_frame.setLayout(QVBoxLayout())
        self.code_frame.layout().setAlignment(Qt.AlignTop)
        self.code_label = QLabel("Source Code:")
        self.show_code_btn = QPushButton("Show Solution")
        self.show_code_btn.clicked.connect(self.show_code)
        self.code_text = QTextEdit()
        self.code_text.setReadOnly(True)
        self.code_text.setPlaceholderText("Click 'Show Solution' to view the code.")
        self.code_frame.layout().addWidget(self.code_label)
        self.code_frame.layout().addWidget(self.show_code_btn)
        self.code_frame.layout().addWidget(self.code_text)
        self.scroll_frame.layout.addWidget(self.code_frame)

    def on_select(self):
        self.show_docs()
        self.update_input_fields()

    def show_docs(self):
        selection = self.algo_list.selectedItems()
        if selection:
            algo_name = selection[0].text().replace(" ", "_").lower()
            docs = self.manager.get_algorithm_documentation(algo_name)
            self.doc_text.setPlainText(docs)

    def update_input_fields(self):
        for widget in self.input_widgets.values():
            widget.deleteLater()
        self.input_widgets.clear()

        selection = self.algo_list.selectedItems()
        if not selection:
            return
        algo_name = selection[0].text().replace(" ", "_").lower()
        test_cases = self.manager.algorithms[algo_name].get_test_cases()
        if not test_cases:
            return

        inputs = test_cases[0]["inputs"]
        for param, value in inputs.items():
            layout = QHBoxLayout()
            label = QLabel(f"{param}:")
            entry = QLineEdit()
            if param == "arr":
                default_input = str(value)[1:-1]
            else:
                default_input = str(value)
            entry.setText(default_input)
            layout.addWidget(label)
            layout.addWidget(entry)
            self.input_widgets[param] = entry
            self.input_frame.layout().addLayout(layout)

        if not self.run_custom_btn.isVisible():
            self.input_frame.layout().addWidget(self.run_custom_btn)

    def run_test(self):
        selection = self.algo_list.selectedItems()
        if not selection:
            QMessageBox.warning(self, "Warning", "Please select an algorithm.")
            return
        algo_name = selection[0].text().replace(" ", "_").lower()
        result = self.manager.algorithms[algo_name].run_test()
        self.output_text.setPlainText(result)

    def run_custom(self):
        selection = self.algo_list.selectedItems()
        if not selection:
            QMessageBox.warning(self, "Warning", "Please select an algorithm.")
            return
        algo_name = selection[0].text().replace(" ", "_").lower()
        try:
            inputs = {}
            for param, entry in self.input_widgets.items():
                value = entry.text()
                if param == "arr":
                    inputs[param] = [int(x.strip()) for x in value.split(",")]
                else:
                    inputs[param] = int(value)
            result = self.manager.execute_algorithm(algo_name, **inputs)
            self.output_text.setPlainText(f"Custom Input: {inputs}\nResult: {result}")
        except ValueError:
            QMessageBox.critical(self, "Error", "Invalid input. Check format (e.g., comma-separated integers for arrays).")

    def show_code(self):
        selection = self.algo_list.selectedItems()
        if not selection:
            QMessageBox.warning(self, "Warning", "Please select an algorithm.")
            return
        algo_name = selection[0].text().replace(" ", "_").lower()
        code = self.manager.get_algorithm_source_code(algo_name)
        self.code_text.setPlainText(code)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    manager = AlgorithmManager()
    manager.add_algorithm("Two Number Sum", TwoNumberSum)
    manager.add_algorithm("Move Zeros", MoveZeros)
    manager.add_algorithm("Find Three Largest Number", FindThreeLargestNumber)
    manager.add_algorithm("Best Time to Buy and Sell Stock", BestTimeToBuyAndSellStocks)
    manager.add_algorithm("Contains Duplicates", ContainsDuplicates)
    manager.add_algorithm("Validate Subsequence", ValidateSubsequence)
    manager.add_algorithm("Palindrome Check", PalindromeCheck)
    manager.add_algorithm("Caesar Cipher Encryptor", CaesarCipherEncryptor)
    manager.add_algorithm("First Non Repeating Character", FirstNonRepeatingCharacter)
    manager.add_algorithm("Valid Anagram", ValidAnagram)
    manager.add_algorithm("Binary Search", BinarySearch)
    manager.add_algorithm("Find Closest Value in BST", FindClosestValueInBST)
    manager.add_algorithm("BST Traversal", BSTTraversal)
    manager.add_algorithm("Validate BST", ValidateBST)
    manager.add_algorithm("Maximum Depth of Binary Tree", MaximumDepthOfBinaryTree)
    manager.add_algorithm("Nth Fibonacci", NthFibonacci)
    manager.add_algorithm("Minimum Coins For Change", MinimumCoinsForChange)
    manager.add_algorithm("Climbing Stairs", ClimbingStairs)
    manager.add_algorithm("Maximum Subarray", MaximumSubarray)
    manager.add_algorithm("House Robber", HouseRobber)
    manager.add_algorithm("Minimum Waiting Time", MinimumWaitingTime)
    manager.add_algorithm("Class Photos", ClassPhotos)
    manager.add_algorithm("Tandem Bicycle", TandemBicycle)
    manager.add_algorithm("Valid Starting City", ValidStartingCity)
    manager.add_algorithm("Task Assignment", TaskAssignment)
    manager.add_algorithm("Boolean Expressions", BooleanExpressions)
    manager.add_algorithm("Sliding Puzzle", SlidingPuzzle)
    manager.add_algorithm("FreqStacks", FreqStacks)
    manager.add_algorithm("Put Marbles", PutMarbles)
    manager.add_algorithm("Split Array", SplitArray)
    manager.add_algorithm("Parenthesis", Parenthesis)
    manager.add_algorithm("Robot Paths", RobotPaths)
    manager.add_algorithm("Train Tickets", TrainTicket)
    manager.add_algorithm("Switch Pair Nodes", SwitchPairNodes)
    manager.add_algorithm("Add Node Numbers", AddNodeNumbers)
    manager.add_algorithm("Make Strings Anagrams", MakeStringsAnagrams)
    manager.add_algorithm("Partition String", PartitionString)
    manager.add_algorithm("Number Of Valid Substrings", NumberOfSubs)
    manager.add_algorithm("Query Nums", QueryNums)
    manager.add_algorithm("Airplane Seats", AirplaneSeats)
    manager.add_algorithm("Partition Palindrome", PartitionPalindromes)
    manager.add_algorithm("Rotate Integers", RotateIntegers)
    manager.add_algorithm("Minimum Extra Characters", MinExtraChars)
    manager.add_algorithm("Break Integer", BreakInteger)
    manager.add_algorithm("Perfect Square", PerfectSquare)
    manager.add_algorithm("Intervals", Intervals)
    manager.add_algorithm("Push and Pop", PushPop)
    manager.add_algorithm("Temperatures", Temperatures)
    manager.add_algorithm("Circular Queue", Circular)
    manager.add_algorithm("Execute Operators", ExecuteOperators)
    window = AlgorithmApp(manager)
    window.show()
    sys.exit(app.exec_())