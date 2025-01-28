# full-stack-project
Youtube full stack project walkthrough

# Run flask app
- flask run

# Sequence Diagram
sequenceDiagram
    participant User
    participant React App
    participant Flask Backend
    User->>React App: Open Application
    React App->>Flask Backend: Fetch Contacts (GET)
    Flask Backend-->>React App: Return Contact List
    React App->>User: Display Contacts
    User->>React App: Open Create/Edit Modal
    React App->>User: Show Contact Form
    User->>React App: Submit Contact Details
    React App->>Flask Backend: Create/Update Contact
    Flask Backend-->>React App: Confirm Operation
    React App->>React App: Update Contact List
