# KuCoNa Digital Operations System

**WordPress website and connected community operations**  
Joshua Nehohwa · Digital systems and web development intern  
Nature's Valley Trust / KuCoNa · June to August 2026

**[Visit the live website →](https://kucona.org.za/)**  
[Back to my GitHub profile](../../README.md) · [Portfolio case-study source](https://github.com/jnehohwa/joshua-portfolio/blob/main/src/data/portfolio.ts)

## The Problem

KuCoNa needed a public website that made its programmes and participation routes easy to understand, alongside structured intake and staff workflows. The public website needed to stay separate from private learner, guardian and operational records.

## My Contribution

I designed and launched the WordPress/Elementor public website and helped connect registration intake to the operations system. My internship work also covered Airtable development, a bilingual community survey, and documentation for staff handover.

| Area | Delivered work recorded in my project documentation |
| --- | --- |
| Website | 15+ structured pages, responsive navigation, programme information and participation routes |
| Programme organisation | Three hubs: Community Care, Learning Hub and Nature Connect |
| Partner directory | 14 partner profiles with descriptions, branding and external links |
| Registration | Tested youth-registration flow through Jotform, Make.com and Airtable, including an integration-log entry |
| Staff workflows | Airtable pages for youth registrations, volunteer applications and integration monitoring |
| Community research | 47-question English/Afrikaans survey with consent branching and linked Google Sheets analytics |
| Handover | Implementation notes, integration specifications, administrator checklists and staff training documentation |

These are delivery details from my internship documentation, not a claim that every workflow is currently operating unchanged on the organisation's live systems.

## Website Work

- Organised the site's content around the centre's programme model.
- Built programme pages, public calls to action, centre information and registration pathways.
- Incorporated stakeholder-approved content and community media.
- Tested desktop, reduced-width Safari and mobile layouts for navigation, alignment, overflow and image positioning.
- Created a partner directory to connect visitors with supporting organisations.

WordPress and Elementor supported a maintainable publishing workflow for the organisation. The custom engineering work centred on content structure, responsive presentation and the boundaries between the website, forms and operational records.

## System Architecture

| Component | Responsibility |
| --- | --- |
| WordPress / Elementor | Public information, programme pages and participation links |
| Jotform | Structured registration intake |
| Make.com | Route registration submissions into Airtable |
| Airtable | Operational records, linked data, staff views and integration logging |
| Google Forms / Sheets | Bilingual community survey and response analysis |

The tested core intake path was **WordPress → Jotform → Make.com → Airtable**. Airtable was treated as the operational source of truth; WordPress remained the public-facing layer.

## Decisions and Tradeoffs

**Keep sensitive data outside the public website.** Learner and guardian details, health information and internal notes belong in controlled operational tools. Public publishing should expose only approved fields.

**Use tools staff can maintain.** WordPress and Elementor support content updates, while Jotform and Airtable support structured intake without requiring staff to maintain a custom application.

**Make integrations diagnosable.** Integration logging and duplicate-prevention support help staff trace intake issues rather than relying on an unexplained form submission.

**Separate the delivered foundation from later expansion.** The website and tested core registration flow do not imply that the entire proposed programme-management roadmap was completed.

## Delivery Boundary

The following remained follow-up work in my handover documentation:

- Full Airtable Staff Home operational dashboard.
- Air WP Sync automated session publishing.
- Final volunteer and indemnity automation acceptance testing.
- Public Google Calendar integration.
- Website contact-form inbox configuration.
- Monitoring dashboards, newsletters and other Phase 2 services.

Attendance QR, certificate-progress workflows and weekly digests appeared in planning notes. They are not presented here as completed features.

## What This Project Demonstrates

A real stakeholder project connecting public web delivery, data modelling, workflow integration, privacy boundaries and handover. It required thinking about both the visitor experience and the people who would operate the system after the internship.

## About This Case Study

This folder documents my contribution to an organisation-owned WordPress project. The live site is hosted at **[kucona.org.za](https://kucona.org.za/)**. This is a portfolio case study, not a WordPress source-code export.

The organisation retains its content and branding. Private records, credentials and internal system exports are not included.
