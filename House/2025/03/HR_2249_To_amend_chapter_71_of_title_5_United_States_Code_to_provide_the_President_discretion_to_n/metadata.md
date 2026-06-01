# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2249?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2249
- Title: Preserving Presidential Management Authority Act
- Congress: 119
- Bill type: HR
- Bill number: 2249
- Origin chamber: House
- Introduced date: 2025-03-21
- Update date: 2025-10-30T21:35:16Z
- Update date including text: 2025-10-30T21:35:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-21: Introduced in House
- 2025-03-21 - IntroReferral: Introduced in House
- 2025-03-21 - IntroReferral: Introduced in House
- 2025-03-21 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-03-25 - Committee: Committee Consideration and Mark-up Session Held
- 2025-03-25 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 23 - 21.
- Latest action: 2025-03-21: Introduced in House

## Actions

- 2025-03-21 - IntroReferral: Introduced in House
- 2025-03-21 - IntroReferral: Introduced in House
- 2025-03-21 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-03-25 - Committee: Committee Consideration and Mark-up Session Held
- 2025-03-25 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 23 - 21.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-21",
    "latestAction": {
      "actionDate": "2025-03-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2249",
    "number": "2249",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "C001115",
        "district": "27",
        "firstName": "Michael",
        "fullName": "Rep. Cloud, Michael [R-TX-27]",
        "lastName": "Cloud",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Preserving Presidential Management Authority Act",
    "type": "HR",
    "updateDate": "2025-10-30T21:35:16Z",
    "updateDateIncludingText": "2025-10-30T21:35:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-25",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 23 - 21.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-25",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
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
      "actionDate": "2025-03-21",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-21",
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
            "date": "2025-03-25T15:17:28Z",
            "name": "Markup By"
          },
          {
            "date": "2025-03-21T20:00:25Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2025-06-30",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2249ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2249\nIN THE HOUSE OF REPRESENTATIVES\nMarch 21, 2025 Mr. Cloud introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo amend chapter 71 of title 5, United States Code, to provide the President discretion to negotiate collective bargaining agreements entered into under such chapter, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Preserving Presidential Management Authority Act .\n#### 2. Discretion to Negotiate Collective Bargaining Agreements By President and Clarifying Effect of Conflicting Presidential Actions\n##### (a) In general\nSubchapter I of chapter 71 of title 5, United States Code, is amended by adding at the end the following:\n7107. Presidential authority to negotiate collective bargaining agreements; clarification of effect of conflicting presidential actions (a) Authority of President To negotiate agreements The President may, acting through the head of an agency, terminate any provision of a collective bargaining agreement entered into under this chapter that is in force and effect on the date such President swears or affirms the oath of office as President. (b) Clarifying effect of conflicting presidential actions A provision of any collective bargaining agreement that conflicts with a rule, executive order, presidential memorandum, or any other presidential order, as determined by the President or the head of an agency, shall not be enforceable. (c) Limitation The authority under subsection (a) may not be exercised by an incumbent President. (d) Notification On the date the President orders any termination under subsection (a) or a determination is made under subsection (b), the head of the relevant agency shall submit a notice (in writing) to the applicable exclusive representative describing such termination or conflicting provisions of such an agreement. .\n##### (b) Clerical amendment\nThe table of sections for such subchapter is amended by adding after the item relating to section 7106 the following:\n7107. Presidential authority to negotiate collective bargaining agreements; clarification of effect of conflicting presidential actions. .",
      "versionDate": "2025-03-21",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Labor-management relations",
            "updateDate": "2025-06-02T20:34:04Z"
          },
          {
            "name": "Presidents and presidential powers, Vice Presidents",
            "updateDate": "2025-06-02T20:34:00Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-19T15:43:20Z"
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
      "date": "2025-03-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2249ih.xml"
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
      "title": "Preserving Presidential Management Authority Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-22T08:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Preserving Presidential Management Authority Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-22T08:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend chapter 71 of title 5, United States Code, to provide the President discretion to negotiate collective bargaining agreements entered into under such chapter, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-22T08:18:38Z"
    }
  ]
}
```
