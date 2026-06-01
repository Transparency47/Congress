# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8649?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8649
- Title: Expanding the Defense Industrial Base Sales Act
- Congress: 119
- Bill type: HR
- Bill number: 8649
- Origin chamber: House
- Introduced date: 2026-05-04
- Update date: 2026-05-14T08:08:37Z
- Update date including text: 2026-05-14T08:08:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-05-04: Introduced in House
- 2026-05-04 - IntroReferral: Introduced in House
- 2026-05-04 - IntroReferral: Introduced in House
- 2026-05-04 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-05-13 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-13 - Committee: Ordered to be Reported Unfavorably by the Yeas and Nays: 23 - 23.
- Latest action: 2026-05-04: Introduced in House

## Actions

- 2026-05-04 - IntroReferral: Introduced in House
- 2026-05-04 - IntroReferral: Introduced in House
- 2026-05-04 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-05-13 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-13 - Committee: Ordered to be Reported Unfavorably by the Yeas and Nays: 23 - 23.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-04",
    "latestAction": {
      "actionDate": "2026-05-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8649",
    "number": "8649",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "B001322",
        "district": "5",
        "firstName": "Michael",
        "fullName": "Rep. Baumgartner, Michael [R-WA-5]",
        "lastName": "Baumgartner",
        "party": "R",
        "state": "WA"
      }
    ],
    "title": "Expanding the Defense Industrial Base Sales Act",
    "type": "HR",
    "updateDate": "2026-05-14T08:08:37Z",
    "updateDateIncludingText": "2026-05-14T08:08:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-13",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported Unfavorably by the Yeas and Nays: 23 - 23.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-05-13",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
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
      "actionDate": "2026-05-04",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-04",
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
            "date": "2026-05-13T15:27:00Z",
            "name": "Markup By"
          },
          {
            "date": "2026-05-04T14:30:50Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8649ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8649\nIN THE HOUSE OF REPRESENTATIVES\nMay 4, 2026 Mr. Baumgartner introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo amend the Arms Export Control Act to authorize the use of foreign military financing for direct commercial contracts, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Expanding the Defense Industrial Base Sales Act .\n#### 2. Authorization of foreign military financing for direct commercial contracts\nThe Arms Export Control Act ( 22 U.S.C. 2751 et seq. ) is amended by inserting after section 23 the following new section:\n23A. Use of foreign military financing for direct commercial contracts (a) Authority Notwithstanding section 23(h), funds made available to carry out the foreign military financing program under this Act may be used to finance the procurement by any foreign country or international organization eligible to receive such financing under this Act of defense articles, defense services, and design and construction services that are not sold by the United States Government. (b) Approval and oversight The use of foreign military financing authorized in subsection (a) shall\u2014 (1) be approved by the Secretary of State, in consultation with the Secretary of Defense, prior to the extension of such authority to any foreign country or international organization; and (2) be subject to such terms, conditions, and limitations as the Secretary of State determines appropriate to advance the foreign policy and national security interests of the United States. (c) Implementing regulations Not later than 180 days after the date of the enactment of this section, the Secretary of State, in coordination with the Secretary of Defense, shall prescribe regulations to implement this section, including regulations relating to, with respect to foreign military financing for direct commercial contracts authorized in subsection (a)\u2014 (1) procedures for review and approval; (2) audit, reporting, and financial accountability standards; (3) compliance with end-use monitoring and export control requirements; and (4) efforts to encourage participation by nontraditional defense companies. (d) Rule of construction The authority provided by this section is in addition to, and shall not be construed to limit or replace, the foreign military sales program otherwise authorized by this Act. .",
      "versionDate": "2026-05-04",
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
        "name": "International Affairs",
        "updateDate": "2026-05-08T20:32:32Z"
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
      "date": "2026-05-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8649ih.xml"
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
      "title": "Expanding the Defense Industrial Base Sales Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-06T04:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Expanding the Defense Industrial Base Sales Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-06T04:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Arms Export Control Act to authorize the use of foreign military financing for direct commercial contracts, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-06T04:18:31Z"
    }
  ]
}
```
