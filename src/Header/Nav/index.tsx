'use client'

import React from 'react'

import type { Header as HeaderType } from '@/payload-types'

import { CMSLink } from '@/components/Link'
import Link from 'next/link'
import { SearchIcon, Menu, X } from 'lucide-react'
import Logo from '@/components/Logo/Logo'

export const HeaderNav: React.FC<{ data: HeaderType }> = ({ data }) => {
  const navItems = data?.navItems || []

  return (
    <nav className="hidden md:flex container py-4 justify-between items-center">
      <Link href={'/'}>
        <Logo loading="eager" priority="high" />
      </Link>
      <div className="md:flex gap-3 items-center">
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
  data: HeaderType
}> = ({ data }) => {
  const navItems = data?.navItems || []
  const [isMobileNavOpen, setIsMobileNavOpen] = React.useState(false)

  const toggleNavBar = () => {
    setIsMobileNavOpen((prev) => !prev)
  }

  const closeNavBar = () => {
    setIsMobileNavOpen(false)
  }

  return (
    <nav className="md:hidden container py-4">
      <div className="flex justify-between items-center">
        <Link href={'/'}>
          <Logo loading="eager" priority="high" />
        </Link>
        <button onClick={toggleNavBar}>{isMobileNavOpen ? <X /> : <Menu />}</button>
      </div>
      {isMobileNavOpen && (
        <div className="flex flex-col gap-3 mt-4 place-items-center">
          {navItems.map(({ link }, i) => {
            return (
              <div key={i} onClick={closeNavBar}>
                <CMSLink {...link} appearance="link" />
              </div>
            )
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
