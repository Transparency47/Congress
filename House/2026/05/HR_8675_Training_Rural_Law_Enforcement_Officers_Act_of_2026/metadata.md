# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8675?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8675
- Title: Training Rural Law Enforcement Officers Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8675
- Origin chamber: House
- Introduced date: 2026-05-07
- Update date: 2026-05-21T14:15:58Z
- Update date including text: 2026-05-21T14:15:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-05-07: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-05-07: Introduced in House

## Actions

- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-07",
    "latestAction": {
      "actionDate": "2026-05-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8675",
    "number": "8675",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "B000740",
        "district": "5",
        "firstName": "Stephanie",
        "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
        "lastName": "Bice",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "Training Rural Law Enforcement Officers Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-21T14:15:58Z",
    "updateDateIncludingText": "2026-05-21T14:15:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-07",
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
      "actionDate": "2026-05-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-07",
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
          "date": "2026-05-07T13:00:25Z",
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
      "bioguideId": "K000009",
      "district": "9",
      "firstName": "Marcy",
      "fullName": "Rep. Kaptur, Marcy [D-OH-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaptur",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
      "state": "OH"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2026-05-11",
      "state": "NJ"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2026-05-19",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8675ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8675\nIN THE HOUSE OF REPRESENTATIVES\nMay 7, 2026 Mrs. Bice (for herself and Ms. Kaptur ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo authorize the Department of Justice to provide grant funding to accredited nonprofit organizations to provide better access to needed training for law enforcement officers in rural and smaller communities.\n#### 1. Short title\nThis Act may be cited as the Training Rural Law Enforcement Officers Act of 2026 .\n#### 2. Training rural lawforcement\n##### (a) Findings\nCongress finds the following:\n**(1)**\nThere are more than 18,000 local police departments and 3,000 sheriff\u2019s offices in the United States. Of the local police departments in the United States\u2014\n**(A)**\nnearly half have fewer than 10 sworn officers;\n**(B)**\n3 out of 4 have fewer than 2 dozen sworn officers; and\n**(C)**\n8 out of 10 have fewer than 50 sworn officers.\n**(2)**\nFederal funding available through grants administered by the Department of Justice for law enforcement is frequently complex in terms of the application process and requires specific reporting mandates.\n**(3)**\nSmaller and rural law enforcement agencies often forego pursuing Federal funding opportunities as that pursuit creates a demand on already limited staffing, and those smaller and rural law enforcement agencies simply lack the experience and resources to navigate through the application process and to successfully adhere to the multitude of reporting requirements.\n##### (b) Definitions\nIn this section:\n**(1) Accredited nonprofit organization**\nThe term accredited nonprofit organization means a nonprofit organization that, as determined by the Attorney General, has\u2014\n**(A)**\nthe proper experience and expertise in relevant law enforcement training; and\n**(B)**\na strong track record of successfully conducting relevant law enforcement training in a particular training discipline.\n**(2) Law enforcement training grant**\nThe term law enforcement training grant means a grant awarded by the Attorney General under the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10101 et seq. ) for the purpose of law enforcement training.\n##### (c) Authorization\nAn accredited nonprofit organization shall be eligible to receive any law enforcement training grant for the purpose of providing training to State and local law enforcement agencies if the training is\u2014\n**(1)**\nconsistent with the priorities and objectives of the Department of Justice;\n**(2)**\nprovided to a law enforcement agency with fewer than 50 sworn law enforcement officers; and\n**(3)**\nconducted at no cost to the law enforcement agency receiving the training.",
      "versionDate": "2026-05-07",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-05-21T14:15:57Z"
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
      "date": "2026-05-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8675ih.xml"
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
      "title": "Training Rural Law Enforcement Officers Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-08T08:23:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Training Rural Law Enforcement Officers Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-08T08:23:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the Department of Justice to provide grant funding to accredited nonprofit organizations to provide better access to needed training for law enforcement officers in rural and smaller communities.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-08T08:18:51Z"
    }
  ]
}
```
