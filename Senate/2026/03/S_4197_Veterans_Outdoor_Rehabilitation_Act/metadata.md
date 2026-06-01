# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4197?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4197
- Title: Veterans Outdoor Rehabilitation Act
- Congress: 119
- Bill type: S
- Bill number: 4197
- Origin chamber: Senate
- Introduced date: 2026-03-25
- Update date: 2026-04-30T11:03:20Z
- Update date including text: 2026-04-30T11:03:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-25: Introduced in Senate
- 2026-03-25 - IntroReferral: Introduced in Senate
- 2026-03-25 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2026-04-29 - Committee: Committee on Veterans' Affairs. Hearings held.
- Latest action: 2026-03-25: Introduced in Senate

## Actions

- 2026-03-25 - IntroReferral: Introduced in Senate
- 2026-03-25 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2026-04-29 - Committee: Committee on Veterans' Affairs. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-25",
    "latestAction": {
      "actionDate": "2026-03-25",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4197",
    "number": "4197",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "C001096",
        "district": "",
        "firstName": "Kevin",
        "fullName": "Sen. Cramer, Kevin [R-ND]",
        "lastName": "Cramer",
        "party": "R",
        "state": "ND"
      }
    ],
    "title": "Veterans Outdoor Rehabilitation Act",
    "type": "S",
    "updateDate": "2026-04-30T11:03:20Z",
    "updateDateIncludingText": "2026-04-30T11:03:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-29",
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
      "actionDate": "2026-03-25",
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
      "actionDate": "2026-03-25",
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
            "date": "2026-04-29T21:37:44Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2026-03-25T19:50:33Z",
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
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "NH"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2026-03-25",
      "state": "AR"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4197is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4197\nIN THE SENATE OF THE UNITED STATES\nMarch 25, 2026 Mr. Cramer (for himself, Ms. Hassan , Mr. Boozman , and Ms. Slotkin ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo require the Secretary of Veterans Affairs to establish a program under which the Secretary shall award grants to certain State entities to expand access to structured outdoor recreation programs for veterans that enhance veteran wellness, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Veterans Outdoor Rehabilitation Act .\n#### 2. Grant program to support outdoor recreation opportunities for veterans\n##### (a) In general\nThe Secretary of Veterans Affairs shall establish a program under which the Secretary shall award grants to covered State entities to expand access to structured outdoor recreation programs for veterans that enhance veteran wellness.\n##### (b) Use of amounts\nA covered State entity awarded a grant under this section may use amounts under such grant as follows:\n**(1)**\nTo directly develop and administer an outdoor recreation program for veterans.\n**(2)**\nTo contract with local outfitters, guides, nonprofit organizations, or community-based outdoor recreation providers to conduct such program.\n**(3)**\nTo develop partnerships to deliver structured outdoor programming for veterans.\n**(4)**\nTo reduce financial barriers to participation in such program, including equipment, program fees, and reasonable transportation costs.\n**(5)**\nTo conduct outreach to veteran populations to raise awareness about such program.\n**(6)**\nTo expand an existing outdoor recreation program for veterans operated in the State.\n**(7)**\nTo coordinate with Federal agencies involved in land management with respect to such program, including the following:\n**(A)**\nThe National Park Service.\n**(B)**\nThe Bureau of Land Management.\n**(C)**\nThe Forest Service.\n**(D)**\nThe United States Fish and Wildlife Service.\n**(E)**\nThe Army Corps of Engineers.\n##### (c) Collaboration and coordination\n**(1) Collaboration**\nThe Secretary shall encourage collaboration between covered State entities participating in the grant program under this section and the Federal agencies described in subsection (b)(7) to\u2014\n**(A)**\nexpand access by veterans to outdoor spaces;\n**(B)**\nto reduce administrative barriers; and\n**(C)**\nto identify appropriate locations for organized activities.\n**(2) Coordination**\nThe Secretary shall encourage covered State entities participating in the grant program under this section to coordinate with other covered State entities to maximize access by veterans to outdoor recreation opportunities.\n##### (d) Application requirements\nTo receive a grant under this section, a covered State entity shall submit to the Secretary an application therefor that includes the following:\n**(1)**\nA plan for administering funds awarded under such grant.\n**(2)**\nCriteria for selecting partners for the outdoor recreation program or programs carried out by such entity.\n**(3)**\nA certification that the outdoor recreation program or programs carried out by such entity meet qualification standards determined by the State.\n**(4)**\nMethods for collecting data for participation in the outdoor recreation program or programs carried out by such entity.\n##### (e) Approval of application and funding amounts\n**(1) In general**\nSubject to the availability of appropriations, each covered State entity that submits an application meeting the requirements under subsection (d) for a grant under this section shall be approved to receive such grant in an amount of not less than $200,000 for the applicable fiscal year.\n**(2) Additional amounts**\nIf additional amounts are available for a fiscal year to carry out this section, those additional amounts shall be distributed among the covered State entities for which an application under subsection (d) was approved under paragraph (1).\n##### (f) Reports\nNot less frequently than annually, each covered State entity in receipt of a grant under this section shall submit to the Secretary a report that includes the following:\n**(1)**\nParticipation metrics regarding any outdoor recreation program carried out by such entity with amounts provided under such grant, including\u2014\n**(A)**\nthe types of activities funded and partnerships established under such program;\n**(B)**\nthe number of veterans served under such program;\n**(C)**\nfrequency of participation by veterans under such program; and\n**(D)**\ndemographic distribution of veterans participating in such program.\n**(2)**\nObservations with respect to any outdoor recreation program carried out by such entity, including\u2014\n**(A)**\nself-reported changes in well-being of veterans;\n**(B)**\nsocial connectedness indicators; and\n**(C)**\nphysical activity engagement.\n##### (g) Definitions\nIn this section:\n**(1) Outdoor recreation program**\nThe term outdoor recreation program means a nature-based activity designed to improve the mental and physical well-being of veterans, including activities that promote physical engagement, peer connection, skill-building, or therapeutic benefit, and may include adaptive or accessible activities designed to accommodate veterans with disabilities.\n**(2) Covered State entity**\nThe term covered State entity means the primary agency of a State that is responsible for programs and services for veterans.\n##### (h) Authorization of appropriations\nThere is authorized to be appropriated to the Secretary of Veterans Affairs $10,000,000 for each fiscal year to carry out this section.",
      "versionDate": "2026-03-25",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2026-04-14T01:28:48Z"
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
      "date": "2026-03-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4197is.xml"
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
      "title": "Veterans Outdoor Rehabilitation Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-30T11:03:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Veterans Outdoor Rehabilitation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-09T02:08:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of Veterans Affairs to establish a program under which the Secretary shall award grants to certain State entities to expand access to structured outdoor recreation programs for veterans that enhance veteran wellness, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-09T02:03:23Z"
    }
  ]
}
```
