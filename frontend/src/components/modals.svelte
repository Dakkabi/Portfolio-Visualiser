<script>
    import { onMount, onDestroy } from "svelte";

    export let isOpen = false;
    export let onClose = () => {};

    function handleOutsideClick(event) {
        /*
        Event fired when user clicks outside the modal content.
         */
        const modalContent = document.querySelector('.modal-content');
        if (modalContent && !modalContent.contains(event.target)) {
            onClose();
        }
    }

    onMount(() => {
      document.addEventListener('click', handleOutsideClick)
    })

    onDestroy(() => {
        document.removeEventListener('click', handleOutsideClick)
    })
</script>

{#if isOpen}
    <div class="modal modal-open">
        <div class="modal-box">
            <!-- Custom Content -->
            <slot></slot>
        </div>
    </div>
{/if}