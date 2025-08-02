<script lang="ts">
    import {api} from "../../config/axios.config.js";
    
    let email = '';
    let password = '';

    /**
     * Create a user in the database.
     *
     * @param email The user's email.
     * @param password The user's password.
     */
    function createUser(email: string, password: string) {
        let response = api.post(
            "/user/",
            {
                "email": email,
                "password": password
            }
        )
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
            </div>
        </div>
    </div>
</div>