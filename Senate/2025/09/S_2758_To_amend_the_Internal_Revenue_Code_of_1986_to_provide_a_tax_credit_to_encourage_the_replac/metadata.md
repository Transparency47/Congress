# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2758?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2758
- Title: Freight RAILCAR Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2758
- Origin chamber: Senate
- Introduced date: 2025-09-10
- Update date: 2026-05-14T11:03:27Z
- Update date including text: 2026-05-14T11:03:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-10: Introduced in Senate
- 2025-09-10 - IntroReferral: Introduced in Senate
- 2025-09-10 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-09-10: Introduced in Senate

## Actions

- 2025-09-10 - IntroReferral: Introduced in Senate
- 2025-09-10 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-10",
    "latestAction": {
      "actionDate": "2025-09-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2758",
    "number": "2758",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "B001299",
        "district": "",
        "firstName": "Jim",
        "fullName": "Sen. Banks, Jim [R-IN]",
        "lastName": "Banks",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "Freight RAILCAR Act of 2025",
    "type": "S",
    "updateDate": "2026-05-14T11:03:27Z",
    "updateDateIncludingText": "2026-05-14T11:03:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-10",
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
      "actionDate": "2025-09-10",
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
            "date": "2025-09-10T17:54:21Z",
            "name": "Referred To"
          },
          {
            "date": "2025-09-10T17:54:21Z",
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
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "DE"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2758is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2758\nIN THE SENATE OF THE UNITED STATES\nSeptember 10, 2025 Mr. Banks (for himself and Mr. Coons ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide a tax credit to encourage the replacement or modernization of inefficient, outdated freight railcars, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Freight Rail Assets Investment to Launch Commercial Activity Revitalization Act of 2025 or the Freight RAILCAR Act of 2025 .\n#### 2. Freight railcar modernization credit\n##### (a) In general\nSubpart D of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n45BB. Freight railcar modernization credit (a) In general For purposes of section 38, the freight railcar modernization credit determined under this section for the taxable year is an amount equal to 10 percent of the taxpayer\u2019s freight railcar fleet modernization expenses. (b) Limitation No more than 1,000 qualified freight railcars per taxpayer may be taken into account for purposes of determining the credit under subsection (a) with respect to a taxable year. (c) Definitions For purposes of this section\u2014 (1) Freight railcar fleet modernization expenses The term freight railcar fleet modernization expenses means the sum of the qualifying railcar replacement and modernization amount. (2) Qualifying railcar replacement and modernization amount The term qualifying railcar replacement and modernization amount means\u2014 (A) the basis of any qualified newly built replacement railcar placed in service by the taxpayer during the taxable year, plus (B) the qualified railcar modernization expenditures of the taxpayer for the taxable year. (3) Qualified newly built replacement railcar The term qualified newly built replacement railcar means a qualified freight railcar which\u2014 (A) is built after the date of the enactment of this section, (B) is ordered or originally placed in service before the date that is three years after the date of the enactment of this section, and (C) replaces two freight railcars owned by the taxpayer that\u2014 (i) were in service within the 48 months preceding the beginning of the taxable year, and (ii) which were both scrapped and permanently removed from the AAR Umler System master file during such taxable year. (4) Qualified freight railcar (A) In general The term qualified freight railcar means a freight railcar that\u2014 (i) is either acquired or modernized by the taxpayer after the date of the enactment of this section, (ii) meets the significant improvement requirements for capacity or performance of subparagraph (B), (iii) was built in a qualified facility, and (iv) with respect to which no credit under this section was previously claimed by any taxpayer. (B) Significant improvement For purposes of this paragraph, an improvement in capacity and performance with respect to a modernized freight railcar is a significant improvement if\u2014 (i) such capacity, as the case may be, is increased by at least 8 percent, or (ii) in the case of performance, the qualified freight railcar meets the requirements of the Association of American Railroads Standard S\u2013286 or is modernized to meet the design standards set forth in final rule HM\u2013251 of the Pipeline and Hazardous Materials Safety Administration (as amended by HM\u2013251C). (C) Modernized The term modernized means modified, retrofitted, converted or rebuilt for the purpose of meeting the significant improvement criteria of subparagraph (B). (5) Qualified railcar modernization expenditure The term qualified railcar modernization expenditure means any amount paid or incurred\u2014 (A) in connection with the modernization of a freight railcar resulting in such railcar being designated a qualified freight railcar, and (B) which is properly chargeable to a capital account with respect to such freight railcar. (6) Qualified facility The term qualified facility means a facility that is not owned or leased by an entity that would be ineligible for an award of a contract or subcontract under 49 U.S.C. 5323(u) . (d) Special rules (1) Denial of double benefit No credit shall be allowed under subsection (a) for any expense for which a deduction or credit is allowed under any other provision of this chapter. (2) Basis adjustment For purposes of this subtitle, if a credit is allowed under subsection (a) with respect to any qualified freight railcar, the basis of such railcar shall be reduced by the amount of the credit so allowed. (3) Sale-leaseback For purposes of subsection (a), if any qualified freight railcar is\u2014 (A) originally placed in service by a person after the date of the enactment of this section, and (B) sold and leased back by such person within 3 months after such railcar is originally placed in service (or, in the case of more than one railcar subject to the same lease, within 3 months after the date the final railcar is placed in service, so long as the period between the time the first railcar is placed in service and the time the last railcar is placed in service does not exceed 24 months), such railcar shall be treated as originally placed in service not earlier than the date on which such railcar is used under the leaseback referred to in this paragraph. (4) Syndication For purposes of subsection (a), if\u2014 (A) any qualified freight railcar is originally placed in service after the date of enactment of this section by the lessor of such railcar, (B) such railcar is sold by such lessor or any subsequent purchaser within 3 months after the date such railcar was originally placed in service (or, in the case of more than one railcar subject to the same lease, within 3 months after the date the final railcar is placed in service and the time the last railcar is placed in service does not exceed 12 months), and (C) the user of such railcar after the last sale during such 3-month period remains the same as when such railcar was originally placed in service, such railcars shall be treated as originally placed in service not earlier than the date of such last sale. (5) Entities owned or controlled by state-owned enterprises ineligible No credit under subsection (a) shall be allowed to any taxpayer that would be ineligible for an award of a contract or subcontract under 49 U.S.C. 5323(u) . (e) Termination This section shall not apply to any qualifying railcar replacement and modernization amount after the date that is three years after the date of the enactment of this section. .\n##### (b) Credit allowed as business credit\nSection 38(b) of the Internal Revenue Code of 1986 (relating to current year business credit) is amended by striking plus at the end of paragraph (40), by striking the period at the end of paragraph (41) and inserting , plus and by inserting at the end thereof the following new paragraph:\n(42) the freight railcar modernization credit determined under section 45BB. .\n##### (c) Coordination with section 55\nSection 38(c)(4)(B) of the Internal Revenue Code of 1986 is amended by redesignating clauses (x), (xi), and (xii) as clauses (xi), (xii), and (xiii), respectively, and by inserting after clause (ix) the following new clause:\n(x) the freight railcar modernization credit determined under section 45BB, .\n##### (d) Clerical amendment\nThe table of sections for subpart D of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after the item relating to section 45AA the following new item:\nSec. 45BB. Freight railcar modernization credit. .\n##### (e) Effective date\nThe amendments made by this section shall apply to property placed in service, and amounts paid or incurred, after December 31, 2024.\n#### 3. Report on the freight railcar modernization credit\n##### (a) In general\nNot later than 3 years after the date of the enactment of this Act, the Secretary of the Treasury (or the Secretary\u2019s delegate), shall submit to the Committee on Ways and Means of the House of Representatives and the Committee on Finance of the Senate a report on activity with respect to the qualified freight railcar credit under section 45BB of the Internal Revenue Code of 1986.\n##### (b) Report contents\nThe report submitted under subsection (a) shall contain information with respect to the following:\n**(1)**\nThe number of times the credit was claimed.\n**(2)**\nThe number of railcars scrapped as a result of the credit.\n**(3)**\nThe number of new railcars entered into contract as a result of the credit.\n**(4)**\nThe number of new railcars built as a result of the credit.",
      "versionDate": "2025-09-10",
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
        "actionDate": "2025-02-11",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "1200",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Freight RAILCAR Act of 2025",
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
        "updateDate": "2025-09-19T16:01:43Z"
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
      "date": "2025-09-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2758is.xml"
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
      "title": "Freight RAILCAR Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-14T11:03:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Freight RAILCAR Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-19T02:53:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Freight Rail Assets Investment to Launch Commercial Activity Revitalization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-19T02:53:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to provide a tax credit to encourage the replacement or modernization of inefficient, outdated freight railcars, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-19T02:48:23Z"
    }
  ]
}
```
