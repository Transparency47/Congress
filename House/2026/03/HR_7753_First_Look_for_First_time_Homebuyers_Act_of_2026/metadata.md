# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7753?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7753
- Title: First Look for First-time Homebuyers Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7753
- Origin chamber: House
- Introduced date: 2026-03-03
- Update date: 2026-03-24T20:19:36Z
- Update date including text: 2026-03-24T20:19:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-03: Introduced in House
- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2026-03-03: Introduced in House

## Actions

- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-03",
    "latestAction": {
      "actionDate": "2026-03-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7753",
    "number": "7753",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "B001321",
        "district": "7",
        "firstName": "Tom",
        "fullName": "Rep. Barrett, Tom [R-MI-7]",
        "lastName": "Barrett",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "First Look for First-time Homebuyers Act of 2026",
    "type": "HR",
    "updateDate": "2026-03-24T20:19:36Z",
    "updateDateIncludingText": "2026-03-24T20:19:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-03",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-03",
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
          "date": "2026-03-03T17:01:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7753ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7753\nIN THE HOUSE OF REPRESENTATIVES\nMarch 3, 2026 Mr. Barrett introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo strengthen and standardize first look protections for covered properties to ensure first-time homebuyers have priority access to foreclosed homes, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the First Look for First-time Homebuyers Act of 2026 .\n#### 2. First look protections for first-time homebuyers\n##### (a) In general\n**(1) 15-day first look period**\nExcept as provided in paragraph (2), each covered entity shall ensure, when selling an covered property, that the covered property is only available for purchase by first-time homebuyers during the 15-day period beginning on the date that the covered property is listed for sale.\n**(2) Extension of period**\nA covered entity may extend the period described in paragraph (1) if such extension would increase the chance of a first-time homebuyer purchasing a covered property.\n##### (b) Pricing of covered properties\n**(1) In general**\nDuring the 15-day period beginning on the date that the covered property is listed for sale during which an covered property is only available for purchase by first-time homebuyers the covered property shall be offered by the covered entity at a price that is the fair market value of the property as determined by an independent third-party appraisal or broker price opinion not more than 60 days before the date on which the property was listed for sale.\n**(2) Exception**\nIf the covered entity selling the covered property determines that the fair market value of the property can not be determined by an independent third-party appraisal or broker price opinion not more than 60 days before the date on which the property was listed for sale the covered entity may offer the covered property at a price based on a standardized valuation model used by the covered entity if the covered entity publically discloses the methodology used by such standardized valuation model.\n##### (c) Listing on public website\nDuring the 15-day period beginning on the date that the covered property is listed for sale during which an covered property is only available for purchase by first-time homebuyers the covered property shall be listed on a publically accessible website by the covered entity in a manner that identifies the covered property as only available for purchase by first-time homebuyers and indicates how many days remain in the 15-day period during which the covered property is only available for purchase by first-time homebuyers.\n##### (d) Prohibition on bundling\nA covered entity may not bundle covered properties during the 15-day period beginning on the date that the covered property is listed for sale by the eligible entity.\n##### (e) Report to congress\nNot later than 6 months after the date described in subsection (h), and every 6 months thereafter, each covered entity shall submit to the Congress a report that describes\u2014\n**(1)**\nthe number of offers made by first-time homebuyers for covered properties during the 15-day window;\n**(2)**\nthe number of covered properties sold to first-time home buyers during the 15-day window;\n**(3)**\nthe pricing methodology used; and\n**(4)**\nthe ratio of the sale price to the fair market value as determined by an independent third party appraisal, broker price opinion, or standardized valuation model.\n##### (f) Annual report\n**(1) In general**\nThe Inspectors General of each covered entity shall, each year, review all sales of covered properties by the covered entity in the prior year and determine whether any provisions of this section were violated during such sale.\n**(2) Report**\nThe Inspectors General of each covered entity shall submit a report to the Congress each year that includes the results of the review conducted under paragraph (1).\n**(3) Public publication**\nThe Inspectors General of each covered entity shall publish the report submitted under paragraph (2) on a publically accessible website of the covered entity.\n##### (g) Rulemaking\nEach covered entity shall, not later than 1 year after the date of the enactment of this section, issue such rules as are necessary to carry out this section and such rules shall include a process to verify the eligibility of first-time homebuyers.\n##### (h) Effective date\nThis section shall take effect 30 days after the date of the final rulemaking described in subsection (g).\n##### (i) Definitions\nIn this section:\n**(1) Covered property**\n**(A) In general**\nExcept as provided in subparagraph (B), the term covered property means any single-family residential property made up of 1 to 4 units that is owned or foreclosed upon by a covered entity.\n**(B) Good Neighbor Next Door Program**\nFor the purposes of this Act, a covered property shall not include any property under the program known as the Good Neighbor Next Door Program .\n**(2) Covered entity**\nThe term covered entity means\u2014\n**(A)**\nthe Federal Housing Administration;\n**(B)**\nthe Federal Housing Finance Agency;\n**(C)**\nthe Federal National Mortgage Association;\n**(D)**\nthe Federal Home Loan Mortgage Corporation; and\n**(E)**\nthe Department of Agriculture.\n**(3) First-time homebuyer**\nThe term first-time homebuyer means any individual if such individual, or such individual\u2019s spouse, has not had a present ownership interest in a principal residence at any time prior to the date of sale to which this Act applies.",
      "versionDate": "2026-03-03",
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
        "name": "Housing and Community Development",
        "updateDate": "2026-03-24T20:19:36Z"
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
      "date": "2026-03-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7753ih.xml"
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
      "title": "First Look for First-time Homebuyers Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-20T01:53:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "First Look for First-time Homebuyers Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-20T01:53:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To strengthen and standardize \"first look\" protections for covered properties to ensure first-time homebuyers have priority access to foreclosed homes, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-20T01:48:19Z"
    }
  ]
}
```
