import sys
import random
import time
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QInputDialog, QComboBox
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtGui import QIcon


class algorithms(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("algorithms")
        self.setGeometry(200, 200, 800, 400)
        self.setWindowIcon(QIcon("icons/algorithms-icon.png"))
        self.array = []
        self.array_length = 5
        self.attempts = 0
        self.start_time = 0
        self.elapsed = 0

        layout = QVBoxLayout()

        self.label = QLabel("Attempts: 0 | Time: 0.00s")
        layout.addWidget(self.label)

        self.algorithm_selector = QComboBox()
        self.algorithm_selector.addItems(["Bogosort", "Bubble Sort", "Insertion Sort", "Quick Sort"])
        layout.addWidget(self.algorithm_selector)

        self.button = QPushButton("Run")
        self.button.clicked.connect(self.ask_length_and_sort)
        layout.addWidget(self.button)

        self.setLayout(layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)

    def update_time(self):
        self.elapsed = time.time() - self.start_time
        self.label.setText(f"Attempts: {self.attempts} | Time: {self.elapsed:.2f}s")

    def paintEvent(self, event):
        if not self.array:
            return
        painter = QPainter(self)
        width = int(self.width() / len(self.array))
        max_val = max(self.array)
        for i, val in enumerate(self.array):
            height = int((val / max_val) * (self.height() - 50))
            painter.fillRect(int(i*width), self.height() - height, width - 2, height, QColor(100, 150, 255))

    def ask_length_and_sort(self):
        length, ok = QInputDialog.getInt(self, "Array Length", "Enter array length:", 5, 2, 1000, 1)
        if ok:
            self.array_length = length
            self.array = random.sample(range(1, self.array_length + 1), self.array_length)
            algorithm = self.algorithm_selector.currentText()
            self.run_sort(algorithm)

    def run_sort(self, algorithm):
        self.attempts = 0
        self.start_time = time.time()
        self.timer.start(50)

        if algorithm == "Bogosort":
            self.bogo_sort()
        elif algorithm == "Bubble Sort":
            self.bubble_sort()
        elif algorithm == "Insertion Sort":
            self.insertion_sort()
        elif algorithm == "Quick Sort":
            self.quick_sort_wrapper(0, len(self.array) - 1)
        else:
            return

        self.timer.stop()
        self.elapsed = time.time() - self.start_time
        self.update()
        self.label.setText(f"Sorted ({algorithm})! Attempts: {self.attempts} | Time: {self.elapsed:.2f}s")

    def bogo_sort(self):
        while not self.is_sorted(self.array):
            self.attempts += 1
            random.shuffle(self.array)
            if self.attempts % max(1, self.array_length // 2) == 0:
                self.update()
                QApplication.processEvents()

    def bubble_sort(self):
        n = len(self.array)
        for i in range(n):
            for j in range(0, n-i-1):
                self.attempts += 1
                if self.array[j] > self.array[j+1]:
                    self.array[j], self.array[j+1] = self.array[j+1], self.array[j]
                if n <= 50:  # Only update GUI for small arrays
                    self.update()
                    QApplication.processEvents()

    def insertion_sort(self):
        for i in range(1, len(self.array)):
            key = self.array[i]
            j = i - 1
            while j >= 0 and self.array[j] > key:
                self.attempts += 1
                self.array[j + 1] = self.array[j]
                j -= 1
                if len(self.array) <= 50:
                    self.update()
                    QApplication.processEvents()
            self.array[j + 1] = key
            if len(self.array) <= 50:
                self.update()
                QApplication.processEvents()

    def quick_sort_wrapper(self, low, high):
        self.quick_sort(low, high)
        if len(self.array) <= 50:
            self.update()
            QApplication.processEvents()

    def quick_sort(self, low, high):
        if low < high:
            pi = self.partition(low, high)
            self.quick_sort(low, pi - 1)
            self.quick_sort(pi + 1, high)

    def partition(self, low, high):
        pivot = self.array[high]
        i = low - 1
        for j in range(low, high):
            self.attempts += 1
            if self.array[j] <= pivot:
                i += 1
                self.array[i], self.array[j] = self.array[j], self.array[i]
            if len(self.array) <= 50:
                self.update()
                QApplication.processEvents()
        self.array[i + 1], self.array[high] = self.array[high], self.array[i + 1]
        return i + 1

    @staticmethod
    def is_sorted(arr):
        return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = algorithms()
    window.show()
    sys.exit(app.exec())
