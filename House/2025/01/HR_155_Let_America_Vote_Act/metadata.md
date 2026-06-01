# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/155?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/155
- Title: Let America Vote Act
- Congress: 119
- Bill type: HR
- Bill number: 155
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2026-01-12T19:43:44Z
- Update date including text: 2026-01-12T19:43:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-03 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-03 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-03",
    "latestAction": {
      "actionDate": "2025-01-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/155",
    "number": "155",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "F000466",
        "district": "1",
        "firstName": "Brian",
        "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
        "lastName": "Fitzpatrick",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Let America Vote Act",
    "type": "HR",
    "updateDate": "2026-01-12T19:43:44Z",
    "updateDateIncludingText": "2026-01-12T19:43:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
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
      "text": "Referred to the Committee on House Administration, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on House Administration, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-03",
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
          "date": "2025-01-03T16:10:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-03T16:10:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
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
      "bioguideId": "G000600",
      "district": "3",
      "firstName": "Marie",
      "fullName": "Rep. Perez, Marie Gluesenkamp [D-WA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Perez",
      "middleName": "Gluesenkamp",
      "party": "D",
      "sponsorshipDate": "2025-01-03",
      "state": "WA"
    },
    {
      "bioguideId": "G000592",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Golden, Jared F. [D-ME-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Golden",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-01-03",
      "state": "ME"
    },
    {
      "bioguideId": "G000597",
      "district": "2",
      "firstName": "Andrew",
      "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Garbarino",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "NY"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
      "state": "NY"
    },
    {
      "bioguideId": "G000581",
      "district": "34",
      "firstName": "Vicente",
      "fullName": "Rep. Gonzalez, Vicente [D-TX-34]",
      "isOriginalCosponsor": "False",
      "lastName": "Gonzalez",
      "party": "D",
      "sponsorshipDate": "2025-08-15",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr155ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 155\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Fitzpatrick (for himself, Ms. Perez , Mr. Golden of Maine , and Mr. Garbarino ) introduced the following bill; which was referred to the Committee on House Administration , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo require States to permit unaffiliated voters to vote in primary elections for Federal office, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Let America Vote Act .\n#### 2. Requiring States to permit unaffiliated voters to vote in primary elections\n##### (a) Sense of Congress\nIt is the sense of Congress that the right of a citizen of the United States to vote in any taxpayer-funded election for public office shall not be denied or abridged by the United States or by any State on the grounds of political party affiliation or lack thereof.\n##### (b) Requirements for elections for Federal office\n**(1) Access of unaffiliated voters to primaries**\nEach State shall permit an unaffiliated voter who is registered to vote in an election for Federal office held in the State to vote in any primary election for such office held in the State, except that the State shall not permit an unaffiliated voter to vote in primary elections for such office of more than one political party.\n**(2) Restrictions relating to unaffiliated voters**\n**(A) Restrictions on sharing of information**\nA State shall not share information relating to an unaffiliated voter in a primary election for Federal office, including the voter\u2019s name and contact information, with a political party or with any other person who may reasonably be expected to use the information for a political or politically-connected commercial purpose, including soliciting funds.\n**(B) Restrictions on status of voter on official registration list**\nFor purposes of a State\u2019s official voter registration list, a State shall not treat an individual who is an unaffiliated voter as a member of, or as an individual who is otherwise affiliated with, the political party who held the primary election in which the individual voted solely on the grounds that the individual voted in that primary election.\n##### (c) Elections for State and local office\nNotwithstanding any other provision of law, a State may not use any funds provided by the Federal Government directly for election administration purposes unless the State certifies to the Election Assistance Commission that\u2014\n**(1)**\nthe State permits an unaffiliated voter who is registered to vote in an election for State or local office held in the State to vote in any primary election for such office held in the State, except that the State shall not permit an unaffiliated voter to vote in primary elections for such office of more than one political party;\n**(2)**\nthe State applies the restrictions on sharing information relating to unaffiliated voters in primary elections for Federal office, as described in subsection (a)(2)(A), to information relating to unaffiliated voters in primary elections for State and local office; and\n**(3)**\nthe State applies the restrictions on treating unaffiliated voters in primary elections for Federal office as members of, or as individuals who are otherwise affiliated with, a political party, as described in subsection (a)(2)(B), to unaffiliated voters in primary elections for State and local office.\n##### (d) Transition assistance grants\n**(1) Payment of grants**\nIf a State certifies to the Election Assistance Commission that the State is in compliance with the requirements of this section with respect to a fiscal year, the Commission shall make a payment to the State during that fiscal year and each of the 4 succeeding fiscal years in an amount equal to 2 percent of the total amount of requirements payments made to the State under section 251 of the Help America Vote Act of 2002 ( 52 U.S.C. 21001 ).\n**(2) Use of funds**\nA State shall use the payment received under this subsection to cover the costs of permitting unaffiliated voters who are registered to vote in elections for Federal, State, or local office held in the State to vote in any primary election for such office held in the State.\n**(3) Authorization of appropriations**\nThere are authorized to be appropriated for fiscal year 2026 and each succeeding fiscal year such sums as may be necessary for grants under this subsection.\n##### (e) Definitions\nFor purposes of this section\u2014\n**(1)**\nthe terms election and Federal office have the meanings give such terms in section 301 of the Federal Election Campaign Act of 1971 ( 52 U.S.C. 30101 );\n**(2)**\nthe term primary election means an election (including a primary election held for the expression of a preference for the nomination of individuals for election to the office of President) held by any political party to nominate individuals who would appear on a general election ballot as a candidate for election for Federal office, including a convention or caucus of a political party which has authority to nominate such a candidate;\n**(3)**\nthe term State has the meaning given such term in section 901 of the Help America Vote Act of 2002 ( 52 U.S.C. 21141 ); and\n**(4)**\nthe term unaffiliated voter means an individual who is not registered to vote as a member of a political party or otherwise affiliated with a political party.\n##### (f) Effective date\nThis Act shall apply with respect to elections held after the date of the enactment of this Act.\n#### 3. Prohibiting noncitizens from voting\n##### (a) Statement of policy\nIt is the policy of the United States that no person who is not a citizen shall be permitted or granted the right to vote in any taxpayer-funded election for public office held by or in the United States or any State.\n##### (b) Elections for Federal office\nNo State shall permit any person who is not a citizen of the United States to vote in any election for Federal office held in the State.\n##### (c) Elections for State and local office\nNotwithstanding any other provision of law, a State may not use any funds provided by the Federal Government directly for election administration purposes unless the State certifies to the Election Assistance Commission that the State does not permit any person who is not a citizen of the United States to vote in any election for State or local office or any ballot initiative or referendum held in the State.",
      "versionDate": "2025-01-03",
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
        "actionDate": "2025-10-24",
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committees on Energy and Commerce, Natural Resources, Education and Workforce, Transportation and Infrastructure, Science, Space, and Technology, Agriculture, Appropriations, Armed Services, the Budget, Rules, Ethics, Financial Services, Foreign Affairs, Homeland Security, House Administration, the Judiciary, Intelligence (Permanent Select), Oversight and Government Reform, Small Business, and Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "5827",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "To advance bipartisan, common sense solutions.",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-12-11",
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committees on Energy and Commerce, Natural Resources, Education and Workforce, Transportation and Infrastructure, Science, Space, and Technology, Agriculture, Appropriations, Armed Services, the Budget, Rules, Ethics, Financial Services, Foreign Affairs, Homeland Security, House Administration, the Judiciary, Intelligence (Permanent Select), Oversight and Government Reform, Small Business, and Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "6636",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "To advance sensible priorities.",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-12-11",
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committees on Energy and Commerce, Natural Resources, Education and Workforce, Transportation and Infrastructure, Science, Space, and Technology, Agriculture, Appropriations, Armed Services, the Budget, Rules, Ethics, Financial Services, Foreign Affairs, Homeland Security, House Administration, the Judiciary, Intelligence (Permanent Select), Oversight and Government Reform, Small Business, and Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "6637",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "To advance bipartisan priorities.",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-04-24",
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committees on Energy and Commerce, Natural Resources, Education and Workforce, Transportation and Infrastructure, Science, Space, and Technology, Agriculture, Appropriations, Armed Services, the Budget, Rules, Ethics, Financial Services, Foreign Affairs, Homeland Security, House Administration, the Judiciary, Intelligence (Permanent Select), Oversight and Government Reform, Small Business, and Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "3001",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "To advance commonsense priorities.",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Elections, voting, political campaign regulation",
            "updateDate": "2025-02-06T15:19:27Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-02-06T15:19:32Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-01-31T18:05:41Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-03",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr155",
          "measure-number": "155",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-02-21"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr155v00",
            "update-date": "2025-02-21"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Let America Vote Act</strong></p><p>This bill requires states to allow unaffiliated voters to vote in primary elections for federal office. It also restricts certain federal election funding for states that allow noncitizens to vote in state or local elections.</p><p>Specifically, each state must permit an unaffiliated voter who is registered to vote in a federal election held in the state to vote in any primary election for federal office. A state shall not permit an unaffiliated voter to vote in primary elections for more than one political party.</p><p>The bill prohibits a state from (1) sharing unaffiliated voter information with a political party or any other person who may reasonably be expected to use the information for political purposes, including soliciting funds; or (2) treating an unaffiliated voter as a member of a political party for purposes of the state's official voter registration list.</p><p>States must, in order to use federal election administration funds, certify their compliance with these unaffiliated voter requirements. Upon certification, the Election Assistance Commission (EAC) must make five-year grants to the state for the costs of permitting unaffiliated voters to vote in primary elections.</p><p>The bill specifically prohibits noncitizens from voting in federal elections. (Current federal law prohibits noncitizens\u00a0from voting in federal elections.)</p><p>A state may not use federal election administration funds unless the state certifies to the EAC that it does not permit a noncitizen to vote in state or local elections or vote on any ballot initiative or referendum held in the state.</p>"
        },
        "title": "Let America Vote Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr155.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Let America Vote Act</strong></p><p>This bill requires states to allow unaffiliated voters to vote in primary elections for federal office. It also restricts certain federal election funding for states that allow noncitizens to vote in state or local elections.</p><p>Specifically, each state must permit an unaffiliated voter who is registered to vote in a federal election held in the state to vote in any primary election for federal office. A state shall not permit an unaffiliated voter to vote in primary elections for more than one political party.</p><p>The bill prohibits a state from (1) sharing unaffiliated voter information with a political party or any other person who may reasonably be expected to use the information for political purposes, including soliciting funds; or (2) treating an unaffiliated voter as a member of a political party for purposes of the state's official voter registration list.</p><p>States must, in order to use federal election administration funds, certify their compliance with these unaffiliated voter requirements. Upon certification, the Election Assistance Commission (EAC) must make five-year grants to the state for the costs of permitting unaffiliated voters to vote in primary elections.</p><p>The bill specifically prohibits noncitizens from voting in federal elections. (Current federal law prohibits noncitizens\u00a0from voting in federal elections.)</p><p>A state may not use federal election administration funds unless the state certifies to the EAC that it does not permit a noncitizen to vote in state or local elections or vote on any ballot initiative or referendum held in the state.</p>",
      "updateDate": "2025-02-21",
      "versionCode": "id119hr155"
    },
    "title": "Let America Vote Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Let America Vote Act</strong></p><p>This bill requires states to allow unaffiliated voters to vote in primary elections for federal office. It also restricts certain federal election funding for states that allow noncitizens to vote in state or local elections.</p><p>Specifically, each state must permit an unaffiliated voter who is registered to vote in a federal election held in the state to vote in any primary election for federal office. A state shall not permit an unaffiliated voter to vote in primary elections for more than one political party.</p><p>The bill prohibits a state from (1) sharing unaffiliated voter information with a political party or any other person who may reasonably be expected to use the information for political purposes, including soliciting funds; or (2) treating an unaffiliated voter as a member of a political party for purposes of the state's official voter registration list.</p><p>States must, in order to use federal election administration funds, certify their compliance with these unaffiliated voter requirements. Upon certification, the Election Assistance Commission (EAC) must make five-year grants to the state for the costs of permitting unaffiliated voters to vote in primary elections.</p><p>The bill specifically prohibits noncitizens from voting in federal elections. (Current federal law prohibits noncitizens\u00a0from voting in federal elections.)</p><p>A state may not use federal election administration funds unless the state certifies to the EAC that it does not permit a noncitizen to vote in state or local elections or vote on any ballot initiative or referendum held in the state.</p>",
      "updateDate": "2025-02-21",
      "versionCode": "id119hr155"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr155ih.xml"
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
      "title": "Let America Vote Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-31T11:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Let America Vote Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-31T11:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require States to permit unaffiliated voters to vote in primary elections for Federal office, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-31T11:03:26Z"
    }
  ]
}
```
