import type { Bill, CalendarEvent } from './types'

type FullCalendarInstance = InstanceType<typeof FullCalendar.Calendar>

interface FullCalendarSelectInfo {
  startStr: string
  endStr: string
}

interface FullCalendarEventInfo {
  event: {
    id: string
    title: string
    startStr: string
    endStr: string
  }
}

function loadBills(): Bill[] {
  const el = document.getElementById('bills-data')
  if (!el?.textContent) return []
  return JSON.parse(el.textContent) as Bill[]
}

export function calendarApp() {
  return {
    open: false as boolean,
    selectedEvent: null as FullCalendarEventInfo['event'] | null,
    calendar: null as FullCalendarInstance | null,
    events: [] as CalendarEvent[],
    newEventTitle: null as string | null,
    newEventStart: null as string | null,
    newEventEnd: null as string | null,

    init() {
      this.events = loadBills().map((item) => ({
        id: item.id,
        title: item.name,
        start: item.deadline,
        end: item.deadline,
      }))

      this.calendar = new FullCalendar.Calendar(this.$refs['calendar'] as HTMLElement, {
        events: (_info: unknown, success: (events: CalendarEvent[]) => void) =>
          success(this.events),
        initialDate: '2026-06-01',
        initialView: 'dayGridMonth',
        selectable: true,
        unselectAuto: false,
        editable: true,
        select: (info: FullCalendarSelectInfo) => {
          this.newEventStart = info.startStr
          this.newEventEnd = info.endStr
        },
        eventClick: (info: FullCalendarEventInfo) => {
          this.selectedEvent = info.event
          this.open = true
        },
        eventChange: (info: FullCalendarEventInfo) => {
          const index = this.getEventIndex(info)
          this.events[index].start = info.event.startStr
          this.events[index].end = info.event.endStr
        },
      })

      this.calendar.render()
    },

    getEventIndex(info: FullCalendarEventInfo): number {
      return this.events.findIndex((event) => event.id == info.event.id)
    },

    addEvent() {
      if (!this.newEventTitle || !this.newEventStart) {
        alert('Please choose a title and start date for the event!')
        return
      }

      this.events.push({
        id: Date.now(),
        title: this.newEventTitle,
        start: this.newEventStart,
        end: this.newEventEnd,
      })

      this.calendar?.refetchEvents()

      this.newEventTitle = null
      this.newEventStart = null
      this.newEventEnd = null

      this.calendar?.unselect()
    },
  }
}
