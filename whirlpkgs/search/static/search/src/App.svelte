<script>
    import SearchDisplay from './components/SearchDisplay.svelte'
    import SearchBar from './components/SearchBar.svelte'
</script>

<svelte:options tag="search-app"/>

<div class="search-app">
    <div class="row">
        <h1 class="display-1">whirlwind packages</h1>
        <SearchBar></SearchBar>
    </div>
    <div class="row">
        <SearchDisplay></SearchDisplay>
    </div>
</div>