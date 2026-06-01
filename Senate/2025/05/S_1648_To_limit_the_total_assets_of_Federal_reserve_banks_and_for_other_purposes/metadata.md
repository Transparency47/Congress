# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1648?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1648
- Title: Right-size the Federal Reserve Act
- Congress: 119
- Bill type: S
- Bill number: 1648
- Origin chamber: Senate
- Introduced date: 2025-05-07
- Update date: 2026-04-28T15:01:11Z
- Update date including text: 2026-04-28T15:01:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-05-07: Introduced in Senate
- 2025-05-07 - IntroReferral: Introduced in Senate
- 2025-05-07 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-05-07: Introduced in Senate

## Actions

- 2025-05-07 - IntroReferral: Introduced in Senate
- 2025-05-07 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1648",
    "number": "1648",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "S001217",
        "district": "",
        "firstName": "Rick",
        "fullName": "Sen. Scott, Rick [R-FL]",
        "lastName": "Scott",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Right-size the Federal Reserve Act",
    "type": "S",
    "updateDate": "2026-04-28T15:01:11Z",
    "updateDateIncludingText": "2026-04-28T15:01:11Z"
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
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
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
          "date": "2025-05-07T20:44:06Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1648is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1648\nIN THE SENATE OF THE UNITED STATES\nMay 7, 2025 Mr. Scott of Florida introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo limit the total assets of Federal reserve banks, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Right-size the Federal Reserve Act .\n#### 2. Limitation on total assets and interest payments\n##### (a) In general\nThe Federal Reserve Act is amended\u2014\n**(1)**\nin section 2B ( 12 U.S.C. 225b ), by adding at the end the following:\n(d) Additional annual report The Board and each Federal reserve bank shall submit to Congress, on an annual basis, a report on how many foreign-owned banks and financial institutions the Board or the Federal reserve banks have paid on interest for reserves or in the lending facilities of the Board. ;\n**(2)**\nin section 19(b) ( 12 U.S.C. 461(b) )\u2014\n**(A)**\nin paragraph (2)(A), by striking solely for the purpose and all that follows through the period at the end and inserting , which shall be not lower than the reserve requirements in effect on March 25, 2020. ; and\n**(B)**\nin paragraph (12)(A), by inserting that are not in excess of the reserves required to be maintained under this subsection after institution ; and\n**(3)**\nby adding at the end the following:\n33. Limitation on total assets (a) In general The total aggregate assets of all Federal reserve banks shall be in an amount that is not more than 10 percent of the gross domestic product of the United States. (b) Effective date Subsection (a) shall take effect on the date that is 10 years after the date of enactment of this section. .\n##### (b) Elimination of facility\nThe Board of Governors of the Federal Reserve System\u2014\n**(1)**\nshall, not later than 1 year after the date of enactment of this Act, eliminate the Overnight Reserve Repurchase Facility; and\n**(2)**\nmay not create another facility similar to the facility eliminated under paragraph (1).\n##### (c) Report\nNot later than 1 year after the date of enactment of this Act, and every year thereafter, the Board of Governors of the Federal Reserve System shall submit to Congress a report on the plan and timeline of the Board for meeting the requirements under this section and the amendments made by this section.",
      "versionDate": "2025-05-07",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-05-23T14:24:17Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-07",
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
          "measure-id": "id119s1648",
          "measure-number": "1648",
          "measure-type": "s",
          "orig-publish-date": "2025-05-07",
          "originChamber": "SENATE",
          "update-date": "2026-04-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1648v00",
            "update-date": "2026-04-28"
          },
          "action-date": "2025-05-07",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Right-size the Federal Reserve Act</strong></p><p>This bill places restrictions on the Federal Reserve System, including by placing a cap on specified assets, eliminating a Federal Reserve Board facility, and setting forth conditions on bank reserve requirements.</p><p>The bill places a cap on the total aggregate assets of all Federal Reserve banks. Specifically, these assets must not amount to more than 10% of the\u00a0U.S. gross domestic product. This cap takes effect 10 years after the bill\u2019s enactment.</p><p>The bill also eliminates the Overnight Reverse Repurchase Facility, a board facility that conducts monetary policy through security repurchase agreements.</p><p>The board\u2019s depository institution reserves requirements must not be lower than the reserve requirements as of March 25, 2020.\u00a0The board and each Federal Reserve bank must annually report on certain interest payments to foreign-owned banks and financial institutions.\u00a0 \u00a0</p>"
        },
        "title": "Right-size the Federal Reserve Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1648.xml",
    "summary": {
      "actionDate": "2025-05-07",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Right-size the Federal Reserve Act</strong></p><p>This bill places restrictions on the Federal Reserve System, including by placing a cap on specified assets, eliminating a Federal Reserve Board facility, and setting forth conditions on bank reserve requirements.</p><p>The bill places a cap on the total aggregate assets of all Federal Reserve banks. Specifically, these assets must not amount to more than 10% of the\u00a0U.S. gross domestic product. This cap takes effect 10 years after the bill\u2019s enactment.</p><p>The bill also eliminates the Overnight Reverse Repurchase Facility, a board facility that conducts monetary policy through security repurchase agreements.</p><p>The board\u2019s depository institution reserves requirements must not be lower than the reserve requirements as of March 25, 2020.\u00a0The board and each Federal Reserve bank must annually report on certain interest payments to foreign-owned banks and financial institutions.\u00a0 \u00a0</p>",
      "updateDate": "2026-04-28",
      "versionCode": "id119s1648"
    },
    "title": "Right-size the Federal Reserve Act"
  },
  "summaries": [
    {
      "actionDate": "2025-05-07",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Right-size the Federal Reserve Act</strong></p><p>This bill places restrictions on the Federal Reserve System, including by placing a cap on specified assets, eliminating a Federal Reserve Board facility, and setting forth conditions on bank reserve requirements.</p><p>The bill places a cap on the total aggregate assets of all Federal Reserve banks. Specifically, these assets must not amount to more than 10% of the\u00a0U.S. gross domestic product. This cap takes effect 10 years after the bill\u2019s enactment.</p><p>The bill also eliminates the Overnight Reverse Repurchase Facility, a board facility that conducts monetary policy through security repurchase agreements.</p><p>The board\u2019s depository institution reserves requirements must not be lower than the reserve requirements as of March 25, 2020.\u00a0The board and each Federal Reserve bank must annually report on certain interest payments to foreign-owned banks and financial institutions.\u00a0 \u00a0</p>",
      "updateDate": "2026-04-28",
      "versionCode": "id119s1648"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1648is.xml"
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
      "title": "Right-size the Federal Reserve Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-21T03:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Right-size the Federal Reserve Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-21T03:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to limit the total assets of Federal reserve banks, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-21T03:48:28Z"
    }
  ]
}
```
