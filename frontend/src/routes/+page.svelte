<script>
    import axios from "axios";
    import {error} from "@sveltejs/kit";
    let email = '';
    let password = '';

    let createUserResponse = '';
    let loginUserResponse = '';

    function createUser(email, password) {
        axios.post(
            '/api/users/',
            {
                "email": email,
                "password": password
            }
        )
            .then(
                response => console.log(response.data)
            )
            .catch(
                error => console.error(error)
            )
    }

    function loginUser(email, password) {

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
                    <p class="">{createUserResponse}</p>
                    <a class="btn mt-4 btn-ghost link-hover" href="/demos/dashboard">See a Demo?</a>
                </fieldset>
            </div>
        </div>
    </div>
</div>