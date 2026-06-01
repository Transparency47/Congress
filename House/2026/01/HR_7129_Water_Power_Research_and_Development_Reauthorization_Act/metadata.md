# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7129?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7129
- Title: Water Power Research and Development Reauthorization Act
- Congress: 119
- Bill type: HR
- Bill number: 7129
- Origin chamber: House
- Introduced date: 2026-01-16
- Update date: 2026-05-21T08:08:56Z
- Update date including text: 2026-05-21T08:08:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-16: Introduced in House
- 2026-01-16 - IntroReferral: Introduced in House
- 2026-01-16 - IntroReferral: Introduced in House
- 2026-01-16 - IntroReferral: Referred to the Committee on Science, Space, and Technology, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-01-16 - IntroReferral: Referred to the Committee on Science, Space, and Technology, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-20 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-20 - Committee: Ordered to be Reported (Amended) by Voice Vote.
- Latest action: 2026-01-16: Introduced in House

## Actions

- 2026-01-16 - IntroReferral: Introduced in House
- 2026-01-16 - IntroReferral: Introduced in House
- 2026-01-16 - IntroReferral: Referred to the Committee on Science, Space, and Technology, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-01-16 - IntroReferral: Referred to the Committee on Science, Space, and Technology, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-20 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-20 - Committee: Ordered to be Reported (Amended) by Voice Vote.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-16",
    "latestAction": {
      "actionDate": "2026-01-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7129",
    "number": "7129",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "B001278",
        "district": "1",
        "firstName": "Suzanne",
        "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
        "lastName": "Bonamici",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "Water Power Research and Development Reauthorization Act",
    "type": "HR",
    "updateDate": "2026-05-21T08:08:56Z",
    "updateDateIncludingText": "2026-05-21T08:08:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-16",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Science, Space, and Technology, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-16",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Science, Space, and Technology, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": [
          {
            "date": "2026-05-20T18:23:37Z",
            "name": "Markup By"
          },
          {
            "date": "2026-01-16T20:02:25Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-01-16T20:02:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "B001323",
      "district": "0",
      "firstName": "Nicholas",
      "fullName": "Rep. Begich, Nicholas J. [R-AK-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Begich",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-01-16",
      "state": "AK"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7129ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7129\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 16, 2026 Ms. Bonamici (for herself and Mr. Begich ) introduced the following bill; which was referred to the Committee on Science, Space, and Technology , and in addition to the Committee on Education and Workforce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Energy Independence and Security Act of 2007 to reauthorize water power research, development, demonstration, and commercial application activities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Water Power Research and Development Reauthorization Act .\n#### 2. Water power research and development\nSubtitle C of title VI of the Energy Independence and Security Act of 2007 ( Public Law 110\u2013140 ; 42 U.S.C. 17211 et seq. ) is amended\u2014\n**(1)**\nin section 633 ( 42 U.S.C. 17212 ; relating to water power technology research, development, and demonstration)\u2014\n**(A)**\nin paragraph (1), by striking capacity and reduce the cost inserting capacity or efficiency, and reduce the cost, ; and\n**(B)**\nby adding at the end the following new paragraph:\n(5) To advance scalable, United States-based manufacturing of composite and additive manufactured marine energy components through collaborations with regional universities and industry, including advanced composite research facilities and additive manufacturing facilities. ;\n**(2)**\nin section 634 ( 42 U.S.C. 17213 ; relating to hydropower research, development, and demonstration)\u2014\n**(A)**\nin the matter preceding paragraph (1), by inserting generation, after efficiency, ;\n**(B)**\nin paragraph (2), in the matter preceding subparagraph (A), by inserting , cybersecurity, after physical ;\n**(C)**\nby amending paragraph (3) to read as follows:\n(3) study, in conjunction with other relevant Federal agencies, State agencies, local agencies, and Tribal entities (including Alaska Native Corporations), as appropriate, methods to improve the hydropower licensing process, including by compiling current environmental data and studies, accepted best practices, public comments, and methodologies to assess the full range of potential environmental and economic impacts; ;\n**(D)**\nin paragraph (6)\u2014\n**(i)**\nin the matter preceding subparagraph (A), by striking develop methods and technologies to improve environmental impact and inserting develop and support studies, methods, and technologies to assess and improve environmental impact ; and\n**(ii)**\nin subparagraph (D), by inserting hydrology, after water quality ;\n**(E)**\nin paragraph (7)(G), by inserting for hydropower and pumped storage applications after components ;\n**(F)**\nin paragraph (9), by inserting , and project management and delivery strategies, after systems analysis ;\n**(G)**\nin paragraph (10)\u2014\n**(i)**\nin subparagraph (B), by striking and at the end;\n**(ii)**\nin subparagraph (C), by inserting and after the semicolon; and\n**(iii)**\nby adding at the end the following new subparagraph:\n(D) improving methods for incorporating hydropower and pumped storage in grid modeling systems. ;\n**(H)**\nin paragraph (13), by striking and at the end; and\n**(I)**\nby striking paragraph (14) and inserting the following:\n(14) identify mechanisms and systems to test, validate, and improve performance and reliability of hydropower and pumped storage technologies; and (15) support workforce development programs, training, student-led research, and education and outreach activities to foster growth of the next generation of hydropower professionals and researchers. ;\n**(3)**\nin section 635(a) ( 42 U.S.C. 17214(a) ; relating to marine energy research, development, and demonstration) is amended\u2014\n**(A)**\nin paragraph (2), in the matter preceding subparagraph (A), by striking infrastructure and facilities and inserting infrastructure, facilities, and equipment ;\n**(B)**\nin paragraph (4), by striking , which may include smart building systems and inserting and microgrids, which may include smart energy management systems ;\n**(C)**\nin paragraph (5), by striking maintaining a sustainable marine energy supply chain based in the United States and inserting establish and support manufacturing and an industrial marine energy supply chain based in the United States ;\n**(D)**\nin paragraph (9), by inserting , which may include production of hydrogen and other transportation fuels before the semicolon;\n**(E)**\nin paragraph (13), by inserting utilization of advanced manufacturing processes, including the after such as the ;\n**(F)**\nin paragraph (17), by striking ; and and inserting , including data centers, subsea or offshore power, and microgrids, sensors, and communications systems; ;\n**(G)**\nin paragraph (18)\u2014\n**(i)**\nin the matter preceding subparagraph (A), by striking to develop and inserting develop ; and\n**(ii)**\nby amending subparagraph (B) to read as follows:\n(B) for the generation and storage of power to promote the resilience of waterside communities, including high-energy tidal environments, and critical infrastructure (as such term is defined in section 1016(e) of Public Law 107\u201356 ( 42 U.S.C. 5195c(e) )), including in applications relating to\u2014 (i) desalination; (ii) disaster recovery and resilience; (iii) aquaculture; (iv) marine carbon dioxide removal; (v) community microgrids in isolated power systems; and (vi) resilience and microgrid demonstration sites integrating marine energy and working waterfront economies. ; and\n**(H)**\nby adding at the end the following new paragraph:\n(19) develop, validate, and demonstrate marine energy systems designed for extreme tidal temperatures and icing conditions. ;\n**(4)**\nin section 636 ( 42 U.S.C. 17215 ; relating to National Marine Energy Centers)\u2014\n**(A)**\nin subsection (b), by adding at the end the following new paragraph:\n(4) Whether the institution is a regional test site with the proven ability to demonstrate unique natural advantages, including high tidal ranges, strong currents, and cold-water operating conditions. ; and\n**(B)**\nin subsection (c)\u2014\n**(i)**\nin the matter preceding paragraph (1), by striking and National Laboratories, and inserting National Laboratories, and other relevant Federal agencies, ;\n**(ii)**\nin paragraph (2)(D), by striking and at the end;\n**(iii)**\nin paragraph (3), by striking the period and inserting ; and ; and\n**(iv)**\nby adding at the end the following new paragraph:\n(4) support workforce development, training, student-led research programs, and development and dissemination of curriculum, education, and outreach activities to foster growth of the next generation of marine energy professionals and researchers. ;\n**(5)**\nin section 637 ( 42 U.S.C. 17216 ; relating to organization and administration of programs)\u2014\n**(A)**\nin subsection (b)\u2014\n**(i)**\nin paragraph (1), by inserting other domestic and after Alaska Native Corporations, and ;\n**(ii)**\nin paragraph (3), by striking (including the United States Agency for International Development) and inserting , including the Department of State and the International Trade Administration of the Department of Commerce, ; and\n**(iii)**\nby adding at the end the following new paragraph:\n(4) Interagency coordination The Secretary shall seek to coordinate with the National Sea Grant College Program and the Department of Commerce to leverage existing ocean networks and coastal innovation initiatives. ;\n**(B)**\nin subsection (f), by amending paragraph (2) to read as follows:\n(2) workforce development and training activities in collaboration with regional workforce hubs, including institutions of higher education, Tribal Colleges and Universities (including Alaska-Native serving institutions), land grant and sea grant institutions, foundations, non-profit organizations, and maritime academies, to support education, recruitment, and the dissemination of standards and best practices for enabling water power production, including hydropower and marine energy collegiate competitions, graduate student research program and fellowships relating to marine energy, and other workforce programs. ;\n**(C)**\nin subsection (g)(1), by striking an annual and inserting a biennial ; and\n**(D)**\nby amending subsection (h) to read as follows:\n(g) Briefing to Congress Not later than one year after the date of the enactment of this subsection, and at least once every two years thereafter, the Secretary shall provide a briefing to the relevant authorizing and appropriations committees of Congress and make available to the public the findings of research conducted and activities carried out pursuant to this subtitle, including the most current strategic plan under subsection (g) and the progress made in implementing such plan. ; and\n**(6)**\nby amending section 639 ( 42 U.S.C. 17218 ; relating to authorization of appropriations) by striking $186,600,000 for each of fiscal years 2021 through 2025, including $137,428,378 for marine energy and $49,171,622 for hydropower research, development, and demonstration activities and inserting $300,000,000 for each of fiscal years 2026 through 2030, including $200,000,000 for marine energy and $100,000,000 for hydropower research, development, and demonstration activities .",
      "versionDate": "2026-01-16",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Energy",
        "updateDate": "2026-02-06T16:41:59Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7129ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Water Power Research and Development Reauthorization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-04T05:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Water Power Research and Development Reauthorization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-04T05:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Energy Independence and Security Act of 2007 to reauthorize water power research, development, demonstration, and commercial application activities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-04T05:04:18Z"
    }
  ]
}
```
