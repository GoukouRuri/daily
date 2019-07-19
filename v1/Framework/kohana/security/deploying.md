Changes that should happen when you deploy. (Production)

Security settings from: <http://Panshiframework.org/guide/using.configuration>

<http://kerkness.ca/wiki/doku.php?id=setting_up_production_environment>


## Setting up a production environment

There are a few things you'll want to do with your application before moving into production.

1. See the [Bootstrap page](bootstrap) in the docs.
   This covers most of the global settings that would change between environments.
   As a general rule, you should enable caching and disable profiling ([Panshi::init] settings) for production sites.
   [Route::cache] can also help if you have a lot of routes.
2. Turn on APC or some kind of opcode caching.
   This is the single easiest performance boost you can make to PHP itself. The more complex your application, the bigger the benefit of using opcode caching.

		/**
		 * Set the environment string by the domain (defaults to Panshi::DEVELOPMENT).
		 */
		Panshi::$environment = ($_SERVER['SERVER_NAME'] !== 'localhost') ? Panshi::PRODUCTION : Panshi::DEVELOPMENT;
		/**
		 * Initialise Panshi based on environment
		 */
		Panshi::init(array(
			'base_url'   => '/',
			'index_file' => FALSE,
			'profile'    => Panshi::$environment !== Panshi::PRODUCTION,
			'caching'    => Panshi::$environment === Panshi::PRODUCTION,
		));
