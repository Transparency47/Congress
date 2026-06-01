# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8023?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8023
- Title: To amend the Internal Revenue Code of 1986 to provide a credit for increasing wages paid to child care providers.
- Congress: 119
- Bill type: HR
- Bill number: 8023
- Origin chamber: House
- Introduced date: 2026-03-19
- Update date: 2026-03-31T15:47:01Z
- Update date including text: 2026-03-31T15:47:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-19: Introduced in House
- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-03-19: Introduced in House

## Actions

- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-19",
    "latestAction": {
      "actionDate": "2026-03-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8023",
    "number": "8023",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "S001156",
        "district": "38",
        "firstName": "Linda",
        "fullName": "Rep. S\u00e1nchez, Linda T. [D-CA-38]",
        "lastName": "S\u00e1nchez",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "To amend the Internal Revenue Code of 1986 to provide a credit for increasing wages paid to child care providers.",
    "type": "HR",
    "updateDate": "2026-03-31T15:47:01Z",
    "updateDateIncludingText": "2026-03-31T15:47:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-19",
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
      "actionDate": "2026-03-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-19",
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
          "date": "2026-03-19T13:01:10Z",
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
      "bioguideId": "M001205",
      "district": "1",
      "firstName": "Carol",
      "fullName": "Rep. Miller, Carol D. [R-WV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2026-03-19",
      "state": "WV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8023ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8023\nIN THE HOUSE OF REPRESENTATIVES\nMarch 19, 2026 Ms. S\u00e1nchez (for herself and Mrs. Miller of West Virginia ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide a credit for increasing wages paid to child care providers.\n#### 1. Child care supply credit\n##### (a) In general\nSubpart D of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n45BB. Child care supply credit (a) In general For purposes of section 38, the amount of the child care supply credit determined under this section with respect to any employer for any taxable year is an amount equal to the lesser of\u2014 (1) the applicable percentage of the qualified child care wages paid or incurred by the employer for such taxable year, or (2) the excess (if any) of\u2014 (A) the qualified child care wages paid or incurred by the employer for such taxable year, over (B) the qualified child care wages paid or incurred by the employer for the preceding taxable year. (b) Requirement of increase in annual average hourly child care wage (1) In general No credit shall be determined under subsection (a) with respect to any employer for any taxable year unless such employer\u2019s average hourly child care wage for such taxable year exceeds such employer\u2019s average hourly child care wage for the preceding taxable year. (2) Average hourly child care wage For purposes of this subsection, the term average hourly child care wage means, with respect to any employer for any taxable year, the ratio of\u2014 (A) the qualified child care wages paid or incurred by such employer for such taxable year, divided by (B) the total number of hours of service for which such wages were paid or incurred. (c) Applicable percentage For purposes of this section\u2014 (1) In general Except as provided in paragraph (2), the applicable percentage is 5 percent. (2) Rural areas (A) In general In the case of qualified child care wages paid or incurred with respect to employment at an eligible childcare facility which is located in a rural area, the applicable percentage is 7 percent. (B) Rural area defined For purposes of this paragraph, the term rural area means any area other than an urban area (as defined in section 101(a)(35) of title 23, United States Code). (d) Definitions For purposes of this section\u2014 (1) Qualified child care wages (A) In general The term qualified child care wages means wages paid to qualified child care workers. (B) Wages The term wages has the meaning given such term by subsection (b) of section 3306 (determined without regard to any dollar limitation contained in such section). Such term shall not include any amount taken into account for purposes of determining any other credit allowed under this subpart. (2) Qualified child care worker (A) In general The term qualified child care worker means any employee who\u2014 (i) is employed at an eligible child care facility, and (ii) provides child care services. (3) Eligible child care facility The term eligible child care facility means any facility which\u2014 (A) provides child care services for at least 6 individuals, (B) receives a fee, payment, or grant for providing such services, and (C) complies with all applicable laws and regulations of a State or unit of local government. (4) Child care services The term child care services means the providing of care, education, protection, supervision, or guidance to children. (e) Election to have credit not apply (1) In general A taxpayer may elect to have this section not apply for any taxable year. (2) Other rules Rules similar to the rules of paragraphs (2) and (3) of section 51(j) shall apply for purposes of this subsection. .\n##### (b) Credit treated as part of general business credit\nSection 38(b) of the Internal Revenue Code of 1986 is amended by striking plus at the end of paragraph (40), by striking the period at the end of paragraph (41) and inserting , plus , and by adding at the end the following new paragraph:\n(42) the child care supply credit determined under section 45BB(a). .\n##### (c) Elective payment\nSection 6417(b) of the Internal Revenue Code of 1986 is amended by adding at the end the following new paragraph:\n(13) The child care supply credit determined under section 45BB(a). .\n##### (d) Denial of double benefit\nSection 280C(a) of the Internal Revenue Code of 1986 is amended by inserting 45BB(a), after 45S(a), .\n##### (e) Clerical amendment\nThe table of sections for subpart D of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by adding at the end the following new item:\nSec. 45BB. Child care supply credit. .\n##### (f) Effective date\nThe amendments made by this section shall apply to taxable years beginning after the date of the enactment of this Act.",
      "versionDate": "2026-03-19",
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
        "actionDate": "2025-12-17",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "3534",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A bill to amend the Internal Revenue Code of 1986 to provide a credit for increasing wages paid to child care providers.",
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
        "name": "Taxation",
        "updateDate": "2026-03-24T01:07:32Z"
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
      "date": "2026-03-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8023ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to provide a credit for increasing wages paid to child care providers.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-20T08:18:19Z"
    },
    {
      "title": "To amend the Internal Revenue Code of 1986 to provide a credit for increasing wages paid to child care providers.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-20T08:06:59Z"
    }
  ]
}
```
