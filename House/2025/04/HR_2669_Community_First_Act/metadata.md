# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2669?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2669
- Title: Community First Act
- Congress: 119
- Bill type: HR
- Bill number: 2669
- Origin chamber: House
- Introduced date: 2025-04-07
- Update date: 2025-05-05T12:14:12Z
- Update date including text: 2025-05-05T12:14:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-07: Introduced in House
- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-04-10 - IntroReferral: Sponsor introductory remarks on measure. (CR H1568)
- Latest action: 2025-04-07: Introduced in House

## Actions

- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-04-10 - IntroReferral: Sponsor introductory remarks on measure. (CR H1568)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-07",
    "latestAction": {
      "actionDate": "2025-04-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2669",
    "number": "2669",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "B001324",
        "district": "1",
        "firstName": "Wesley",
        "fullName": "Rep. Bell, Wesley [D-MO-1]",
        "lastName": "Bell",
        "party": "D",
        "state": "MO"
      }
    ],
    "title": "Community First Act",
    "type": "HR",
    "updateDate": "2025-05-05T12:14:12Z",
    "updateDateIncludingText": "2025-05-05T12:14:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "B00100",
      "actionDate": "2025-04-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H1568)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-07",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-07",
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
          "date": "2025-04-07T16:00:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "MO"
    },
    {
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "NY"
    },
    {
      "bioguideId": "F000481",
      "district": "2",
      "firstName": "Shomari",
      "fullName": "Rep. Figures, Shomari [D-AL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Figures",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "AL"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "NJ"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "IL"
    },
    {
      "bioguideId": "B000490",
      "district": "2",
      "firstName": "Sanford",
      "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bishop",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "GA"
    },
    {
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "MS"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "MI"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "GA"
    },
    {
      "bioguideId": "I000058",
      "district": "4",
      "firstName": "Glenn",
      "fullName": "Rep. Ivey, Glenn [D-MD-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Ivey",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "MD"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "DC"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "AZ"
    },
    {
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "True",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "TX"
    },
    {
      "bioguideId": "W000808",
      "district": "24",
      "firstName": "Frederica",
      "fullName": "Rep. Wilson, Frederica S. [D-FL-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Wilson",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2669ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2669\nIN THE HOUSE OF REPRESENTATIVES\nApril 7, 2025 Mr. Bell (for himself, Mr. Cleaver , Ms. Clarke of New York , Mr. Figures , Mrs. McIver , Mr. Jackson of Illinois , Mr. Bishop , Mr. Thompson of Mississippi , Mr. Thanedar , Mr. Johnson of Georgia , Mr. Ivey , Ms. Norton , Ms. Ansari , Ms. Crockett , and Ms. Wilson of Florida ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo establish a new Justice Department grant program to reduce the number of individuals incarcerated in local jails, reduce the number of days individuals are incarcerated in local jails, and support community-led local justice reinvestment.\n#### 1. Short title\nThis Act may be cited as the Community First Pretrial Reform Act or the Community First Act .\n#### 2. Grants authorized\n##### (a) Grants authorized\nThe Attorney General, acting through the Bureau of Justice Assistance, shall make grants to eligible partnerships for purposes of reducing the number of individuals in jails operated by units of local government and the number of days such individuals spend in jail as follows:\n**(1)**\nGrants for analysis and planning, which shall be used to\u2014\n**(A)**\ncollect and analyze local criminal justice and incarceration data, including data on equity disparities; and\n**(B)**\ndevelop a strategic, collaborative plan to decrease local jail incarceration that shall be public facing.\n**(2)**\nGrants for implementation of the plan described in paragraph (1)(B) and which may be used for activities to reduce the number of individuals incarcerated in local jails and to reduce the number of days that individuals are so incarcerated including\u2014\n**(A)**\nreducing the use of cash bail;\n**(B)**\nreducing revocations of conditional release;\n**(C)**\ncreating or increasing the availability of pretrial services, including efforts undertaken in collaboration with community-based organizations and nonprofits;\n**(D)**\ninvesting in case processing and processes to reduce overall time to disposition and time between court events;\n**(E)**\nensuring early assignment of counsel and presence of counsel at individuals\u2019 first court appearance or bail hearing;\n**(F)**\nproviding training to various actors within the criminal justice system on indigent defense that is aligned with best practices in the field;\n**(G)**\ncreating or expanding diversion programs that do not require an individual to enter into a guilty plea and do not use incarceration as a sanction for noncompliance\u2014\n**(i)**\nat the pre-arrest phase;\n**(ii)**\nat the pre-booking phase; and\n**(iii)**\nat the post-booking phase; or\n**(H)**\nany other emerging, promising, or evidence-based practices that an eligible partnership proposes and the Attorney General deems likely to reduce local jail incarceration.\n##### (b) Eligible partnership\nAn eligible partnership is a partnership between not less than two of the following:\n**(1)**\nA unit of local government.\n**(2)**\nA territory.\n**(3)**\nAn Indian tribe.\n**(4)**\nA nonprofit organization.\n##### (c) Application\nAn application for a grant shall include the following:\n**(1)**\nDetails of the range of pretrial services available within the jurisdiction where the jail being targeted for incarceration rate reduction under this Act is located.\n**(2)**\nA plan to ensure that individuals in pretrial contact with the justice system will be subject to the least restrictive conditions or combination of conditions necessary to reasonably address the imminent risk of willful flight or the risk of imminent threat of serious physical harm to a reasonably identifiable person.\n**(3)**\nA plan for ongoing process evaluation and outcome evaluation.\n**(4)**\nEither\u2014\n**(A)**\ndata\u2014\n**(i)**\ndisaggregated by key demographic indicators, including factors such as community background and identity, on incarceration for correctional facilities within the local jurisdiction for each of the last five calendar years that includes\u2014\u2014\n**(I)**\nthe average daily population;\n**(II)**\nthe percentage of individuals held pretrial and post-conviction; and\n**(III)**\nthe average length of stay for individuals held pretrial and post-conviction; and\n**(ii)**\ndisaggregated by key demographic indicators on arrests made by all law enforcement entities operating within the local jurisdiction over each of the last five calendar years; or\n**(B)**\nin the event that elements of such incarceration or arrest data are not able to be compiled and reported, a comprehensive plan to obtain as much of the unavailable data as possible within the first year of the award.\n#### 3. Requirements\n##### (a) In general\nGrantees shall\u2014\n**(1)**\nconsult in all phases of planning, implementation, and evaluation with municipal, county, and State law enforcement agencies, courts in the local jurisdiction, public defense organizations and criminal defense practitioners in the local jurisdiction, local substance use and mental health authorities, local community members, local community members who have been justice-involved, and community-based organizations and service providers;\n**(2)**\nanalyze local jail incarceration and arrest data to identify the drivers of jail incarceration and equity disparities and ground jail population reduction strategies in that data;\n**(3)**\nreduce incarceration rates by no less than 5 percent the first year of an implementation grant, 10 percent in each subsequent year, and 50 percent by the end of the grant period;\n**(4)**\nin consultation with the Bureau of Justice Assistance\u2014\n**(A)**\nadopt and implement a methodology for measuring equity disparities in jail incarceration;\n**(B)**\nset goals for the reduction of equity jail incarceration disparities; and\n**(C)**\ndecrease levels of incarceration across all races and ethnicities;\n**(5)**\nengage an external evaluator to coordinate data collection and reporting in an ongoing fashion and perform both a process and outcome evaluation, with support from the Bureau of Justice Assistance; and\n**(6)**\nuse financial savings created through decreased incarceration to sustain programmatic and community-based efforts to reduce jail incarceration.\n##### (b) Grant oversight requirement\n**(1) In general**\nIf a grantee fails to meet the incarceration rate and equity disparities reduction requirements under subsection (a)(3) in any year of the award, the Bureau of Justice Assistance shall perform an audit of the use of their award and the grantee shall implement new strategies based on that audit. If a grantee fails to meet the incarceration rate and equity disparities reduction requirements under subsection (a)(3) in any two consecutive years of the award, the Attorney General shall terminate the award.\n**(2) Modification authority**\nThe Bureau of Justice Assistance may grant a modification to the incarceration rate reduction requirement under subsection (a)(3) if the Bureau determines after an audit that the failure to meet the incarceration rate reduction requirement was caused by an increase in population in the covered jurisdiction. If a grantee fails to meet the modified reduction requirements in any two subsequent years of the award, the Attorney General shall terminate the award.\n#### 4. Grant amounts\n##### (a) Planning grants\nA grant under section 2(a)(1) may be for not more than $100,000 for a single grantee, and shall be for a term of 1 year.\n##### (b) Implementation grants\nA grant under section 2(a)(2) shall be for a term of 6 years, and shall be structured as follows:\n**(1)**\nFor the first year of the grant term, an amount shall be disbursed that is to be not less than $500,000 and not more than $3,000,000, contingent upon acceptance of a grantee\u2019s proposed budget for activities under the grant, which may be subject to revision during the award process.\n**(2)**\nAward amounts shall decrease annually by\u2014\n**(A)**\n10 percent in the second year;\n**(B)**\n15 percent in the third year;\n**(C)**\n20 percent in the fourth year; and\n**(D)**\n25 percent in the fifth year.\n**(3)**\nAward amounts during the sixth year of the award may not be used for programmatic activities and shall support only program evaluation and the drafting of a final report, and such funds shall be available to the grantees until expended.\n#### 5. Selection priority\nIn selecting grantees, the Attorney General shall\u2014\n**(1)**\ngive priority to applicants from jurisdictions with the highest incarceration rates that are not already in decline and whose applications contain the most ambitious and attainable plans for reducing that rate;\n**(2)**\ngive additional priority to applicants from jurisdictions seeking to use funds under this Act to prevent the local government from expanding the number of beds in local correctional facilities;\n**(3)**\nfor any year in which there will only be one new or ongoing award, ensure that a small metropolitan, micropolitan, or noncore area is the recipient of the award;\n**(4)**\nfor any year in which there will be more than one new or ongoing award, ensure that small metropolitan, micropolitan, or noncore areas are the recipients of at least two awards; and\n**(5)**\nfor any year in which there will be three or more new or ongoing awards, ensure that no more than one large central metropolitan area is a recipient of an award.\n#### 6. Definitions\nIn this Act:\n**(1)**\nThe term conditional release means probation, parole, supervised release, home confinement, community supervision, and other practices under which an individual is supervised in the community by the criminal justice system and may be incarcerated if found in violation of the conditions of their release.\n**(2)**\nThe term diversion means a program or practice that\u2014\n**(A)**\nplaces individuals who come into contact with the criminal justice system into alternative processes outside the standard scope of criminal justice processing; and\n**(B)**\nreduces an individual\u2019s involvement in the criminal justice system in both the short and long term.\n**(3)**\nThe term emerging practice means a program or practice\u2014\n**(A)**\nwith initial implementation resulting in decreased local jail incarceration in one or more communities; and\n**(B)**\nthat will be evaluated through a well-designed and rigorous study.\n**(4)**\nThe term evidence-based practice means a program or practice that\u2014\n**(A)**\nis demonstrated to be effective when implemented with fidelity;\n**(B)**\nis based on a clearly articulated and empirically supported theory;\n**(C)**\nhas measurable outcomes relevant to reducing jail incarceration, including a detailed description of the outcomes produced in a particular population, whether urban or rural; and\n**(D)**\nhas been scientifically tested and proven effective through randomized control studies or comparison group studies and with the ability to replicate and scale.\n**(5)**\nThe term micropolitan area has the meaning established under the Centers for Disease Control and Prevention\u2019s (hereinafter in this Act referred to as the CDC ) National Center for Health Statistics Urban-Rural Classification Scheme for Counties.\n**(6)**\nThe term small metropolitan area has the meaning established under the CDC\u2019s National Center for Health Statistics Urban-Rural Classification Scheme for Counties.\n**(7)**\nThe term noncore areas has the meaning established under the CDC\u2019s National Center for Health Statistics Urban-Rural Classification Scheme for Counties.\n**(8)**\nThe term post-booking diversion means a program or practice that diverts individuals from formal criminal justice system processing after formal intake processing into jail.\n**(9)**\nThe term pre-booking diversion means a program or practice that diverts individuals from formal criminal justice system processing prior to arrest or prior to formal intake processing into jail.\n**(10)**\nThe term promising practice means a program or practice that\u2014\n**(A)**\nis demonstrated to be effective based on positive outcomes relevant to reducing jail incarceration from one or more objective, independent, and scientifically valid evaluations, as documented in writing to the Attorney General; and\n**(B)**\nwill be evaluated through a well-designed and rigorous study.\n**(11)**\nThe term equity disparities means an measurable differences in outcomes, treatment, or access to services within the criminal justice system that are correlated with demographic factors such community background and identity.\n#### 7. Authorization of appropriations\nThere are authorized to be appropriated\u2014\n**(1)**\n$20,000,000 for each of fiscal years 2026 through 2030 for planning grants; and\n**(2)**\n$100,000,000 for each of fiscal years 2026 through 2030 for implementation grants, of which 10 percent of any appropriated amount is reserved specifically for evaluation activities.",
      "versionDate": "2025-04-07",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-05-05T12:14:12Z"
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
      "date": "2025-04-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2669ih.xml"
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
      "title": "Community First Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-16T08:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Community First Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-16T08:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Community First Pretrial Reform Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-16T08:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a new Justice Department grant program to reduce the number of individuals incarcerated in local jails, reduce the number of days individuals are incarcerated in local jails, and support community-led local justice reinvestment.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-16T08:33:21Z"
    }
  ]
}
```
