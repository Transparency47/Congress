# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3776?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3776
- Title: Don’t Settle for Bribes Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3776
- Origin chamber: House
- Introduced date: 2025-06-05
- Update date: 2025-07-22T12:09:59Z
- Update date including text: 2025-07-22T12:09:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-05: Introduced in House
- 2025-06-05 - IntroReferral: Introduced in House
- 2025-06-05 - IntroReferral: Introduced in House
- 2025-06-05 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-06-05: Introduced in House

## Actions

- 2025-06-05 - IntroReferral: Introduced in House
- 2025-06-05 - IntroReferral: Introduced in House
- 2025-06-05 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-05",
    "latestAction": {
      "actionDate": "2025-06-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3776",
    "number": "3776",
    "originChamber": "House",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "M001223",
        "district": "2",
        "firstName": "Seth",
        "fullName": "Rep. Magaziner, Seth [D-RI-2]",
        "lastName": "Magaziner",
        "party": "D",
        "state": "RI"
      }
    ],
    "title": "Don\u2019t Settle for Bribes Act of 2025",
    "type": "HR",
    "updateDate": "2025-07-22T12:09:59Z",
    "updateDateIncludingText": "2025-07-22T12:09:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-05",
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
      "actionDate": "2025-06-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-05",
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
          "date": "2025-06-05T14:02:40Z",
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
      "bioguideId": "I000058",
      "district": "4",
      "firstName": "Glenn",
      "fullName": "Rep. Ivey, Glenn [D-MD-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Ivey",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "MD"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "CT"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "DC"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3776ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3776\nIN THE HOUSE OF REPRESENTATIVES\nJune 5, 2025 Mr. Magaziner (for himself, Mr. Ivey , Mrs. Hayes , Ms. Norton , and Mr. Thanedar ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo restrict the President from initiating civil lawsuits regarding any civil matters.\n#### 1. Short title\nThis Act may be cited as the Don\u2019t Settle for Bribes Act of 2025 .\n#### 2. Restriction\nIn the case of the filing, initiation, or continuation of a civil action by a person who is a candidate for the office of President (within 90 days of the general Presidential election), the President-elect, or the President, the court shall immediately stay any further proceedings until the end of that person\u2019s term as President, or, in the case of a candidate for the office of President who is not elected to the office, the date on which the House of Representatives ratifies the results of the election.\n#### 3. Special Rules\nThe restriction shall apply\u2014\n**(1)**\nto each member of the immediate family of the President; and\n**(2)**\nto any business or entity if the President or a member of the immediate family of the President is listed as a grantor or beneficiary.\n#### 4. Tolling of statute of limitations\nAny statute of limitations pertaining to a civil action stayed pursuant to section 2 shall be tolled and will resume upon the end of that person\u2019s term as President or in the case of candidates for President who is not elected to the office, upon certification of the presidential election.\n#### 5. Rule of construction\nNothing in this Act may be construed\u2014\n**(1)**\nto prohibit the President\u2019s right to access the court; or\n**(2)**\nto preclude an executive branch agency from bringing or defending civil actions involving the United States government.\n#### 6. Definition\nIn this Act, the term immediate family means the spouse and any child of a person.",
      "versionDate": "2025-06-05",
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
        "name": "Law",
        "updateDate": "2025-07-22T12:09:59Z"
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
      "date": "2025-06-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3776ih.xml"
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
      "title": "Don\u2019t Settle for Bribes Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-12T06:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Don\u2019t Settle for Bribes Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-12T06:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To restrict the President from initiating civil lawsuits regarding any civil matters.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-12T06:18:32Z"
    }
  ]
}
```
