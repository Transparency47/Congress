# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6815?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6815
- Title: Environmental Justice Screening Tool Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6815
- Origin chamber: House
- Introduced date: 2025-12-17
- Update date: 2026-01-13T09:05:53Z
- Update date including text: 2026-01-13T09:05:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-17: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-17 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-12-17: Introduced in House

## Actions

- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-17 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6815",
    "number": "6815",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "R000620",
        "district": "29",
        "firstName": "Luz",
        "fullName": "Rep. Rivas, Luz M. [D-CA-29]",
        "lastName": "Rivas",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Environmental Justice Screening Tool Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-13T09:05:53Z",
    "updateDateIncludingText": "2026-01-13T09:05:53Z"
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
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-17",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
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
          "date": "2025-12-17T14:07:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-12-17T14:07:30Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "AZ"
    },
    {
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "CA"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "IN"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "LA"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "LA"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "IL"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "NY"
    },
    {
      "bioguideId": "H001103",
      "district": "0",
      "firstName": "Pablo",
      "fullName": "Rescom. Hern\u00e1ndez, Pablo Jose [D-PR-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Hern\u00e1ndez",
      "middleName": "Jose",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "PR"
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
      "sponsorshipDate": "2025-12-17",
      "state": "DC"
    },
    {
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "PA"
    },
    {
      "bioguideId": "P000610",
      "district": "0",
      "firstName": "Stacey",
      "fullName": "Del. Plaskett, Stacey E. [D-VI-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Plaskett",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "VI"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "FL"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "FL"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "MI"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2026-01-12",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6815ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6815\nIN THE HOUSE OF REPRESENTATIVES\nDecember 17, 2025 Ms. Rivas (for herself, Ms. Ansari , Ms. Barrag\u00e1n , Mr. Carson , Mr. Carter of Louisiana , Mr. Fields , Mr. Garc\u00eda of Illinois , Mr. Goldman of New York , Mr. Hern\u00e1ndez , Ms. Norton , Ms. Lee of Pennsylvania , Ms. Plaskett , and Mr. Soto ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Natural Resources , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo require the Administrator of the Environmental Protection Agency to develop a geospatial mapping tool to identify disproportionately burdened communities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Environmental Justice Screening Tool Act of 2025 .\n#### 2. Geospatial mapping tool of Environmental Protection Agency to identify disproportionately burdened communities\n##### (a) In general\nNot later than one year after the date of the enactment of this Act, the Administrator of the Environmental Protection Agency shall develop and publish on a publicly available website of the Environmental Protection Agency a geospatial mapping tool to identify disproportionately burdened communities, to be known as the Environmental Justice Screening Tool .\n##### (b) Determination of disproportionate burden thresholds\n**(1) Thresholds**\nIn developing the tool under subsection (a), the Administrator shall, for each category of factors described in paragraph (2)\u2014\n**(A)**\ndetermine a threshold for a census tract to be considered disproportionately burdened with respect to that category; and\n**(B)**\nensure the tool identifies as disproportionately burdened with respect to that category any community within a census tract that meets such threshold.\n**(2) Categories of factors**\nThe categories of factors described in this paragraph are the following:\n**(A)**\nEnvironmental factors, including the following:\n**(i)**\nAir quality.\n**(ii)**\nAccess to safe drinking water.\n**(iii)**\nProximity to any environmental hazard or potential environmental hazard, including\u2014\n**(I)**\na site that is listed on the National Priorities List developed by the President in accordance with section 105(a)(8)(B) of the Comprehensive Environmental Response, Compensation, and Liability Act of 1980 ( 42 U.S.C. 9605(a)(8)(B) );\n**(II)**\na brownfield site;\n**(III)**\na well, pipeline, refinery, or other facility relating to the production, refining, or downstream processing of oil or gas; or\n**(IV)**\na municipal solid waste landfill unit.\n**(B)**\nClimate change factors, including the following:\n**(i)**\nFrequency of natural disasters, including wildfires, hurricanes, earthquakes, tornadoes, landslides, and flooding.\n**(ii)**\nFrequency of extreme drought.\n**(C)**\nHuman health factors, including the following:\n**(i)**\nRate of asthma or chronic obstructive pulmonary disease.\n**(ii)**\nRate of diabetes.\n**(iii)**\nRate of obesity.\n**(iv)**\nRate of preterm or low birth weight births.\n**(v)**\nRate of maternal mortality.\n**(D)**\nEconomic factors, including the following:\n**(i)**\nPoverty rate.\n**(ii)**\nUnemployment rate.\n**(iii)**\nAccess to affordable housing.\n**(iv)**\nAccess to hospitals and other health care facilities.\n**(E)**\nSocial factors, including the following:\n**(i)**\nRacial or ethnic demographics.\n**(ii)**\nEducational attainment.\n**(iii)**\nPopulation density.\n**(iv)**\nAge distribution.\n**(v)**\nGender distribution.\n**(F)**\nAny other category of factors the Administrator may prescribe.\n**(3) Solicitation of feedback and data**\nThe Administrator shall solicit feedback and data regarding the thresholds under paragraph (1) and the categories of factors described in paragraph (2) from institutions of higher education, nonprofit organizations, community-based organizations, and State, local, and tribal government officials, as determined appropriate by the Administrator.\n##### (c) Annual review and report\nNot later than one year after the date on which the Administrator publishes the tool under subsection (a), and annually thereafter, the Administrator shall\u2014\n**(1)**\nreview the data informing the tool and, as the Administrator determines appropriate, update the tool; and\n**(2)**\nsubmit to the appropriate congressional committees a report on the implementation of this section that contains, at a minimum\u2014\n**(A)**\na description of any updates made to the tool; and\n**(B)**\nan identification of any census tract that, as a result of any such update, became identified as disproportionately burdened under the tool or ceased to be so identified.\n##### (d) Adoption across Federal government\nBeginning not later than one year after the date on which the Administrator publishes the tool under subsection (a), the head of each Federal department or agency shall, to the extent and in the manner determined appropriate by such head, adopt such tool for use in identifying disproportionately burdened communities and prioritizing funding or other resources of the department or agency to the benefit of communities so identified.\n##### (e) Definitions\nIn this section:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Appropriations and the Committee on Energy and Commerce of the House of Representatives; and\n**(B)**\nthe Committee on Appropriations and the Committee on Environment and Public Works of the Senate.\n**(2) Brownfield site**\nThe term brownfield site has the meaning given that term in section 101 of the Comprehensive Environmental Response, Compensation, and Liability Act of 1980 ( 42 U.S.C. 9601 ).\n**(3) Institution of higher education**\nThe term institution of higher education has the meaning given such term in section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 ).\n**(4) State**\nThe term State includes each territory or possession of the United States.",
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
        "name": "Environmental Protection",
        "updateDate": "2025-12-19T15:45:31Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6815ih.xml"
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
      "title": "Environmental Justice Screening Tool Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-18T10:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Environmental Justice Screening Tool Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-18T10:08:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Administrator of the Environmental Protection Agency to develop a geospatial mapping tool to identify disproportionately burdened communities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-18T10:03:46Z"
    }
  ]
}
```
