# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4891?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4891
- Title: Secure Our Embassies Act
- Congress: 119
- Bill type: HR
- Bill number: 4891
- Origin chamber: House
- Introduced date: 2025-08-05
- Update date: 2025-10-09T08:06:01Z
- Update date including text: 2025-10-09T08:06:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-08-05: Introduced in House
- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2025-08-05: Introduced in House

## Actions

- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-05",
    "latestAction": {
      "actionDate": "2025-08-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4891",
    "number": "4891",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "L000599",
        "district": "17",
        "firstName": "Michael",
        "fullName": "Rep. Lawler, Michael [R-NY-17]",
        "lastName": "Lawler",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Secure Our Embassies Act",
    "type": "HR",
    "updateDate": "2025-10-09T08:06:01Z",
    "updateDateIncludingText": "2025-10-09T08:06:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-05",
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
      "actionDate": "2025-08-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-05",
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
          "date": "2025-08-05T14:01:20Z",
          "name": "Referred To"
        }
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
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-08-26",
      "state": "NJ"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4891ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4891\nIN THE HOUSE OF REPRESENTATIVES\nAugust 5, 2025 Mr. Lawler introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo address the growing complexity of the threat environment at United States diplomatic posts.\n#### 1. Short title\nThis Act may be cited as the Secure Our Embassies Act .\n#### 2. Sense of Congress\nCongress\u2014\n**(1)**\nrecognizes the growing complexity of the threat environment at United States diplomatic posts and the critical need for seamless coordination among personnel responsible for information security, physical security, and facility operations;\n**(2)**\nsupports the Department of State\u2019s efforts to strengthen coordination among Regional Security Officers (RSOs), Diplomatic Technology Officers (DTOs), Regional Security Engineering Officers (RSEOs), and personnel from the Bureau of Overseas Buildings Operations (OBO), particularly during the design, construction, and operations of overseas facilities;\n**(3)**\nsupports that Department of State personnel serving in these positions receive appropriate and role-specific counterintelligence (CI) and regional specific security training, which should address regional and functional threat vectors, as well as protocols for identifying and mitigating insider threats, foreign intelligence collection risks, and cyber vulnerabilities; and\n**(4)**\nsupports the development of joint training modules or inter-bureau CI briefings to reinforce shared security responsibilities and to prevent siloed operational cultures.\n#### 3. Report\nNot later than 180 days after the date of the enactment of this Act, the Secretary of State shall submit to Congress a report on actions the Secretary has taken and will take to improve coordination across the positions described in section 2 and to implement CI training standards for such positions. The report should include a description of current CI training requirements, planned improvements, and any resource needs to support implementation.",
      "versionDate": "2025-08-05",
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
        "updateDate": "2025-09-11T21:25:59Z"
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
      "date": "2025-08-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4891ih.xml"
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
      "title": "Secure Our Embassies Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-09T03:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Secure Our Embassies Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To address the growing complexity of the threat environment at United States diplomatic posts.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-09T03:33:39Z"
    }
  ]
}
```
