# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4020?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4020
- Title: Housing Supply and Affordability Act
- Congress: 119
- Bill type: S
- Bill number: 4020
- Origin chamber: Senate
- Introduced date: 2026-03-05
- Update date: 2026-03-24T17:27:53Z
- Update date including text: 2026-03-24T17:27:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-05: Introduced in Senate
- 2026-03-05 - IntroReferral: Introduced in Senate
- 2026-03-05 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2026-03-05: Introduced in Senate

## Actions

- 2026-03-05 - IntroReferral: Introduced in Senate
- 2026-03-05 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4020",
    "number": "4020",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "K000367",
        "district": "",
        "firstName": "Amy",
        "fullName": "Sen. Klobuchar, Amy [D-MN]",
        "lastName": "Klobuchar",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "Housing Supply and Affordability Act",
    "type": "S",
    "updateDate": "2026-03-24T17:27:53Z",
    "updateDateIncludingText": "2026-03-24T17:27:53Z"
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
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
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
          "date": "2026-03-05T21:02:56Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "DE"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4020is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4020\nIN THE SENATE OF THE UNITED STATES\nMarch 5, 2026 Ms. Klobuchar (for herself, Ms. Blunt Rochester , and Mr. Kaine ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo authorize a grant program for the development and implementation of housing supply and affordability plans, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Housing Supply and Affordability Act .\n#### 2. Grants for planning and implementation associated with affordable housing\n##### (a) Definitions\nIn this section:\n**(1) Eligible entity**\nThe term eligible entity means\u2014\n**(A)**\na State, insular area, metropolitan city, or urban county, as those terms are defined in section 102 of the Housing and Community Development Act of 1974 ( 42 U.S.C. 5302 ); or\n**(B)**\na regional planning agency or consortia of regional planning agencies.\n**(2) Housing plan**\nThe term housing plan means a plan to, with respect to an area within the jurisdiction of an eligible entity\u2014\n**(A)**\nincrease the amount of available housing to meet the demand for such housing and any projected increase in the demand for such housing;\n**(B)**\nincrease the affordability of housing;\n**(C)**\nincrease the accessibility of housing for people with disabilities, including location-efficient housing;\n**(D)**\npreserve or improve the quality of housing;\n**(E)**\nreduce barriers to housing development; and\n**(F)**\ncoordinate with transportation-related agencies.\n**(3) Housing strategy**\nThe term housing strategy means a housing strategy required under section 105 of the Cranston-Gonzalez National Affordable Housing Act ( 42 U.S.C. 12705 ).\n**(4) Secretary**\nThe term Secretary means the Secretary of Housing and Urban Development.\n##### (b) Establishment\nNot later than 1 year after the date of enactment of this Act, the Secretary shall establish a program to award grants on a competitive basis to eligible entities to assist planning and implementation activities associated with affordable housing, except that such grant awards may not be used for construction, alteration, or repair work.\n##### (c) Use of amounts\n**(1) By regional planning agencies**\nIf an eligible entity that receives amounts under this section is an eligible entity described in subsection (a)(1)(B), the eligible entity shall use those amounts to assist planning activities with respect to affordable housing, including\u2014\n**(A)**\nthe development of housing plans;\n**(B)**\nthe substantial improvement of State or local housing strategies;\n**(C)**\nthe development of new regulatory requirements and processes;\n**(D)**\nupdating zoning codes;\n**(E)**\nincreasing the capacity to conduct housing inspections;\n**(F)**\nincreasing the capacity to reduce barriers to housing supply elasticity and housing affordability;\n**(G)**\nthe development of local or regional plans for community development; and\n**(H)**\nthe substantial improvement of community development strategies, including strategies designed to\u2014\n**(i)**\nincrease the availability of affordable housing and access to affordable housing;\n**(ii)**\nincrease access to public transportation; and\n**(iii)**\nadvance sustainable or location-efficient community development goals.\n**(2) By States, insular areas, metropolitan cities, and urban counties**\nIf an eligible entity that receives amounts under this section is an eligible entity described in subsection (a)(1)(A), the eligible entity shall use those amounts to\u2014\n**(A)**\nimplement and administer housing strategies and housing plans;\n**(B)**\nimplement and administer any plans to increase housing choice, address disparities in housing needs, and provide greater access to opportunity;\n**(C)**\nfund any community investments that support goals identified in a housing strategy or housing plan;\n**(D)**\nimplement and administer regulatory requirements and processes with respect to reformed zoning codes;\n**(E)**\nincrease the capacity to conduct housing inspections;\n**(F)**\nincrease the capacity to reduce barriers to housing supply elasticity and housing affordability;\n**(G)**\nimplement and administer local or regional plans for community development; and\n**(H)**\nfund any planning to increase\u2014\n**(i)**\nthe availability of affordable housing and access to affordable housing;\n**(ii)**\naccess to public transportation; and\n**(iii)**\nany location-efficient community development goals.\n**(3) Use for administrative costs**\nA eligible entity that receives amounts under this section may not use more than 10 percent of those amounts for administrative costs.\n##### (d) Coordination\nTo the extent practicable, the Secretary shall coordinate with the Administrator of the Federal Transit Administration in carrying out this section.\n##### (e) Expiration of authority\nAfter the expiration of the 5-year period beginning on the date of enactment of this Act, the Secretary may not newly establish a program as described in this section.\n##### (f) Sunset\nThe program established under this section shall terminate on the date that is 5 years after the date of enactment of this Act.",
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
        "actionDate": "2026-03-16",
        "text": "Message on Senate action sent to the House."
      },
      "number": "6644",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "21st Century ROAD to Housing Act",
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
        "name": "Housing and Community Development",
        "updateDate": "2026-03-24T17:27:53Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4020is.xml"
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
      "title": "Housing Supply and Affordability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-20T02:23:29Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Housing Supply and Affordability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-20T02:23:29Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to authorize a grant program for the development and implementation of housing supply and affordability plans, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-20T02:18:28Z"
    }
  ]
}
```
