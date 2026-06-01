# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/439?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/439
- Title: Incentivizing Readiness and Environmental Protection Integration Sales Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 439
- Origin chamber: Senate
- Introduced date: 2025-02-06
- Update date: 2026-05-12T11:03:31Z
- Update date including text: 2026-05-12T11:03:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-06: Introduced in Senate
- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-02-06: Introduced in Senate

## Actions

- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-06",
    "latestAction": {
      "actionDate": "2025-02-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/439",
    "number": "439",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "B001305",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Budd, Ted [R-NC]",
        "lastName": "Budd",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Incentivizing Readiness and Environmental Protection Integration Sales Act of 2025",
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
      "actionDate": "2025-02-06",
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
      "actionDate": "2025-02-06",
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
            "date": "2025-02-06T15:22:21Z",
            "name": "Referred To"
          },
          {
            "date": "2025-02-06T15:22:21Z",
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
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "VA"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-04-29",
      "state": "NC"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "GA"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "GA"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2026-05-11",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s439is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 439\nIN THE SENATE OF THE UNITED STATES\nFebruary 6 (legislative day, February 5), 2025 Mr. Budd (for himself and Mr. Kaine ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to exclude from gross income gain from the sale of qualified real property interests acquired under the authority of the Readiness and Environmental Protection Integration (REPI) program administered by the Department of Defense pursuant to section 2684a of title 10, United States Code, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Incentivizing Readiness and Environmental Protection Integration Sales Act of 2025 .\n#### 2. Exclusion of gain from sale of qualified real property interests acquired for purposes related to the readiness and environmental protection integration program\n##### (a) In general\nPart III of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 139I the following new section:\n139J. Gain from sale of qualified real property interest for purposes related to the readiness and environmental protection integration program (a) In general Gross income shall not include any gain from the sale of qualified real property interest to a qualified organization for REPI purposes. (b) Definitions For purposes of this section\u2014 (1) Qualified real property interest (A) In general The term qualified real property interest means any of the following interests in real property: (i) The entire interest of the taxpayer. (ii) A remainder interest. (iii) A restriction (granted in perpetuity and created pursuant to State real property law) on the use which may be made of the real property. (B) Special rule for mineral interests An interest in real property shall not fail to be treated as a qualified real property interest solely by reason of a retention of a qualified mineral interest (as defined in section 170(h)(6)), but only if the right to access such mineral interest is not accomplished by any surface mining method. (2) Qualified organization The term qualified organization has the meaning given such term by section 170(h)(3). (3) REPI purposes A sale of qualified real property interest shall be treated as being for REPI purposes if such sale is pursuant to the authority of the Readiness and Environmental Protection Integration (REPI) program administered by the Department of Defense under section 2684a of title 10, United States Code. (c) Limitation (1) In general In the case of a pass-through entity, no amount shall be excluded from gross income under subsection (a) with respect to a sale if such entity acquired the qualified real property interest by sale within 3 years of the date of the sale described in subsection (a). (2) Exception for family partnerships or family pass-through entities (A) In general Paragraph (1) shall not apply with respect to any sale made by any partnership if substantially all of the partnership interests in such partnership are held, directly or indirectly, by an individual and members of the family of such individual. (B) Members of the family For purposes of this paragraph, the term members of the family means, with respect to any individual\u2014 (i) the spouse of such individual, and (ii) any individual who bears a relationship to such individual which is described in subparagraphs (A) through (G) of section 152(d)(2). (C) Application to other pass-through entities Except as may be otherwise provided by the Secretary, the rules of this paragraph shall apply to S corporations and other pass-through entities in the same manner as such rules apply to partnerships. .\n##### (b) Clerical amendment\nThe table of sections for part III of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after the item relating to section 139I the following new item:\nSec. 139J. Gain from sale of qualified real property interest for purposes related to the readiness and environmental protection integration program. .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after the date of the enactment of this Act.",
      "versionDate": "2025-02-06",
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
        "actionDate": "2025-02-06",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "1083",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Incentivizing Readiness and Environmental Protection Integration Sales Act of 2025",
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
        "updateDate": "2025-05-05T16:02:47Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-06",
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
          "measure-id": "id119s439",
          "measure-number": "439",
          "measure-type": "s",
          "orig-publish-date": "2025-02-06",
          "originChamber": "SENATE",
          "update-date": "2026-04-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s439v00",
            "update-date": "2026-04-08"
          },
          "action-date": "2025-02-06",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Incentivizing Readiness and Environmental Protection Integration Sales Act of 2025\u00a0</strong></p><p>This bill excludes the gain from the sale of a qualified real property interest under\u00a0the Readiness and Environmental Protection Integration (REPI) Program from gross income for federal tax purposes. (Some limitations apply.)</p><p>As background, the REPI Program supports cost-sharing agreements between the Armed Forces, other federal agencies, state and local governments, and certain private organizations to address land use near military installations, address environmental restrictions that limit military activities, and increase military installation resilience.</p><p>Under the bill, the exclusion from gross income applies to gain from the sale of a real property interest (pursuant to an agreement under the REPI Program) to</p><ul><li>a state or U.S. possession (or a political subdivision of a state or U.S. possession) or the District of Columbia;</li><li>the United States;</li><li>certain corporations, trusts, community chest, funds, or foundations; or</li><li>certain charitable organizations.</li></ul><p>Further, under the bill, the real property interest that is sold may be (1) the entire interest in the real property, (2) a remainder interest in the real property, or (3) a restriction on the use of the real property (e.g., easement) that is granted in perpetuity and created under state law.</p><p>However, the bill limits such exclusion from gross income for a partnership or other pass-through entity (other than a family partnership or family pass-through entity) to gain from the sale of a real property interest that is held for at least three years.</p>"
        },
        "title": "Incentivizing Readiness and Environmental Protection Integration Sales Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s439.xml",
    "summary": {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Incentivizing Readiness and Environmental Protection Integration Sales Act of 2025\u00a0</strong></p><p>This bill excludes the gain from the sale of a qualified real property interest under\u00a0the Readiness and Environmental Protection Integration (REPI) Program from gross income for federal tax purposes. (Some limitations apply.)</p><p>As background, the REPI Program supports cost-sharing agreements between the Armed Forces, other federal agencies, state and local governments, and certain private organizations to address land use near military installations, address environmental restrictions that limit military activities, and increase military installation resilience.</p><p>Under the bill, the exclusion from gross income applies to gain from the sale of a real property interest (pursuant to an agreement under the REPI Program) to</p><ul><li>a state or U.S. possession (or a political subdivision of a state or U.S. possession) or the District of Columbia;</li><li>the United States;</li><li>certain corporations, trusts, community chest, funds, or foundations; or</li><li>certain charitable organizations.</li></ul><p>Further, under the bill, the real property interest that is sold may be (1) the entire interest in the real property, (2) a remainder interest in the real property, or (3) a restriction on the use of the real property (e.g., easement) that is granted in perpetuity and created under state law.</p><p>However, the bill limits such exclusion from gross income for a partnership or other pass-through entity (other than a family partnership or family pass-through entity) to gain from the sale of a real property interest that is held for at least three years.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119s439"
    },
    "title": "Incentivizing Readiness and Environmental Protection Integration Sales Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Incentivizing Readiness and Environmental Protection Integration Sales Act of 2025\u00a0</strong></p><p>This bill excludes the gain from the sale of a qualified real property interest under\u00a0the Readiness and Environmental Protection Integration (REPI) Program from gross income for federal tax purposes. (Some limitations apply.)</p><p>As background, the REPI Program supports cost-sharing agreements between the Armed Forces, other federal agencies, state and local governments, and certain private organizations to address land use near military installations, address environmental restrictions that limit military activities, and increase military installation resilience.</p><p>Under the bill, the exclusion from gross income applies to gain from the sale of a real property interest (pursuant to an agreement under the REPI Program) to</p><ul><li>a state or U.S. possession (or a political subdivision of a state or U.S. possession) or the District of Columbia;</li><li>the United States;</li><li>certain corporations, trusts, community chest, funds, or foundations; or</li><li>certain charitable organizations.</li></ul><p>Further, under the bill, the real property interest that is sold may be (1) the entire interest in the real property, (2) a remainder interest in the real property, or (3) a restriction on the use of the real property (e.g., easement) that is granted in perpetuity and created under state law.</p><p>However, the bill limits such exclusion from gross income for a partnership or other pass-through entity (other than a family partnership or family pass-through entity) to gain from the sale of a real property interest that is held for at least three years.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119s439"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s439is.xml"
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
      "title": "Incentivizing Readiness and Environmental Protection Integration Sales Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-12T11:03:31Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Incentivizing Readiness and Environmental Protection Integration Sales Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:38:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to exclude from gross income gain from the sale of qualified real property interests acquired under the authority of the Readiness and Environmental Protection Integration (REPI) program administered by the Department of Defense pursuant to section 2684a of title 10, United States Code, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:33:35Z"
    }
  ]
}
```
