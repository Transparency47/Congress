# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2383?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2383
- Title: CANADA Act
- Congress: 119
- Bill type: S
- Bill number: 2383
- Origin chamber: Senate
- Introduced date: 2025-07-22
- Update date: 2026-05-15T18:25:48Z
- Update date including text: 2026-05-15T18:25:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-07-22: Introduced in Senate
- 2025-07-22 - IntroReferral: Introduced in Senate
- 2025-07-22 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-07-22: Introduced in Senate

## Actions

- 2025-07-22 - IntroReferral: Introduced in Senate
- 2025-07-22 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-22",
    "latestAction": {
      "actionDate": "2025-07-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2383",
    "number": "2383",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "W000800",
        "district": "",
        "firstName": "Peter",
        "fullName": "Sen. Welch, Peter [D-VT]",
        "lastName": "Welch",
        "party": "D",
        "state": "VT"
      }
    ],
    "title": "CANADA Act",
    "type": "S",
    "updateDate": "2026-05-15T18:25:48Z",
    "updateDateIncludingText": "2026-05-15T18:25:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-22",
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
      "actionDate": "2025-07-22",
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
          "date": "2025-07-22T20:41:01Z",
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
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "NY"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "VA"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "NH"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "MA"
    },
    {
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-07-22",
      "state": "AK"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-07-22",
      "state": "ME"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2383is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2383\nIN THE SENATE OF THE UNITED STATES\nJuly 22, 2025 Mr. Welch (for himself, Mr. Schumer , Mr. Kaine , Mrs. Shaheen , Mr. Markey , Ms. Murkowski , Ms. Collins , and Mr. Wyden ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo exempt goods imported by or for the use of small business concerns from the duties imposed by the national emergency declared on February 1, 2025 by the President.\n#### 1. Short title\nThe Act may be cited as the Creating Access to Necessary American-Canadian Duty Adjustments Act or the CANADA Act .\n#### 2. Exemption for certain goods from national emergency\nDuties imposed by the national emergency declared on February 1, 2025 by the President in Executive Order 14193 (90 Fed. Reg. 9113), as amended by Executive Order 14197 (90 Fed. Reg. 9183) and Executive Order 14226 (90 Fed. Reg. 11369), shall not apply with respect to goods imported by or for the use of small business concerns, as defined in section 3 of the Small Business Act ( 15 U.S.C. 632 ).",
      "versionDate": "2025-07-22",
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
        "actionDate": "2025-08-05",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "4899",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "CANADA Act",
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
        "name": "Foreign Trade and International Finance",
        "updateDate": "2025-09-15T16:43:10Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-22",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119s2383",
          "measure-number": "2383",
          "measure-type": "s",
          "orig-publish-date": "2025-07-22",
          "originChamber": "SENATE",
          "update-date": "2026-05-15"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2383v00",
            "update-date": "2026-05-15"
          },
          "action-date": "2025-07-22",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Creating Access to Necessary American-Canadian Duty Adjustments Act or the CANADA Act</strong></p><p>This bill exempts goods imported by or for the use of small business concerns from duties (i.e., tariffs) imposed under <a href=\"https://www.federalregister.gov/documents/2025/02/07/2025-02406/imposing-duties-to-address-the-flow-of-illicit-drugs-across-our-northern-border\">Executive Order 14193</a>. This executive order, issued by President Donald J. Trump on February 1, 2025, imposed a 25% tariff on most imports from Canada (except for Canadian energy or energy resources, which have a 10% tariff).</p>"
        },
        "title": "CANADA Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2383.xml",
    "summary": {
      "actionDate": "2025-07-22",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Creating Access to Necessary American-Canadian Duty Adjustments Act or the CANADA Act</strong></p><p>This bill exempts goods imported by or for the use of small business concerns from duties (i.e., tariffs) imposed under <a href=\"https://www.federalregister.gov/documents/2025/02/07/2025-02406/imposing-duties-to-address-the-flow-of-illicit-drugs-across-our-northern-border\">Executive Order 14193</a>. This executive order, issued by President Donald J. Trump on February 1, 2025, imposed a 25% tariff on most imports from Canada (except for Canadian energy or energy resources, which have a 10% tariff).</p>",
      "updateDate": "2026-05-15",
      "versionCode": "id119s2383"
    },
    "title": "CANADA Act"
  },
  "summaries": [
    {
      "actionDate": "2025-07-22",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Creating Access to Necessary American-Canadian Duty Adjustments Act or the CANADA Act</strong></p><p>This bill exempts goods imported by or for the use of small business concerns from duties (i.e., tariffs) imposed under <a href=\"https://www.federalregister.gov/documents/2025/02/07/2025-02406/imposing-duties-to-address-the-flow-of-illicit-drugs-across-our-northern-border\">Executive Order 14193</a>. This executive order, issued by President Donald J. Trump on February 1, 2025, imposed a 25% tariff on most imports from Canada (except for Canadian energy or energy resources, which have a 10% tariff).</p>",
      "updateDate": "2026-05-15",
      "versionCode": "id119s2383"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2383is.xml"
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
      "title": "CANADA Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-05T05:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "CANADA Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-05T05:08:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Creating Access to Necessary American-Canadian Duty Adjustments Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-05T05:08:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to exempt goods imported by or for the use of small business concerns from the duties imposed by the national emergency declared on February 1, 2025 by the President.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-05T05:03:37Z"
    }
  ]
}
```
