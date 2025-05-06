'use client'

import React from 'react'

import type { Header as HeaderType } from '@/payload-types'

import { CMSLink } from '@/components/Link'
import Link from 'next/link'
import { SearchIcon, Menu, X } from 'lucide-react'

export const HeaderNav: React.FC<{ data: HeaderType }> = ({ data }) => {
  const navItems = data?.navItems || []

  return (
    <nav>
      <div className="hidden md:flex gap-3 items-center">
        {navItems.map(({ link }, i) => {
          return <CMSLink key={i} {...link} appearance="link" />
        })}
        <Link href="/search">
          <span className="sr-only">Search</span>
          <SearchIcon className="w-5 text-text" />
        </Link>
      </div>
    </nav>
  )
}

export const HeaderMobileNav: React.FC<{
  data: HeaderType}> = ({ data }) => {
  const navItems = data?.navItems || []
  const [isMobileNavOpen, setIsMobileNavOpen] = React.useState(false)
  const toggleNavBar = () => {
    setIsMobileNavOpen((prev) => !prev)
  }
  return (
    <nav className="md:hidden">
      <button onClick={toggleNavBar}>
        {isMobileNavOpen ? <X /> : <Menu />}
      </button>
      {isMobileNavOpen && (
        <div>
          {navItems.map(({ link }, i) => {
            return <CMSLink key={i} {...link} appearance="link" />
          })}
          <Link href="/search">
            <span className="sr-only">Search</span>
            <SearchIcon className="w-5 text-text" />
          </Link>
        </div>
      )}
    </nav>
  )
}
