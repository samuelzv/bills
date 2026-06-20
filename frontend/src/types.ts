export interface Bill {
  id: number
  name: string
  deadline: string,
  amount: number,
}

export interface CalendarEvent {
  id: number | string
  title: string
  start: string
  end: string | null
  amount: number | null
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
