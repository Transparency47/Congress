# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2747?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2747
- Title: Healthy Affordable Housing Act
- Congress: 119
- Bill type: HR
- Bill number: 2747
- Origin chamber: House
- Introduced date: 2025-04-08
- Update date: 2025-05-15T17:58:34Z
- Update date including text: 2025-05-15T17:58:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-08: Introduced in House
- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-04-08: Introduced in House

## Actions

- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-08",
    "latestAction": {
      "actionDate": "2025-04-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2747",
    "number": "2747",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "S001215",
        "district": "11",
        "firstName": "Haley",
        "fullName": "Rep. Stevens, Haley M. [D-MI-11]",
        "lastName": "Stevens",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Healthy Affordable Housing Act",
    "type": "HR",
    "updateDate": "2025-05-15T17:58:34Z",
    "updateDateIncludingText": "2025-05-15T17:58:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-08",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-08",
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
          "date": "2025-04-08T14:00:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "T000486",
      "district": "15",
      "firstName": "Ritchie",
      "fullName": "Rep. Torres, Ritchie [D-NY-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Torres",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2747ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2747\nIN THE HOUSE OF REPRESENTATIVES\nApril 8, 2025 Ms. Stevens (for herself and Mr. Torres of New York ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo require the Secretary of Housing and Urban Development to establish a grant and loan program that provides amounts to eligible entities to use to develop, create, or preserve qualifying affordable dwelling units, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Healthy Affordable Housing Act .\n#### 2. Grant and loan program for affordable dwelling units\n##### (a) In general\nThe Secretary of Housing and Urban Development shall, not later than 1 year after the date of the enactment of this section, establish a grant and loan program that provides amounts to eligible entities to use to develop, create, or preserve qualifying affordable dwelling units in neighborhoods that the Secretary has determined have shortages of affordable housing.\n##### (b) Application and selection\n**(1) In general**\nTo apply for a grant or loan under this section, an eligible entity shall submit an application to the Secretary at such time and in such manner as the Secretary may reasonably require.\n**(2) Location requirement**\n**(A) In general**\nGrants and loans may only be awarded to applicants that propose to develop, create, or preserve qualifying affordable dwelling units that are in a neighborhood with\u2014\n**(i)**\na Federally qualified health center;\n**(ii)**\na health care provider who, as determined by the Secretary accepts Medicaid and provides primary care services;\n**(iii)**\na grocery store that accepts Supplemental Nutrition Assistance Program, or the Nutrition Assistance Program, benefits and Special Supplemental Nutrition Program for Women, Infants, and Children benefits;\n**(iv)**\na State licensed child care provider or an eligible child care provider under the Child Care and Development Block Grant Act that cares for at least one child to whom the provider is not related;\n**(v)**\na pharmacy; or\n**(vi)**\npublic transportation, as such term is defined in paragraph (15) of section 5302 of title 49, United States Code.\n**(B) Preference**\nThe Secretary shall give preference to applicants that are\u2014\n**(i)**\ndeveloping, creating, or preserving qualifying affordable dwelling units that are not more than a mile from 2 or more of the types of amenities listed in subparagraph (A); or\n**(ii)**\ndeveloping, creating, or preserving, with or without the assistance of a partnering entity, qualifying affordable dwelling units that are located in buildings that have or will contain any of the amenities listed in subparagraph (A).\n**(C) Selection criteria**\nThe Secretary, in administering the grant and loan program, may establish selection criteria relating to\u2014\n**(i)**\nhow many qualifying affordable housing units will be developed, created, or preserved;\n**(ii)**\nthe boundaries of the neighborhood in which the qualifying affordable dwelling units are to be developed, created, or preserved; and\n**(iii)**\nthe area median income in the area in which the qualifying affordable housing units are to be developed, created, or preserved.\n##### (c) Survey\n**(1) In general**\n**(A) In general**\nTwo years after the date that any qualifying affordable dwelling unit is first occupied after being developed, created, or preserved using amounts provided under this section, and every 2 years thereafter for 10 years, the Secretary shall conduct a voluntary survey of residents in such dwelling unit about any benefits they perceive associated with being physically near the amenities listed in subsection (b)(2)(A).\n**(B) Control group permitted**\nThe Secretary may, if the Secretary determines appropriate, survey persons who are not residents in a qualifying affordable dwelling unit that received amounts under this section as part of a control group for the survey required under subparagraph (A).\n**(2) Report**\n**(A) In general**\nThe Secretary shall, not later than 1 year after the date on which the Secretary completes a survey required under paragraph (1), compile the results of each survey conducted under paragraph (1) and submit a report about such results to the Committees on Appropriations and Financial Services of the House of Representatives and the Committees on Appropriations and Banking, Housing, and Urban Affairs of the Senate.\n**(B) Requirement**\nEach report submitted under subparagraph (A) shall evaluate, with respect to each qualifying affordable dwelling unit developed, created, or preserved using amounts provided under this section, whether nearby the amenities identified in subsection (b)(2)(A) have closed or changed location in the time since the previous report submitted under subparagraph (A).\n##### (d) Rules of construction\n**(1) In general**\nNothing in this section may be construed to prohibit the Secretary from awarding a grant or loan under this section to a person who has applied for another funding opportunity administered by the Secretary relating to the development, creation, or preservation of affordable housing units.\n**(2) Rental assistance**\nNothing in this section may be construed to prohibit a qualifying affordable dwelling unit that is developed, created, or preserved using amounts provided under this section from receiving tenant-based assistance or project-based assistance under section 8(o) of the United States Housing Act of 1937.\n##### (e) Authorization of appropriations\nThere is authorized to be appropriated to the Secretary $100,000,000 in each of fiscal years 2025 to 2029 carry out this section.\n##### (f) Definitions\nIn this section:\n**(1) Eligible entity**\nThe term eligible entity means\u2014\n**(A)**\na unit of general local government, including county government;\n**(B)**\na tribe, tribal entity or tribally designated housing entity;\n**(C)**\nan owner or developer of a qualifying affordable dwelling unit;\n**(D)**\na public housing agency;\n**(E)**\nan organization with a mission that involves the development, creation, preservation, renovation, operation, or maintenance of affordable housing; or\n**(F)**\nany combination of the entities described in subparagraphs (A) through (E).\n**(2) Federally qualified health center**\nThe term Federally qualified health center has the meaning given the term in section 1861(aa)(4) of the Social Security 22 Act ( 42 U.S.C. 1395x(aa) ).\n**(3) Qualifying affordable dwelling unit**\nThe term qualifying affordable dwelling unit means a dwelling unit that\u2014\n**(A)**\nqualifies as affordable housing under 215(a) of the Cranston-Gonzalez National Affordable Housing Act; and\n**(B)**\nmeets the income targeting requirements described in section 214(1) of such Act.\n**(4) Secretary**\nThe term Secretary means the Secretary of Housing and Urban Development.",
      "versionDate": "2025-04-08",
      "versionType": "Introduced in House"
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
        "updateDate": "2025-05-15T17:58:34Z"
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
      "date": "2025-04-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2747ih.xml"
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
      "title": "Healthy Affordable Housing Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-22T03:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Healthy Affordable Housing Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-22T03:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Housing and Urban Development to establish a grant and loan program that provides amounts to eligible entities to use to develop, create, or preserve qualifying affordable dwelling units, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-22T03:48:20Z"
    }
  ]
}
```
