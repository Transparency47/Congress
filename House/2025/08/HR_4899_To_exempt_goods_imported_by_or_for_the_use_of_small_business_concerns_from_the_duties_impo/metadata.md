# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4899?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4899
- Title: CANADA Act
- Congress: 119
- Bill type: HR
- Bill number: 4899
- Origin chamber: House
- Introduced date: 2025-08-05
- Update date: 2026-05-18T11:42:14Z
- Update date including text: 2026-05-18T11:42:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-08-05: Introduced in House
- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-08-05: Introduced in House

## Actions

- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-05",
    "latestAction": {
      "actionDate": "2025-08-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4899",
    "number": "4899",
    "originChamber": "House",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "P000614",
        "district": "1",
        "firstName": "Chris",
        "fullName": "Rep. Pappas, Chris [D-NH-1]",
        "lastName": "Pappas",
        "party": "D",
        "state": "NH"
      }
    ],
    "title": "CANADA Act",
    "type": "HR",
    "updateDate": "2026-05-18T11:42:14Z",
    "updateDateIncludingText": "2026-05-18T11:42:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-05",
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
      "actionDate": "2025-08-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-05",
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
          "date": "2025-08-05T14:00:25Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "NH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4899ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4899\nIN THE HOUSE OF REPRESENTATIVES\nAugust 5, 2025 Mr. Pappas (for himself and Ms. Goodlander ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo exempt goods imported by or for the use of small business concerns from the duties imposed by the national emergency declared on February 1, 2025, by the President.\n#### 1. Short title\nThe Act may be cited as the Creating Access to Necessary American-Canadian Duty Adjustments Act or the CANADA Act .\n#### 2. Exemption for certain goods from national emergency\nDuties imposed by the national emergency declared on February 1, 2025, by the President in Executive Order 14193 (90 Fed. Reg. 9113), as amended by Executive Order 14197 (90 Fed. Reg. 9183) and Executive Order 14226 (90 Fed. Reg. 11369), shall not apply with respect to goods imported by or for the use of small business concerns, as defined in section 3 of the Small Business Act ( 15 U.S.C. 632 ).",
      "versionDate": "2025-08-05",
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
        "actionDate": "2025-07-22",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "2383",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "CANADA Act",
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
        "name": "Foreign Trade and International Finance",
        "updateDate": "2025-09-15T17:26:51Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-08-05",
    "originChamber": "House",
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
          "measure-id": "id119hr4899",
          "measure-number": "4899",
          "measure-type": "hr",
          "orig-publish-date": "2025-08-05",
          "originChamber": "HOUSE",
          "update-date": "2026-05-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr4899v00",
            "update-date": "2026-05-18"
          },
          "action-date": "2025-08-05",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Creating Access to Necessary American-Canadian Duty Adjustments Act or the CANADA Act</strong></p><p>This bill exempts goods imported by or for the use of small business concerns from duties (i.e., tariffs) imposed under <a href=\"https://www.federalregister.gov/documents/2025/02/07/2025-02406/imposing-duties-to-address-the-flow-of-illicit-drugs-across-our-northern-border\">Executive Order 14193</a>. This executive order, issued by President Donald J. Trump on February 1, 2025, imposed a 25% tariff on most imports from Canada (except for Canadian energy or energy resources, which have a 10% tariff).</p>"
        },
        "title": "CANADA Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr4899.xml",
    "summary": {
      "actionDate": "2025-08-05",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Creating Access to Necessary American-Canadian Duty Adjustments Act or the CANADA Act</strong></p><p>This bill exempts goods imported by or for the use of small business concerns from duties (i.e., tariffs) imposed under <a href=\"https://www.federalregister.gov/documents/2025/02/07/2025-02406/imposing-duties-to-address-the-flow-of-illicit-drugs-across-our-northern-border\">Executive Order 14193</a>. This executive order, issued by President Donald J. Trump on February 1, 2025, imposed a 25% tariff on most imports from Canada (except for Canadian energy or energy resources, which have a 10% tariff).</p>",
      "updateDate": "2026-05-18",
      "versionCode": "id119hr4899"
    },
    "title": "CANADA Act"
  },
  "summaries": [
    {
      "actionDate": "2025-08-05",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Creating Access to Necessary American-Canadian Duty Adjustments Act or the CANADA Act</strong></p><p>This bill exempts goods imported by or for the use of small business concerns from duties (i.e., tariffs) imposed under <a href=\"https://www.federalregister.gov/documents/2025/02/07/2025-02406/imposing-duties-to-address-the-flow-of-illicit-drugs-across-our-northern-border\">Executive Order 14193</a>. This executive order, issued by President Donald J. Trump on February 1, 2025, imposed a 25% tariff on most imports from Canada (except for Canadian energy or energy resources, which have a 10% tariff).</p>",
      "updateDate": "2026-05-18",
      "versionCode": "id119hr4899"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-08-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4899ih.xml"
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
      "title": "CANADA Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-09T03:53:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CANADA Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Creating Access to Necessary American-Canadian Duty Adjustments Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To exempt goods imported by or for the use of small business concerns from the duties imposed by the national emergency declared on February 1, 2025, by the President.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-09T03:48:27Z"
    }
  ]
}
```
