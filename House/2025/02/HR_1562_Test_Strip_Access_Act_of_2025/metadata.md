# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1562?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1562
- Title: Test Strip Access Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1562
- Origin chamber: House
- Introduced date: 2025-02-25
- Update date: 2025-05-05T12:48:22Z
- Update date including text: 2025-05-05T12:48:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-25: Introduced in House
- 2025-02-25 - IntroReferral: Introduced in House
- 2025-02-25 - IntroReferral: Introduced in House
- 2025-02-25 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-02-25: Introduced in House

## Actions

- 2025-02-25 - IntroReferral: Introduced in House
- 2025-02-25 - IntroReferral: Introduced in House
- 2025-02-25 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-25",
    "latestAction": {
      "actionDate": "2025-02-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1562",
    "number": "1562",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001130",
        "district": "30",
        "firstName": "Jasmine",
        "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
        "lastName": "Crockett",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "Test Strip Access Act of 2025",
    "type": "HR",
    "updateDate": "2025-05-05T12:48:22Z",
    "updateDateIncludingText": "2025-05-05T12:48:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-25",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-25",
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
          "date": "2025-02-25T15:03:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "G000589",
      "district": "5",
      "firstName": "Lance",
      "fullName": "Rep. Gooden, Lance [R-TX-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gooden",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1562ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1562\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 25, 2025 Ms. Crockett (for herself and Mr. Gooden ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the 21st Century Cures Act to expressly authorize the use of certain grants to implement substance use disorder and overdose prevention activities with respect to fentanyl and xylazine test strips.\n#### 1. Short title\nThis Act may be cited as the Test Strip Access Act of 2025 .\n#### 2. Grant program for State and Tribal response to opioid use disorders\nSection 1003(b)(4)(A) of the 21st Century Cures Act (42 U.S.C. 290ee\u20133a(b)(4)(A)) is amended by inserting or fentanyl or xylazine test strips after which may include drugs or devices approved, cleared, or otherwise legally marketed under the Federal Food, Drug, and Cosmetic Act .",
      "versionDate": "2025-02-25",
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
        "name": "Health",
        "updateDate": "2025-05-05T12:48:22Z"
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
      "date": "2025-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1562ih.xml"
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
      "title": "Test Strip Access Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-19T04:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Test Strip Access Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-19T04:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the 21st Century Cures Act to expressly authorize the use of certain grants to implement substance use disorder and overdose prevention activities with respect to fentanyl and xylazine test strips.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-19T04:33:22Z"
    }
  ]
}
```
