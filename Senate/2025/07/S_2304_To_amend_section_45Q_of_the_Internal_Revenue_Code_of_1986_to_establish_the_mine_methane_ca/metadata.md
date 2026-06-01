# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2304?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2304
- Title: Methane Reduction and Economic Growth Act
- Congress: 119
- Bill type: S
- Bill number: 2304
- Origin chamber: Senate
- Introduced date: 2025-07-16
- Update date: 2026-03-25T11:03:19Z
- Update date including text: 2026-03-25T11:03:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-16: Introduced in Senate
- 2025-07-16 - IntroReferral: Introduced in Senate
- 2025-07-16 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-07-16: Introduced in Senate

## Actions

- 2025-07-16 - IntroReferral: Introduced in Senate
- 2025-07-16 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-16",
    "latestAction": {
      "actionDate": "2025-07-16",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2304",
    "number": "2304",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "W000805",
        "district": "",
        "firstName": "Mark",
        "fullName": "Sen. Warner, Mark R. [D-VA]",
        "lastName": "Warner",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Methane Reduction and Economic Growth Act",
    "type": "S",
    "updateDate": "2026-03-25T11:03:19Z",
    "updateDateIncludingText": "2026-03-25T11:03:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-16",
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
      "actionDate": "2025-07-16",
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
            "date": "2025-07-16T17:06:30Z",
            "name": "Referred To"
          },
          {
            "date": "2025-07-16T17:06:30Z",
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
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-07-16",
      "state": "WV"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "PA"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-11-04",
      "state": "AL"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-11-18",
      "state": "WV"
    },
    {
      "bioguideId": "H001104",
      "firstName": "Jon",
      "fullName": "Sen. Husted, Jon [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Husted",
      "party": "R",
      "sponsorshipDate": "2026-03-24",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2304is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2304\nIN THE SENATE OF THE UNITED STATES\nJuly 16, 2025 Mr. Warner (for himself and Mrs. Capito ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend section 45Q of the Internal Revenue Code of 1986 to establish the mine methane capture incentive credit.\n#### 1. Short title\nThis Act may be cited as the Methane Reduction and Economic Growth Act .\n#### 2. Mine methane capture incentive credit\n##### (a) In general\nSection 45Q(f) of the Internal Revenue Code of 1986 is amended by adding at the end the following new paragraph:\n(10) Methane capture (A) In general In the case of qualified methane\u2014 (i) paragraph (4) of subsection (a) shall be applied\u2014 (I) by substituting per metric ton of CO2e (as defined in section 45Z(d)(2)) of qualified methane for per metric ton of qualified carbon oxide , (II) by substituting methane capture equipment for carbon capture equipment , and (III) by applying the following in lieu of subparagraph (B) thereof: (i) either\u2014 (I) injected by the taxpayer for energy use\u2014 (aa) in a pipeline which satisfies the pipeline integrity management guidelines of section 192 of title 49, Code of Federal Regulations, and is in compliance with instrumental leak monitoring and other preventive and mitigative measures under section 192.935 of title 49, Code of Federal Regulations, or (bb) in a gathering system that feeds a pipeline described in subclause (I), or (II) otherwise used for producing heat (for industrial use or to heat a structure) or other energy, in a manner that does not involve more than de-minimis release of methane into the atmosphere. , (ii) the term qualified facility shall mean any individual source of qualified methane such as borehole, well, or vent shaft constructed at a mining facility\u2014 (I) the construction of which begins before January 1, 2036, (II) for which construction of methane capture equipment begins before such date, and (III) which captures not less than 2,500 metric tons of CO2e methane during the taxable year, (iii) subsection (b)(2)(A)(ii) shall be applied by substituting the greatest amount of methane captured at such facility in any year ending prior to for the total amount of the carbon dioxide capture capacity of the carbon capture equipment in service at such facility on the day before , and (iv) this section shall be applied by substituting methane capture for carbon capture and qualified methane for qualified carbon oxide in subsection (b)(2), (f)(1), (h), and (i)(1). (B) Qualified methane defined For purposes of this paragraph, the term qualified methane means any methane which\u2014 (i) is captured from mining activities, including underground mines, abandoned or closed mines, or surface mines, by methane capture equipment, (ii) would otherwise be released into the atmosphere as industrial emission of greenhouse gas or lead to such release, and (iii) is measured at the source of capture and verified at the point of injection or utilization. (C) Methane capture equipment defined For purposes of this paragraph, the term methane capture equipment means equipment built to connect a qualified facility to\u2014 (i) a preexisting or new pipeline system, or (ii) to energy generation equipment, to capture qualified methane from such source. .\n##### (b) Effective date\nThe amendments made by this section shall apply to qualified methane captured after December 31, 2024.",
      "versionDate": "2025-07-16",
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
        "actionDate": "2025-03-05",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "1881",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Methane Reduction and Economic Growth Act",
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
        "updateDate": "2025-09-05T19:27:34Z"
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
      "date": "2025-07-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2304is.xml"
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
      "title": "Methane Reduction and Economic Growth Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-25T11:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Methane Reduction and Economic Growth Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-31T04:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend section 45Q of the Internal Revenue Code of 1986 to establish the mine methane capture incentive credit.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-31T04:18:26Z"
    }
  ]
}
```
