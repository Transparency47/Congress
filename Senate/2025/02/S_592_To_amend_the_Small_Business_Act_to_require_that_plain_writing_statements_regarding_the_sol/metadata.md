# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/592?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/592
- Title: Simplifying Subcontracting Act
- Congress: 119
- Bill type: S
- Bill number: 592
- Origin chamber: Senate
- Introduced date: 2025-02-13
- Update date: 2025-12-18T12:03:18Z
- Update date including text: 2025-12-18T12:03:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-13: Introduced in Senate
- 2025-02-13 - IntroReferral: Introduced in Senate
- 2025-02-13 - IntroReferral: Read twice and referred to the Committee on Small Business and Entrepreneurship.
- Latest action: 2025-02-13: Introduced in Senate

## Actions

- 2025-02-13 - IntroReferral: Introduced in Senate
- 2025-02-13 - IntroReferral: Read twice and referred to the Committee on Small Business and Entrepreneurship.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-13",
    "latestAction": {
      "actionDate": "2025-02-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/592",
    "number": "592",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
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
    "title": "Simplifying Subcontracting Act",
    "type": "S",
    "updateDate": "2025-12-18T12:03:18Z",
    "updateDateIncludingText": "2025-12-18T12:03:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-13",
      "committees": {
        "item": {
          "name": "Small Business and Entrepreneurship Committee",
          "systemCode": "sssb00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Small Business and Entrepreneurship.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-13",
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
          "date": "2025-02-13T20:26:59Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Small Business and Entrepreneurship Committee",
      "systemCode": "sssb00",
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
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "ID"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "CO"
    },
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "LA"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "IN"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "NV"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-05-06",
      "state": "GA"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s592is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 592\nIN THE SENATE OF THE UNITED STATES\nFebruary 13, 2025 Mr. Risch (for himself, Mr. Crapo , Mr. Hickenlooper , Mr. Kennedy , and Mr. Young ) introduced the following bill; which was read twice and referred to the Committee on Small Business and Entrepreneurship\nA BILL\nTo amend the Small Business Act to require that plain writing statements regarding the solicitation of subcontractors be included in certain subcontracting plans, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Simplifying Subcontracting Act .\n#### 2. Plain writing application requirements for solicitation of subcontractors\n##### (a) In general\nSection 8(d) of the Small Business Act ( 15 U.S.C. 637(d) ) is amended\u2014\n**(1)**\nin paragraph (6)\u2014\n**(A)**\nin subparagraph (H)(ii), by striking and at the end;\n**(B)**\nin subparagraph (I)(ii), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(J) a representation that\u2014 (i) the offeror or bidder will communicate all solicitations of subcontracts in plain writing (as defined in section 3 of the Plain Writing Act of 2010 ( Public Law 111\u2013274 ; 124 Stat. 2861)) so that the solicitation is easily understood by small business concerns seeking to obtain a subcontracting opportunity from the offeror or bidder; and (ii) the offeror or bidder will include the plain writing requirement described in clause (i) in all subcontracts that offer subcontracting opportunities. ; and\n**(2)**\nby adding at the end the following:\n(18) Compliance with plain writing requirement If the Administrator determines that a prime contractor failed to communicate any solicitation of a subcontract in plain writing in accordance with paragraph (6)(J), the prime contractor shall communicate a new solicitation of the subcontract in plain writing not later than 30 days after the date on which the Administrator made that determination. .\n##### (b) Rulemaking\nNot later than 90 days after the date of enactment of this Act, the Administrator of the Small Business Administration shall promulgate regulations to carry out paragraphs (6)(J) and (18) of section 8(d) of the Small Business Act ( 15 U.S.C. 637(d) ), as added by subsection (a).",
      "versionDate": "2025-02-13",
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
        "name": "Commerce",
        "updateDate": "2025-03-17T15:03:12Z"
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
      "date": "2025-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s592is.xml"
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
      "title": "Simplifying Subcontracting Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-18T12:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Simplifying Subcontracting Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-14T03:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Small Business Act to require that plain writing statements regarding the solicitation of subcontractors be included in certain subcontracting plans, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-14T03:18:17Z"
    }
  ]
}
```
