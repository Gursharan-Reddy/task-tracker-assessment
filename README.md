Associate Software Engineer - Cheguri - Assessment
1. Project OverviewThis project is a Task Tracker built as part of the Associate Software Engineer assessment. The primary goal was to build a small but clean software product that demonstrates technical structure, correctness, and strict data validation. The application allows users to create, view, filter, and manage tasks while enforcing specific business logic regarding task states.
2. Tech StackFrontend: React (Single-Page Application) Backend API: Flask (Python) Database: SQLite (Relational) Validation: Marshmallow (Backend Request Validation) Testing: Pytest (Backend Logic Verification) 
3. Architecture SummaryThe project follows a layered architecture to ensure the system remains understandable and maintainable :Frontend (React): Handles the UI, forms, and filtering logic.Backend API (Flask): Manages routes and request validation.Service Layer: A central place for business rules and logic, keeping them separate from routes.Database (SQLite): Stores state and prevents invalid data relationships.
4. Folder StructureThe repository is organized to keep UI logic separate from backend rules:Plaintextbackend/
├── models/           # SQLAlchemy database models
├── routes/           # API route definitions (Blueprints)
├── schemas/          # Marshmallow validation schemas
├── services/         # Business logic and rules
├── tests/            # Pytest suite
└── app.py            # Main entry point

frontend/
├── src/
│   ├── api/          # Axios API wrappers
│   ├── components/   # Reusable UI components (Form, List, Filter)
│   ├── pages/        # Main Dashboard view
│   └── utils/        # Constants and Enums
5. How to Run BackendNavigate to the backend directory: cd backend.Activate the virtual environment: .\venv\Scripts\activate.Install dependencies: pip install flask flask-sqlalchemy flask-marshmallow marshmallow-sqlalchemy flask-cors pytest.Run the application: python app.py.The API will be available at http://127.0.0.1:5000.
6. How to Run FrontendNavigate to the frontend directory: cd frontend.Install dependencies: npm install.Start the development server: npm start.The UI will open at http://localhost:3000.
7. Database SetupThis project uses SQLite for ease of local setup.The database file (tasks.db) is automatically generated in the backend folder when the Flask app starts for the first time.No manual schema migration is required for the initial run.
8. Testing InstructionsBackend tests are provided to verify core behaviors and validation rules.Navigate to the backend folder.Run the test suite: python -m pytest tests/test_tasks.py.Verification covers: task creation, empty title rejection, invalid priority/status rejection, and restricted status transitions.
9. Key Technical DecisionsService Layer Pattern: I used a service layer to isolate business logic (like status transition rules) from the API routes, ensuring the codebase is modular.Marshmallow for Safety: All incoming data is strictly validated via Marshmallow schemas to prevent "invalid states" in the database.Functional React: Used functional components and hooks for state management to maintain modern coding standards.10. AI Usage SummaryAI Tool: Gemini 3 Flash.Interaction: AI helped generate boilerplate code for the layered architecture and initial component structures.Review Process: I manually reviewed and adjusted all generated code to ensure it followed the specific "Archived task" business rules and integrated correctly with the relational database.11. Known Limitations and Future ImprovementsScalability: While SQLite is used for this assessment, the backend is designed for easy migration to PostgreSQL.Authentication: To prioritize "clean engineering" within the 48-hour limit, login systems were excluded in favor of strong validation and testing