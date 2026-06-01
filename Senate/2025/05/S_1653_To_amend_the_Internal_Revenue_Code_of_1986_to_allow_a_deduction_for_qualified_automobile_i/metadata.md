# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1653?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1653
- Title: USA CAR Act
- Congress: 119
- Bill type: S
- Bill number: 1653
- Origin chamber: Senate
- Introduced date: 2025-05-07
- Update date: 2026-01-10T07:23:08Z
- Update date including text: 2026-01-10T07:23:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-07: Introduced in Senate
- 2025-05-07 - IntroReferral: Introduced in Senate
- 2025-05-07 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-05-07: Introduced in Senate

## Actions

- 2025-05-07 - IntroReferral: Introduced in Senate
- 2025-05-07 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-07",
    "latestAction": {
      "actionDate": "2025-05-07",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1653",
    "number": "1653",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "M001242",
        "district": "",
        "firstName": "Bernie",
        "fullName": "Sen. Moreno, Bernie [R-OH]",
        "lastName": "Moreno",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "USA CAR Act",
    "type": "S",
    "updateDate": "2026-01-10T07:23:08Z",
    "updateDateIncludingText": "2026-01-10T07:23:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-07",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-07",
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
        "item": {
          "date": "2025-05-07T20:55:29Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1653is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1653\nIN THE SENATE OF THE UNITED STATES\nMay 7, 2025 Mr. Moreno introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to allow a deduction for qualified automobile interest.\n#### 1. Short title\nThis Act may be cited as the United States Automobile Consumer Assistance and Relief Act or the USA CAR Act .\n#### 2. Deduction for qualified automobile interest\n##### (a) In general\nSection 163(h)(2) of the Internal Revenue Code of 1986 is amended by striking and at the end of subparagraph (E), by striking the period at the end of subparagraph (F) and inserting , and , and by adding at the end the following new subparagraph:\n(G) any qualified automobile interest (as defined in paragraph (5)). .\n##### (b) Qualified automobile interest\nSection 163(h) is amended by adding at the end the following new paragraph:\n(5) Qualified automobile interest For purposes of this subsection\u2014 (A) In general The term qualified automobile interest means any interest which is paid or accrued during the taxable year on indebtedness which\u2014 (i) is incurred on or after January 1, 2025, (ii) is incurred in acquiring a qualified automobile, and (iii) is secured by such automobile. (B) Qualified automobile (i) In general The term qualified automobile means an automobile (within the mean of section 2 of the Automobile Information Disclosure Act ( 15 U.S.C. 1231 )) which is made by a manufacturer (within the meaning of section 2 of such Act) the final assembly of which occurs within the United States. (ii) Final assembly The term final assembly means the process by which a manufacturer produced an automobile at, or through the use of, a plant, factory, or other place from which the automobile is delivered to a dealer with all component parts necessary for the mechanical operation of the automobile included with the automobile, whether or not the component parts are permanently installed in or on the automobile. .\n##### (c) Deduction allowed above-the-Line\nSection 62(a) of the Internal Revenue Code of 1986 is amended by inserting after paragraph (21) the following new paragraph:\n(22) In the case of a taxpayer other than a corporation, so much of the deduction allowed under section 163 which is attributable to qualified automobile interest (as defined in section 163(h)(5)). .\n##### (d) Effective date\nThe amendments made by this section shall apply to amounts paid or accrued on indebtedness incurred on or after the date of the enactment of this Act.",
      "versionDate": "2025-05-07",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-04-21",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "2981",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "USA CAR Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-04-01",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "1219",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "USA CAR Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-05-21",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "3570",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "USA CAR Act",
      "type": "HR"
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
        "name": "Taxation",
        "updateDate": "2025-06-06T18:11:30Z"
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
      "date": "2025-05-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1653is.xml"
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
      "title": "USA CAR Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-20T04:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "USA CAR Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-20T04:38:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "United States Automobile Consumer Assistance and Relief Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-20T04:38:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to allow a deduction for qualified automobile interest.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-20T04:33:24Z"
    }
  ]
}
```
