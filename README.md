# Weather Application

## Project Overview
A comprehensive weather tracking and information application built with Django and modern web technologies.

## Features
- Real-time weather data retrieval
- User-friendly web interface
- Backend API for weather information
- Caching with Redis for improved performance

## Technology Stack
- **Backend**: 
  - Django 5.1.4
  - Django REST Framework
  - Redis for caching
- **Frontend**: 
  - Vanilla JavaScript
  - HTML5
  - Bootstrap

## Prerequisites
- Python 3.8+
- pip
- Redis

## Installation

### Backend Setup
1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r backend/requirements.txt
   ```
4. Set up environment variables in `.env`
5. Run migrations:
   ```bash
   python backend/manage.py migrate
   ```
6. Start the development server:
   ```bash
   python backend/manage.py runserver
   ```

### Frontend Setup
- Simply open `frontend/index.html` in a modern web browser

## Configuration
- Check `.env` file for configuration details
- Modify `backend/weather_api/settings.py` for advanced settings

## Contributing
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request
