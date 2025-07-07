<script>
    import { globalColour } from "../../../components/svgGlobalColour.js";
    import { brokersInfo } from "./brokerModalInstructions.js";

    import BrokerModal from "../../../components/brokerModal.svelte";
    const brokers = brokersInfo

</script>

<div class="drawer drawer-open">
    <input class="drawer-toggle">
    <div class="drawer-content">
        <div class="text-center">
            <!-- Page Content -->
            <h1 class="text-5xl font-bold mt-2">API Keys</h1>

            <!-- Stock -->
            <div class="divider text-xl mt-4">Stock Brokers</div>
            <ul class="menu menu-horizontal">
                <li class="card bg-base-100 image-full w-72 shadow-sm">
                    <label for="trading212_modal">
                        <img
                            src="/brokers/trading212/trading_212_logo.png"
                            alt="Trading212"
                        />
                    </label>
                </li>
            </ul>
            <!-- Crypto -->
            <div class="divider text-xl mt-4">Crypto Exchanges</div>
            <ul class="menu menu-horizontal">
                <li class="card bg-base-100 image-full w-72 shadow-sm">
                    <label for="kraken_modal">
                        <img
                            src="/brokers/kraken/kraken_logo.png"
                            alt="Kraken Crypto Exchange"
                        />
                    </label>
                </li>
            </ul>
        </div>
    </div>
    <div class="drawer-side">
        <ul class="menu bg-base-200 text-base-content min-h-full w-80 p-4">
            <li>
                <details open>
                    <summary>
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="{globalColour}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <circle cx="12" cy="12" r="3"></circle>
                            <path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path>
                        </svg>
                        Settings
                    </summary>
                    <ul>
                        <li><a href="/settings/api">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="{globalColour}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path>
                                <path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path>
                            </svg>
                            API Keys
                        </a></li>
                    </ul>
                </details>
            </li>

            <div class="divider"></div>

            <li><a href="/">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="{globalColour}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M15 3h6v18h-6M10 17l5-5-5-5M13.8 12H3"/>
                </svg>
                Log Out
            </a></li>
        </ul>
    </div>
</div>

{#each brokers as broker}
    <BrokerModal
        id={broker.id}
        title={broker.title}
        instructions={broker.instructions}
        isPrivateKeyRequired={broker.isPrivateKeyRequired}
    />
{/each}