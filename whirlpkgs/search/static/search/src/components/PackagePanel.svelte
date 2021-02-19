<script>
    export let pkg
</script>

<div class="package-panel">
    <span class="name">{pkg.name}</span>
    {#if !pkg.isStdpkg}
        <div class="stars">
            <span class="star-count">pkg.starCount</span>
        </div>
    {/if}
    <div class="date">Last release: {pkg.date}</div>
    <div class="description">{pkg.description}</div>
</div>