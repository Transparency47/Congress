# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6060?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6060
- Title: SAFE Taps Act
- Congress: 119
- Bill type: HR
- Bill number: 6060
- Origin chamber: House
- Introduced date: 2025-11-17
- Update date: 2025-11-24T17:39:05Z
- Update date including text: 2025-11-24T17:39:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-11-17: Introduced in House
- 2025-11-17 - IntroReferral: Introduced in House
- 2025-11-17 - IntroReferral: Introduced in House
- 2025-11-17 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-11-17: Introduced in House

## Actions

- 2025-11-17 - IntroReferral: Introduced in House
- 2025-11-17 - IntroReferral: Introduced in House
- 2025-11-17 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-17",
    "latestAction": {
      "actionDate": "2025-11-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6060",
    "number": "6060",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "K000391",
        "district": "8",
        "firstName": "Raja",
        "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
        "lastName": "Krishnamoorthi",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "SAFE Taps Act",
    "type": "HR",
    "updateDate": "2025-11-24T17:39:05Z",
    "updateDateIncludingText": "2025-11-24T17:39:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-17",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-17",
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
          "date": "2025-11-17T17:01:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6060ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6060\nIN THE HOUSE OF REPRESENTATIVES\nNovember 17, 2025 Mr. Krishnamoorthi introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo direct the Administrator of the Environmental Protection Agency to establish a program to provide grants to units of local governments, drinking water systems, and federally recognized Indian Tribes for the replacement of lead, galvanized steel, and iron service lines and lead drinking water mains, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Safe and Fair Elimination of Taps with Lead Service Lines Act or the SAFE Taps Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe presence of lead in drinking water poses a grave and ongoing threat to public health in the United States. The Environmental Protection Agency and the Centers for Disease Control and Prevention agree that there is no known safe level of lead exposure, which causes irreversible neurological damage in children and serious health conditions in adults.\n**(2)**\nLead service lines, which connect drinking water mains to millions of homes, schools, and childcare facilities, are the most significant source of lead contamination in drinking water. The Environmental Protection Agency estimates that 9.2 million lead service lines serve water to buildings in communities across the United States.\n**(3)**\nThe Environmental Protection Agency, through subpart I of part 141 of title 40, Code of Federal Regulations, has mandated the full replacement of most lead service lines within a 10-year period, placing a significant legal and financial obligation on units of local governments and public water systems.\n**(4)**\nWhile State revolving loan funds established under section 1452 of the Safe Drinking Water Act ( 42 U.S.C. 300j\u201312 ) are a critical tool to finance water infrastructure, the primary structure of such funds as a loan program is inadequate to meet the needs of many communities facing the lead service line replacement mandate under subpart I of part 141 of title 40, Code of Federal Regulations. Financially distressed and disadvantaged communities often lack the debt capacity to accept loans or the technical capacity to navigate the complex application process under a State revolving loan fund.\n**(5)**\nThe funds made available for lead service line replacement projects and associated activities by the Infrastructure Investment and Jobs Act ( Public Law 117\u201358 ) provided a historic and vital down payment for lead service line replacement, but the overwhelming demand for these funds demonstrated that a substantial funding gap remains and that a loan-based system presents significant barriers to the most vulnerable communities.\n**(6)**\nIn many older communities, lead service lines are connected to aging drinking water mains that are also at or near the end of their useful life. Forcing municipalities to replace lead service lines without addressing these deteriorating drinking water mains is fiscally inefficient and fails to ensure the long-term integrity of the water system.\n**(7)**\nA dedicated Federal grant program is therefore necessary to ensure the equitable, efficient, and timely replacement of all lead service lines and drinking water mains that are not lead free to protect public health, to achieve compliance with subpart I of part 141 of title 40, Code of Federal Regulations, and to advance environmental justice for all Americans.\n#### 3. Grant program for the replacement of lead, galvanized steel, and iron service lines and lead drinking water mains\n##### (a) Establishment\nThe Administrator shall establish a program to provide grants, subject to the availability of appropriations, to eligible recipients to pay for eligible project costs.\n##### (b) Labor standards\nAll laborers and mechanics employed by contractors or subcontractors in the performance of construction, alteration, or repair work financed in whole or in part with a grant provided under the program shall be paid wages at rates not less than those prevailing on similar work in the locality as determined by the Secretary of Labor in accordance with subchapter IV of chapter 31 of title 40, United States Code (commonly referred to as the Davis-Bacon Act ).\n#### 4. Definitions\nIn this Act:\n**(1) Administrator**\nThe term Administrator means the Administrator of the Environmental Protection Agency.\n**(2) Eligible project costs**\nThe term eligible project costs means costs to\u2014\n**(A)**\nreplace a lead service line;\n**(B)**\nreplace galvanized steel or iron service lines that are or were downstream of lead components;\n**(C)**\nreplace a drinking water main that is not lead free;\n**(D)**\nplan for or otherwise design the replacement of a lead service line, galvanized steel or iron service line, or drinking water main using a grant provided under the program;\n**(E)**\ndevelop or update any inventory of lead service lines; and\n**(F)**\nrestore the site at which a service line or drinking water main is replaced using a grant provided under the program.\n**(3) Eligible recipient**\nThe term eligible recipient means\u2014\n**(A)**\na unit of local government;\n**(B)**\na public water system; or\n**(C)**\na federally recognized Indian Tribe.\n**(4) Lead free**\nThe term lead free has the meaning given such term in section 1417(d)(1) of the Safe Drinking Water Act ( 42 U.S.C. 300g\u20136(d)(1) ).\n**(5) Lead service line**\nThe term lead service line has the meaning given such term in section 1459B(a) of the Safe Drinking Water Act (42 U.S.C. 300j\u201319b(a)).\n**(6) Program**\nThe term program means the program established under section 3(a).\n**(7) Public water system**\nThe term public water system has the meaning given such term in section 1401(4) of the Safe Drinking Water Act ( 42 U.S.C. 300f(4) ).",
      "versionDate": "2025-11-17",
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
        "name": "Environmental Protection",
        "updateDate": "2025-11-24T17:39:05Z"
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
      "date": "2025-11-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6060ih.xml"
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
      "title": "SAFE Taps Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-22T04:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SAFE Taps Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-22T04:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Safe and Fair Elimination of Taps with Lead Service Lines Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-22T04:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Administrator of the Environmental Protection Agency to establish a program to provide grants to units of local governments, drinking water systems, and federally recognized Indian Tribes for the replacement of lead, galvanized steel, and iron service lines and lead drinking water mains, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-22T04:33:23Z"
    }
  ]
}
```
