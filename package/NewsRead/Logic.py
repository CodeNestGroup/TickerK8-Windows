#   --- Improt ---
import json
#   --- Import PySide6 ---
from PySide6.QtWidgets import (
    QLabel,
    QSizePolicy
)
from PySide6.QtCore import (
    Qt
)
def SetupContent(self):
    for index, rows in enumerate(json.loads(self.NewsData[3]), start=0):
        label = QLabel(self.ContentW)
        label.setObjectName(f'news_content_label_{index}')
        label.setText(rows[3])
        label.setWordWrap(True)
        label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        label.setStyleSheet(rows[2])
        if rows[0] == 'Plain_Text':
            label.setObjectName(f"Plain_Text_{index}")
            label.setAlignment(Qt.AlignLeft)
        elif rows[0] == 'Title_Text':
            label.setObjectName(f"Title_Text_{index}")
            label.setAlignment(Qt.AlignCenter)
        elif rows[0] == 'Heading_1_Text':
            label.setObjectName(f"Heading_1_Text_{index}")
            label.setAlignment(Qt.AlignLeft)
        elif rows[0] == 'Heading_2_Text':
            label.setObjectName(f"Heading_2_Text_{index}")
            label.setAlignment(Qt.AlignLeft)
        elif rows[0] == 'Heading_3_Text':
            label.setObjectName(f"Heading_3_Text_{index}")
            label.setAlignment(Qt.AlignLeft)
        elif rows[0] == 'Heading_4_Text':
            label.setObjectName(f"Heading_4_Text_{index}")
            label.setAlignment(Qt.AlignLeft)
        self.ContentL.addWidget(label, index, 2, 1, 96)