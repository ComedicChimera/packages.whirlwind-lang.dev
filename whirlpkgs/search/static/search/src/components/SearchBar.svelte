<script>
    export let query, errorMessage

    function updateQuery(event) {
        query = event.target.value
    }
</script>

<div class="search-bar">
    <h1 class="display-1">whirlwind packages</h1>
    <input id="search-input" placeholder="search..." on:change={updateQuery}/>
    {#if errorMessage != ''}
        <div class="error-display">
            {errorMessage}
        </div>
    {/if}
</div>