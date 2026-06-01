# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6962?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6962
- Title: Families First Housing Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 6962
- Origin chamber: House
- Introduced date: 2026-01-07
- Update date: 2026-03-06T09:06:41Z
- Update date including text: 2026-03-06T09:06:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-07: Introduced in House
- 2026-01-07 - IntroReferral: Introduced in House
- 2026-01-07 - IntroReferral: Introduced in House
- 2026-01-07 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2026-01-07: Introduced in House

## Actions

- 2026-01-07 - IntroReferral: Introduced in House
- 2026-01-07 - IntroReferral: Introduced in House
- 2026-01-07 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-07",
    "latestAction": {
      "actionDate": "2026-01-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6962",
    "number": "6962",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "H001101",
        "district": "10",
        "firstName": "Pat",
        "fullName": "Rep. Harrigan, Pat [R-NC-10]",
        "lastName": "Harrigan",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Families First Housing Act of 2026",
    "type": "HR",
    "updateDate": "2026-03-06T09:06:41Z",
    "updateDateIncludingText": "2026-03-06T09:06:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-07",
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
      "actionDate": "2026-01-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-07",
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
          "date": "2026-01-07T15:01:45Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "NY"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
      "state": "NM"
    },
    {
      "bioguideId": "B001321",
      "district": "7",
      "firstName": "Tom",
      "fullName": "Rep. Barrett, Tom [R-MI-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrett",
      "party": "R",
      "sponsorshipDate": "2026-01-30",
      "state": "MI"
    },
    {
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "GU"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "CO"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "MI"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "CA"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "ME"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-02-23",
      "state": "NY"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6962ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 6962\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 7, 2026 Mr. Harrigan (for himself and Mr. Riley of New York ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo strengthen and standardize first look protections for covered properties to ensure families and communities have priority access to foreclosed homes, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Families First Housing Act of 2026 .\n#### 2. First look protections\n##### (a) In general\nEach covered entity shall ensure, when selling an eligible property, that the eligible property is only available for purchase by qualified first look buyers during the 180 day period beginning on the date that the eligible property is listed for sale.\n##### (b) Pricing of eligible properties\n**(1) In general**\nDuring the 180 day period beginning on the date that the eligible property is listed for sale during which an eligible property is only available for purchase by qualified first look buyers the eligible property shall be offered by the covered entity at a price that is the fair market value of the property as determined by an independent third-party appraisal or broker price opinion not more than 60 days before the date on which the property was listed for sale.\n**(2) Exception**\nIf the covered entity selling the eligible property determines that the fair market value of the property can not be determined by an independent third-party appraisal or broker price opinion not more than 60 days before the date on which the property was listed for sale the covered entity may offer the covered property at a price based on a standardized valuation model used by the covered entity if the covered entity publically discloses the methodology used by such standardized valuation model.\n##### (c) Listing on public website\nDuring the 180-day period beginning on the date that the eligible property is listed for sale during which an eligible property is only available for purchase by qualified first look buyers the eligible property shall be listed on a publically accessible website by the covered entity in a manner that identifies the eligible property as only available for purchase by qualified first look buyers and indicates how many days remain in the 180-day period during which the eligible property is only available for purchase by qualified first look buyers.\n##### (d) Prohibition on bundling\nAn eligible entity may not bundle eligible properties during the 180 day period beginning on the date that the eligible property is listed for sale by the eligible entity.\n##### (e) Publication of information\nEach covered entity shall, each quarter, publish on a website of the covered entity, information about\u2014\n**(1)**\nthe number of covered properties sold during the prior quarter;\n**(2)**\nthe number of covered properties sold to qualified first look buyers during the prior quarter;\n**(3)**\nthe number of covered properties sold to institutional investors during the prior quarter;\n**(4)**\nthe pricing methodology used by the covered entity when selling covered properties; and\n**(5)**\nfor each covered property sold during the prior quarter, the ratio of the sale price to the fair market value of the covered property as determined by an independent third-party appraisal, broker price opinion, or standardized valuation model.\n##### (f) Annual report\n**(1) In general**\nThe Inspectors General of each covered entity shall, each year, review all sales of covered properties by the covered entity in the prior year and determine whether any provisions of this section were violated during such sale.\n**(2) Report**\nThe Inspectors General of each covered entity shall submit a report to the Congress each year that includes the results of the review conducted under paragraph (1).\n**(3) Public publication**\nThe Inspectors General of each covered entity shall publish the report submitted under paragraph (2) on a publically accessible website of the covered entity.\n##### (g) Violations\nIf the Secretary of Housing and Urban Development determines that a covered entity has violated this section, the Secretary of Housing and Urban Development may\u2014\n**(1)**\nrequire the covered entity to publically disclose the violation;\n**(2)**\nimpose a civil penalty of the greater of $100,000 or 1/3 of the price for which the covered property was sold on each employee of the covered entity involved in the violating transaction; and\n**(3)**\nrequire the covered entity, if practicable without breaching contracts, to reverse or unwind the transaction associated with the violation.\n##### (h) Rulemaking\nEach covered entity shall, not later than 180 days after the date of the enactment of this section, issue such rules are necessary to carry out this section and such rules shall include a process to verify the eligibility of qualified first look buyers.\n##### (i) Effective date\nThis section shall take effect 180 days after the date of the enactment of this Act.\n##### (j) Definitions\nIn this section:\n**(1) Covered property**\nThe term covered property means any single-family residential property made up of 1 to 4 units, owned, foreclosed upon, or under disposition by a covered entity.\n**(2) Covered entity**\nThe term covered entity means\u2014\n**(A)**\nthe Federal Housing Administration;\n**(B)**\nthe Federal Housing Finance Agency;\n**(C)**\nthe Federal National Mortgage Association;\n**(D)**\nthe Federal Home Loan Mortgage Corporation; and\n**(E)**\nthe Department of Agriculture.\n**(3) Institutional Investor**\nThe term institutional investor means any entity that purchases properties for rental, resale, or investment purposes, including trusts, corporations, real estate investment trusts, limited liability companies, and partnerships.\n**(4) Qualified First Look Buyer**\nThe term qualified first look buyer means\u2014\n**(A)**\na natural person intending to occupy the property as their primary residence;\n**(B)**\na nonprofit housing organization which is an organization described in section 501(c)(3) of the Internal Revenue Code of 1986 and is exempt from taxation under section 501(a) of such Code;\n**(C)**\na unit of local government; or\n**(D)**\na community land trust.",
      "versionDate": "2026-01-07",
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
        "updateDate": "2026-01-22T15:31:45Z"
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
      "date": "2026-01-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6962ih.xml"
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
      "title": "Families First Housing Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-21T11:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Families First Housing Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-21T11:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To strengthen and standardize \"first look\" protections for covered properties to ensure families and communities have priority access to foreclosed homes, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-21T11:18:30Z"
    }
  ]
}
```
