# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4859?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4859
- Title: DEAL Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4859
- Origin chamber: House
- Introduced date: 2025-08-01
- Update date: 2025-09-11T18:49:47Z
- Update date including text: 2025-09-11T18:49:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-08-01: Introduced in House
- 2025-08-01 - IntroReferral: Introduced in House
- 2025-08-01 - IntroReferral: Introduced in House
- 2025-08-01 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-08-01: Introduced in House

## Actions

- 2025-08-01 - IntroReferral: Introduced in House
- 2025-08-01 - IntroReferral: Introduced in House
- 2025-08-01 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-01",
    "latestAction": {
      "actionDate": "2025-08-01",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4859",
    "number": "4859",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "M001241",
        "district": "47",
        "firstName": "Dave",
        "fullName": "Rep. Min, Dave [D-CA-47]",
        "lastName": "Min",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "DEAL Act of 2025",
    "type": "HR",
    "updateDate": "2025-09-11T18:49:47Z",
    "updateDateIncludingText": "2025-09-11T18:49:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-01",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-08-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-01",
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
          "date": "2025-08-01T14:03:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "MD"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "GA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4859ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4859\nIN THE HOUSE OF REPRESENTATIVES\nAugust 1, 2025 Mr. Min (for himself, Mrs. McClain Delaney , Mr. Johnson of Georgia , and Mr. Thanedar ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo direct the Comptroller General to report on settlements with covered law firms.\n#### 1. Short title\nThis Act may be cited as the Disclosure of Engagements with Attorney Law Firms Act of 2025 or the DEAL Act of 2025 .\n#### 2. Report on settlements with covered law firms\n##### (a) Report\nNot later than 180 days after the date of the enactment of this Act, the Comptroller General shall report on any settlement made with a covered law firms to determine if there has been a violation of section 3302(b) of title 31, United States Code (commonly known as the Miscellaneous Receipts Act ).\n##### (b) Settlement made with a covered law firm defined\nIn this section, the term settlement made with a covered law firm means any written or oral agreement, arrangement, memorandum of understanding, or other commitment between any law firm and any officer, employee, or agent of the Executive Branch, including the President, that\u2014\n**(1)**\nprovides the delivery of legal services, including pro bono representation, by the law firm or its agents;\n**(2)**\nimplies that legal services provided by the law firm are directed toward causes, initiatives, or beneficiaries identified, approved, or jointly selected by the Executive Branch;\n**(3)**\nwas entered into in connection with, or contemporaneously with, the withdrawal, rescission, or non-enforcement of any executive order, administration action, or regulatory threat directed at the law firm;\n**(4)**\nhas an estimated value of legal services exceeding $1,000,000 over the term of the agreement; and\n**(5)**\nwas entered into between the date of February 1, 2025, and April 30, 2025.",
      "versionDate": "2025-08-01",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-09-11T18:49:47Z"
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
      "date": "2025-08-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4859ih.xml"
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
      "title": "DEAL Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-06T05:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "DEAL Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-06T05:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Disclosure of Engagements with Attorney Law Firms Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-06T05:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Comptroller General to report on settlements with covered law firms.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-06T05:34:04Z"
    }
  ]
}
```
