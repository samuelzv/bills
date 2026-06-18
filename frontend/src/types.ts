export interface Bill {
  id: number
  name: string
  deadline: string
}

export interface CalendarEvent {
  id: number | string
  title: string
  start: string
  end: string | null
}

// FullCalendar is loaded from CDN — declare only what we use
declare global {
  const FullCalendar: {
    Calendar: new (
      el: HTMLElement,
      options: Record<string, unknown>
    ) => {
      render(): void
      refetchEvents(): void
      unselect(): void
    }
  }
}
