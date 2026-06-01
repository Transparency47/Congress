# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1375?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1375
- Title: SNOOP Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1375
- Origin chamber: Senate
- Introduced date: 2025-04-09
- Update date: 2025-12-06T06:37:35Z
- Update date including text: 2025-12-06T06:37:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-09: Introduced in Senate
- 2025-04-09 - IntroReferral: Introduced in Senate
- 2025-04-09 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-04-09: Introduced in Senate

## Actions

- 2025-04-09 - IntroReferral: Introduced in Senate
- 2025-04-09 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-09",
    "latestAction": {
      "actionDate": "2025-04-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1375",
    "number": "1375",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "H000601",
        "district": "",
        "firstName": "Bill",
        "fullName": "Sen. Hagerty, Bill [R-TN]",
        "lastName": "Hagerty",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "SNOOP Act of 2025",
    "type": "S",
    "updateDate": "2025-12-06T06:37:35Z",
    "updateDateIncludingText": "2025-12-06T06:37:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-09",
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
      "actionDate": "2025-04-09",
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
          "date": "2025-04-09T16:39:05Z",
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
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "False",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-06-02",
      "state": "ND"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "False",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-06-10",
      "state": "IA"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-06-10",
      "state": "AL"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-06-11",
      "state": "TN"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-06-18",
      "state": "IN"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-06-25",
      "state": "NE"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "WY"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
      "state": "MS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1375is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1375\nIN THE SENATE OF THE UNITED STATES\nApril 9, 2025 Mr. Hagerty introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to reinstate the exception for de minimis payments by third party settlement organizations with respect to returns relating to payments made in settlement of payment card and third party network transactions, as in effect prior to the enactment of the American Rescue Plan Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stop the Nosy Obsession with Online Payments Act of 2025 or the SNOOP Act of 2025 .\n#### 2. Reinstatement of exception for de minimis payments as in effect prior to enactment of American Rescue Plan Act\n##### (a) In general\nSection 6050W(e) of the Internal Revenue Code of 1986 is amended to read as follows:\n(e) Exception for de minimis payments by third party settlement organizations A third party settlement organization shall be required to report any information under subsection (a) with respect to third party network transactions of any participating payee only if\u2014 (1) the amount which would otherwise be reported under subsection (a)(2) with respect to such transactions exceeds $20,000, and (2) the aggregate number of such transactions exceeds 200. .\n##### (b) Effective date\nThe amendment made by this section shall take effect as if included in section 9674(a) of the American Rescue Plan Act.\n#### 3. Application of de minimis rule for third party network transactions to backup withholding\n##### (a) In general\nSection 3406(b) of the Internal Revenue Code of 1986 is amended by adding at the end the following new paragraph:\n(8) Other reportable payments include payments in settlement of third party network transactions only where aggregate transactions exceed reporting threshold for the calendar year (A) In general Any payment in settlement of a third party network transaction required to be shown on a return required under section 6050W which is made during any calendar year shall be treated as a reportable payment only if\u2014 (i) the aggregate number of transactions with respect to the participating payee during such calendar year exceeds the number of transactions specified in section 6050W(e)(2), and (ii) the aggregate amount of transactions with respect to the participating payee during such calendar year exceeds the dollar amount specified in section 6050W(e)(1) at the time of such payment. (B) Exception if third party network transactions made in prior year were reportable Subparagraph (A) shall not apply with respect to payments to any participating payee during any calendar year if one or more payments in settlement of third party network transactions made by the payor to the participating payee during the preceding calendar year were reportable payments. .\n##### (b) Effective date\nThe amendment made by this section shall apply to calendar years beginning after December 31, 2024.",
      "versionDate": "2025-04-09",
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
        "actionDate": "2025-03-05",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "1882",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Saving Gig Economy Taxpayers Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-04-10",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "1425",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Red Tape Reduction Act of 2025",
      "type": "S"
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
        "updateDate": "2025-05-12T14:05:45Z"
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
      "date": "2025-04-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1375is.xml"
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
      "title": "SNOOP Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-22T11:03:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SNOOP Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-23T02:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Stop the Nosy Obsession with Online Payments Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-23T02:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to reinstate the exception for de minimis payments by third party settlement organizations with respect to returns relating to payments made in settlement of payment card and third party network transactions, as in effect prior to the enactment of the American Rescue Plan Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-23T02:48:23Z"
    }
  ]
}
```
