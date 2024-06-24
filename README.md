# Giberish about project

will be here womp womp

# Test Setup in docker

clone this repository:

```sh
git clone https://github.com/jansevounek/Password.git
```

create the .env file:

```sh
touch .env
```

And add three lines:

```sh
VITE_SUPPORTED_LOCALES=en,cz

VITE_SUPABASE_URL=
VITE_SUPABASE_ANON_KEY=
```

Note: you need to add your own values for the last two. That means that you need to create your own supabase project and add the values. [Tutorial](https://supabase.com/docs/guides/getting-started/quickstarts/vue "Tutorial").

And that is basically it run:

```sh
sudo docker-compose up -d
```

That is it your server should be now running on port on localhost 8080.

Note: this is a setup fow linux only (windows is a lot more complicated)

# Test Setup normally

clone this repository:

```sh
git clone https://github.com/jansevounek/Password.git
```

create the .env file:

```sh
touch .env
```

And add three lines:

```sh
VITE_SUPPORTED_LOCALES=en,cz

VITE_SUPABASE_URL=
VITE_SUPABASE_ANON_KEY=
```

Note: you need to add your own values for the last two. That means that you need to create your own supabase project and add the values. [Tutorial](https://supabase.com/docs/guides/getting-started/quickstarts/vue "Tutorial").

The last part is running:

```sh
npm install
```

and then

```sh
npm run dev
```

Your development server is now running at the adress: http://127.0.0.1:5173/
