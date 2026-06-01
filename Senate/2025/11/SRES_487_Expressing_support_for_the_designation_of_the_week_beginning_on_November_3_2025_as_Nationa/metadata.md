# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/487?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/487
- Title: A resolution expressing support for the designation of the week beginning on November 3, 2025, as "National School Psychology Week".
- Congress: 119
- Bill type: SRES
- Bill number: 487
- Origin chamber: Senate
- Introduced date: 2025-11-06
- Update date: 2025-11-25T17:45:53Z
- Update date including text: 2025-11-25T17:45:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-06: Introduced in Senate
- 2025-11-06 - IntroReferral: Introduced in Senate
- 2025-11-06 - IntroReferral: Referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-11-06: Introduced in Senate

## Actions

- 2025-11-06 - IntroReferral: Introduced in Senate
- 2025-11-06 - IntroReferral: Referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-06",
    "latestAction": {
      "actionDate": "2025-11-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/487",
    "number": "487",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "P000145",
        "district": "",
        "firstName": "Alex",
        "fullName": "Sen. Padilla, Alex [D-CA]",
        "lastName": "Padilla",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "A resolution expressing support for the designation of the week beginning on November 3, 2025, as \"National School Psychology Week\".",
    "type": "SRES",
    "updateDate": "2025-11-25T17:45:53Z",
    "updateDateIncludingText": "2025-11-25T17:45:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-06",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-11-06",
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
          "date": "2025-11-06T17:53:29Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-11-06",
      "state": "TX"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-11-06",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres487is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 487\nIN THE SENATE OF THE UNITED STATES\nNovember 6, 2025 Mr. Padilla (for himself, Mr. Cornyn , and Ms. Smith ) submitted the following resolution; which was referred to the Committee on Health, Education, Labor, and Pensions\nRESOLUTION\nExpressing support for the designation of the week beginning on November 3, 2025, as National School Psychology Week .\nThat the Senate\u2014\n**(1)**\nsupports the designation of the week beginning on November 3, 2025, as National School Psychology Week ;\n**(2)**\nhonors and recognizes the contributions of school psychologists to the success of students in schools across the United States; and\n**(3)**\nencourages the people of the United States to observe the week with appropriate ceremonies and activities that promote awareness of the vital role school psychologists play in schools, in the community, and in helping students develop into successful and productive members of society.",
      "versionDate": "2025-11-06",
      "versionType": "IS"
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
        "actionDate": "2025-11-04",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "857",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Expressing support for the designation of the week beginning on November 3, 2025, as \"National School Psychology Week\".",
      "type": "HRES"
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
        "name": "Education",
        "updateDate": "2025-11-19T15:43:32Z"
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
      "date": "2025-11-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres487is.xml"
        }
      ],
      "type": "IS"
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
      "title": "A resolution expressing support for the designation of the week beginning on November 3, 2025, as \"National School Psychology Week\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-08T05:33:23Z"
    },
    {
      "title": "A resolution expressing support for the designation of the week beginning on November 3, 2025, as \"National School Psychology Week\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-07T11:56:15Z"
    }
  ]
}
```
