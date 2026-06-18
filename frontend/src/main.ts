import Alpine from 'alpinejs'
import focus from '@alpinejs/focus'
import ui from '@alpinejs/ui'
import { calendarApp } from './calendar-app'

Alpine.plugin(focus)
Alpine.plugin(ui)

Alpine.data('calendarApp', calendarApp)

Alpine.start()
