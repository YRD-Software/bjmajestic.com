'use client'

import { useRouter, usePathname } from 'next/navigation'
import { useState, useTransition, useEffect } from 'react'
import { cn } from '@/utilities/ui'
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from '@/components/ui/select'

type Locale = 'en' | 'zh-Hans'

interface LocaleSelectorProps {
  className?: string
}

export function LocaleSelector({ className }: LocaleSelectorProps) {
  const router = useRouter()
  const pathname = usePathname()
  const [isPending, startTransition] = useTransition()
  const [currentLocale, setCurrentLocale] = useState<Locale>('en')

  useEffect(() => {
    if (typeof window !== 'undefined') {
      const savedLocale = localStorage.getItem('preferredLocale') as Locale | null
      setCurrentLocale(savedLocale || 'en')
    }
  }, [])

  const handleLocaleChange = (newLocale: Locale) => {
    // Save preference to localStorage
    localStorage.setItem('preferredLocale', newLocale)
    // Save preference to cookie that will be sent with requests
    document.cookie = `NEXT_LOCALE=${newLocale};path=/;max-age=31536000`

    setCurrentLocale(newLocale)

    // Reload the page to apply the new locale
    startTransition(() => {
      router.refresh()
    })
  }

  return (
    <div className={cn('', className)}>
      <Select onValueChange={handleLocaleChange} value={currentLocale} disabled={isPending}>
        <SelectTrigger
          aria-label="Select a language"
          className="w-auto bg-transparent gap-2 pl-0 md:pl-3 border-none"
        >
          <SelectValue placeholder="Language" />
        </SelectTrigger>
        <SelectContent>
          <SelectItem value="en">English</SelectItem>
          <SelectItem value="zh-Hans">中文</SelectItem>
        </SelectContent>
      </Select>
    </div>
  )
}
