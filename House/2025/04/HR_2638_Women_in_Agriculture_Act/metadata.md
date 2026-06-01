# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2638?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2638
- Title: Women in Agriculture Act
- Congress: 119
- Bill type: HR
- Bill number: 2638
- Origin chamber: House
- Introduced date: 2025-04-03
- Update date: 2025-06-09T14:38:52Z
- Update date including text: 2026-04-15T16:27:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-04-03: Introduced in House
- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-04-18 - Committee: Referred to the Subcommittee on Conservation, Research, and Biotechnology.
- Latest action: 2025-04-03: Introduced in House

## Actions

- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-04-18 - Committee: Referred to the Subcommittee on Conservation, Research, and Biotechnology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-03",
    "latestAction": {
      "actionDate": "2025-04-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2638",
    "number": "2638",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "L000273",
        "district": "3",
        "firstName": "Teresa",
        "fullName": "Rep. Leger Fernandez, Teresa [D-NM-3]",
        "lastName": "Leger Fernandez",
        "party": "D",
        "state": "NM"
      }
    ],
    "title": "Women in Agriculture Act",
    "type": "HR",
    "updateDate": "2025-06-09T14:38:52Z",
    "updateDateIncludingText": "2026-04-15T16:27:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-18",
      "committees": {
        "item": {
          "name": "Conservation, Research, and Biotechnology Subcommittee",
          "systemCode": "hsag14"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Conservation, Research, and Biotechnology.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-03",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-03",
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
          "date": "2025-04-03T15:06:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-04-18T21:16:00Z",
              "name": "Referred to"
            }
          },
          "name": "Conservation, Research, and Biotechnology Subcommittee",
          "systemCode": "hsag14"
        }
      },
      "systemCode": "hsag00",
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
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-04-03",
      "state": "VA"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "ME"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "NC"
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
      "sponsorshipDate": "2025-04-10",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2638ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2638\nIN THE HOUSE OF REPRESENTATIVES\nApril 3, 2025 Ms. Leger Fernandez (for herself, Mrs. Kiggans of Virginia , Ms. Pingree , and Ms. Ross ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Department of Agriculture Reorganization Act of 1994 to establish the position of Women Farmers and Ranchers Liaison, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Women in Agriculture Act .\n#### 2. Women Farmers and Ranchers Liaison\n##### (a) In general\nThe Department of Agriculture Reorganization Act of 1994 is amended by inserting after section 222 ( 7 U.S.C. 6923 ) the following:\n223. Women Farmers and Ranchers Liaison (a) Establishment Not later than 120 days after the date of the enactment of the Women in Agriculture Act, the Secretary shall establish in the Department the position of Women Farmers and Ranchers Liaison (in this section referred to as the Liaison ). (b) Duties (1) In general The Liaison shall carry out the following duties: (A) With respect to agricultural programs available to women who are farmers and ranchers\u2014 (i) provide information to such women about the availability of such programs and the eligibility requirements for such programs; and (ii) assist such women, and women who are potential farmers or ranchers, in applying for such programs. (B) Advocate on behalf of women who are farmers and ranchers in interactions with employees of the Department. (C) Promote the advancement of women in leadership roles within the Department. (D) Submit and make publicly available the report required under paragraph (2)(A). (E) Consult and provide technical assistance to the Equity Commission of the Department. (F) Consult with and provide technical assistance to any Federal agency that requests such assistance with respect to the duties described in subparagraphs (A) through (E). (2) Report (A) In general Not later than 1 year after the date of the enactment of the Women in Agriculture Act, and annually thereafter, the Liaison shall submit to Congress and make publicly available a report on the grants, loans, loan guarantees, and cost share programs made by the Secretary to woman-owned agriculture operations. (B) Contents Each report required under subparagraph (A) shall include, with respect to the fiscal year preceding such report\u2014 (i) the total number of grants, loans, loan guarantees, and cost share programs made by each of the Farm Service Agency and the Natural Resources Conservation Service to agriculture operations; (ii) the percentage of such grants, loans, loan guarantees, and cost share programs made to woman-owned agriculture operations; (iii) the percentage of total funding directed to woman-owned agriculture operations, disaggregated by program; (iv) the percentage of applications made by women-owned agricultural operations; and (v) the percentage of women at different GS levels at the Department, disaggregated by office. (3) Contract or cooperative agreement The Liaison may enter into a contract or cooperative agreement with a research center of the Agricultural Research Service, an institution of higher education (as such term is defined in section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 )), or a nonprofit organization to carry out 1 or more of the following activities with respect to women who are farmers and ranchers: (A) Conducting research on the profitability of small farms run by such women. (B) Developing educational materials for such women. (C) Conducting workshops, courses, and certified vocational training for such women. (D) Conducting mentoring activities for such women. (E) Providing internship opportunities for such women. (c) Staff support The Secretary may appoint staff of the Department of Agriculture to support the Liaison. .\n##### (b) Termination of authority\nSection 296(b) of the Department of Agriculture Reorganization Act of 1994 ( 7 U.S.C. 7014(b) ) is amended by adding at the end the following:\n(11) The authority of the Secretary to carry out the amendment made to this title by the Women in Agriculture Act. .\n#### 3. High-priority research and extension areas\nSection 1672(d) of the Food, Agriculture, Conservation, and Trade Act of 1990 ( 7 U.S.C. 5925(d) ) is amended by adding at the end the following:\n(21) Ergonomically designed agriculture equipment and machinery Research and extension grants may be made under this section for the purposes of developing and making widely available agriculture equipment and machinery that is ergonomically designed for use by women. .\n#### 4. Child care priority\nSection 306(a) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1926(a) ) is amended by adding at the end the following:\n(27) Child care priority In selecting recipients of loans and grants under this subsection, the Secretary shall give priority to any qualified applicant that proposes to use the loan or grant to address the availability, quality, or cost of childcare in an agricultural or rural community. .",
      "versionDate": "2025-04-03",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-05-06T20:28:47Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-03",
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
          "measure-id": "id119hr2638",
          "measure-number": "2638",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-03",
          "originChamber": "HOUSE",
          "update-date": "2025-06-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2638v00",
            "update-date": "2025-06-09"
          },
          "action-date": "2025-04-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Women in Agriculture Act</strong></p><p>This bill directs the Department of Agriculture (USDA) to establish the position of Women Farmers and Ranchers Liaison within USDA.</p><p>Among other things, the liaison must advocate on behalf of women who are farmers and ranchers in interactions with USDA employees and promote the advancement of women in USDA leadership roles. The liaison may also enter into a contract or cooperative agreement to conduct various research, training, and other activities with respect to women who are farmers and ranchers.</p><p>The liaison must submit an annual report to Congress on USDA grants, loans, loan guarantees, and cost-share programs for woman-owned agriculture operations.</p><p>In addition, the bill expands the USDA high-priority research and extension areas to authorize grants\u00a0for developing and making widely available agriculture equipment and machinery that is ergonomically designed for use by women.</p><p>Further,\u00a0USDA must give priority to certain loans or grants to address the availability, quality, or cost of childcare in an agricultural or rural community.</p>"
        },
        "title": "Women in Agriculture Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2638.xml",
    "summary": {
      "actionDate": "2025-04-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Women in Agriculture Act</strong></p><p>This bill directs the Department of Agriculture (USDA) to establish the position of Women Farmers and Ranchers Liaison within USDA.</p><p>Among other things, the liaison must advocate on behalf of women who are farmers and ranchers in interactions with USDA employees and promote the advancement of women in USDA leadership roles. The liaison may also enter into a contract or cooperative agreement to conduct various research, training, and other activities with respect to women who are farmers and ranchers.</p><p>The liaison must submit an annual report to Congress on USDA grants, loans, loan guarantees, and cost-share programs for woman-owned agriculture operations.</p><p>In addition, the bill expands the USDA high-priority research and extension areas to authorize grants\u00a0for developing and making widely available agriculture equipment and machinery that is ergonomically designed for use by women.</p><p>Further,\u00a0USDA must give priority to certain loans or grants to address the availability, quality, or cost of childcare in an agricultural or rural community.</p>",
      "updateDate": "2025-06-09",
      "versionCode": "id119hr2638"
    },
    "title": "Women in Agriculture Act"
  },
  "summaries": [
    {
      "actionDate": "2025-04-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Women in Agriculture Act</strong></p><p>This bill directs the Department of Agriculture (USDA) to establish the position of Women Farmers and Ranchers Liaison within USDA.</p><p>Among other things, the liaison must advocate on behalf of women who are farmers and ranchers in interactions with USDA employees and promote the advancement of women in USDA leadership roles. The liaison may also enter into a contract or cooperative agreement to conduct various research, training, and other activities with respect to women who are farmers and ranchers.</p><p>The liaison must submit an annual report to Congress on USDA grants, loans, loan guarantees, and cost-share programs for woman-owned agriculture operations.</p><p>In addition, the bill expands the USDA high-priority research and extension areas to authorize grants\u00a0for developing and making widely available agriculture equipment and machinery that is ergonomically designed for use by women.</p><p>Further,\u00a0USDA must give priority to certain loans or grants to address the availability, quality, or cost of childcare in an agricultural or rural community.</p>",
      "updateDate": "2025-06-09",
      "versionCode": "id119hr2638"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2638ih.xml"
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
      "title": "Women in Agriculture Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-11T10:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Women in Agriculture Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-11T10:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Department of Agriculture Reorganization Act of 1994 to establish the position of Women Farmers and Ranchers Liaison, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-11T10:18:15Z"
    }
  ]
}
```
