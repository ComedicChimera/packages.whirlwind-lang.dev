<script>
    let count = 0;

    function handleClick(event) {
        count += 1
    }
</script>

<svelte:options tag="test-element"/>

<div class="element">
    <button on:click={handleClick}>Count: {count}</button>
</div>