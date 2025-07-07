<script>
    export let id;
    export let title;
    export let instructions = [];
    export let isPrivateKeyRequired;

    let apiKey = '';
    let privateKey = '';

    function addApiKey(brokerName, apiKey, privateKey = '') {

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