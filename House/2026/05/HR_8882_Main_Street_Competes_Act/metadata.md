# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8882?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8882
- Title: Main Street Competes Act
- Congress: 119
- Bill type: HR
- Bill number: 8882
- Origin chamber: House
- Introduced date: 2026-05-19
- Update date: 2026-05-22T08:08:52Z
- Update date including text: 2026-05-22T08:08:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, text, titles

## Timeline

- 2026-05-19: Introduced in House
- 2026-05-19 - IntroReferral: Introduced in House
- 2026-05-19 - IntroReferral: Introduced in House
- 2026-05-19 - IntroReferral: Referred to the House Committee on Small Business.
- 2026-05-20 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-20 - Committee: Ordered to be Reported by the Yeas and Nays: 23 - 0.
- Latest action: 2026-05-19: Introduced in House

## Actions

- 2026-05-19 - IntroReferral: Introduced in House
- 2026-05-19 - IntroReferral: Introduced in House
- 2026-05-19 - IntroReferral: Referred to the House Committee on Small Business.
- 2026-05-20 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-20 - Committee: Ordered to be Reported by the Yeas and Nays: 23 - 0.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-19",
    "latestAction": {
      "actionDate": "2026-05-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8882",
    "number": "8882",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "S001221",
        "district": "3",
        "firstName": "Hillary",
        "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
        "lastName": "Scholten",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Main Street Competes Act",
    "type": "HR",
    "updateDate": "2026-05-22T08:08:52Z",
    "updateDateIncludingText": "2026-05-22T08:08:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Small Business Committee",
          "systemCode": "hssm00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported by the Yeas and Nays: 23 - 0.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Small Business Committee",
          "systemCode": "hssm00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-19",
      "committees": {
        "item": {
          "name": "Small Business Committee",
          "systemCode": "hssm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Small Business.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-19",
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
        "item": [
          {
            "date": "2026-05-20T21:46:05Z",
            "name": "Markup By"
          },
          {
            "date": "2026-05-19T16:00:25Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Small Business Committee",
      "systemCode": "hssm00",
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
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2026-05-19",
      "state": "KS"
    },
    {
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
      "state": "NH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8882ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8882\nIN THE HOUSE OF REPRESENTATIVES\nMay 19, 2026 Ms. Scholten (for herself and Mr. Schmidt ) introduced the following bill; which was referred to the Committee on Small Business\nA BILL\nTo amend the Small Business Economic Policy Act of 1980 to examine how the competitiveness of small businesses is affected by the enforcement of Federal antitrust laws, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Main Street Competes Act .\n#### 2. Congressional declaration of small business economic policy\nSection 302(a) of the Small Business Economic Policy Act of 1980 ( 15 U.S.C. 631a(a) ) is amended\u2014\n**(1)**\nby striking and provide and inserting provide ; and\n**(2)**\nby striking the period at the end and inserting ; and promote competitive markets, consumer choice, and business ownership through enforcement of Federal antitrust laws in the case of anticompetitive conduct and illegal mergers that harms small businesses and the growth of small businesses. .\n#### 3. State of small businesses\n##### (a) In general\nSection 303 of the Small Business Economic Policy Act of 1980 ( 15 U.S.C. 631b ) is amended to read as follows:\n303. Report on the state of small business concerns (a) Specified entity report Not later than 180 days after the end of the fiscal year in which the Main Street Competes Act is enacted, and every two fiscal years thereafter, the head of each specified entity shall submit to the Chief Counsel for Advocacy of the Office of Advocacy of the Small Business Administration a report including\u2014 (1) an analysis of how enforcement by the specified entity of Federal antitrust laws promoted competition during the preceding fiscal year by deterring and remedying anticompetitive conduct, including illegal mergers, that harms small businesses and the growth of small businesses; (2) the number of complaints of alleged antitrust violations filed by self-identified small businesses with the specified entity during such fiscal year, disaggregated by type of offense and the specific Federal antitrust laws allegedly violated; (3) the number of inquiries, investigations, and enforcement actions undertaken by the specified entity in response to complaints filed by small businesses with the specified entity during such fiscal year; and (4) the number of inquiries, investigations, and enforcement actions undertaken by the specified entity during such fiscal year pursuant to an alleged antitrust violation, opened for a reason other than a complaint filed by a small business as described in paragraph (3), to deter and remedy anticompetitive conduct that harms small businesses and the growth of small businesses. (b) Office of Advocacy report Not later than 180 days after receipt of the report required by subsection (a), the Chief Counsel for Advocacy shall submit to the Committee on Small Business of the House of Representatives and the Committee on Small Business and Entrepreneurship of Senate a report that includes\u2014 (1) a summary of the report submitted under subsection (a); (2) an analysis of the data in such report, disaggregated by industry category; (3) an evaluation of the issues identified in such report relating to\u2014 (A) anticompetitive conduct, including illegal mergers, that harmed small businesses and the growth of small businesses; and (B) administrative actions that promoted competition and growth of small businesses; (4) as appropriate, recommendations for administrative actions that could\u2014 (A) promote competition; (B) deter anticompetitive conduct, including illegal mergers, that harmed small business and the growth of small businesses; and (C) remedy such anticompetitive conduct; and (5) as appropriate, recommendations for legislative actions that could\u2014 (A) promote competition; (B) deter anticompetitive conduct, including illegal mergers, that harmed small business and the growth of small businesses; and (C) remedy such anticompetitive conduct. .\n##### (b) Definitions\nThe Small Business Economic Policy Act of 1980 ( Public Law 96\u2013302 ; 94 Stat. 848; 15 U.S.C. 631a et seq. ) is amended by adding at the end the following new section:\n304. Definitions In this title: (1) Antitrust violation The term antitrust violation means any violation of Federal antitrust laws. (2) Federal antitrust laws The term Federal antitrust laws has the meaning given the term antitrust laws in subsection (a) of the first section of the Clayton Act ( 15 U.S.C. 12(a) ), except that such term shall also include section 5 of the Federal Trade Commission Act ( 15 U.S.C. 45 ) to the extent that such section 5 applies to unfair methods of competition. (3) Small business The term small business has the meaning given the term small business concern under section 3 of the Small Business Act ( 15 U.S.C. 632 ). (4) Specified entity The term specified entity means\u2014 (A) the Department of Justice; and (B) the Federal Trade Commission. .",
      "versionDate": "2026-05-19",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-05-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8882ih.xml"
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
      "title": "Main Street Competes Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-20T08:23:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Main Street Competes Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-20T08:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Small Business Economic Policy Act of 1980 to examine how the competitiveness of small businesses is affected by the enforcement of Federal antitrust laws, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-20T08:19:37Z"
    }
  ]
}
```
