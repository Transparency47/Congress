# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3299?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3299
- Title: DSH in Tennessee Act
- Congress: 119
- Bill type: S
- Bill number: 3299
- Origin chamber: Senate
- Introduced date: 2025-12-02
- Update date: 2026-01-09T15:17:30Z
- Update date including text: 2026-01-09T15:17:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-02: Introduced in Senate
- 2025-12-02 - IntroReferral: Introduced in Senate
- 2025-12-02 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-12-02: Introduced in Senate

## Actions

- 2025-12-02 - IntroReferral: Introduced in Senate
- 2025-12-02 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-02",
    "latestAction": {
      "actionDate": "2025-12-02",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3299",
    "number": "3299",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001243",
        "district": "",
        "firstName": "Marsha",
        "fullName": "Sen. Blackburn, Marsha [R-TN]",
        "lastName": "Blackburn",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "DSH in Tennessee Act",
    "type": "S",
    "updateDate": "2026-01-09T15:17:30Z",
    "updateDateIncludingText": "2026-01-09T15:17:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-02",
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
      "actionDate": "2025-12-02",
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
          "date": "2025-12-02T17:02:56Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "H000601",
      "firstName": "Bill",
      "fullName": "Sen. Hagerty, Bill [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Hagerty",
      "party": "R",
      "sponsorshipDate": "2025-12-02",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3299is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3299\nIN THE SENATE OF THE UNITED STATES\nDecember 2, 2025 Mrs. Blackburn (for herself and Mr. Hagerty ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XIX of the Social Security Act to provide a permanent disproportionate share hospital allotment to Tennessee for fiscal year 2026 and succeeding fiscal years, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Delivering Support for Hospitals in Tennessee Act or the DSH in Tennessee Act .\n#### 2. Permanent Tennessee DSH allotment for fiscal year 2026 and succeeding fiscal years\nSection 1923(f)(3) of the Social Security Act ( 42 U.S.C. 1396r\u20134(f)(3) ) is amended\u2014\n**(1)**\nin subparagraph (A), by striking subparagraphs (E) and (F) and inserting subparagraphs (E), (F), and (G) ; and\n**(2)**\nby adding at the end the following new subparagraph:\n(G) Tennessee DSH restoration (i) In general Notwithstanding any other provision of this subsection, the State of Tennessee shall receive a DSH allotment under this paragraph beginning with fiscal year 2026 and for each succeeding fiscal year. (ii) Allotment for fiscal year 2026 Notwithstanding the table set forth in paragraph (2) or the terms of the TennCare Demonstration Project in effect for the State, the DSH allotment for Tennessee for fiscal year 2026, shall be equal to the DSH allotment for Tennessee under paragraph (6)(A)(vi) for fiscal year 2015, increased in each succeeding fiscal year by the percentage change in the consumer price index for all urban consumers (all items; U.S. city average). (iii) Treatment as a low DSH state For any fiscal year after fiscal year 2026\u2014 (I) Tennessee shall be deemed to be a State described in paragraph (5)(B); and (II) the DSH allotment for Tennessee shall be the DSH allotment for the previous fiscal year increased in the same manner as DSH allotments for low DSH States are increased for such fiscal year under clause (iii) of such paragraph. .",
      "versionDate": "2025-12-02",
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
        "actionDate": "2025-12-03",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "6393",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "DSH in Tennessee Act",
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
        "name": "Health",
        "updateDate": "2026-01-06T18:06:41Z"
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
      "date": "2025-12-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3299is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XIX of the Social Security Act to provide a permanent disproportionate share hospital allotment to Tennessee for fiscal year 2026 and succeeding fiscal years, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-19T07:58:42Z"
    },
    {
      "title": "DSH in Tennessee Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-19T05:38:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "DSH in Tennessee Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-19T05:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Delivering Support for Hospitals in Tennessee Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-19T05:38:19Z"
    }
  ]
}
```
