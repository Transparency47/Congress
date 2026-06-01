# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1979?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1979
- Title: Rare Earth Magnet Security Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1979
- Origin chamber: Senate
- Introduced date: 2025-06-05
- Update date: 2026-01-10T07:14:34Z
- Update date including text: 2026-01-10T07:14:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-05: Introduced in Senate
- 2025-06-05 - IntroReferral: Introduced in Senate
- 2025-06-05 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-06-05: Introduced in Senate

## Actions

- 2025-06-05 - IntroReferral: Introduced in Senate
- 2025-06-05 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-05",
    "latestAction": {
      "actionDate": "2025-06-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1979",
    "number": "1979",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "C001113",
        "district": "",
        "firstName": "Catherine",
        "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
        "lastName": "Cortez Masto",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Rare Earth Magnet Security Act of 2025",
    "type": "S",
    "updateDate": "2026-01-10T07:14:34Z",
    "updateDateIncludingText": "2026-01-10T07:14:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-05",
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
      "actionDate": "2025-06-05",
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
          "date": "2025-06-05T17:59:21Z",
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
      "bioguideId": "M001190",
      "firstName": "Markwayne",
      "fullName": "Sen. Mullin, Markwayne [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "OK"
    },
    {
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "SC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1979is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1979\nIN THE SENATE OF THE UNITED STATES\nJune 5, 2025 Ms. Cortez Masto (for herself, Mr. Mullin , and Mr. Graham ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to establish a credit for the domestic production of high-performance rare earth magnets, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Rare Earth Magnet Security Act of 2025 .\n#### 2. Credit for production of rare earth magnets\n##### (a) In general\nThe Internal Revenue Code of 1986 is amended by inserting the following new section after section 45AA:\n45BB. Credit for production of rare earth magnets (a) In general (1) Allowance of credit For purposes of section 38, the credit for production of rare earth magnets determined under this section for any taxable year is an amount equal to the sum of the credit amounts determined under subsection (b) with respect to rare earth magnets which are\u2014 (A) manufactured or produced by the taxpayer, and (B) sold by such taxpayer to an unrelated person during the taxable year. (2) Unrelated person (A) In general For purposes of this subsection, a taxpayer shall be treated as selling rare earth magnets to an unrelated person if such magnet is sold to such person by a person related to the taxpayer. (B) Election (i) In general At the election of the taxpayer (in such form and manner as the Secretary may prescribe), a sale of rare earth magnets by such taxpayer to a related person shall be deemed to have been made to an unrelated person. (ii) Requirement As a condition of, and prior to, any election described in clause (i), the Secretary may require such information or registration as the Secretary deems necessary for purposes of preventing duplication, fraud, or any improper or excessive amount determined under paragraph (1). (b) Credit amount (1) In general The amount determined under this subsection is\u2014 (A) $20 per kilogram of rare earth magnets manufactured or produced in the United States by the taxpayer during the taxable year, and (B) $30 per kilogram of rare earth magnets manufactured or produced in the United States by the taxpayer during the taxable year if not less than 90 percent by weight of the component rare earth materials of such magnets are produced within the United States. (2) Phase-Out (A) In general In the case of any rare earth magnet manufactured or produced after December 31, 2034, the amount determined under this section with respect to such rare earth magnet shall be equal to the product of\u2014 (i) the amount determined under paragraph (1) with respect to such rare earth magnet, as determined without regard to this subsection, multiplied by (ii) the phase-out percentage described in subparagraph (B). (B) Phase-out percentage The phase-out percentage described in this paragraph is\u2014 (i) in the case of any rare earth magnet manufactured or produced in calendar year 2035, 70 percent, (ii) in the case of any rare earth magnet manufactured or produced in calendar year 2036 or 2037, 35 percent, or (iii) in the case of any rare earth magnet manufactured or produced after December 31, 2037, 0 percent. (c) Definitions For the purposes of this section\u2014 (1) Rare earth magnet The term rare earth magnet means a permanent magnet\u2014 (A) with an intrinsic coercivity (HCj) of 10 kOe or higher at 68 \u00b0F (20 \u00b0C), and (B) comprised of\u2014 (i) an alloy of neodymium, iron, and boron, which may also include praseodymium, terbium, or dysprosium, or (ii) an alloy of samarium and cobalt, which may also include gadolinium or any associated host mineral of a component rare earth material. (2) Component rare earth material The term component rare earth material means neodymium, praseodymium, dysprosium, terbium, samarium, gadolinium, and cobalt. (3) Manufactured The term manufactured means the manufacturing of a rare earth magnet, including the milling, pressing, sintering, and recycling of component rare earth material. (4) Non-allied foreign nation The term non-allied foreign nation has the meaning given to the term covered nation in section 4872(f) of title 10, United States Code. (5) United States and possession of the United States The terms United States and possession of the United States have the meaning given such terms in section 638. (d) Special rules (1) Restriction on component sourcing (A) In general Except as provided in subparagraph (B) or (C), no credit shall be allowed under this section with respect to a rare earth magnet if any component rare earth material used to manufacture or produce such magnet is produced in a non-allied foreign nation. (B) Delayed restriction for certain component rare earth materials In the case of the rare earth materials dysprosium, terbium, samarium, and gadolinium, the restriction under subparagraph (A) shall not apply to magnets manufactured or produced using such materials before January 1, 2027. (C) Material seized from non-allied foreign nation during wartime (i) In general Subparagraph (A) shall not apply with respect to any component rare earth material which is seized from a non-allied foreign nation during wartime by\u2014 (I) Ukraine, or (II) an allied country. (ii) Certification For purposes of this subparagraph, the taxpayer which manufactured or produced the rare earth magnet shall certify to the Secretary (at such time, and in such form and manner, as the Secretary may prescribe) that the component rare earth material used to manufacture or produce such magnet satisfies the requirements described in clause (i). (iii) Allied country For purposes of this subparagraph, the term allied country means any of the following: (I) A country that is a member of the North Atlantic Treaty Organization. (II) Australia, New Zealand, Japan, and the Republic of Korea. (III) Any other country designated as an allied country for the purposes of this subparagraph by the Secretary (with the concurrence of the Secretary of State and the Secretary of Defense). (2) Trade or business requirement No credit shall be allowed under this section with respect to a rare earth magnet unless such magnet is manufactured or produced in the ordinary course of a trade or business of the taxpayer. (3) Coercivity requirement exception for eligible manufacturers (A) In general The Secretary may elect to treat a magnet which does not meet the coercivity requirements of subsection (c)(1)(A) as a rare earth magnet if such magnet is manufactured by an eligible manufacturer. (B) Eligible manufacturer For purposes of subparagraph (A), the term eligible manufacturer means a manufacturer that\u2014 (i) receives a grant from, or is contracted by, the Department of Energy or the Department of Defense to produce a magnet, and (ii) commits to place in service a domestic manufacturing facility that produces magnets that the Secretary determines to demonstrate national security merit. (e) Elective payment for production of rare earth magnets (1) In general In the case of a taxpayer making an election (at such time and in such manner as the Secretary may provide) under this section with respect to any portion of the credit allowed under subsection (a), such taxpayer shall be treated as making a payment against the tax imposed by this subtitle for the taxable year equal to the amount of such portion. (2) Timing The payment described in paragraph (1) shall be treated as made on the later of the due date of the return of tax for such taxable year or the date on which such return is filed. .\n##### (b) Credit To be part of general business credit\nSection 38(b) of such Code is amended by striking plus at the end of paragraph (40), by striking the period at the end of paragraph (41) and inserting , plus , and by adding at the end the following new paragraph:\n(42) the credit for production of rare earth magnets determined under section 45BB(a). .\n##### (c) Conforming amendment\nThe table of sections for subpart D of part IV of subchapter A of chapter 1 of such Code is amended by inserting after the item relating to section 45AA the following new item:\nSec. 45BB. Credit for production of rare earth magnets. .\n##### (d) Effective date\nThe amendments made by this Act shall apply to taxable years beginning after December 31, 2024.",
      "versionDate": "2025-06-05",
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
      "number": "1496",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Rare Earth Magnet Security Act of 2025",
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
        "updateDate": "2025-07-17T20:06:55Z"
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
      "date": "2025-06-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1979is.xml"
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
      "title": "Rare Earth Magnet Security Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-19T03:38:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Rare Earth Magnet Security Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-19T03:38:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to establish a credit for the domestic production of high-performance rare earth magnets, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-19T03:33:16Z"
    }
  ]
}
```
