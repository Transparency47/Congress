# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1054?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1054
- Title: United States African Development Foundation Dissolution Act
- Congress: 119
- Bill type: S
- Bill number: 1054
- Origin chamber: Senate
- Introduced date: 2025-03-13
- Update date: 2026-02-04T12:03:15Z
- Update date including text: 2026-02-04T12:03:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-13: Introduced in Senate
- 2025-03-13 - IntroReferral: Introduced in Senate
- 2025-03-13 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2025-03-13: Introduced in Senate

## Actions

- 2025-03-13 - IntroReferral: Introduced in Senate
- 2025-03-13 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-13",
    "latestAction": {
      "actionDate": "2025-03-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1054",
    "number": "1054",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "R000584",
        "district": "",
        "firstName": "James",
        "fullName": "Sen. Risch, James E. [R-ID]",
        "lastName": "Risch",
        "party": "R",
        "state": "ID"
      }
    ],
    "title": "United States African Development Foundation Dissolution Act",
    "type": "S",
    "updateDate": "2026-02-04T12:03:15Z",
    "updateDateIncludingText": "2026-02-04T12:03:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-13",
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
      "actionDate": "2025-03-13",
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
            "date": "2025-03-13T20:53:39Z",
            "name": "Referred To"
          },
          {
            "date": "2025-03-13T20:53:39Z",
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
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-03-13",
      "state": "TX"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "False",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "ND"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1054is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1054\nIN THE SENATE OF THE UNITED STATES\nMarch 13, 2025 Mr. Risch (for himself and Mr. Cruz ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo abolish the United States African Development Foundation.\n#### 1. Short title\nThis Act may be cited as the United States African Development Foundation Dissolution Act .\n#### 2. Abolition\nThe United States African Development Foundation established under section 503 of the African Development Foundation Act (title V of Public Law 96\u2013533 ; 22 U.S.C. 290h\u20131 ) is abolished.\n#### 3. Repeal\nThe African Development Foundation Act (title V of Public Law 96\u2013533 ; 22 U.S.C. 290h et seq. ) is repealed.\n#### 4. Transfer of functions and authorities\n##### (a) Transfers to Secretary of State\nThere are transferred to the Secretary of State all of the functions of the United States African Development Foundation, as of the day before the date of the enactment of this Act, including any unexpended balances, assets, or responsibilities of such agency under any statute, reorganization plan, executive order, or other provision of law.\n##### (b) No retention of officers\nNothing in this subsection (a) may be construed to require the reappointment of any officer of the United States African Development Foundation as of the day before the date of the enactment of this Act.\n#### 5. References\nBeginning on the date of the enactment of this Act, any reference in any statute, reorganization plan, executive order, regulation, agreement, determination, or other official document or proceeding to the United States African Development Foundation, or to the President and Chief Executive Officer or any other officer or employee of the United States African Development Foundation, shall be deemed to refer to the Secretary of State or the Department of State, as appropriate.",
      "versionDate": "2025-03-13",
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
        "name": "International Affairs",
        "updateDate": "2025-05-14T12:40:24Z"
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
      "date": "2025-03-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1054is.xml"
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
      "title": "United States African Development Foundation Dissolution Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-04T12:03:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "United States African Development Foundation Dissolution Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-01T04:09:33Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to abolish the United States African Development Foundation.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-01T04:08:19Z"
    }
  ]
}
```
