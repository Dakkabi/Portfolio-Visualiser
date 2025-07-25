<script>
    import api from "@api";

    export let id;
    export let title;
    export let instructions = [];
    export let isPrivateKeyRequired;

    let apiKey = '';
    let privateKey = '';

    /**
     * Trim the broker name from the modal id, slicing the "_modal" and capitalising the first letter.
     * "broker_modal" -> "Broker".
     *
     * @param brokerModalId The modal id opened currently.
     * @return String The broker name.
     */
    function trimBrokerNameFromModalId(brokerModalId) {
        let brokerName = brokerModalId.slice(0, -5);
        return brokerName.charAt(0).toUpperCase() + brokerName.slice(1)
    }

    /**
     * Send an API request to add (or update if already exists) the API Key and if provided Private Key
     * into the database.
     *
     * @param brokerModalId The modal the user was on when they entered their API keys.
     * @param apiKey The API key.
     * @param privateKey The Private key if required.
     */
    function addApiKey(brokerModalId, apiKey, privateKey = '') {
        let brokerName = trimBrokerNameFromModalId(brokerModalId);

        try {
            const response = api.post(
                "/api-keys/",
                {
                    "api_key": {
                        "broker_name": brokerName,
                        "api_key": apiKey,
                        "private_key": privateKey
                    },
                    "secret_key": {
                        "secret_key": sessionStorage.getItem("secret_key")
                    }
                }
            )
        } catch (error) {
            console.log(error);
        }
    }
</script>

<input type="checkbox" id={id} class="modal-toggle">
<div class="modal" role="dialog">
    <div class="modal-box bg-base-200">
        <h1 class="text-center font-bold text-2xl">{title}</h1>
        <p>
            {#each instructions as step, i}
                {@html step} <br>
            {/each}
        </p>

        {#if isPrivateKeyRequired}
            <div class="join mt-4">
                <fieldset class="fieldset">
                    <legend class="fieldset-legend">Enter API Key.</legend>
                    <input bind:value={apiKey} type="text" class="input btn btn-neutral rounded-2xl" placeholder="...">
                    <legend class="fieldset-legend">Enter Private Key.</legend>
                    <input bind:value={privateKey} type="text" class="input btn btn-neutral rounded-2xl" placeholder="...">

                    <button on:click={() => addApiKey(id, apiKey, privateKey)} class="btn btn-wide btn-neutral rounded-2xl mt-4">Verify Keys</button>
                </fieldset>
            </div>
        {:else}
            <div class="join mt-4">
                <div>
                    <label class="input join-item">
                        <input bind:value={apiKey} type="text" placeholder="Your API Key here." required>
                    </label>
                </div>
                <button on:click={() => addApiKey(id, apiKey)} class="btn btn-neutral join-item">Verify API Key</button>
            </div>
        {/if}
    </div>
    <label class="modal-backdrop" for={id}>Close</label>
</div>