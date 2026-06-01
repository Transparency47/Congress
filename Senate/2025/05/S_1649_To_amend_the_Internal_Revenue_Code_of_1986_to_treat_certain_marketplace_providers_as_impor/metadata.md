# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1649?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1649
- Title: Sporting Goods Excise Tax Modernization Act
- Congress: 119
- Bill type: S
- Bill number: 1649
- Origin chamber: Senate
- Introduced date: 2025-05-07
- Update date: 2026-05-12T11:03:31Z
- Update date including text: 2026-05-12T11:03:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-07: Introduced in Senate
- 2025-05-07 - IntroReferral: Introduced in Senate
- 2025-05-07 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-05-07: Introduced in Senate

## Actions

- 2025-05-07 - IntroReferral: Introduced in Senate
- 2025-05-07 - IntroReferral: Read twice and referred to the Committee on Finance.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1649",
    "number": "1649",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "T000278",
        "district": "",
        "firstName": "Tommy",
        "fullName": "Sen. Tuberville, Tommy [R-AL]",
        "lastName": "Tuberville",
        "party": "R",
        "state": "AL"
      }
    ],
    "title": "Sporting Goods Excise Tax Modernization Act",
    "type": "S",
    "updateDate": "2026-05-12T11:03:31Z",
    "updateDateIncludingText": "2026-05-12T11:03:31Z"
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
        "item": [
          {
            "date": "2025-05-07T20:43:24Z",
            "name": "Referred To"
          },
          {
            "date": "2025-05-07T20:43:24Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "ID"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "GA"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-10-06",
      "state": "WY"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "False",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "WY"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "NV"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "False",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2026-05-11",
      "state": "KS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1649is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1649\nIN THE SENATE OF THE UNITED STATES\nMay 7, 2025 Mr. Tuberville (for himself and Mr. Crapo ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to treat certain marketplace providers as importers for purposes of the excise tax on sporting goods.\n#### 1. Short title\nThis Act may be cited as the Sporting Goods Excise Tax Modernization Act .\n#### 2. Certain marketplace providers treated as importers for purposes of the excise tax on sporting goods\n##### (a) In general\nSection 4162 of the Internal Revenue Code of 1986 is amended by adding at the end the following new subsection:\n(c) Certain marketplace providers treated as importers (1) In general In the case of any specified marketplace sale of a taxable sporting good article, the marketplace provider with respect to such sale shall be treated for purposes of section 4161 as the importer and seller of such article. (2) Specified marketplace sale For purposes of this subsection, the term specified marketplace sale means, with respect to any article, any sale if\u2014 (A) a marketplace provider provides the services described in subparagraphs (A) and (B) of paragraph (3) with respect to such sale, (B) such article is transported to the United States from outside the United States in connection with (including in anticipation of) a sale of such article, and (C) the manufacturer of such article is not the marketplace provider referred to in subparagraph (A). (3) Marketplace provider For purposes of this subsection, the term marketplace provider means any person in the trade or business of\u2014 (A) hosting or facilitating listings, or advertisements, of products for sale, and (B) collecting gross receipts from the purchaser and transmitting any portion of such receipts to the seller. (4) Treatment of related persons For purposes of this subsection, related persons (within the meaning of subsection (b)(3)) shall be treated as one person for purposes of applying paragraphs (2) and (3). (5) Taxable sporting good article For purposes of this subsection, the term taxable sporting good article means any article of a type subject to tax under section 4161. (6) Exception if tax would otherwise be imposed on person other than purchaser Paragraph (1) shall not apply with respect to any sale if tax under section 4161 would (without regard to paragraph (1)) be imposed on a person other than the purchaser with respect to such sale. (7) Regulations The Secretary shall issue such regulations or other guidance as may be necessary or appropriate to carry out the purposes of this subsection, including regulations or other guidance specifying, in the case of the application of paragraph (4), the taxpayer treated as the marketplace provider for purposes of paragraph (1). .\n##### (b) Effective date\nThe amendment made by this section shall apply to sales during calendar quarters beginning after the date that is 60 days after the date of the enactment of this Act.\n##### (c) No inference\nSection 4162(c) of the Internal Revenue Code of 1986 shall not be applied or interpreted as creating any inference with respect to whether any person not treated as an importer under such section is nonetheless properly treated an importer for purposes of section 4161.",
      "versionDate": "2025-05-07",
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
        "actionDate": "2025-02-21",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "1494",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Sporting Goods Excise Tax Modernization Act",
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
        "name": "Taxation",
        "updateDate": "2025-06-06T18:10:18Z"
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
      "date": "2025-05-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1649is.xml"
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
      "title": "Sporting Goods Excise Tax Modernization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-12T11:03:31Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Sporting Goods Excise Tax Modernization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-21T04:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to treat certain marketplace providers as importers for purposes of the excise tax on sporting goods.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-21T04:03:46Z"
    }
  ]
}
```
