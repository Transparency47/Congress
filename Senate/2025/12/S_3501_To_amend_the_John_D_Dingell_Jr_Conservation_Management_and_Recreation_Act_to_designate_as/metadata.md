# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3501?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3501
- Title: Calumet National Heritage Area Act
- Congress: 119
- Bill type: S
- Bill number: 3501
- Origin chamber: Senate
- Introduced date: 2025-12-16
- Update date: 2026-04-10T19:38:35Z
- Update date including text: 2026-04-10T19:38:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-16: Introduced in Senate
- 2025-12-16 - IntroReferral: Introduced in Senate
- 2025-12-16 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- Latest action: 2025-12-16: Introduced in Senate

## Actions

- 2025-12-16 - IntroReferral: Introduced in Senate
- 2025-12-16 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-16",
    "latestAction": {
      "actionDate": "2025-12-16",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3501",
    "number": "3501",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "Y000064",
        "district": "",
        "firstName": "Todd",
        "fullName": "Sen. Young, Todd [R-IN]",
        "lastName": "Young",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "Calumet National Heritage Area Act",
    "type": "S",
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
      "actionDate": "2025-12-16",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-16",
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
          "date": "2025-12-16T21:04:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "systemCode": "sseg00",
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
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "IL"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "IN"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3501is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3501\nIN THE SENATE OF THE UNITED STATES\nDecember 16, 2025 Mr. Young (for himself, Mr. Durbin , Mr. Banks , and Ms. Duckworth ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo amend the John D. Dingell, Jr. Conservation, Management, and Recreation Act to designate as a component of the National Heritage Area System the Calumet National Heritage Area in the States of Indiana and Illinois, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Calumet National Heritage Area Act .\n#### 2. Findings\nCongress finds that\u2014\n**(1)**\nthe Calumet region is composed of\u2014\n**(A)**\n3 counties in the State of Indiana; and\n**(B)**\nportions of 2 counties in the State of Illinois;\n**(2)**\ntaken as a whole, the Calumet region\u2014\n**(A)**\npossesses exceptional cultural, natural, and historical resources that form a cohesive and nationally distinctive landscape;\n**(B)**\nshowcases landscapes that arose from the unprecedented encounter of United States industrial urbanization with a richly biodiverse natural region at the southern end of Lake Michigan; and\n**(C)**\noffers compelling educational opportunities relating to\u2014\n**(i)**\nthe manner in which industrial progress forged dramatic changes to the natural world;\n**(ii)**\nthe importance of environmental conservation and restoration, innovation, and change for industries and workers; and\n**(iii)**\nthe range of cultural practices brought to the Calumet region by the large numbers of immigrants and migrants who settled in the Calumet region;\n**(3)**\nthere is a national interest in conserving, restoring, promoting, and interpreting the benefits of the Calumet National Heritage Area for\u2014\n**(A)**\nthe residents of the Calumet region; and\n**(B)**\nvisitors to the Calumet National Heritage Area;\n**(4)**\nthe nationally significant historical and cultural resources located in the Calumet National Heritage Area represent unique aspects of the heritage of the United States;\n**(5)**\nthe Calumet region\u2014\n**(A)**\nwas previously designated as a natural botanical preserve; and\n**(B)**\nwas the site of early advances in the science of ecology;\n**(6)**\nwith respect to the economic development of the United States\u2014\n**(A)**\nthe post-Civil War industrial boom in the Calumet region made the Calumet region the largest industrial district in the world during the first half of the 20th century;\n**(B)**\nthe Calumet region remains the leading steel producing region in the United States;\n**(C)**\nthe economic development took place at the water, rail, and highway transportation crossroads of the United States; and\n**(D)**\nindustrialists pioneered new methods of housing employees in industrial towns at Pullman, Marktown, and Gary;\n**(7)**\nemployees that were drawn to the Calumet region made the Calumet region a crucible of working class and ethnic cultures;\n**(8)**\nnew approaches to natural resource management in an industrial region were developed in the Calumet region;\n**(9)**\nsignificant historical and cultural sites in the Calumet region include\u2014\n**(A)**\nthe ongoing presence of the steel industry in the United States, including the most recently constructed integrated steelworks and the largest operating integrated steelworks;\n**(B)**\nPullman National Historical Park;\n**(C)**\nIndiana Dunes National Park;\n**(D)**\na National Historic Landmark;\n**(E)**\n4 Historic American Engineering Record sites;\n**(F)**\n5 Historic American Buildings Survey sites;\n**(G)**\n2 National Scenic Byways;\n**(H)**\n2 units of the National Water Trails System; and\n**(I)**\n2 National Underground Railroad Network to Freedom sites;\n**(10)**\nnationally significant natural and physical resources in the Calumet region include spectacular natural, scenic, and recreational assets, including\u2014\n**(A)**\nIndiana Dunes National Park, 1 of the most species-rich units of the National Park System, including the critical conservation land that buffers the unit;\n**(B)**\noutstanding examples of glaciated landscapes that illustrate ecological succession;\n**(C)**\n5 national natural landmarks;\n**(D)**\n48,000 acres of land protected outside the boundary of the Indiana Dunes National Park, a significant record of urban conservation by land trusts, local park districts, and forest preserve districts; and\n**(E)**\nan active legacy of ecological restoration, including on the Grand Calumet Area of Concern and at hundreds of sites benefitting from volunteer contributions;\n**(11)**\nlocal public and private partnerships based on the visions of the community and region that are working together to promote the stewardship, enhancement, and interpretation of the resources of the Calumet National Heritage Area;\n**(12)**\nto promote the goals described in paragraph (11), local residents, organizations, and governments support the establishment of a national heritage area, as indicated in the Calumet National Heritage Area Feasibility Study approved by the National Park Service; and\n**(13)**\nthe designation of the Calumet National Heritage Area would enhance the efforts to promote the cultural, natural, historical, and recreational resources of the Calumet region that have been made by\u2014\n**(A)**\nthe States of Indiana and Illinois;\n**(B)**\npolitical subdivisions of the States of Indiana and Illinois;\n**(C)**\nthe Field Museum of Natural History;\n**(D)**\nIndiana Dunes Tourism;\n**(E)**\nthe South Shore Convention and Visitors Authority;\n**(F)**\nvolunteer organizations; and\n**(G)**\nprivate businesses.\n#### 3. Designation of Calumet National Heritage Area\n##### (a) Designation\nSection 6001(a) of the John D. Dingell, Jr. Conservation, Management, and Recreation Act ( Public Law 116\u20139 ; 133 Stat. 768; 136 Stat. 6163) is amended by adding at the end the following:\n(14) Calumet National Heritage Area (A) In general There is established as a component of the National Heritage Area System the Calumet National Heritage Area in the States of Indiana and Illinois, as depicted on the map on page 25 of the Calumet National Heritage Area Feasibility Study, dated April 14, 2018, as subsequently modified, the boundaries of which start at 71st Street and Lake Michigan in Chicago and proceed west along 71st Street to Western Avenue, then south on Western Avenue to 95th Street, then west on 95th Street to Pulaski Road, then south on Pulaski Road to I\u201357, then south on I\u201357 to Crete-Monee Road, then east on Crete-Monee Road, continuing on West New Monee Road to end at State Street, and then extend to the Indiana State Line, with Lake, Porter, and LaPorte Counties included. (B) Local coordinating entity The Calumet Heritage Partnership shall be the local coordinating entity for the National Heritage Area designated by subparagraph (A). .\n##### (b) Management plan\nFor the purposes of section 6001(c) of the John D. Dingell, Jr. Conservation, Management, and Recreation Act ( Public Law 116\u20139 ; 133 Stat. 772; 136 Stat. 6173), the local coordinating entity for the Calumet National Heritage Area designated under the amendment made by subsection (a) shall submit to the Secretary of the Interior for approval a proposed management plan for the Calumet National Heritage Area not later than 3 years after the date of enactment of this Act.\n##### (c) Termination of authority\nFor the purposes of subsection (g)(4) of section 6001 of the John D. Dingell, Jr. Conservation, Management, and Recreation Act ( Public Law 116\u20139 ; 133 Stat. 776), the authority of the Secretary of the Interior to provide assistance under that section for the Calumet National Heritage Area designated under the amendment made by subsection (a) shall terminate on the date that is 15 years after the date of enactment of this Act.",
      "versionDate": "2025-12-16",
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
        "actionDate": "2025-12-17",
        "text": "Referred to the House Committee on Natural Resources."
      },
      "number": "6798",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Calumet National Heritage Area Act",
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
        "name": "Public Lands and Natural Resources",
        "updateDate": "2026-01-09T20:45:40Z"
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
      "date": "2025-12-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3501is.xml"
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
      "title": "Calumet National Heritage Area Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-09T10:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Calumet National Heritage Area Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-09T10:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the John D. Dingell, Jr. Conservation, Management, and Recreation Act to designate as a component of the National Heritage Area System the Calumet National Heritage Area in the States of Indiana and Illinois, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-09T10:48:23Z"
    }
  ]
}
```
