<script>
    import axios from "axios";
    import { goto } from '$app/navigation'

    let email = '';
    let password = '';

    let createUserResponse = '';
    let loginUserResponse = '';

    function createUser(email, password) {
        axios.post(
            '/api/users/',
            {
                email: email,
                password: password
            }
        )
            .then(() => {
                createUserResponse = 'Successfully created an account, login using the same credentials!'
            })
            .catch(error => {
                console.error(error);
                createUserResponse = 'There was an issue creating your account.'
            })
    }

    function createSecretKey(password) {
        return axios.post(
            'api/encryption/derive-key',
            {
                'password': password
            },
            {
                headers: {
                    'Authorization': `Bearer ${sessionStorage.getItem('access_token')}`,
                    'Content-Type': 'application/json'
                }
            }
        ).then(response => response.data);
    }

     async function loginUser(email, password) {
        // OAuth2 requires a url-encoded form, and will deny JSON
        const formData = new URLSearchParams();
        formData.append('grant_type', 'password');
        formData.append('username', email);
        formData.append('password', password)

         axios.post(
             'api/auth/login',
             formData,
             {
                 headers: {
                     'Content-Type': 'application/x-www-form-urlencoded'
                 }
             }
         )
             .then(
                 async response => {
                    const token = response.data.access_token;
                    loginUserResponse = 'Successful login, you will be redirected shortly.';

                    sessionStorage.setItem("access_token", token);

                    const secret_key = await createSecretKey(password);
                    sessionStorage.setItem("secret_key", secret_key);

                    goto('/dashboard');
                 }
             )
             .catch(error => {
                 console.log(error);
                 loginUserResponse = 'There was an issue trying to login.'
             })
    }
</script>

<div class="hero min-h-screen">
    <div class="hero-content flex-col lg:flex-row-reverse">
        <div class="text-center lg:text-left">
            <h1 class="text-5xl font-bold">Portfolio Visualiser</h1>
            <p class="py-6">
                Investment Portfolio Analyser, Visualiser and Performance Backtesting. <br>
                Supporting a range of Brokers specialising from Stocks to Crypto Exchanges.
            </p>
        </div>
        <div class="card w-full max-w-sm shrink-0">
            <div class="card-body">
                <fieldset class="fieldset">
                    <p>Email</p>
                    <label class="input validator">
                        <svg class="h-[1em] opacity-50" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                            <g
                                    stroke-linejoin="round"
                                    stroke-linecap="round"
                                    stroke-width="2.5"
                                    fill="none"
                                    stroke="currentColor"
                            >
                                <rect width="20" height="16" x="2" y="4" rx="2"></rect>
                                <path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"></path>
                            </g>
                        </svg>
                        <input bind:value={email} type="email" required/>
                    </label>

                    <p>Password</p>
                    <label class="input validator">
                        <svg class="h-[1em] opacity-50" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                            <g
                                    stroke-linejoin="round"
                                    stroke-linecap="round"
                                    stroke-width="2.5"
                                    fill="none"
                                    stroke="currentColor"
                                >
                                <path d="M2.586 17.414A2 2 0 0 0 2 18.828V21a1 1 0 0 0 1 1h3a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h1a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h.172a2 2 0 0 0 1.414-.586l.814-.814a6.5 6.5 0 1 0-4-4z"></path>
                                <circle cx="16.5" cy="7.5" r=".5" fill="currentColor"></circle>
                            </g>
                        </svg>
                        <input bind:value={password} type="password" required/>
                    </label>
                    <button on:click={() => loginUser(email, password)} class="btn btn-neutral mt-4">Login</button>
                    <p>{loginUserResponse}</p>

                    <div class="divider"></div>

                    <button on:click={() => createUser(email, password)} class="btn">Create an Account</button>
                    <p>{createUserResponse}</p>
                    <a class="btn mt-4 btn-ghost link-hover" href="/demos/dashboard">See a Demo?</a>
                </fieldset>
            </div>
        </div>
    </div>
</div>