# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4021?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4021
- Title: Promoting Reduction of Emissions through Landscaping Equipment Act
- Congress: 119
- Bill type: S
- Bill number: 4021
- Origin chamber: Senate
- Introduced date: 2026-03-05
- Update date: 2026-03-24T01:40:24Z
- Update date including text: 2026-03-24T01:40:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-05: Introduced in Senate
- 2026-03-05 - IntroReferral: Introduced in Senate
- 2026-03-05 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-03-05: Introduced in Senate

## Actions

- 2026-03-05 - IntroReferral: Introduced in Senate
- 2026-03-05 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-05",
    "latestAction": {
      "actionDate": "2026-03-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4021",
    "number": "4021",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "H001046",
        "district": "",
        "firstName": "Martin",
        "fullName": "Sen. Heinrich, Martin [D-NM]",
        "lastName": "Heinrich",
        "party": "D",
        "state": "NM"
      }
    ],
    "title": "Promoting Reduction of Emissions through Landscaping Equipment Act",
    "type": "S",
    "updateDate": "2026-03-24T01:40:24Z",
    "updateDateIncludingText": "2026-03-24T01:40:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-05",
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
      "actionDate": "2026-03-05",
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
          "date": "2026-03-05T21:10:26Z",
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
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4021is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4021\nIN THE SENATE OF THE UNITED STATES\nMarch 5, 2026 Mr. Heinrich (for himself and Mr. Schiff ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to establish a business tax credit for the purchase of zero-emission electric lawn, garden, and landscape equipment, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Promoting Reduction of Emissions through Landscaping Equipment Act .\n#### 2. Tax credit for zero-emission electric lawn, garden, and landscape equipment\n##### (a) In general\nSubpart E of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 48E the following new section:\n48F. Zero-emission electric lawn, garden, and landscape equipment credit (a) In general For purposes of section 46, the credit for zero-emission electric lawn, garden, and landscape equipment for any taxable year is an amount equal to 40 percent of the basis of any zero-emission electric lawn, garden, and landscape equipment placed in service by the taxpayer during such taxable year. (b) Limitations (1) Annual limitation The amount of any credit determined under subsection (a) for any taxable year may not exceed $25,000. (2) Aggregate limitation The aggregate amount of credits determined under subsection (a) for all taxable years within any consecutive 10-year period may not exceed $100,000. (c) Zero-Emission electric lawn, garden, and landscape equipment For purposes of this section, the term zero-emission electric lawn, garden, and landscape equipment means\u2014 (1) any equipment which\u2014 (A) is\u2014 (i) used primarily for lawn, garden, or landscaping purposes, and (ii) powered\u2014 (I) by an electric motor drawing current from solar power, chargeable batteries, replaceable batteries, fuel cells, or through electricity drawn through a cord from the electrical power grid, or (II) by such alternative power sources as the Secretary may identify as generating zero-emissions, and (B) is not powered\u2014 (i) by a gasoline or diesel generator, or (ii) solely through manual effort, (2) any zero-emission generator used to charge equipment described in paragraph (1), (3) any battery which\u2014 (A) is used to charge or operate equipment described in paragraph (1), and (B) is not included as part of such equipment, and (4) any property used to retrofit existing lawn, garden, or landscaping equipment to allow such equipment to operate without generating emissions. (d) Collaboration with Department of Energy For purposes of identifying alternative power sources under subsection (c)(1)(A)(ii)(II), the Secretary may consult with the Secretary of Energy. (e) Product identification number requirement With respect to any zero-emission electric lawn, garden, and landscape equipment placed in service after December 31, 2025, rules similar to the rules of section 25C(h) shall apply for purposes of this section. (f) Denial of double benefit (1) In general No credit shall be allowed under subsection (a) with respect to any property for which a deduction or credit is allowed under any other provision of this chapter. (2) Exception Paragraph (1) shall not apply with respect to any deduction allowed under section 167(a) to which section 168(k) applies for the taxable year in which the property is placed in service. (g) Exception from recapture in event of bankruptcy or business dissolution With respect to any zero-emission electric lawn, garden, and landscape equipment for which a credit was determined under subsection (a), section 50(a)(1) shall not apply if such equipment is disposed of, or otherwise ceases to be investment credit property with respect to the taxpayer, due to\u2014 (1) the dissolution or bankruptcy of the trade or business in which such equipment was used, or (2) any other circumstances as the Secretary may prescribe in regulations. (h) Termination This section shall not apply with respect to any property placed in service during any taxable year beginning after the date which is 5 years after the date of enactment of this section. .\n##### (b) Elective payment and transfer of credit\n**(1) Elective payment**\nSection 6417(b) of the Internal Revenue Code of 1986 is amended by adding at the end the following:\n(13) The credit for zero-emission electric lawn, garden, and landscape equipment under section 48F. .\n**(2) Transfer**\nSection 6418(f)(1)(A) of the Internal Revenue Code of 1986, as amended by section 70521 of Public Law 119\u201321 , is amended by adding at the end the following:\n(xiii) The credit for zero-emission electric lawn, garden, and landscape equipment under section 48F. .\n##### (c) Conforming amendments\n**(1)**\nSection 46 of the Internal Revenue Code of 1986, as amended by section 13702 of Public Law 117\u2013169 , is amended\u2014\n**(A)**\nin paragraph (6), by striking and at the end,\n**(B)**\nin paragraph (7), by striking the period at the end and inserting , and , and\n**(C)**\nby adding at the end the following:\n(8) the credit for zero-emission electric lawn, garden, and landscape equipment. .\n**(2)**\nSection 49(a)(1)(C) of such Code, as amended by section 13702 of Public Law 117\u2013169 , is amended\u2014\n**(A)**\nin clause (vii), by striking and at the end,\n**(B)**\nin clause (viii), by striking the period at the end and inserting , and , and\n**(C)**\nby adding at the end the following:\n(ix) the basis of any zero-emission electric lawn, garden, and landscape equipment under section 48F. .\n##### (d) Clerical amendment\nThe table of sections for subpart E of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after the item relating to section 48E the following new item:\nSec. 48F. Zero-emission electric lawn, garden, and landscape equipment credit. .\n##### (e) Effective date\nThe amendments made by this section shall apply to property placed in service after December 31, 2024.",
      "versionDate": "2026-03-05",
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
        "actionDate": "2026-03-05",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "7821",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Promoting Reduction of Emissions through Landscaping Equipment Act",
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
        "updateDate": "2026-03-24T01:06:58Z"
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
      "date": "2026-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4021is.xml"
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
      "title": "Promoting Reduction of Emissions through Landscaping Equipment Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-20T02:23:29Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Promoting Reduction of Emissions through Landscaping Equipment Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-20T02:23:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to establish a business tax credit for the purchase of zero-emission electric lawn, garden, and landscape equipment, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-20T02:18:27Z"
    }
  ]
}
```
