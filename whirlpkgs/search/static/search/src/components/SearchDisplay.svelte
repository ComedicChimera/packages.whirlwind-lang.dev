<script>
    import { PackagePanel } from './PackagePanel.svelte'
    import { Client } from '../client.js'

    export let query, errorMessage

    let client = Client()

    let queryResults = []

    $: {
        client.fetchResults(query)
            .then(results => {
                queryResults = results
            }).catch(err => {
                errorMessage = err
            })
    }
</script>

<div class="search-display">
    {#each queryResults as pkg (pkg.id)}
        <PackagePanel pkg={pkg}></PackagePanel>
    {/each}
</div>