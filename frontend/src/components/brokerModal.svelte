<script>
    export let id;
    export let title;
    export let instructions = [];
    export let isPrivateKeyRequired;
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
                <div>
                    <input type="text" placeholder="Your API Key here." required>
                    <input type="text" placeholder="Your Private Key here." required>
                </div>
            </div>
        {:else}
            <div class="join mt-4">
                <div>
                    <label class="input join-item">
                        <input type="text" placeholder="Your API Key here." required>
                    </label>
                </div>
                <button class="btn btn-neutral join-item">Verify API Key</button>
            </div>
        {/if}
    </div>
    <label class="modal-backdrop" for={id}>Close</label>
</div>