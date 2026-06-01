# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8116?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8116
- Title: SHARE Act
- Congress: 119
- Bill type: HR
- Bill number: 8116
- Origin chamber: House
- Introduced date: 2026-03-26
- Update date: 2026-05-13T08:06:36Z
- Update date including text: 2026-05-13T08:06:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-26: Introduced in House
- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-03-26: Introduced in House

## Actions

- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-26",
    "latestAction": {
      "actionDate": "2026-03-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8116",
    "number": "8116",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "M001213",
        "district": "1",
        "firstName": "Blake",
        "fullName": "Rep. Moore, Blake D. [R-UT-1]",
        "lastName": "Moore",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "SHARE Act",
    "type": "HR",
    "updateDate": "2026-05-13T08:06:36Z",
    "updateDateIncludingText": "2026-05-13T08:06:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-26",
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
      "actionDate": "2026-03-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-26",
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
          "date": "2026-03-26T14:02:45Z",
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
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "CA"
    },
    {
      "bioguideId": "B001282",
      "district": "6",
      "firstName": "Andy",
      "fullName": "Rep. Barr, Andy [R-KY-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Barr",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "KY"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8116ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8116\nIN THE HOUSE OF REPRESENTATIVES\nMarch 26, 2026 Mr. Moore of Utah (for himself, Mr. Panetta , and Mr. Barr ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to exclude from gross income certain proceeds of shared appreciation mortgage contracts.\n#### 1. Short title\nThis Act may be cited as the Shared Home Appreciation for Residential Equity Act or the SHARE Act .\n#### 2. Exclusion of certain proceeds of a shared appreciation mortgage contract\n##### (a) In general\nPart III of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 139I the following new section:\n139J. Certain proceeds of a shared appreciation mortgage contract (a) In general Gross income shall not include\u2014 (1) any amount received by a lender as repayment of a shared appreciation mortgage which exceeds the original principal obligation of such mortgage if\u2014 (A) the income of the borrower did not exceed 140 percent of the area median income for the census tract in which the real property is located for the calendar year in which such loan was issued, and (B) the real property is a residential property which was the principal residence (as such term is used in section 121) of the borrower, or (2) any gain from the disposition of so much of a capital asset as is composed of or secured by mortgages described in paragraph (1). (b) Shared appreciation mortgage For purposes of this section, the term shared appreciation mortgage means a mortgage secured by a second lien on a property upon which there is located a dwelling designed principally for occupancy by one to four families which\u2014 (1) provides for the mortgagee to share in a predetermined percentage of the property's net appreciated value which does not exceed the percentage which is the quotient of\u2014 (A) the amount of such mortgage, divided by (B) the purchase price of such property, (2) does not require the mortgagor to make any payment other than the payment described in paragraph (1), (3) the amount of which does not exceed 49 percent of the purchase price of such property, (4) is subordinate to a first lien that is a qualified mortgage as such term is defined under section 129C(c)(2) of the Truth in Lending Act, and (5) does not require repayment before\u2014 (A) the scheduled maturity date of the mortgage secured by the first lien on the property; (B) the sale of the property; (C) repayment in full of the mortgage secured by the first lien on the property; (D) the scheduled maturity date of the mortgage secured by the first lien on the property as altered by any acceleration of such mortgage in accordance with the terms of such mortgage; or (E) a default under the mortgage. .\n##### (b) Clerical amendment\nThe table of sections for part III of subchapter B of chapter 1 of such Code is amended by inserting after the item relating to section 139I the following new item:\nSec. 139J. Certain proceeds of a shared appreciation mortgage contract. .\n##### (c) Effective date\nThe amendments made by this section shall apply to amounts received after December 31, 2025.",
      "versionDate": "2026-03-26",
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
        "name": "Taxation",
        "updateDate": "2026-04-21T01:23:41Z"
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
      "date": "2026-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8116ih.xml"
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
      "title": "SHARE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-17T05:38:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SHARE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-17T05:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Shared Home Appreciation for Residential Equity Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-17T05:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to exclude from gross income certain proceeds of shared appreciation mortgage contracts.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-17T05:33:38Z"
    }
  ]
}
```
