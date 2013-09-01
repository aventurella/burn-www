from confypy import Config, Location

settings = Config()
settings.locations = [
    Location.from_env_path('BURN_CONFIG')
]
