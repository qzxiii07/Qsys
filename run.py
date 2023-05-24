import os
from app import app
# from app.config import DevelopmentConfig, ProductionConfig, TestingConfig

if __name__ == '__main__':
    # if os.environ.get('FLASK_ENV') == 'production':
    #     app.config.from_object(ProductionConfig)
    # elif os.environ.get('FLASK_ENV') == 'testing':
    #     app.config.from_object(TestingConfig)
    # else:
    #     app.config.from_object(DevelopmentConfig)
    
    app.app.run(debug=True) 