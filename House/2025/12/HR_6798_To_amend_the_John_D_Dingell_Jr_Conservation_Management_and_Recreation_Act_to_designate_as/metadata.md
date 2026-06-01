# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6798?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6798
- Title: Calumet National Heritage Area Act
- Congress: 119
- Bill type: HR
- Bill number: 6798
- Origin chamber: House
- Introduced date: 2025-12-17
- Update date: 2026-04-10T19:38:35Z
- Update date including text: 2026-04-10T19:38:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-17: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-12-17: Introduced in House

## Actions

- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Referred to the House Committee on Natural Resources.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6798",
    "number": "6798",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "K000385",
        "district": "2",
        "firstName": "Robin",
        "fullName": "Rep. Kelly, Robin L. [D-IL-2]",
        "lastName": "Kelly",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Calumet National Heritage Area Act",
    "type": "HR",
    "updateDate": "2026-04-10T19:38:35Z",
    "updateDateIncludingText": "2026-04-10T19:38:35Z"
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
      "text": "Referred to the House Committee on Natural Resources.",
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
          "date": "2025-12-17T14:02:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "bioguideId": "Y000067",
      "district": "2",
      "firstName": "Rudy",
      "fullName": "Rep. Yakym, Rudy [R-IN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Yakym",
      "party": "R",
      "sponsorshipDate": "2025-12-17",
      "state": "IN"
    },
    {
      "bioguideId": "M001214",
      "district": "1",
      "firstName": "Frank",
      "fullName": "Rep. Mrvan, Frank J. [D-IN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mrvan",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "IN"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "IL"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "IL"
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
      "sponsorshipDate": "2025-12-17",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6798ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6798\nIN THE HOUSE OF REPRESENTATIVES\nDecember 17, 2025 Ms. Kelly of Illinois (for herself, Mr. Yakym , Mr. Mrvan , Mr. Davis of Illinois , Mr. Casten , and Mr. Jackson of Illinois ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo amend the John D. Dingell, Jr. Conservation, Management, and Recreation Act to designate as a component of the National Heritage Area System the Calumet National Heritage Area in the States of Indiana and Illinois, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Calumet National Heritage Area Act .\n#### 2. Findings\nCongress finds that\u2014\n**(1)**\nthe Calumet region is composed of\u2014\n**(A)**\n3 counties in the State of Indiana; and\n**(B)**\nportions of 2 counties in the State of Illinois;\n**(2)**\ntaken as a whole, the Calumet region\u2014\n**(A)**\npossesses exceptional cultural, natural, and historical resources that form a cohesive and nationally distinctive landscape;\n**(B)**\nshowcases landscapes that arose from the unprecedented encounter of United States industrial urbanization with a richly biodiverse natural region at the southern end of Lake Michigan; and\n**(C)**\noffers compelling educational opportunities relating to\u2014\n**(i)**\nthe manner in which industrial progress forged dramatic changes to the natural world;\n**(ii)**\nthe importance of environmental conservation and restoration, innovation, and change for industries and workers; and\n**(iii)**\nthe range of cultural practices brought to the Calumet region by the large numbers of immigrants and migrants who settled in the Calumet region;\n**(3)**\nthere is a national interest in conserving, restoring, promoting, and interpreting the benefits of the Calumet National Heritage Area for\u2014\n**(A)**\nthe residents of the Calumet region; and\n**(B)**\nvisitors to the Calumet National Heritage Area;\n**(4)**\nthe nationally significant historical and cultural resources located in the Calumet National Heritage Area represent unique aspects of the heritage of the United States;\n**(5)**\nthe Calumet region\u2014\n**(A)**\nwas previously designated as a natural botanical preserve; and\n**(B)**\nwas the site of early advances in the science of ecology;\n**(6)**\nwith respect to the economic development of the United States\u2014\n**(A)**\nthe post-Civil War industrial boom in the Calumet region made the Calumet region the largest industrial district in the world during the first half of the 20th century;\n**(B)**\nthe Calumet region remains the leading steel producing region in the United States;\n**(C)**\nthe economic development took place at the water, rail, and highway transportation crossroads of the United States; and\n**(D)**\nindustrialists pioneered new methods of housing employees in industrial towns at Pullman, Marktown, and Gary;\n**(7)**\nemployees that were drawn to the Calumet region made the Calumet region a crucible of working class and ethnic cultures;\n**(8)**\nnew approaches to natural resource management in an industrial region were developed in the Calumet region;\n**(9)**\nsignificant historical and cultural sites in the Calumet region include\u2014\n**(A)**\nthe ongoing presence of the steel industry in the United States, including the most recently constructed integrated steelworks and the largest operating integrated steelworks;\n**(B)**\nPullman National Historical Park;\n**(C)**\nIndiana Dunes National Park;\n**(D)**\na National Historic Landmark;\n**(E)**\n4 Historic American Engineering Record sites;\n**(F)**\n5 Historic American Buildings Survey sites;\n**(G)**\n2 National Scenic Byways;\n**(H)**\n2 units of the National Water Trails System; and\n**(I)**\n2 National Underground Railroad Network to Freedom sites;\n**(10)**\nnationally significant natural and physical resources in the Calumet region include spectacular natural, scenic, and recreational assets, including\u2014\n**(A)**\nIndiana Dunes National Park, 1 of the most species-rich units of the National Park System, including the critical conservation land that buffers the unit;\n**(B)**\noutstanding examples of glaciated landscapes that illustrate ecological succession;\n**(C)**\n5 national natural landmarks;\n**(D)**\n48,000 acres of land protected outside the boundary of the Indiana Dunes National Park, a significant record of urban conservation by land trusts, local park districts, and forest preserve districts; and\n**(E)**\nan active legacy of ecological restoration, including on the Grand Calumet Area of Concern and at hundreds of sites benefitting from volunteer contributions;\n**(11)**\nlocal public and private partnerships based on the visions of the community and region that are working together to promote the stewardship, enhancement, and interpretation of the resources of the Calumet National Heritage Area;\n**(12)**\nto promote the goals described in paragraph (11), local residents, organizations, and governments support the establishment of a national heritage area, as indicated in the Calumet National Heritage Area Feasibility Study approved by the National Park Service; and\n**(13)**\nthe designation of the Calumet National Heritage Area would enhance the efforts to promote the cultural, natural, historical, and recreational resources of the Calumet region that have been made by\u2014\n**(A)**\nthe States of Indiana and Illinois;\n**(B)**\npolitical subdivisions of the States of Indiana and Illinois;\n**(C)**\nthe Field Museum of Natural History;\n**(D)**\nIndiana Dunes Tourism;\n**(E)**\nthe South Shore Convention and Visitors Authority;\n**(F)**\nvolunteer organizations; and\n**(G)**\nprivate businesses.\n#### 3. Designation of Calumet National Heritage Area\n##### (a) Designation\nSection 6001(a) of the John D. Dingell, Jr. Conservation, Management, and Recreation Act ( Public Law 116\u20139 ; 133 Stat. 768; 136 Stat. 6163) is amended by adding at the end the following:\n(14) Calumet National Heritage Area (A) In general There is established as a component of the National Heritage Area System the Calumet National Heritage Area in the States of Indiana and Illinois, as depicted on the map on page 25 of the Calumet National Heritage Area Feasibility Study, dated April 14, 2018, as subsequently modified, the boundaries of which start at 71st Street and Lake Michigan in Chicago and proceed west along 71st Street to Western Avenue, then south on Western Avenue to 95th Street, then west on 95th Street to Pulaski Road, then south on Pulaski Road to I\u201357, then south on I\u201357 to Crete-Monee Road, then east on Crete-Monee Road, continuing on West New Monee Road to end at State Street, and then extend to the Indiana State Line, with Lake, Porter, and LaPorte Counties included. (B) Local coordinating entity The Calumet Heritage Partnership shall be the local coordinating entity for the National Heritage Area designated by subparagraph (A). .\n##### (b) Management plan\nFor the purposes of section 6001(c) of the John D. Dingell, Jr. Conservation, Management, and Recreation Act ( Public Law 116\u20139 ; 133 Stat. 772; 136 Stat. 6173), the local coordinating entity for the Calumet National Heritage Area designated under the amendment made by subsection (a) shall submit to the Secretary of the Interior for approval a proposed management plan for the Calumet National Heritage Area not later than 3 years after the date of enactment of this Act.\n##### (c) Termination of authority\nFor the purposes of subsection (g)(4) of section 6001 of the John D. Dingell, Jr. Conservation, Management, and Recreation Act ( Public Law 116\u20139 ; 133 Stat. 776), the authority of the Secretary of the Interior to provide assistance under that section for the Calumet National Heritage Area designated under the amendment made by subsection (a) shall terminate on the date that is 15 years after the date of enactment of this Act.",
      "versionDate": "2025-12-17",
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
        "actionDate": "2025-12-16",
        "text": "Read twice and referred to the Committee on Energy and Natural Resources."
      },
      "number": "3501",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Calumet National Heritage Area Act",
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
        "name": "Public Lands and Natural Resources",
        "updateDate": "2026-01-21T16:19:56Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6798ih.xml"
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
      "title": "Calumet National Heritage Area Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-21T05:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Calumet National Heritage Area Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-21T05:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the John D. Dingell, Jr. Conservation, Management, and Recreation Act to designate as a component of the National Heritage Area System the Calumet National Heritage Area in the States of Indiana and Illinois, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-21T05:18:26Z"
    }
  ]
}
```
