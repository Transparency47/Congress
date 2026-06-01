# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3827?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3827
- Title: Financial Disclosure Modernization Act
- Congress: 119
- Bill type: S
- Bill number: 3827
- Origin chamber: Senate
- Introduced date: 2026-02-11
- Update date: 2026-02-27T21:31:09Z
- Update date including text: 2026-02-27T21:31:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-11: Introduced in Senate
- 2026-02-11 - IntroReferral: Introduced in Senate
- 2026-02-11 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2026-02-11: Introduced in Senate

## Actions

- 2026-02-11 - IntroReferral: Introduced in Senate
- 2026-02-11 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-11",
    "latestAction": {
      "actionDate": "2026-02-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3827",
    "number": "3827",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "S001150",
        "district": "",
        "firstName": "Adam",
        "fullName": "Sen. Schiff, Adam B. [D-CA]",
        "lastName": "Schiff",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Financial Disclosure Modernization Act",
    "type": "S",
    "updateDate": "2026-02-27T21:31:09Z",
    "updateDateIncludingText": "2026-02-27T21:31:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-11",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-02-11",
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
          "date": "2026-02-11T19:37:58Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-02-11",
      "state": "NY"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2026-02-11",
      "state": "CT"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2026-02-11",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3827is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3827\nIN THE SENATE OF THE UNITED STATES\nFebruary 11, 2026 Mr. Schiff (for himself, Mrs. Gillibrand , Mr. Blumenthal , and Mr. Merkley ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo modify reporting value categories for financial disclosure reports required under chapter 131 of title 5, United States Code.\n#### 1. Short title\nThis Act may be cited as the Financial Disclosure Modernization Act .\n#### 2. Dividends, rents, interest, and capital gains\nSection 13104(a)(1)(B) of title 5, United States Code, is amended\u2014\n**(1)**\nin clause (viii), by striking or ; and\n**(2)**\nby striking clause (ix) and inserting the following:\n(ix) greater than $5,000,000 but not more than $25,000,000; (x) greater than $25,000,000 but not more than $100,000,000; (xi) greater than $100,000,000 but not more than $500,000,000; (xii) greater than $500,000,000 but not more than $1,000,000,000; or (xiii) greater than $1,000,000,000. .\n#### 3. Categories for reporting amounts or values\nSection 13104(d)(1) of title 5, United States Code, is amended\u2014\n**(1)**\nin subparagraph (I), by striking and ; and\n**(2)**\nby striking subparagraph (J) and inserting the following:\n(J) greater than $50,000,000 but not more than $100,000,000; (K) greater than $100,000,000 but not more than $250,000,000; (L) greater than $250,000,000 but not more than $500,000,000; (M) greater than $500,000,000 but not more than $1,000,000,000; and (N) greater than $1,000,000,000. .\n#### 4. Effective date\nThe amendments made by this Act shall apply with respect to financial disclosure reports under chapter 131 of title 5, United States Code, that are required to be filed on or after the date of the enactment of this Act.",
      "versionDate": "2026-02-11",
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
        "actionDate": "2026-02-11",
        "text": "Referred to the Committee on Oversight and Government Reform, and in addition to the Committees on House Administration, and the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "7508",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Financial Disclosure Modernization Act",
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-02-27T21:31:09Z"
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
      "date": "2026-02-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3827is.xml"
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
      "title": "Financial Disclosure Modernization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-26T05:38:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Financial Disclosure Modernization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-26T05:38:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to modify reporting value categories for financial disclosure reports required under chapter 131 of title 5, United States Code.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-26T04:33:29Z"
    }
  ]
}
```
