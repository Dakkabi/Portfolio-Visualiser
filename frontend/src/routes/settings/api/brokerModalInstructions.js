export let brokersInfo = [
    {
        id: 'trading212_modal',
        title: 'Trading212',
        instructions: [
            `1. On the Trading212 main page, click the Hamburger icon to bring up an Information page.`,
            `<img src="/brokers/trading212/trading212_settings_instruction.png" alt="">`,
            `2. Click the Settings row, and then the API row.`,
            `<img src="/brokers/trading212/trading212_api_creation_instruction.png" alt="">`,
            `3. Give it a meaningful name, and please give all permissions for the least issues.`,
            `<img src="/brokers/trading212/trading212_api_permission_instruction.png" alt="">`,
            `4. Upon creation, copy it using the Copy icon, and input it into the box below.`,
            `<img src="/brokers/trading212/trading212_api_key_save.png" alt="">`
        ]
    },
    {
        id: 'kraken_exchange_modal',
        title: "Kraken Exchange",
        instructions: [
            `1. On the Kraken main page, click your User icon, go to Settings. Choose <b>Connections & API</b> tab, and click Create API Key for Spot Trading API.`,
            `<img src="/brokers/kraken/kraken_create_api_key_instruction.png" alt="" >`,
            `2. For permissions, all would be best in terms of least issues, however the image below offers the bare minimum requirement.`,
            `<img src="/brokers/kraken/kraken_permissions_instruction.png" alt="" >`,
            `3. Once created, copy the API key and Private key into their respective boxes below, they are not interchangeable, and cannot be viewed once closed!`,
            `<img src="/brokers/kraken/kraken_save_api_keys.png" alt="" >`
        ]
    }
]