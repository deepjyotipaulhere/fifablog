<template>
    <div>
        <div class="header">
            <div class="bx--grid">
                <div class="bx--row">
                <div class="bx--col-xs-12 " style="padding:2rem 0">
                    <h1 class="page-title" style="margin:0">Share your experience</h1>
                </div>
                </div>
            </div>
        </div>
        <div class="bx--grid">
            <br>
            <div class="bx--form-item">
                <input id="text-input-3" type="text" class="bx--text-input" placeholder="Optional placeholder text">
                <label for="text-input-3" class="bx--label">Give a proper title</label>
            </div>
            <br>
            <div class="bx--form-item">
                <textarea id="text-area-2" class="bx--text-area" rows="10" cols="50" placeholder="Placeholder text."></textarea>
                <label for="text-area-2" class="bx--label">Write your story here</label>
            </div>
            <br>
            <div class="bx--form-item">
                <strong class="bx--label">Add good photos</strong>
                <p class="bx--label-description">only .jpg and .png files. 500kb max file size.</p>
                <div class="bx--file" data-file>
                    <label
                    for="your-file-importer-id-here"
                    class="bx--file-btn bx--btn bx--btn--secondary"
                    role="button"
                    tabindex="0">Add files</label>
                    <input
                    type="file"
                    class="bx--file-input"
                    id="your-file-importer-id-here"
                    data-file-uploader
                    data-target="[data-file-container]"
                    multiple
                    />
                    <div data-file-container class="bx--file-container"></div>
                </div>
            </div>
            <br>
            <div class="bx--form-item">
                <button class="bx--btn bx--btn--primary" type="button">Submit</button>
            </div>
        </div>

    </div>
</template>

<script>
export default {

}
</script>

<style>

</style>
