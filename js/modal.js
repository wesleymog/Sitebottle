/**
 * Created by wesleymog on 07/10/16.
 */
$(document).on( "click", '.edit_button',function(e) {

    var content = $(this).data('noticia');

    tinyMCE.get('business_skill_content').setContent(content);

});
