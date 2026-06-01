# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3836?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3836
- Title: FENCES Act
- Congress: 119
- Bill type: S
- Bill number: 3836
- Origin chamber: Senate
- Introduced date: 2026-02-11
- Update date: 2026-04-13T11:24:36Z
- Update date including text: 2026-04-13T11:24:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-11: Introduced in Senate
- 2026-02-11 - IntroReferral: Introduced in Senate
- 2026-02-11 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- Latest action: 2026-02-11: Introduced in Senate

## Actions

- 2026-02-11 - IntroReferral: Introduced in Senate
- 2026-02-11 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-11",
    "latestAction": {
      "actionDate": "2026-02-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3836",
    "number": "3836",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "L000571",
        "district": "",
        "firstName": "Cynthia",
        "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
        "lastName": "Lummis",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "FENCES Act",
    "type": "S",
    "updateDate": "2026-04-13T11:24:36Z",
    "updateDateIncludingText": "2026-04-13T11:24:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-11",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Environment and Public Works.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-02-11",
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
          "date": "2026-02-11T20:13:16Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
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
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2026-03-04",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3836is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3836\nIN THE SENATE OF THE UNITED STATES\nFebruary 11, 2026 Ms. Lummis introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo amend the Clean Air Act to clarify standards for emissions emanating from outside of the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Foreign Emissions and Nonattainment Clarification for Economic Stability Act or the FENCES Act .\n#### 2. Emissions beyond control\n##### (a) Clarification of emissions covered\nSection 179B of the Clean Air Act ( 42 U.S.C. 7509a ) is amended\u2014\n**(1)**\nby inserting (regardless of whether such emissions result from human activity) after but for emissions emanating from outside of the United States each place it appears; and\n**(2)**\nin subsection (d), by inserting (regardless of whether such emissions result from human activity) after but for emissions emanating from outside the United States .\n##### (b) Designations\nSection 179B of the Clean Air Act ( 42 U.S.C. 7509a ) is amended by adding at the end the following:\n(e) Designations Notwithstanding any other provision of law, an area within a State may not be designated as a nonattainment area with respect to any new or revised primary or secondary national ambient air quality standard for a pollutant if such State establishes to the satisfaction of the Administrator that such area would be in attainment with such national ambient air quality standard for such pollutant but for emissions emanating from outside of the United States (regardless of whether such emissions result from human activity). .\n##### (c) Applicability of sanctions and fees if emissions beyond control\nSubpart 1 of part D of title I of the Clean Air Act is amended by inserting after section 179 ( 42 U.S.C. 7509 ) the following:\n179A. Applicability of sanctions and fees if emissions beyond control (a) In general Notwithstanding any other provision of this Act, with respect to any nonattainment area that is classified under section 181 as a Severe Area or an Extreme Area for ozone or under section 188 as a Serious Area for particulate matter, no sanction or fee under section 179 or 185 shall apply with respect to a State (or an area or source therein) on the basis of a deficiency described in section 179(a), or the failure to attain a national ambient air quality standard for ozone or particulate matter by the applicable attainment date, if the State demonstrates that the State would have avoided such deficiency, or such standard would have been attained, but for one or more of the following: (1) Emissions emanating from outside the nonattainment area. (2) Emissions from an exceptional event (as defined in section 319(b)(1)). (3) Emissions from mobile sources to the extent the State demonstrates that\u2014 (A) such emissions are beyond the control of the State to reduce or eliminate; and (B) the State is fully implementing such measures as are within the authority of the State to control emissions from the mobile sources. (b) No effect on underlying standards The inapplicability of sanctions or fees with respect to a State (or an area or source therein) pursuant to subsection (a) does not affect the obligation of a State, area, source, or other entity under other provisions of this Act to establish and implement measures to attain a national ambient air quality standard for ozone or particulate matter. (c) Periodic renewal of demonstration For subsection (a) to continue to apply with respect to a State (or an area or source therein), the State involved shall renew the demonstration required by subsection (a) at least once every 5 years. .",
      "versionDate": "2026-02-11",
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
        "actionDate": "2026-04-09",
        "text": "Placed on the Union Calendar, Calendar No. 514."
      },
      "number": "6409",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "FENCES Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Air quality",
            "updateDate": "2026-03-09T18:09:42Z"
          },
          {
            "name": "Climate change and greenhouse gases",
            "updateDate": "2026-03-09T18:09:42Z"
          },
          {
            "name": "Sanctions",
            "updateDate": "2026-03-09T18:09:42Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2026-03-09T18:09:42Z"
          },
          {
            "name": "Trade restrictions",
            "updateDate": "2026-03-09T18:09:42Z"
          },
          {
            "name": "User charges and fees",
            "updateDate": "2026-03-09T18:09:42Z"
          }
        ]
      },
      "policyArea": {
        "name": "Environmental Protection",
        "updateDate": "2026-02-27T17:08:18Z"
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
      "date": "2026-02-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3836is.xml"
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
      "title": "FENCES Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-05T12:03:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "FENCES Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-25T04:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Foreign Emissions and Nonattainment Clarification for Economic Stability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-25T04:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Clean Air Act to clarify standards for emissions emanating from outside of the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-25T04:48:27Z"
    }
  ]
}
```
