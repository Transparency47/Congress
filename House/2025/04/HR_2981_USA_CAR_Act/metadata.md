# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2981?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2981
- Title: USA CAR Act
- Congress: 119
- Bill type: HR
- Bill number: 2981
- Origin chamber: House
- Introduced date: 2025-04-21
- Update date: 2026-01-10T07:21:59Z
- Update date including text: 2026-01-10T07:21:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-21: Introduced in House
- 2025-04-21 - IntroReferral: Introduced in House
- 2025-04-21 - IntroReferral: Introduced in House
- 2025-04-21 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-04-21: Introduced in House

## Actions

- 2025-04-21 - IntroReferral: Introduced in House
- 2025-04-21 - IntroReferral: Introduced in House
- 2025-04-21 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-21",
    "latestAction": {
      "actionDate": "2025-04-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2981",
    "number": "2981",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "T000490",
        "district": "2",
        "firstName": "David",
        "fullName": "Rep. Taylor, David [R-OH-2]",
        "lastName": "Taylor",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "USA CAR Act",
    "type": "HR",
    "updateDate": "2026-01-10T07:21:59Z",
    "updateDateIncludingText": "2026-01-10T07:21:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-21",
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
      "actionDate": "2025-04-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-21",
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
          "date": "2025-04-21T16:00:15Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2981ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2981\nIN THE HOUSE OF REPRESENTATIVES\nApril 21, 2025 Mr. Taylor introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to allow a deduction for qualified automobile interest.\n#### 1. Short title\nThis Act may be cited as the United States Automobile Consumer Assistance and Relief Act or the USA CAR Act .\n#### 2. Deduction for qualified automobile interest\n##### (a) In general\nSection 163(h)(2) of the Internal Revenue Code of 1986 is amended by striking and at the end of subparagraph (E), by striking the period at the end of subparagraph (F) and inserting , and , and by adding at the end the following new subparagraph:\n(G) any qualified automobile interest (as defined in paragraph (5)). .\n##### (b) Qualified automobile interest\nSection 163(h) is amended by adding at the end the following new paragraph:\n(5) Qualified automobile interest For purposes of this subsection\u2014 (A) In general The term qualified automobile interest means any interest which is paid or accrued during the taxable year on indebtedness which\u2014 (i) is incurred on or after January 1, 2025, (ii) is incurred in acquiring a qualified automobile, and (iii) is secured by such automobile. (B) Qualified automobile (i) In general The term qualified automobile means an automobile (within the mean of section 2 of the Automobile Information Disclosure Act ( 15 U.S.C. 1231 ) which is made by a manufacturer (within the meaning of section 2 of such Act) the final assembly of which occurs within the United States. (ii) Final assembly The term final assembly means the process by which a manufacturer produced an automobile at, or through the use of, a plant, factory, or other place from which the automobile is delivered to a dealer with all component parts necessary for the mechanical operation of the automobile included with the automobile, whether or not the component parts are permanently installed in or on the automobile. .\n##### (c) Effective date\nThe amendments made by this section shall apply to amounts paid or accrued on indebtedness incurred on or after January 1, 2025.",
      "versionDate": "2025-04-21",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-04-01",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "1219",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "USA CAR Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-05-07",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "1653",
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
          "type": "Related bill"
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
        "updateDate": "2025-05-28T15:44:16Z"
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
      "date": "2025-04-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2981ih.xml"
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
      "title": "USA CAR Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-07T04:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "USA CAR Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-07T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "United States Automobile Consumer Assistance and Relief Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-07T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to allow a deduction for qualified automobile interest.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-07T04:18:27Z"
    }
  ]
}
```
