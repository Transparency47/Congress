# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5796?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5796
- Title: BUILD Act
- Congress: 119
- Bill type: HR
- Bill number: 5796
- Origin chamber: House
- Introduced date: 2025-10-21
- Update date: 2026-02-18T09:05:48Z
- Update date including text: 2026-02-18T09:05:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-21: Introduced in House
- 2025-10-21 - IntroReferral: Introduced in House
- 2025-10-21 - IntroReferral: Introduced in House
- 2025-10-21 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-10-21 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-01 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- Latest action: 2025-10-21: Introduced in House

## Actions

- 2025-10-21 - IntroReferral: Introduced in House
- 2025-10-21 - IntroReferral: Introduced in House
- 2025-10-21 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-10-21 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-01 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-21",
    "latestAction": {
      "actionDate": "2025-10-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5796",
    "number": "5796",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "C001059",
        "district": "21",
        "firstName": "Jim",
        "fullName": "Rep. Costa, Jim [D-CA-21]",
        "lastName": "Costa",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "BUILD Act",
    "type": "HR",
    "updateDate": "2026-02-18T09:05:48Z",
    "updateDateIncludingText": "2026-02-18T09:05:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-01",
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
      "actionDate": "2025-10-21",
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
      "actionDate": "2025-10-21",
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
      "actionDate": "2025-10-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-21",
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
          "date": "2025-10-21T18:01:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-01T19:53:13Z",
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
          "date": "2025-10-21T18:01:25Z",
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
      "bioguideId": "W000821",
      "district": "4",
      "firstName": "Bruce",
      "fullName": "Rep. Westerman, Bruce [R-AR-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Westerman",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "AR"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2026-02-17",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5796ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5796\nIN THE HOUSE OF REPRESENTATIVES\nOctober 21, 2025 Mr. Costa (for himself and Mr. Westerman ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure , and in addition to the Committee on Financial Services , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo establish a grant program for certain institutions of higher education to plan and implement projects for economic and community development in economically distressed communities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Boosting University Investments in Low-Income Districts Act or the BUILD Act .\n#### 2. Distressed communities grant program\n##### (a) Establishment\nThe Secretary shall establish a program to award grants to institutions of higher education designated under subsection (b) to plan and implement eligible projects for economic and community development in economically distressed communities.\n##### (b) Designation of institutions of higher education\n**(1) List of institutions of higher education**\nThe Secretary shall develop a list of every institution of higher education that the Secretary determines is located in a distressed community, in accordance with the criteria described in paragraph (2).\n**(2) Distressed community criteria**\nThe Secretary shall determine that an institution of higher education is located in a distressed community if one of the following circumstances applies to such institution:\n**(A)**\nIn the case of an institution of higher education that is located in a metropolitan or a micropolitan statistical area, as defined by the Office of Management and Budget, and in a State in which the median family income is higher than the national median family income, the institution of higher education is located in a ZIP Code in which the median family income is at least 25 percent lower than the median family income for such State.\n**(B)**\nIn the case of an institution of higher education that is located in a metropolitan or a micropolitan statistical area, as defined by the Office of Management and Budget, and in a State in which the median family income is lower than the national median family income, the institution of higher education is located in a Zip Code in which the median family income is at least 25 percent lower than the national median family income.\n**(C)**\nIn the case of an institution of higher education that is not located in a metropolitan or micropolitan statistical area and is located in a State in which the median family income is higher than the national median family income, the institution of higher education is located in a county in which the median family income is at least 25 percent lower than the median family income for such State.\n**(D)**\nIn the case of an institution of higher education that is not located in a metropolitan or micropolitan statistical area and is located in a State in which the median family income is lower than the national median family income, the institution of higher education is located in a county in which the median family income is at least 25 percent lower than the national median family income.\n**(3) Designation**\n**(A) Notification to institutions of higher education**\nUpon development of the list of institutions of higher education located in a distressed community under paragraph (1), the Secretary shall notify each institution of higher education that is included in such list that such institution may be designated under this paragraph to receive a planning grant and an implementation grant under this section.\n**(B) Notification to Secretary**\nAn institution of higher education that receives a notification from the Secretary under subparagraph (A) that intends to receive a planning grant and an implementation grant under this section shall submit to the Secretary a notification of such intent in such form and at such time as the Secretary determines appropriate.\n**(C) Grant eligibility**\nThe Secretary shall designate each institution of higher education that submits a notification under subparagraph (B) as eligible to receive a planning grant and an implementation grant under this section.\n##### (c) Planning grants\n**(1) In general**\nThe Secretary shall provide a grant to each institution of higher education designated under subsection (b) for such institution to develop an implementation plan describing\u2014\n**(A)**\nthe eligible projects that such institution intends to carry out with an implementation grant under subsection (d); and\n**(B)**\nhow such projects will support economic and community revitalization in the community in which such institution is located.\n**(2) Implementation plan**\n**(A) In general**\nA recipient of a planning grant under this subsection shall complete the implementation plan required under paragraph (1) not later than 2 years after the date on which the Secretary provides a planning grant to such recipient.\n**(B) Approval**\nUpon completion of an implementation plan with a planning grant provided under this subsection, the Secretary shall review such plan for approval.\n**(3) Grant amounts**\n**(A) Grant term**\nThe Secretary may distribute funds for a grant provided under this subsection for a period of not more than 2 years.\n**(B) Total grant amounts**\nEach grant awarded under this subsection shall be in an amount that does not exceed $100,000 for each year of the grant term.\n**(C) Additional amounts**\n**(i) Application for additional grant funds**\nNot later than 1 year after grant funds are first awarded under subparagraph (A), a grant recipient may submit to the Secretary an application to receive additional funds to complete the implementation plan required under paragraph (1).\n**(ii) Deadline to receive additional grant funds**\nNot later than 90 days after a grant recipient submits an application for additional grant funds under clause (i), the Secretary shall determine whether to award additional grant funds to such recipient and shall distribute such additional grant funds to such recipient.\n**(D) Formula**\nThe Secretary shall establish a formula by which the Secretary shall distribute funds for each grant under this subsection in accordance with this paragraph.\n##### (d) Implementation grants\n**(1) In general**\nUpon approval of an implementation plan under subsection (c)(2), the Secretary shall provide a grant to the institution of higher education to carry out eligible projects described in such plan.\n**(2) Grant term**\nThe term of a grant provided under this subsection shall be 5 years.\n**(3) Grant amounts**\nThe Secretary shall establish a formula by which the Secretary shall distribute funds for each grant under this subsection in accordance with the following requirements:\n**(A)**\nThe Secretary shall provide each recipient of a grant under this subsection with a grant in an amount that is not less than $25,000,000 and not more than $50,000,000.\n**(B)**\nThe Secretary shall distribute funds for each grant under this subsection at least once during each year of the grant term.\n**(4) Use of funds**\nA recipient of a grant under this subsection may only use such grant to carry out an eligible project in the distressed community in which such recipient is located, as determined by the Secretary under subsection (b)(2).\n**(5) Report required**\nAt least once each year during the term of a grant provided under this subsection, a recipient of such grant shall submit to the Secretary a report describing the activities for which such grant was used during such year.\n##### (e) Definitions\nIn this section:\n**(1) Eligible project**\nThe term eligible project means a project that will spur economic development in the community in which such project is carried out, including a project to\u2014\n**(A)**\nrenovate, construct, or maintain buildings that will benefit and be accessible to the community, including\u2014\n**(i)**\ncommercial buildings located on the campus of the institution of higher education carrying out the project;\n**(ii)**\nhousing for students, faculty, staff, or members of the community;\n**(iii)**\ncultural institutions such as museums, theaters, and arts centers; and\n**(iv)**\nfacilities such as laboratories or libraries;\n**(B)**\nestablish programs, hosted by the institution of higher education carrying out the project, that provide seed money to early-stage companies for small business development;\n**(C)**\ndevelop and fund apprenticeships, hosted by the institution of higher education carrying out the project, in local industries to decrease unemployment in the community;\n**(D)**\nbuild and maintain municipal broadband networks and related infrastructure for the institution of higher education that is carrying out the project and the community;\n**(E)**\nbuild and maintain health clinics accessible to the public on or near the campus of the institution of higher education that is carrying out the project;\n**(F)**\nestablish programs at local health clinics to educate, recruit, and train members of the community to become healthcare professionals;\n**(G)**\nestablish partnerships between the institution of higher education carrying out the project and local school districts to provide\u2014\n**(i)**\ngraduate student teaching support;\n**(ii)**\nadministrative support to such school districts; and\n**(iii)**\naccess to facilities of such institution of higher education to local elementary and secondary schools; and\n**(H)**\nfund research on the campus of the institution of higher education carrying out the project that is relevant to the economic needs of the community.\n**(2) Institution of higher education**\n**(A) In general**\nThe term institution of higher education means an institution of higher education (as defined in section 101(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1001(a) )), including an institution of higher education established under the Morrill Act of 1890 ( 7 U.S.C. 321 et seq. ), that\u2014\n**(i)**\noffers more than 50 percent of such institution\u2019s courses by correspondence; and\n**(ii)**\nenrolls 50 percent or more of the institution\u2019s students in correspondence courses.\n**(B) Exclusion**\nThe term institution of higher education does not include an institution of higher education that\u2014\n**(i)**\nis an institution of higher education established under the Morrill Act of 1862 ( 7 U.S.C. 301 et seq. );\n**(ii)**\nhas very high research activity status, as designated by the Carnegie Classification of Institutions of Higher Education; or\n**(iii)**\nis a service academy.\n**(3) Secretary**\nThe term Secretary means the Secretary of Commerce, acting through the Assistant Secretary of Commerce for Economic Development.\n**(4) Service academy**\nThe term service academy means the following:\n**(A)**\nThe United States Military Academy.\n**(B)**\nThe United States Naval Academy.\n**(C)**\nThe United States Air Force Academy.\n**(D)**\nThe United States Coast Guard Academy.\n**(E)**\nThe United States Merchant Marine Academy.\n**(F)**\nAny college or university designated by the Secretary of Defense as a military college.",
      "versionDate": "2025-10-21",
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
        "updateDate": "2025-12-08T16:39:23Z"
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
      "date": "2025-10-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5796ih.xml"
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
      "title": "BUILD Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-22T10:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "BUILD Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-22T10:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Boosting University Investments in Low-Income Districts Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-22T10:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a grant program for certain institutions of higher education to plan and implement projects for economic and community development in economically distressed communities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-22T10:48:12Z"
    }
  ]
}
```
