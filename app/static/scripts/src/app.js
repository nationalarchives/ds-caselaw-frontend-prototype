import $ from 'jquery'

(function ($) {
    $.fn.manage_filters = function (options) {
        const settings = $.extend({}, $.fn.manage_filters.defaults, options);
        return this.each(() => {

            const $toggle_area = $('.js-results-facets', $(this));

            const $control_container = $('.js-results-control-container', $(this));

            const btn = $('<button>', {
                'class': 'results__toggle-control',
                'type': 'button',
                'text': settings.collapsed_text,
                'click': (e) => {
                    $toggle_area.slideToggle(500);

                    const $el = $(e.target);

                    $el.toggleClass('collapsed');

                    $el.text(() => {
                        return $el.text() === settings.collapsed_text ? settings.expanded_text : settings.collapsed_text;
                    })
                }
            });

            if (settings.initially_hidden) {
                btn.trigger('click');
            }

            $control_container.append(btn)
        });
    };

    $.fn.manage_filters.defaults = {
        'collapsed_text': 'Collapse search options',
        'expanded_text': 'Expand search options',
        'initially_hidden': true
    }
}($));

$('.js-results-facets-wrapper').manage_filters();