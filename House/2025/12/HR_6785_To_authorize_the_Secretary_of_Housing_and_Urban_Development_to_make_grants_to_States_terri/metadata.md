# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6785?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6785
- Title: CLEAR Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6785
- Origin chamber: House
- Introduced date: 2025-12-17
- Update date: 2026-01-22T15:41:01Z
- Update date including text: 2026-01-22T15:41:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-17: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-12-17: Introduced in House

## Actions

- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-17",
    "latestAction": {
      "actionDate": "2025-12-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6785",
    "number": "6785",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "C001121",
        "district": "6",
        "firstName": "Jason",
        "fullName": "Rep. Crow, Jason [D-CO-6]",
        "lastName": "Crow",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "CLEAR Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-22T15:41:01Z",
    "updateDateIncludingText": "2026-01-22T15:41:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-17",
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
      "actionDate": "2025-12-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-17",
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
          "date": "2025-12-17T14:03:45Z",
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
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-12-17",
      "state": "CA"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "NM"
    },
    {
      "bioguideId": "M001205",
      "district": "1",
      "firstName": "Carol",
      "fullName": "Rep. Miller, Carol D. [R-WV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-12-17",
      "state": "WV"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6785ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6785\nIN THE HOUSE OF REPRESENTATIVES\nDecember 17, 2025 Mr. Crow (for himself, Mrs. Kim , Mr. Vasquez , and Mrs. Miller of West Virginia ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo authorize the Secretary of Housing and Urban Development to make grants to States, territories, and Indian tribes to support local resiliency offices, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Championing Local Efforts to Advance Resilience Act of 2025 or the CLEAR Act of 2025 .\n#### 2. Resiliency office grants\n##### (a) Authority\nThe Secretary of Housing and Urban Development, in consultation with the Administrator of the Federal Emergency Management Agency, the Secretary of Commerce, and the Secretary of the Interior, may make grants under this section to States, territories, and Indian tribes that are eligible for such grants pursuant to subsection (b) for use in accordance with subsection (c).\n##### (b) Eligibility\nTo be eligible for a grant under this section, a State, territory, or Indian tribe shall establish and maintain, or show a plan and ability to establish and maintain, an office specifically responsible for issues relating to resilience and that has among its duties the following:\n**(1)**\nTo develop and update, not less frequently than every 5 years, a resiliency framework, in consultation with vulnerable and impacted communities, that identifies current and projected risks and vulnerabilities due to extreme weather and other challenges, and provides recommendations to address such risks and vulnerabilities, in each of the areas of\u2014\n**(A)**\nenvironmental and natural hazards;\n**(B)**\nthe economy and workforce;\n**(C)**\ninfrastructure;\n**(D)**\nhealth and social services; and\n**(E)**\nhousing.\n**(2)**\nTo implement programming to address risks and vulnerabilities identified in the resiliency framework, including\u2014\n**(A)**\nproviding technical assistance to local governments for the implementation of resilience planning;\n**(B)**\nassisting State, territory, or tribal agencies in the implementation of resilience policies and procedures;\n**(C)**\nintegrating resilience criteria into existing competitive grant funding administered by such office or State agencies; and\n**(D)**\nsupporting long-term community pre-disaster mitigation and recovery efforts and facilitating access to resources before and after a disaster.\n**(3)**\nTo improve coordination among State, territory, or tribal agencies and regional and local jurisdictions to support community and economic recovery efforts and address risk and vulnerability reduction.\n##### (c) Use\nAmounts from a grant under this section may be used by the grantee, or any unit of local government that is a subgrantee of such grantee, only for\u2014\n**(1)**\ncosts of establishing or maintaining, or both, a resiliency office and implementing resiliency programming, developing resilience planning and analytic tools, enhancing community planning and capacity, enhancing coordination among State, territory, or tribal agencies and regional and local jurisdictions and stakeholders, and providing technical assistance, in accordance with the requirements of subsection (b); and\n**(2)**\npayment of any non-Federal share required in connection with a Federal program undertaken to carry out any of the purposes of subsection (b)(2).\n##### (d) Applications\nTo apply for a grant under this section, a State, territory, or Indian tribe shall submit an application at such time, in such form, and containing such information as the Secretary may prescribe for establishing a formula-based grant program.\n##### (e) Priority\nIn awarding grants under this section to States or territories, the Secretary shall give priority to applications that\u2014\n**(1)**\ndemonstrate the greatest need for assistance under this section, as determined by the Secretary;\n**(2)**\nidentify vulnerabilities and risks in disadvantaged communities and prioritize projects to benefit such communities and promote equity in resilience;\n**(3)**\ndemonstrate a broad approach to resilience, as such term is defined in subsection (j)(3); and\n**(4)**\nprovide for subgrants to entities that adhere to prevailing wage provisions as published by the Department of Labor.\n##### (f) Amount\nThe Secretary shall award formula grants in an amount sufficient to provide funding to a grantee to cover a minimum of 24 months of grant activities.\n##### (g) Technical assistance\nThe Secretary shall, in consultation with the Administrator of the Federal Emergency Management Agency, the Secretary of Commerce, the Secretary of the Interior, and such other heads of Federal agencies as the Secretary considers appropriate, provide technical assistance to grantees regarding developing resiliency frameworks and implementing resiliency strategies.\n##### (h) Administrative costs\nOf any amounts made available for grants under this section, the Secretary may use 1.0 percent for\u2014\n**(1)**\nthe costs of administering the program under this section for such grants; and\n**(2)**\nfor providing technical assistance\u2014\n**(A)**\nto applicants for such grants; and\n**(B)**\nunder subsection (g).\n##### (i) Reports to HUD\nNot later than 90 days after the end of each fiscal year for which a grantee receives a grant under this section, the grantee shall submit a report to the Secretary regarding the use of such grant amounts, which shall include\u2014\n**(1)**\na description of the activities undertaken by the grantee using such grant amounts;\n**(2)**\nidentification of the costs of each of the services provided using such grant amounts; and\n**(3)**\nassessments of the effectiveness of the grant program under this section and the programs carried out by the resiliency office of the grantee and recommendations for improving such programs.\n##### (j) Definitions\nIn this section:\n**(1) Disadvantaged community**\nThe term disadvantaged community shall have such meaning as shall be established by regulation by the Secretary, in consultation with the heads of other appropriate Federal agencies, using such indicators and metrics as the Secretary considers appropriate.\n**(2) Grantee**\nThe term grantee means a State, territory, or Indian tribe to which a grant under this section is made.\n**(3) Indian tribe**\nThe term Indian tribe has the meaning given such term in section 4 of the Native American Housing and Self-Determination Act of 1996 ( 25 U.S.C. 4103 ).\n**(4) Resilience**\nThe term resilience means, with respect to a community, the ability to rebound, positively adapt to, or thrive amidst changing conditions or challenges, including human-caused and natural disasters, and to maintain quality of life, healthy growth, durable systems, economic vitality, and conservation of resources for present and future generations.\n**(5) Secretary**\nThe term Secretary means the Secretary of Housing and Urban Development.\n**(6) State**\nThe term State means a State of the United States and the District of Columbia.\n**(7) Territory**\nThe term territory means the Commonwealth of Puerto Rico, Guam, the Northern Mariana Islands, the Virgin Islands, and American Samoa.\n##### (k) Funding\n**(1) Authorization of appropriations**\nThere is authorized to be appropriated for grants under this section $100,000,000 for each of fiscal years 2025 through 2030.\n**(2) Set-aside for Indian tribes**\nOf any amounts appropriated for a fiscal year for grants under this section, the Secretary shall reserve 10 percent for grants to Indian tribes. The Secretary shall allocate such amounts reserved, among Indian tribes having applications for grants under this section for such fiscal year approved by the Secretary, on the basis of a competition conducted pursuant to specific criteria for the selection of Indian tribes to receive such amounts. The criteria shall be contained in a regulation promulgated by the Secretary, in consultation with the Secretary of the Interior, after notice and opportunity for public comment.",
      "versionDate": "2025-12-17",
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
        "updateDate": "2026-01-22T15:41:01Z"
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
      "date": "2025-12-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6785ih.xml"
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
      "title": "CLEAR Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-21T05:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CLEAR Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-21T05:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Championing Local Efforts to Advance Resilience Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-21T05:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the Secretary of Housing and Urban Development to make grants to States, territories, and Indian tribes to support local resiliency offices, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-21T05:33:33Z"
    }
  ]
}
```
