# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4185?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4185
- Title: Stop Subsidizing Giant Mergers Act
- Congress: 119
- Bill type: S
- Bill number: 4185
- Origin chamber: Senate
- Introduced date: 2026-03-25
- Update date: 2026-04-09T16:42:46Z
- Update date including text: 2026-04-09T16:42:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-25: Introduced in Senate
- 2026-03-25 - IntroReferral: Introduced in Senate
- 2026-03-25 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-03-25: Introduced in Senate

## Actions

- 2026-03-25 - IntroReferral: Introduced in Senate
- 2026-03-25 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-25",
    "latestAction": {
      "actionDate": "2026-03-25",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4185",
    "number": "4185",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "W000802",
        "district": "",
        "firstName": "Sheldon",
        "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
        "lastName": "Whitehouse",
        "party": "D",
        "state": "RI"
      }
    ],
    "title": "Stop Subsidizing Giant Mergers Act",
    "type": "S",
    "updateDate": "2026-04-09T16:42:46Z",
    "updateDateIncludingText": "2026-04-09T16:42:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-25",
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
      "actionDate": "2026-03-25",
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
          "date": "2026-03-25T16:19:00Z",
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
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2026-03-25",
      "state": "MO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4185is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4185\nIN THE SENATE OF THE UNITED STATES\nMarch 25, 2026 Mr. Whitehouse (for himself and Mr. Hawley ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to end the tax-free treatment of certain corporate reorganizations that involve large corporations.\n#### 1. Short title\nThis Act may be cited as the Stop Subsidizing Giant Mergers Act .\n#### 2. Modification of rules relating to corporate reorganizations for certain large corporations\n##### (a) Acquisitive reorganizations\nSection 368(a)(2) of the Internal Revenue Code of 1986 is amended by adding at the end the following new subparagraph:\n(I) Special rules with respect to certain acquisitive reorganizations described in paragraph (1)(A), (1)(B), (1)(C), and (1)(D) (i) In general A merger, consolidation, acquisition, or transfer which is described in clause (ii) shall not be treated as a merger, consolidation, acquisition, or transfer described in paragraph (1)(A), (1)(B), (1)(C), or (1)(D). (ii) Transactions described A merger, consolidation, acquisition, or transfer is described in this clause if\u2014 (I) such merger, consolidation, acquisition, or transfer is, or is treated as, the acquisition of the stock or assets of another corporation, (II) such merger, consolidation, acquisition, or transfer is not excepted under clause (iii), and (III) the combined average annual gross receipts of the acquiring corporation and the acquired corporation for the 3-taxable year period which precedes the taxable year in which the merger, consolidation, acquisition, or transfer is completed exceeds $500,000,000. (iii) Exceptions A merger, consolidation, acquisition, or transfer is excepted under this clause if\u2014 (I) either the acquiring corporation or the acquired corporation controls the other immediately before (and, if both corporations continue to exist, after) the merger, consolidation, acquisition, or transfer (as the case may be), (II) any other corporation controls both the acquiring corporation and the acquired corporation immediately before (and, if both corporations continue to exist, after) the merger, consolidation, acquisition, or transfer (as the case may be), or (III) either the acquiring corporation or the acquired corporation meets the gross receipts test of section 448(c)(1) for the taxable year in which the merger, consolidation, acquisition, or transfer is completed. (iv) Aggregation and other special rules Rules similar to the rules of paragraphs (2) and (3) of section 448(c) shall apply for purposes of clause (i)(II), except that (unless otherwise provided by the Secretary) the rules of section 448(c)(2) shall not apply in determining the average annual gross receipts of the acquired corporation. (v) Inflation adjustment In the case of any taxable year beginning after 2026, the dollar amount in clause (ii)(III) shall be increased by an amount equal to\u2014 (I) such dollar amount, multiplied by (II) the cost-of-living adjustment determined under section 1(f)(3) for the calendar year in which such taxable year begins, determined by substituting calendar year 2025 for calendar year 2016 in subparagraph (A)(ii) thereof. If any amount as increased under the preceding sentence is not a multiple of $1,000,000, such amount shall be rounded to the nearest multiple of $1,000,000. (vi) Regulations and guidance The Secretary may prescribe such regulations and other guidance as are necessary or appropriate to carry out, and to prevent the abuse of the purposes of, this subparagraph, including rules\u2014 (I) to prevent the avoidance of the application of this subparagraph through the use of a series of transactions designed and executed as parts of a unitary plan, and (II) for the nonapplication of the rules of clause (i) where such nonapplication is consistent with the purposes of this subparagraph. .\n##### (b) Transfers to corporations controlled by transferors\nSection 351 is amended by redesignating subsection (h) as subsection (i) and by inserting after subsection (g) the following new subsection:\n(h) Special rule with respect to multiple transferors (1) In general Subsection (a) shall not apply to any transfer of property by two or more persons which are corporations if the combined average annual gross receipts of such persons for the 3-taxable year period which precedes the taxable year of the transfer exceeds $500,000,000. (2) Exception Clause (i) shall not apply if\u2014 (A) such persons control the corporation to which the property is transferred immediately before the transfer, (B) another corporation controls all such persons and the corporation to which the property is transferred immediately before the transfer, or (C) all such persons meet the gross receipts test of section 448(c)(1) for the taxable year in which the transfer is made. (3) Aggregation and other special rules Rules similar to the rules of paragraphs (2) and (3) of section 448(c) shall apply for purposes of paragraph (1). (4) Inflation adjustment In the case of any taxable year beginning after 2026, the dollar amount in paragraph (1) shall be increased by an amount equal to\u2014 (A) such dollar amount, multiplied by (B) the cost-of-living adjustment determined under section 1(f)(3) for the calendar year in which such taxable year begins, determined by substituting calendar year 2025 for calendar year 2016 in subparagraph (A)(ii) thereof. If any amount as increased under the preceding sentence is not a multiple of $1,000,000, such amount shall be rounded to the nearest multiple of $1,000,000. (5) Regulations and guidance The Secretary may prescribe such regulations and other guidance as are necessary or appropriate to carry out, and to prevent the abuse of the purposes of, this subparagraph, including rules\u2014 (A) to prevent the avoidance of the application of this subsection through the use of a series of transactions designed and executed as parts of a unitary plan, and (B) for the nonapplication of the rules of paragraph (1) where such nonapplication is consistent with the purposes of this subsection. .\n##### (c) Effective date\nThe amendments made by this section shall apply to transfers after the date of the enactment of this Act.",
      "versionDate": "2026-03-25",
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
        "name": "Taxation",
        "updateDate": "2026-04-09T16:42:46Z"
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
      "date": "2026-03-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4185is.xml"
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
      "title": "Stop Subsidizing Giant Mergers Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-03T05:38:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Stop Subsidizing Giant Mergers Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-03T05:38:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to end the tax-free treatment of certain corporate reorganizations that involve large corporations.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-03T05:33:26Z"
    }
  ]
}
```
