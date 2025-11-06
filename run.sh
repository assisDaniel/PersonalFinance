#!/bin/bash

# Define project-specific variables
PROJECT_NAME="PersonalFinance"
DEV_SETTINGS="$PROJECT_NAME.settings.dev"
PROD_SETTINGS="$PROJECT_NAME.settings.prod"
STATIC_DIR="$PROJECT_NAME/static/" # Adjusted based on previous discussion for STATIC_ROOT

# --- Helper Functions ---

clean_build() {
    echo "Removing built files from '$STATIC_DIR'"
    rm -rf "$STATIC_DIR"
}

# --- Main Logic ---

case "$1" in
    build)
        echo "Building app for production..."
        # Set Django settings to production for static file collection
        export DJANGO_SETTINGS_MODULE="$DEV_SETTINGS"
        clean_build
        echo "Collecting static files..."
        python manage.py collectstatic --no-input --clear --settings="$DEV_SETTINGS"
        echo "Build process complete."
    ;;
    clean)
        clean_build
        echo "Static files cleaned."
    ;;
    # UPDATED COMMAND: migrate
    migrate)
        echo "Running database migrations..."
        export DJANGO_SETTINGS_MODULE="$DEV_SETTINGS" # Default to dev settings for migrations

        APP_NAME=""
        if [ -n "$2" ]; then # Check if a second argument (app name) is provided
            APP_NAME="$2"
            echo "Creating migrations for app: '$APP_NAME'"
            python manage.py makemigrations "$APP_NAME" # Pass the app name to makemigrations
        else
            echo "Creating migrations for all apps (no app name provided)."
            python manage.py makemigrations # No app name, creates for all
        fi

        echo "Applying migrations to the database..."
        python manage.py migrate # migrate always applies for all apps
        echo "Database migrations complete."
    ;;
    help)
        echo "Available commands:"
        echo "  (no parameters)    => Starts the application in development mode (default port 8013)"
        echo "  clean              => Cleans the target static directory"
        echo "  build              => Executes static file collection, preparing for deployment."
        echo "  migrate [app_name] => Runs Django database migrations."
        echo "                       'app_name' is optional. If provided, makemigrations will run for that app only."
        echo "  help               => Displays this help message."
    ;;
    *)
        echo "Starting app in development mode on 0.0.0.0:8013..."
        export DJANGO_SETTINGS_MODULE="$DEV_SETTINGS"
        clean_build
        python manage.py runserver localhost:4321 --settings="$DEV_SETTINGS"
    ;;
esac