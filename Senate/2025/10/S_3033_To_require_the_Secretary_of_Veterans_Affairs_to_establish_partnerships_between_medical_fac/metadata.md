# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3033?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3033
- Title: Improving Access to Care for Rural Veterans Act
- Congress: 119
- Bill type: S
- Bill number: 3033
- Origin chamber: Senate
- Introduced date: 2025-10-22
- Update date: 2026-03-19T11:03:28Z
- Update date including text: 2026-03-19T11:03:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-22: Introduced in Senate
- 2025-10-22 - IntroReferral: Introduced in Senate
- 2025-10-22 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-12-10 - Committee: Committee on Veterans' Affairs. Hearings held.
- 2026-03-18 - Committee: Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.
- Latest action: 2025-10-22: Introduced in Senate

## Actions

- 2025-10-22 - IntroReferral: Introduced in Senate
- 2025-10-22 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-12-10 - Committee: Committee on Veterans' Affairs. Hearings held.
- 2026-03-18 - Committee: Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-22",
    "latestAction": {
      "actionDate": "2025-10-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3033",
    "number": "3033",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "D000622",
        "district": "",
        "firstName": "Tammy",
        "fullName": "Sen. Duckworth, Tammy [D-IL]",
        "lastName": "Duckworth",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Improving Access to Care for Rural Veterans Act",
    "type": "S",
    "updateDate": "2026-03-19T11:03:28Z",
    "updateDateIncludingText": "2026-03-19T11:03:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-18",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-10",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-10-22",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-10-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
            "date": "2026-03-18T20:00:30Z",
            "name": "Markup By"
          },
          {
            "date": "2025-12-10T21:00:36Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-10-22T21:53:51Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-10-22",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3033is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3033\nIN THE SENATE OF THE UNITED STATES\nOctober 22 (legislative day, October 21), 2025 Ms. Duckworth (for herself and Mrs. Blackburn ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo require the Secretary of Veterans Affairs to establish partnerships between medical facilities of the Department of Veterans Affairs and medical facilities in rural areas, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Improving Access to Care for Rural Veterans Act .\n#### 2. Partnerships between medical facilities of Department of Veterans Affairs and rural medical facilities\n##### (a) Partnerships\n**(1) In general**\nThe Secretary of Veterans Affairs shall require that each medical facility of the Department of Veterans Affairs enter into a partnership with a medical facility in a rural area.\n**(2) Agreements**\nEach partnership entered into under paragraph (1) may include an agreement for provision of telehealth, co-location or leasing of space or equipment, training, care coordination, emergency services (including transportation), or other services as determined appropriate.\n**(3) Purpose of partnership**\nThe purpose of any partnership entered into under paragraph (1) shall be to provide greater access to care for veterans in rural areas and to reduce costs to all entities within the partnership.\n##### (b) Waiver\n**(1) In general**\nThe Secretary may waive the requirement under subsection (a)(1) with respect to a medical facility for a period not to exceed five years, subject to such requirements as the Secretary may establish, if the Secretary notifies Congress of the waiver not later than 48 hours before the waiver takes effect.\n**(2) Renewal**\nThe Secretary may renew a waiver under paragraph (1) with respect to a medical facility only if the Secretary, in consultation with the head of the medical facility, evaluates the need for the waiver and determines that the waiver is necessary.\n##### (c) Briefing\nNot later than 180 days after the date of the enactment of this Act, the Secretary shall provide to the appropriate committees of Congress a briefing on the plans of the Secretary for the implementation of the requirement under subsection (a)(1), including\u2014\n**(1)**\na timeline for implementation of such requirement;\n**(2)**\nan identification of an official of the Department responsible for oversight and implementation of such requirement;\n**(3)**\nan update on the establishment of any office, task force, or personnel assignments to support the implementation of such requirement;\n**(4)**\na description of the plan of the Department for oversight of such requirement;\n**(5)**\na standardized form or forms to be used for waivers under subsection (b) and an explanation of the criteria for eligibility for such a waiver; and\n**(6)**\nsuch other information as the Secretary considers to be of interest to the appropriate committees of Congress.\n##### (d) Report\nNot later than two years after the date of the enactment of this Act, and biennially thereafter, the Secretary shall submit to the appropriate committees of Congress a report on the operation and performance of partnerships entered into under subsection (a), including\u2014\n**(1)**\nnew partnerships created, in the case of the initial report, since the date of the enactment of this Act, and, in the case of any subsequent report, during the period following the previous report;\n**(2)**\nexisting partnerships between medical facilities of the Department and medical facilities in rural areas; and\n**(3)**\nas assessment of the success of all partnerships described in paragraphs (1) and (2) in delivering services to veterans in rural areas, including\u2014\n**(A)**\nthe number of veterans enrolled in the system of annual patient enrollment of the Department under section 1705(a) of title 38, United States Code, in the region in which the partnered medical facilities are located compared to the previous five-year period;\n**(B)**\nan evaluation of accessibility to services as compared to the services available to those veterans prior to the implementation of such partnerships;\n**(C)**\nan overview of new best practices developed for such partnerships and the Department more broadly; and\n**(D)**\nthe number of veterans receiving compensation from the Department for a service-connected disability in the region in which the partnered medical facilities are located compared to the previous five-year period.\n##### (e) Timeline\n**(1) Existing facilities**\nExcept as provided in paragraph (2), by not later than three years after the date of the enactment of this Act, the Secretary shall ensure that all medical facilities of the Department that are seeing patients are compliant with the requirement under subsection (a)(1) or have received a waiver under subsection (b).\n**(2) New facilities**\nThe Secretary shall ensure that any medical facility of the Department established after the date of the enactment of this Act is compliant with the requirement under subsection (a)(1) or has received a waiver under subsection (b) by not later than three years after the date on which patients are first seen at the medical facility.\n##### (f) Relationship to existing law\nThe requirements and authorities under this section are in addition to, and separate from, the authority under section 8153 of title 38, United States Code.\n##### (g) Definitions\nIn this section:\n**(1) Appropriate committees of Congress**\nThe term appropriate committees of Congress means\u2014\n**(A)**\nthe Committee on Veterans\u2019 Affairs and the Committee on Appropriations of the Senate; and\n**(B)**\nthe Committee on Veterans\u2019 Affairs and the Committee on Appropriations of the House of Representatives.\n**(2) Partnership**\nThe term partnership includes a leasing or co-location agreement, a memorandum of understanding, a partnership agreement, an employment contract, an independent contractor agreement, a service agreement, or any other similar agreement.\n**(3) Rural**\nThe term rural has the meaning given that term under the Rural-Urban Commuting Areas (RUCA) coding system of the Department of Agriculture.\n**(4) Service-connected**\nThe term service-connected has the meaning given that term in section 101(16) of title 38, United States Code.",
      "versionDate": "2025-10-22",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Congressional oversight",
            "updateDate": "2026-01-09T16:42:03Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2026-01-09T16:41:55Z"
          },
          {
            "name": "Health facilities and institutions",
            "updateDate": "2026-01-09T16:42:00Z"
          },
          {
            "name": "Performance measurement",
            "updateDate": "2026-01-09T16:42:07Z"
          },
          {
            "name": "Rural conditions and development",
            "updateDate": "2026-01-09T16:41:48Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2026-01-09T16:41:45Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-12-05T16:38:53Z"
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
      "date": "2025-10-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3033is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Improving Access to Care for Rural Veterans Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-19T11:03:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Improving Access to Care for Rural Veterans Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-24T02:23:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of Veterans Affairs to establish partnerships between medical facilities of the Department of Veterans Affairs and medical facilities in rural areas, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-24T02:18:19Z"
    }
  ]
}
```
