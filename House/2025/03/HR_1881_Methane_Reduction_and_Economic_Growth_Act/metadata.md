# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1881?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1881
- Title: Methane Reduction and Economic Growth Act
- Congress: 119
- Bill type: HR
- Bill number: 1881
- Origin chamber: House
- Introduced date: 2025-03-05
- Update date: 2026-03-27T08:06:46Z
- Update date including text: 2026-03-27T08:06:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-05: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-03-05: Introduced in House

## Actions

- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-05",
    "latestAction": {
      "actionDate": "2025-03-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1881",
    "number": "1881",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "M001205",
        "district": "1",
        "firstName": "Carol",
        "fullName": "Rep. Miller, Carol D. [R-WV-1]",
        "lastName": "Miller",
        "party": "R",
        "state": "WV"
      }
    ],
    "title": "Methane Reduction and Economic Growth Act",
    "type": "HR",
    "updateDate": "2026-03-27T08:06:46Z",
    "updateDateIncludingText": "2026-03-27T08:06:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-05",
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
      "actionDate": "2025-03-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-05",
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
          "date": "2025-03-05T15:01:10Z",
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
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "AL"
    },
    {
      "bioguideId": "R000610",
      "district": "14",
      "firstName": "Guy",
      "fullName": "Rep. Reschenthaler, Guy [R-PA-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Reschenthaler",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "PA"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "PA"
    },
    {
      "bioguideId": "L000585",
      "district": "16",
      "firstName": "Darin",
      "fullName": "Rep. LaHood, Darin [R-IL-16]",
      "isOriginalCosponsor": "False",
      "lastName": "LaHood",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "IL"
    },
    {
      "bioguideId": "G000568",
      "district": "9",
      "firstName": "H.",
      "fullName": "Rep. Griffith, H. Morgan [R-VA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Griffith",
      "middleName": "Morgan",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "VA"
    },
    {
      "bioguideId": "K000376",
      "district": "16",
      "firstName": "Mike",
      "fullName": "Rep. Kelly, Mike [R-PA-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "PA"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-10-28",
      "state": "AL"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "PA"
    },
    {
      "bioguideId": "C001126",
      "district": "15",
      "firstName": "Mike",
      "fullName": "Rep. Carey, Mike [R-OH-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Carey",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1881ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1881\nIN THE HOUSE OF REPRESENTATIVES\nMarch 5, 2025 Mrs. Miller of West Virginia (for herself, Ms. Sewell , Mr. Reschenthaler , and Mr. Deluzio ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend section 45Q of the Internal Revenue Code of 1986 to establish the mine methane capture incentive credit.\n#### 1. Short title\nThis Act may be cited as the Methane Reduction and Economic Growth Act .\n#### 2. Mine methane capture incentive credit\n##### (a) In general\nSection 45Q(f) of the Internal Revenue Code of 1986 is amended by adding at the end the following new paragraph:\n(10) Methane capture (A) In general In the case of qualified methane\u2014 (i) paragraph (4) of subsection (a) shall be applied\u2014 (I) by substituting per metric ton of CO2e (as defined in section 45Z(d)(2)) of qualified methane for per metric ton of qualified carbon oxide , (II) by substituting methane capture equipment for carbon capture equipment , and (III) by applying the following in lieu of subparagraph (B) thereof: (B) either\u2014 (i) injected by the taxpayer for energy use\u2014 (I) in a pipeline which satisfies the pipeline integrity management guidelines of section 192 of title 49, Code of Federal Regulations, and is in compliance with instrumental leak monitoring and other preventive and mitigative measures under section 192.935 of title 49, Code of Federal Regulations, or (II) in a gathering system that feeds a pipeline described in subclause (I), or (ii) otherwise used for producing heat (for industrial use or to heat a structure) or other energy, in a manner that does not involve more than de-minimis release of methane into the atmosphere' for \u2018used by the taxpayer as a tertiary injectant in a qualified enhanced oil or natural gas recovery project and disposed of by the taxpayer in secure geological storage', , (ii) the term qualified facility shall mean any individual source of qualified methane such as borehole, well, or vent shaft constructed at a mining facility\u2014 (I) the construction of which begins before January 1, 2036, (II) for which construction of methane capture equipment begins before such date, and (III) which captures not less than 2,500 metric tons of CO2e methane during the taxable year, and (iii) this section shall be applied by substituting methane capture for carbon capture and qualified methane for qualified carbon oxide in subsections (b)(2), (f)(1), (f)(4), (h), and (i)(1). (B) Qualified methane defined For purposes of this paragraph, the term qualified methane means any methane which\u2014 (i) is captured from mining activities, including underground mines, abandoned or closed mines, or surface mines, by methane capture equipment, (ii) would otherwise be released into the atmosphere as industrial emission of greenhouse gas or lead to such release, and (iii) is measured at the source of capture and verified at the point of injection or utilization. (C) Methane capture equipment defined For purposes of this paragraph, the term \u2018methane capture equipment\u2019 means equipment built to connect a qualified facility to\u2014 (i) a preexisting or new pipeline system, or (ii) to energy generation equipment, to capture qualified methane from such source. .\n##### (b) Effective date\nThe amendments made by this section shall apply to qualified methane captured after December 31, 2024.",
      "versionDate": "2025-03-05",
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
        "actionDate": "2025-07-16",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "2304",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Methane Reduction and Economic Growth Act",
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
        "updateDate": "2025-05-08T19:35:18Z"
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
      "date": "2025-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1881ih.xml"
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
      "title": "Methane Reduction and Economic Growth Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-25T06:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Methane Reduction and Economic Growth Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-25T06:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend section 45Q of the Internal Revenue Code of 1986 to establish the mine methane capture incentive credit.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-25T06:03:25Z"
    }
  ]
}
```
