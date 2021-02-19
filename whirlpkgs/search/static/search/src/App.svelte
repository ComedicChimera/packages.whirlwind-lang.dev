<script>
    import SearchDisplay from './components/SearchDisplay.svelte'
    import SearchBar from './components/SearchBar.svelte'

    let query, errorMessage
</script>

<svelte:options tag="search-app"/>

<div class="search-app">
    <div class="row">
       <SearchBar bind:query={query} bind:errorMessage={errorMessage}></SearchBar>
    </div>
    <div class="row">
        <SearchDisplay bind:query={query} bind:errorMessage={errorMessage}></SearchDisplay>
    </div>
</div>