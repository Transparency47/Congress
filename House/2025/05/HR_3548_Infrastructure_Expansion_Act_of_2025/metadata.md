# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3548?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3548
- Title: Infrastructure Expansion Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3548
- Origin chamber: House
- Introduced date: 2025-05-21
- Update date: 2025-09-22T15:31:37Z
- Update date including text: 2025-09-22T15:31:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-21: Introduced in House
- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-05-21: Introduced in House

## Actions

- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-21",
    "latestAction": {
      "actionDate": "2025-05-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3548",
    "number": "3548",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "L000600",
        "district": "23",
        "firstName": "Nicholas",
        "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
        "lastName": "Langworthy",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Infrastructure Expansion Act of 2025",
    "type": "HR",
    "updateDate": "2025-09-22T15:31:37Z",
    "updateDateIncludingText": "2025-09-22T15:31:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-21",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-21",
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
        "item": {
          "date": "2025-05-21T14:00:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-05-21",
      "state": "NY"
    },
    {
      "bioguideId": "S001196",
      "district": "21",
      "firstName": "Elise",
      "fullName": "Rep. Stefanik, Elise M. [R-NY-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Stefanik",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-05-21",
      "state": "NY"
    },
    {
      "bioguideId": "M001177",
      "district": "5",
      "firstName": "Tom",
      "fullName": "Rep. McClintock, Tom [R-CA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "McClintock",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "CA"
    },
    {
      "bioguideId": "E000235",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Ezell, Mike [R-MS-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Ezell",
      "party": "R",
      "sponsorshipDate": "2025-09-19",
      "state": "MS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3548ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3548\nIN THE HOUSE OF REPRESENTATIVES\nMay 21, 2025 Mr. Langworthy (for himself, Ms. Tenney , and Ms. Stefanik ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo preclude absolute liability in any action against a property owner or contractor for projects receiving Federal financial assistance for infrastructure and transportation development, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Infrastructure Expansion Act of 2025 .\n#### 2. Preservation of Federal financial assistance for infrastructure and transportation development\n##### (a) No absolute liability on certain projects\nFor any project that receives Federal financial assistance, benefits from Federal tax incentives, or is subject to Federal permitting requirements, no action on the basis of absolute liability may be instituted by a covered person against a property owner or a party to a contract or subcontract relating to the property that is the subject of the project for any injury associated with an elevation or gravity-related risk occurring on that project.\n##### (b) Comparative negligence liability standard for certain claims\nFor any project described in subsection (a)\u2014\n**(1)**\na State may not impose absolute liability in any form for elevation or gravity-related risks; and\n**(2)**\na comparative negligence liability standard shall apply to any claim brought by a covered person against a property owner or contractor for an injury associated with an elevation or gravity-related risk in which\u2014\n**(A)**\nsuch negligence is a proximate cause of an injury to a person; and\n**(B)**\nState law would otherwise apply absolute liability as the basis for such a claim.\n##### (c) Federal preemption\nThis Act shall supersede and preempt any State law that imposes absolute liability standards for elevation or gravity-related risks on projects receiving Federal financial assistance. States shall adopt comparative negligence standards pursuant to this Act for claims arising under a project described in subsection (a).\n##### (d) Federal court jurisdiction\nAll claims arising under this Act shall be subject to exclusive jurisdiction of the Federal courts of the United States, precluding State courts from applying absolute liability standards to covered projects.\n##### (e) Definitions\nIn this section:\n**(1) Absolute liability**\nThe term absolute liability means liability for a personal injury or death that is imposed without consideration of the responsibility of the injured person, including failure to follow safety instructions or safe work practices in accordance with training provided, failure to utilize provided safety equipment or devices, impairment by the use of drugs or alcohol, or involvement in a criminal act, when such failure, impairment, or act is a proximate cause of an injury to such person.\n**(2) Covered person**\nThe term covered person means any person who supervises or performs any work on or who is otherwise affiliated with a project.\n**(3) Elevation or gravity-related risk**\nThe term elevation or gravity-related risk means a hazard related to the effects of gravity either due to the difference between the elevation level of the required work and a lower level or a difference between the elevation level where the worker is positioned and the higher level of the materials or load being hoisted or secured.\n**(4) Federal financial assistance**\nThe term Federal financial assistance means any direct or indirect funding, including grants, loans, loan guarantees, tax credits, Build America Bonds, bonds, or other incentives provided by the Federal Government to support infrastructure or transportation development.\n**(5) Project**\nThe term project means\u2014\n**(A)**\nthe construction, erection, demolition, repairing, altering, painting, cleaning, or pointing of a highway, bridge, tunnel, airport, railway, bus or railroad station, depot, pier, harbor, park, building, support facility, or utilities; and\n**(B)**\nany infrastructure associated with an activity described in subparagraph (A), including private developments required to modify public assets as a condition of construction or permitting.\n**(6) State**\nThe term State includes an authority, agency, metropolitan planning organization, district, commission, corporation, or other political subdivision of, or affiliation with, a State or local government, or bi-State entity or compact.\n##### (f) Workers\u2019 compensation laws\nNothing in this section shall be construed to preempt any law of a State providing for workers\u2019 compensation.\n##### (g) Effective date\nThis section applies to claims arising from projects in which a State or local government accepts Federal financial assistance on or after January 1, 2026.",
      "versionDate": "2025-05-21",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-05-30T12:49:38Z"
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
      "date": "2025-05-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3548ih.xml"
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
      "title": "Infrastructure Expansion Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-29T13:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Infrastructure Expansion Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-29T13:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To preclude absolute liability in any action against a property owner or contractor for projects receiving Federal financial assistance for infrastructure and transportation development, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-29T13:18:19Z"
    }
  ]
}
```
