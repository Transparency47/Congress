# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7069?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7069
- Title: Affordable Food and Energy Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7069
- Origin chamber: House
- Introduced date: 2026-01-14
- Update date: 2026-05-22T08:08:52Z
- Update date including text: 2026-05-22T08:08:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-01-14: Introduced in House
- 2026-01-14 - IntroReferral: Introduced in House
- 2026-01-14 - IntroReferral: Introduced in House
- 2026-01-14 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-05-20 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.
- Latest action: 2026-01-14: Introduced in House

## Actions

- 2026-01-14 - IntroReferral: Introduced in House
- 2026-01-14 - IntroReferral: Introduced in House
- 2026-01-14 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-05-20 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-14",
    "latestAction": {
      "actionDate": "2026-01-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7069",
    "number": "7069",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "M001237",
        "district": "8",
        "firstName": "Kristen",
        "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
        "lastName": "McDonald Rivet",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Affordable Food and Energy Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-22T08:08:52Z",
    "updateDateIncludingText": "2026-05-22T08:08:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Nutrition and Foreign Agriculture Subcommittee",
          "systemCode": "hsag03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Nutrition and Foreign Agriculture.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-14",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-14",
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
          "date": "2026-01-14T15:00:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-05-20T14:42:26Z",
              "name": "Referred to"
            }
          },
          "name": "Nutrition and Foreign Agriculture Subcommittee",
          "systemCode": "hsag03"
        }
      },
      "systemCode": "hsag00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7069ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7069\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 14, 2026 Ms. McDonald Rivet introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Food and Nutrition Act of 2008 to expand benefits to households eligible for Federal and State energy assistance programs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Affordable Food and Energy Act of 2026 .\n#### 2. Household assistance\nSection 5 of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2014 ) is amended\u2014\n**(1)**\nby amending subsection (e)(6)(C)(iv)(I) to read as follows:\n(I) In general Subject to subclause (II), if a State agency elects to use a standard utility allowance that reflects heating and cooling costs, the standard utility allowance shall be made available to households that received a payment, or on behalf of which a payment was made, under the Low-Income Home Energy Assistance Act of 1981 ( 42 U.S.C. 8621 et seq. ) or other similar energy assistance program, if in the current month or in the immediately preceding 12 months, the household either received such a payment, or such a payment was made on behalf of the household, that was greater than $20 annually, as determined by the Secretary. , and\n**(2)**\nby amending subsection (k)(4) to read as follows:\n(4) Third party energy assistance payments (A) Energy assistance payments For purposes of subsection (d)(1), a payment made under a State law (other than a law referred to in paragraph (2)(G)) to provide energy assistance to a household shall be considered money payable directly to the household. (B) Energy assistance expenses For purposes of subsection (e)(6), an expense paid on behalf of a household under a State law to provide energy assistance shall be considered an out-of-pocket expense incurred and paid by the household. .\n#### 3. Effective date\nThis Act and the amendments made by this Act shall take effect July 4, 2025.",
      "versionDate": "2026-01-14",
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
        "name": "Agriculture and Food",
        "updateDate": "2026-02-10T00:07:56Z"
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
      "date": "2026-01-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7069ih.xml"
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
      "title": "Affordable Food and Energy Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-03T11:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Affordable Food and Energy Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-03T11:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Food and Nutrition Act of 2008 to expand benefits to households eligible for Federal and State energy assistance programs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-03T11:04:00Z"
    }
  ]
}
```
