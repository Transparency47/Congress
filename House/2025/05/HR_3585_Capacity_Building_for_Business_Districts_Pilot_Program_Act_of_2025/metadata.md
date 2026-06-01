# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3585?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3585
- Title: Capacity Building for Business Districts Pilot Program Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3585
- Origin chamber: House
- Introduced date: 2025-05-23
- Update date: 2026-04-30T08:06:31Z
- Update date including text: 2026-04-30T08:06:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-23: Introduced in House
- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-23 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-24 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- Latest action: 2025-05-23: Introduced in House

## Actions

- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-23 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-24 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-23",
    "latestAction": {
      "actionDate": "2025-05-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3585",
    "number": "3585",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "E000235",
        "district": "4",
        "firstName": "Mike",
        "fullName": "Rep. Ezell, Mike [R-MS-4]",
        "lastName": "Ezell",
        "party": "R",
        "state": "MS"
      }
    ],
    "title": "Capacity Building for Business Districts Pilot Program Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-30T08:06:31Z",
    "updateDateIncludingText": "2026-04-30T08:06:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-24",
      "committees": {
        "item": {
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-23",
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
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-23",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-23",
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
          "date": "2025-05-23T14:01:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-05-24T18:50:34Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "systemCode": "hspw00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-05-23T14:01:15Z",
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
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-05-23",
      "state": "LA"
    },
    {
      "bioguideId": "A000369",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Amodei, Mark E. [R-NV-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Amodei",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2026-02-23",
      "state": "NV"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "DC"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2026-03-16",
      "state": "DE"
    },
    {
      "bioguideId": "K000388",
      "district": "1",
      "firstName": "Trent",
      "fullName": "Rep. Kelly, Trent [R-MS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2026-03-16",
      "state": "MS"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2026-03-18",
      "state": "KS"
    },
    {
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "False",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3585ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3585\nIN THE HOUSE OF REPRESENTATIVES\nMay 23, 2025 Mr. Ezell (for himself and Mr. Carter of Louisiana ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure , and in addition to the Committee on Financial Services , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Public Works and Economic Development Act of 1965 to establish the Capacity Building for Business Districts Pilot Program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Capacity Building for Business Districts Pilot Program Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nVibrant and prosperous business districts are vital components of thriving communities, providing critical commercial goods and services to community residents.\n**(2)**\nBusiness districts contribute to the vitality, character, and identity of urban neighborhoods, small towns, and rural and Native communities.\n**(3)**\nBusiness districts drive entrepreneurship, local business ownership, economic growth, and job creation.\n**(4)**\nBusiness districts are an essential part of the economic development ecosystem for towns, cities and rural communities, helping to attract consumers, visitors, new residents and new businesses to those communities and neighborhoods.\n**(5)**\nLocally based business district organizations are well positioned to provide technical assistance and support to small and underserved businesses, while also helping to attract customers for those businesses by shaping and nurturing the physical environment of the business districts.\n**(6)**\nLocally based business district organizations need technical assistance and flexible capital to support their ongoing operations, and cannot readily access these funds from existing programs at the Economic Development Administration due to the relatively small scale and highly local scope of their operations.\n**(7)**\nThere exists a substantial number of intermediary organizations that are well positioned to receive and responsibly deploy funding from the Economic Development Administration to currently unserved or underserved business district organizations for capacity building grants, technical assistance, training, and dissemination of best practices.\n#### 3. Capacity building for business districts pilot program\nSection 207 of the Public Works and Economic Development Act of 1965 ( 42 U.S.C. 3147 ) is amended\u2014\n**(1)**\nin subsection (a)(2)\u2014\n**(A)**\nby redesignating subparagraph (I) as subparagraph (J); and\n**(B)**\nin subparagraph (H) by striking the and at the end and inserting the following:\n(I) carrying out the pilot program established under subsection (c); and ; and\n**(2)**\nby adding at the end the following:\n(c) Capacity building for business districts pilot program (1) In general Within the program authorized under subsection (a), the Secretary shall establish a pilot program, to be known as the Capacity Building for Business Districts Pilot Program . (2) Grants The Secretary may award to specified recipients Capacity Building for Business Districts Pilot Program grants, on a competitive basis, to carry out place-based initiatives that provide specialized technical assistance, capacity building, and related services to eligible subrecipients that support business district revitalization in low-income, rural, minority and Native communities. (3) Multiple awards In providing assistance under this subsection, the Secretary shall make multiple awards to multiple organizations. (4) Administration The Secretary may not carry out this subsection through a regional office. (5) Prioritization The Secretary shall ensure a broad geographic distribution of award activities, and give priority to an applicant\u2014 (A) that would serve a distressed community in an area described under section 301(a), including rural communities and Indian Tribes; and (B) that has the demonstrated capacity to serve multiple States or multiple geographies within a State. (6) Reporting Specified recipients shall submit to the Secretary (at such time and in such manner as the Secretary may prescribe, but no more frequently than annually) a report specifying\u2014 (A) the names and addresses of eligible subrecipients receiving services and support from the specified recipient; (B) the use of funds by the specified recipient, including direct technical assistance and pass-through grant funds; (C) the use of funds by the eligible subrecipients, including internal operations, direct services to businesses, and district revitalization activities; (D) the specific geographic areas served by the eligible subrecipients; (E) the name, address, and industry as determined by the North American Industry Classification System, of each entity receiving assistance from eligible subrecipients; (F) the total number of jobs created and retained during the reporting period; and (G) any other information as the Secretary considers appropriate consistent with the findings under section 2 of the Capacity Building for Business Districts Pilot Program Act of 2025 . (7) Term The term of an initial grant shall be for a period that the Secretary determines appropriate for the proposed activities but not less than 2 years. (8) Definitions In this subsection: (A) Business district The term business district means a geographic area, which may have been designated as a business district by a State, county, regional or local unit of government, that is characterized by dense development, efficient land use, and a concentration of small businesses, economic activity, and employment opportunities or an area that could contain such concentration, including a rural main street or neighborhood commercial corridor. (B) Business district organization The term business district organization means a public or nonprofit entity located in a business district and established to provide services to the business district to promote the district, attract private investment and create jobs, and enhance the physical environment through property development and planning activities. (C) Capacity building The term capacity building means training, education, support, advice, and the provision of operating grants to enhance the technical and administrative capabilities of business district organizations. (D) Eligible subrecipient The term eligible subrecipient means a business district organization that\u2014 (i) is an organization that\u2014 (I) is described in paragraph (3), (4), (5), or (6) of section 501(c) of the Internal Revenue Code of 1986 and is exempt from taxation under section 501(a) of such Code; or (II) is a public entity; and (ii) provides services to a business district located in an area described under section 301(a) to support economic development, including providing business support services and physical space enhancements to such district. (E) Specified recipient The term specified recipient means an organization that\u2014 (i) is described in paragraph (3), (4), (5), or (6) of section 501(c) of the Internal Revenue Code of 1986 and is exempt from taxation under section 501(a) of such Code; (ii) operates, including through affiliates, membership networks or partnerships with third party entities, in multiple geographic areas served by multiple regional offices of the Economic Development Administration; and (iii) has experience and expertise in providing technical assistance and executing capacity building programs in support of business district organizations and similar community-based organizations that focus on revitalizing business districts and commercial corridors, including through support of underserved small businesses. .",
      "versionDate": "2025-05-23",
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
        "name": "Commerce",
        "updateDate": "2025-06-12T14:10:38Z"
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
      "date": "2025-05-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3585ih.xml"
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
      "title": "Capacity Building for Business Districts Pilot Program Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-03T04:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Capacity Building for Business Districts Pilot Program Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-03T04:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Works and Economic Development Act of 1965 to establish the Capacity Building for Business Districts Pilot Program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-03T04:18:27Z"
    }
  ]
}
```
