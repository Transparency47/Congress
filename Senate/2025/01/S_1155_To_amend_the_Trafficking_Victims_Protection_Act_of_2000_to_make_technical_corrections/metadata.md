# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1155?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1155
- Title: A bill to amend the Trafficking Victims Protection Act of 2000 to make technical corrections.
- Congress: 119
- Bill type: S
- Bill number: 1155
- Origin chamber: Senate
- Introduced date: 2025-03-26
- Update date: 2025-08-13T11:31:50Z
- Update date including text: 2025-08-13T11:31:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-26: Introduced in Senate
- 2025-03-26 - IntroReferral: Introduced in Senate
- 2025-03-26 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- 2025-08-02 - Floor: Passed Senate without amendment by Unanimous Consent. (text: CR S5521; consideration: CR S5521)
- 2025-08-02 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.
- 2025-08-02 - Discharge: Senate Committee on Foreign Relations discharged by Unanimous Consent.
- 2025-08-02 - Committee: Senate Committee on Foreign Relations discharged by Unanimous Consent.
- 2025-08-08 - Floor: Message on Senate action sent to the House.
- 2025-08-08 11:33:34 - Floor: Received in the House.
- 2025-08-08 11:44:57 - Floor: Held at the desk.
- Latest action: 2025-03-26: Introduced in Senate

## Actions

- 2025-03-26 - IntroReferral: Introduced in Senate
- 2025-03-26 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- 2025-08-02 - Floor: Passed Senate without amendment by Unanimous Consent. (text: CR S5521; consideration: CR S5521)
- 2025-08-02 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.
- 2025-08-02 - Discharge: Senate Committee on Foreign Relations discharged by Unanimous Consent.
- 2025-08-02 - Committee: Senate Committee on Foreign Relations discharged by Unanimous Consent.
- 2025-08-08 - Floor: Message on Senate action sent to the House.
- 2025-08-08 11:33:34 - Floor: Received in the House.
- 2025-08-08 11:44:57 - Floor: Held at the desk.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-26",
    "latestAction": {
      "actionDate": "2025-03-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1155",
    "number": "1155",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "H001079",
        "district": "",
        "firstName": "Cindy",
        "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
        "lastName": "Hyde-Smith",
        "party": "R",
        "state": "MS"
      }
    ],
    "title": "A bill to amend the Trafficking Victims Protection Act of 2000 to make technical corrections.",
    "type": "S",
    "updateDate": "2025-08-13T11:31:50Z",
    "updateDateIncludingText": "2025-08-13T11:31:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H15000",
      "actionDate": "2025-08-08",
      "actionTime": "11:44:57",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Held at the desk.",
      "type": "Floor"
    },
    {
      "actionCode": "H14000",
      "actionDate": "2025-08-08",
      "actionTime": "11:33:34",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Received in the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-08-08",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Message on Senate action sent to the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-08-02",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Passed Senate without amendment by Unanimous Consent. (text: CR S5521; consideration: CR S5521)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-08-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-08-02",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Senate Committee on Foreign Relations discharged by Unanimous Consent.",
      "type": "Discharge"
    },
    {
      "actionCode": "14500",
      "actionDate": "2025-08-02",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Senate Committee on Foreign Relations discharged by Unanimous Consent.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-26",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-26",
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
            "date": "2025-08-03T02:00:33Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-03-26T19:53:46Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-06-16",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1155is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1155\nIN THE SENATE OF THE UNITED STATES\nMarch 26, 2025 Mrs. Hyde-Smith introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo amend the Trafficking Victims Protection Act of 2000 to make technical corrections.\n#### 1. Technical corrections to the Trafficking Victims Protection Act of 2000\nSection 103 of the Trafficking Victims Protection Act of 2000 ( 22 U.S.C. 7102 ) is amended\u2014\n**(1)**\nin paragraph (16), by striking paragraph (9) and inserting paragraph (11) ; and\n**(2)**\nin paragraph (17), by striking paragraph (9) or (10) and inserting paragraph (11) or (12) .",
      "versionDate": "2025-03-26",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1155es.xml",
      "text": "119th CONGRESS\n1st Session\nS. 1155\nIN THE SENATE OF THE UNITED STATES\nAN ACT\nTo amend the Trafficking Victims Protection Act of 2000 to make technical corrections.\n#### 1. Technical corrections to the Trafficking Victims Protection Act of 2000\nSection 103 of the Trafficking Victims Protection Act of 2000 ( 22 U.S.C. 7102 ) is amended\u2014\n**(1)**\nin paragraph (16), by striking paragraph (9) and inserting paragraph (11) ; and\n**(2)**\nin paragraph (17), by striking paragraph (9) or (10) and inserting paragraph (11) or (12) .",
      "versionDate": "",
      "versionType": "Engrossed in Senate"
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
            "name": "Human trafficking",
            "updateDate": "2025-08-06T16:04:27Z"
          },
          {
            "name": "Legislative rules and procedure",
            "updateDate": "2025-08-06T16:15:34Z"
          },
          {
            "name": "Senate",
            "updateDate": "2025-08-06T16:15:48Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-05-14T17:27:40Z"
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
      "date": "2025-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1155is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1155es.xml"
        }
      ],
      "type": "Engrossed in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Trafficking Victims Protection Act of 2000 to make technical corrections.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-11T02:33:34Z"
    },
    {
      "title": "A bill to amend the Trafficking Victims Protection Act of 2000 to make technical corrections.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-27T10:56:23Z"
    }
  ]
}
```
