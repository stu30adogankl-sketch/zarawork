import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, 
    QLabel, QPushButton
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Choose Your Own Adventure: The Cosmic Bus")
        self.setGeometry(100, 100, 800, 600)
        
        # Central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        # Story text label
        self.story_label = QLabel()
        self.story_label.setWordWrap(True)
        self.story_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.story_label.setStyleSheet("""
            QLabel {
                padding: 20px;
                font-size: 14px;
                background-color: #1a1a2e;
                color: #eaeaea;
                border-radius: 10px;
            }
        """)
        layout.addWidget(self.story_label)
        
        # Button container widget
        self.button_container = QWidget()
        self.button_layout = QVBoxLayout()
        self.button_container.setLayout(self.button_layout)
        layout.addWidget(self.button_container)
        
        # Initialize story state
        self.current_state = "intro"
        
        # Start the story
        self.update_story()
        
        # Set window style
        self.setStyleSheet("""
            QMainWindow {
                background-color: #0f0f1e;
            }
            QPushButton {
                background-color: #16213e;
                color: #eaeaea;
                border: 2px solid #533483;
                border-radius: 8px;
                padding: 10px;
                font-size: 12px;
                min-height: 30px;
            }
            QPushButton:hover {
                background-color: #533483;
                border: 2px solid #81679e;
            }
            QPushButton:pressed {
                background-color: #81679e;
            }
        """)
    
    def clear_buttons(self):
        """Remove all buttons from the button container"""
        while self.button_layout.count():
            item = self.button_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
    
    def add_choice_button(self, text, action):
        """Add a choice button"""
        button = QPushButton(text)
        button.clicked.connect(action)
        self.button_layout.addWidget(button)
    
    def update_story(self):
        """Update the story display based on current state"""
        self.clear_buttons()
        
        if self.current_state == "intro":
            self.story_label.setText(
                "You find yourself standing at a cosmic bus stop, where stars shimmer "
                "like streetlights and nebulae drift like morning mist.\n\n"
                "A strange bus approaches, its wheels made of pure light. Through the "
                "windows, you see countless legs stepping in rhythm: step step step step step step.\n\n"
                "The bus door opens with a sound like distant thunder. Inside, the conductor "
                "grins—their face seems to shift between dimensions.\n\n"
                "Beyond the bus, you notice something odd: lemons are scattered across the "
                "cosmic road, and they're making sounds—bark bark bark bark bark bark—as if "
                "they were alive, or perhaps trying to communicate something about the void ahead.\n\n"
                "What do you do?"
            )
            self.add_choice_button("Board the cosmic bus", lambda: self.make_choice("board_bus"))
            self.add_choice_button("Approach the barking lemons", lambda: self.make_choice("lemons"))
            self.add_choice_button("Stay at the bus stop", lambda: self.make_choice("wait"))
        
        elif self.current_state == "board_bus":
            self.story_label.setText(
                "You step onto the bus. The floor pulses beneath your feet like a heartbeat.\n\n"
                "The legs continue their endless stepping, creating a mesmerizing rhythm "
                "that seems to echo through all of existence. The conductor points to a seat "
                "that appears to be made of stardust.\n\n"
                "Through the windows, you watch as entire galaxies drift past like scenery. "
                "The bus travels through the universe, and you realize you're not entirely sure "
                "what your destination is.\n\n"
                "The conductor leans close and whispers: 'This bus goes step step step step step step, "
                "all through the universe. But where do you want to go?'"
            )
            self.add_choice_button("Ask to go to the void", lambda: self.make_choice("void_ending"))
            self.add_choice_button("Stay on the bus forever", lambda: self.make_choice("eternal_ending"))
        
        elif self.current_state == "lemons":
            self.story_label.setText(
                "You approach the lemons scattered on the cosmic road. Up close, you realize "
                "they're not quite lemons—they're something else entirely, shaped like lemons "
                "but pulsing with an otherworldly energy.\n\n"
                "Their barks grow louder: bark bark bark bark bark bark bark bark bark. "
                "You begin to understand: they're warning you about something.\n\n"
                "The lemons roll together, forming a path that leads deeper into the void. "
                "As you follow, you notice the bus has vanished, and reality itself seems to "
                "be unraveling around you.\n\n"
                "The lemons' barks transform into words: 'Enter the void. Enter the void.'"
            )
            self.add_choice_button("Follow the lemons into the void", lambda: self.make_choice("void_ending"))
            self.add_choice_button("Turn back and run", lambda: self.make_choice("escape_ending"))
        
        elif self.current_state == "wait":
            self.story_label.setText(
                "You decide to stay at the bus stop. The cosmic bus continues on its journey, "
                "its legs still stepping: step step step step step step.\n\n"
                "The lemons continue their barking chorus: bark bark bark bark bark bark bark bark bark.\n\n"
                "Time seems to stretch and warp. You watch as countless buses pass by, each "
                "more surreal than the last. Some have wheels made of questions, others have "
                "windows that show alternate realities.\n\n"
                "You realize you've been waiting for an eternity—or perhaps no time at all. "
                "The distinction loses meaning here.\n\n"
                "Still, you wait. There's something peaceful about this place, this liminal "
                "space between destinations."
            )
            self.add_choice_button("Restart your journey", lambda: self.make_choice("intro"))
        
        elif self.current_state == "void_ending":
            self.story_label.setText(
                "You enter the void.\n\n"
                "Or perhaps the void enters you.\n\n"
                "The distinction collapses. You are everywhere and nowhere. You are the legs "
                "stepping on the bus, you are the lemons barking on the road, you are the void "
                "itself.\n\n"
                "Reality dissolves into possibility. You have become part of the cosmic song: "
                "'Legs on the bus go step step step step step step, legs on the bus go step step "
                "step all through the universe. Lemons on the road go bark bark bark bark bark "
                "bark bark bark bark, lemons on the road go bark bark bark enter the void.'\n\n"
                "You are home.\n\n"
                "THE END"
            )
            self.add_choice_button("Play Again", lambda: self.make_choice("intro"))
        
        elif self.current_state == "eternal_ending":
            self.story_label.setText(
                "You choose to remain on the cosmic bus forever.\n\n"
                "The legs continue their endless stepping, and you find yourself joining in. "
                "Your own legs begin to move in sync: step step step step step step.\n\n"
                "You've become part of the bus's rhythm, part of its journey through the universe. "
                "Through the windows, you watch countless realities flicker past—worlds where "
                "gravity is sideways, where time flows backward, where lemons sing instead of bark.\n\n"
                "You realize this is your destination: to be forever in motion, forever stepping, "
                "forever traveling through the infinite cosmos.\n\n"
                "The bus never stops. You never want it to.\n\n"
                "THE END"
            )
            self.add_choice_button("Play Again", lambda: self.make_choice("intro"))
        
        elif self.current_state == "escape_ending":
            self.story_label.setText(
                "You turn and run from the barking lemons, back toward the bus stop.\n\n"
                "But when you arrive, everything has changed. The bus stop is gone. The bus "
                "is gone. Even the lemons have vanished.\n\n"
                "You find yourself standing on an ordinary street corner in what seems like "
                "an ordinary city. But something feels off—the shadows move wrong, the colors "
                "are slightly different than they should be.\n\n"
                "Was it all a dream? Or did you escape into a different reality?\n\n"
                "In the distance, you hear something faint: the sound of legs stepping, "
                "and perhaps... the barking of lemons?\n\n"
                "THE END"
            )
            self.add_choice_button("Play Again", lambda: self.make_choice("intro"))
    
    def make_choice(self, choice):
        """Handle player choice and update state"""
        self.current_state = choice
        self.update_story()


def main():
    app = QApplication(sys.argv)
    
    # Set application style
    app.setStyle('Fusion')
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

