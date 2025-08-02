<script lang="ts">
    import {api} from "../../config/axios.config.js";
    
    let email = '';
    let password = '';

    let displayCreateUserMessage = '';
    let createUserAlertType = '';

    /**
     * Create a user in the database.
     *
     * @param email The user's email.
     * @param password The user's password.
     */
    function createUser(email: string, password: string) {
        api.post(
            "/user/",
            {
                "email": email,
                "password": password
            }
        )
            .then(response => {
                createUserAlertType = "success";
                displayCreateUserMessage = "Success! You will be shortly redirected.";
            })
            .catch(error => {
                createUserAlertType = "error";
                displayCreateUserMessage = `${error.status}: ${error.response.data.detail}`;
            })
    }
</script>

<div class="hero bg-base-200 min-h-screen">
    <div class="hero-content bg-base-100 flex-col rounded-lg">
        <div class="text-center">
            <h1 class="text-3xl font-bold">Sign up for Portfolio Analysis</h1>
        </div>
        <div class="card w-full max-w-sm shrink-0">
            <div class="card-body">
                <fieldset class="fieldset">
                    <label class="label">Email</label>
                    <input bind:value={email} type="email" class="input" placeholder="name@domain.com" />
                    <label class="label">Password</label>
                    <input bind:value={password} type="password" class="input" placeholder="Password"/>

                    <button on:click={() => createUser(email, password)} class="btn btn-neutral mt-4">Sign Up</button>
                </fieldset>

                {#if displayCreateUserMessage}
                    <div role="alert" class="alert alert-soft alert-{createUserAlertType}">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="h-6 w-6 shrink-0 stroke-current">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                        </svg>
                        <span>{displayCreateUserMessage}</span>
                    </div>
                {/if}

                <div class="divider"></div>

                <span class="text-center">Already have an account? <a href="/login" class="link-hover font-bold">Login Here.</a></span>
            </div>
        </div>
    </div>
</div>