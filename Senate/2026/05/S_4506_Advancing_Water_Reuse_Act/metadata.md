# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4506?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4506
- Title: Advancing Water Reuse Act
- Congress: 119
- Bill type: S
- Bill number: 4506
- Origin chamber: Senate
- Introduced date: 2026-05-13
- Update date: 2026-05-29T15:20:30Z
- Update date including text: 2026-05-29T15:20:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-05-13: Introduced in Senate
- 2026-05-13 - IntroReferral: Introduced in Senate
- 2026-05-13 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-05-13: Introduced in Senate

## Actions

- 2026-05-13 - IntroReferral: Introduced in Senate
- 2026-05-13 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-13",
    "latestAction": {
      "actionDate": "2026-05-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4506",
    "number": "4506",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "L000570",
        "district": "",
        "firstName": "Ben",
        "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
        "lastName": "Luj\u00e1n",
        "party": "D",
        "state": "NM"
      }
    ],
    "title": "Advancing Water Reuse Act",
    "type": "S",
    "updateDate": "2026-05-29T15:20:30Z",
    "updateDateIncludingText": "2026-05-29T15:20:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-13",
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
      "actionDate": "2026-05-13",
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
          "date": "2026-05-13T14:51:44Z",
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
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "AL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4506is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4506\nIN THE SENATE OF THE UNITED STATES\nMay 13, 2026 Mr. Luj\u00e1n (for himself and Mrs. Britt ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to allow an investment credit for certain water reuse projects.\n#### 1. Short title\nThis Act may be cited as the Advancing Water Reuse Act .\n#### 2. Qualifying water reuse project credit\n##### (a) In general\nSubpart E of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 48E the following new section:\n48F. Qualifying water reuse project credit (a) In general For purposes of section 46, the qualifying water reuse project credit for any taxable year is an amount equal to 30 percent of the qualified investment for such taxable year with respect to any qualifying water reuse project of the taxpayer. (b) Qualified investment (1) In general For purposes of subsection (a), the qualified investment with respect to any qualifying water reuse project for any taxable year is the basis of qualified property placed in service by the taxpayer during such taxable year which is part of such qualifying water reuse project. (2) Qualified property For purposes of this subsection, the term qualified property means property\u2014 (A) which is tangible property, (B) with respect to which depreciation (or amortization in lieu of depreciation) is allowable, and (C) which is\u2014 (i) constructed, reconstructed, or erected by the taxpayer, or (ii) acquired by the taxpayer if the original use of such property commences with the taxpayer. (3) Certain qualified progress expenditures rules made applicable Rules similar to the rules of subsections (c)(4) and (d) of section 46 (as in effect on the day before the enactment of the Revenue Reconciliation Act of 1990) shall apply for purposes of this section. (c) Qualifying water reuse project For purposes of this section\u2014 (1) In general The term qualifying water reuse project means a project which\u2014 (A) installs, replaces, or modifies an onsite water recycling system within an industrial, manufacturing, data center, or food processing facility, (B) replaces the use of freshwater, such as groundwater, with recycled water from a municipal water provider for the production of goods or provision of services by the taxpayer, or (C) builds or expands a municipal water recycling system for the purpose of securing recycled water for the production of goods or provision of services. (2) Water recycling system The term water recycling system means infrastructure needed for the production, storage, conveyance, and use of recycled water. (3) Recycled water The term recycled water means former wastewater, including both industrial and municipal wastewater, that has been treated and cleaned for a specific beneficial use. (d) Special rule for certain property transferred to utilities (1) In general In the case of any qualified transfer property transferred from a person to a utility\u2014 (A) such property shall be treated as qualified property with respect to such person, (B) such person shall be treated as having placed such property in service at the time of such transfer, (C) the basis of such person in such property which is taken into account under subsection (b)(1) shall be the basis of such person in such property at the time of such transfer, and (D) such property shall not be taken into account for purposes of determining any credit allowed under this section to such utility. (2) Qualified transfer property For purposes of this subsection, the term qualified transfer property means property transferred from a person to a utility if\u2014 (A) such property is qualified property with respect to such utility, and (B) such person and such utility enter into a binding written agreement under which such person is treated as eligible for the credit allowed under this section with respect to such property in lieu of such utility. (e) Termination This section shall not apply to any qualified investment with respect to any qualifying water reuse project unless such project is placed in service not later than the date which is 10 years after the date of the enactment of this section. .\n##### (b) Part of investment credit\nSection 46 of such Code is amended by striking and at the end of paragraph (6), by striking the period at the end of paragraph (7) and inserting , and , and by adding at the end the following new paragraph:\n(8) the qualifying water reuse project credit. .\n##### (c) Clerical amendment\nThe table of sections for subpart D of part IV of subchapter A of chapter 1 of such Code is amended by inserting after the item relating to section 48E the following new item:\nSec. 48F. Qualifying water reuse project credit. .\n##### (d) Effective date\nThe amendments made by this section shall apply to qualifying water reuse projects (as defined in section 48F of the Internal Revenue Code of 1986, as added by this section) the construction of which begins after the date of the enactment of this Act.",
      "versionDate": "2026-05-13",
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
        "actionDate": "2025-04-17",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "2940",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Advancing Water Reuse Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-12-18",
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committees on Education and Workforce, and Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "6900",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "American Affordability Act of 2025",
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
        "updateDate": "2026-05-28T20:37:36Z"
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
      "date": "2026-05-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4506is.xml"
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
      "title": "Advancing Water Reuse Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-19T00:53:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Advancing Water Reuse Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-19T00:53:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to allow an investment credit for certain water reuse projects.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-19T00:48:37Z"
    }
  ]
}
```
